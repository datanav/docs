Receiving webhook events
========================

The pipe should be called ``-event``.

Key concepts
------------
Key concepts in receiving webhook events:

* Before consuming webhook events, you must make sure to register the webhooks. See section :ref:`registering webhooks <registering_webhooks>`.
* In order to consume the webhook events, verify that the manifest includes ``"use_webhook_secrets": true``. This will create webhook secret and set ``group:Anonymous`` and ``write_data`` permissions to all event pipes.
* webhooks sign the payload with a secret key (often ``HMAC``). The secret key is typically set by the ``-registerwebhook`` pipe. The event pipe must have the correct validation expression that uses the webhook secret. This is done to make sure that the webhook event is coming from the correct source.
* some systems use a default secret key, e.g. Shopify uses the ``client_secret`` to sign the webhook payload. In this case, the event pipe must have the correct validation expression that uses the ``client_secret`` and ``-registerwebhoook`` pipe don't send any secret key.

Example: validation expression
------------------------------

::

   "validation_expression": "{% if request_headers['X-Shopify-Hmac-SHA256'] == b64encode(hmacsha256digest(secret('oauth_client_secret'), request_body)) %}{% else %}FAIL!{% endif %}"

* When testing the webhooks with Sesampy on dev nodes, this is not automatically handled and you may need to manually put the ``client_secret`` value into the validation expression.

Example: -event pipe
--------------------

::

  {
    "_id": "<system>-<datatype>-event",
    "compaction": {
      "keep_versions": 1
    },
    "namespaced_identifiers": false,
    "sink": {
      "set_initial_offset": "onload"
    },
    "source": {
      "system": "<system>",
      "type": "http_endpoint",
      "validation_expression": "{% if request_headers['<webhook_signature_param>'] == b64encode(hmacsha256digest(secret('webhook_secret'), request_body)) %}{% else %}FAIL!{% endif %}"
    },
    "type": "pipe"
  }

Partial webhook events
----------------------

Need to do a lookup to find the complete entity. Avoid doing the lookup in the pipe that receives the event, as the lookup can take time and block the receiver. Instead set up a pipeline with two pipes and call the second one ``-event2``. For more information see section :ref:`parametrized input <parameterized-datatypes>`.

Example: -event2 pipe
----------------------

::

  {
      "_id": "<system>-<datatype>-event2",
      "namespaced_identifiers": false,
      "sink": {
        "deletion_tracking": false,
        "set_initial_offset": "onload"
      },
      "source": {
        "dataset": "<system>-<datatype>-event",
        "type": "dataset"
      },
      "transform": [
        {
          "allowed_status_codes": "200,404",
          "operation": "<datatype>-lookup",
          "replace_entity": false,
          "response_status_property": "status",
          "system": "<system>",
          "type": "rest"
        },
        {
          "rules": {
            "default": [
              [
                "if",
                [
                  "neq",
                  404,
                  "_S.status"
                ],
                [
                  "merge",
                  "_S.response"
                ]
              ]
            ]
          },
          "type": "dtl"
        }
      ],
      "type": "pipe"
    }


Shared webhook events
---------------------

If multitenant, receive all in one dataset and use subset expression with tenant id to filter out relevant events into tenant pipes. The tenant pipe should be called ``-event``.
If when webhook events are shared, we need to separate them into datatype specific pipes before merging.

If we have webhooks they need to combine with full scan pipes in the collect pipe.

Example: -collect pipe (webhook)
--------------------------------

::

  {
      "_id": "<system>-<datatype>-collect",
      "exclude_completeness": [
        "<system>-<datatype>-share",
        "<system>-<datatype>-event2",
        "<system>-<datatype>-collect"
      ],
      "namespaced_identifiers": false,
      "pump": {
        "run_at_startup_if_not_populated": true
      },
      "source": {
        "datasets": [
          "<system>-<datatype>-all",
          "<system>-<datatype>-event2"
        ],
        "type": "merge_datasets"
      },
      "transform": [
        {
          "properties": {
            "operation_lookup_delete": "<datatype>-lookup",
            "primary_key": "id",
            "rest_system": "<system>",
            "share_dataset": "<system>-<datatype>-share"
          },
          "template": "transform-collect-rest",
          "type": "template"
        },
        {
          "rules": {
            "default": [
              [
                "copy",
                "*"
              ]
            ]
          },
          "type": "dtl"
        }
      ],
      "type": "pipe"
    }