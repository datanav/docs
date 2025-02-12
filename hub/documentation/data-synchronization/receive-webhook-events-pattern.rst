.. _receive_webhook_events:

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

* When testing the webhooks with `Sesampy <https://github.com/sesam-community/sesam-py/blob/master/README.md>`__ on dev nodes, this is not automatically handled and you may need to manually put the ``client_secret`` value into the validation expression.

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

A full connector example of an ``-event`` pipe can be found in the `Tripletex connector's playground branch <https://github.com/sesam-io/tripletex-connector/blob/playground>`__ in the `contact template <https://github.com/sesam-io/tripletex-connector/blob/playground/templates/contact.json>`__.

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
                  "eq",
                  "<webhook_filter_criteria>.deletion",
                  "_S.<property>"
                ],
                [
                  "add",
                  "_deleted",
                  true
                ]
              ],
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
                ],
                [
                "discard",
                [
                  "eq",
                  "<webhook_filter_criteria>.deletion",
                  "_S.<property>"
                ]
                ]
              ]
            ]
          },
          "type": "dtl"
        }
      ],
      "type": "pipe"
    }

A full connector example of ``-event2`` pipe can be found in the `Hubspot connector's playground branch <https://github.com/sesam-io/hubspot-connector/blob/playground>`__ in the `company template <https://github.com/sesam-io/hubspot-connector/blob/playground/templates/company.json>`__.

Shared webhook events
---------------------

If webhook events are shared, we need to separate them into datatype specific pipes before merging. When all events, regardless of their datatype, are received by a single pipe, we can filter out relevant events using a :ref:`subset <dataset_source>` expression. This allows us to route events of a specific datatype to another pipe.

* A webhook dataset gathers all incoming webhook events.
* The -event pipe filters and processes webhooks for a specific datatype, using a subset expression to select the relevant events.

Example: -event pipe with subset expression
-------------------------------------------

::

  {
    "_id": "<system>-<webhook_filter_criteria>-event",
    "namespaced_identifiers": false,
    "sink": {
      "deletion_tracking": false,
      "set_initial_offset": "onload"
    },
    "source": {
      "dataset": "<hubspot_webhook_dataset>",
      "subset": [
        "eq",
        [
          "matches",
          "<webhook_filter_criteria>.*",
          [
            "list",
            "_S.<property>"
          ]
        ],
        true
      ],
      "type": "dataset"
    },
    "type": "pipe"
  }

A full connector example of ``-event`` pipe with subset expression can be found in the `Hubspot connector's playground branch <https://github.com/sesam-io/hubspot-connector/blob/playground>`__ in the `company template <https://github.com/sesam-io/hubspot-connector/blob/playground/templates/company.json>`__.


Combining regular data (non event) and event data
-------------------------------------------------

If we have webhooks we need to combine them with full scan pipes in the collect pipe.

Example: -collect pipe (webhook)
--------------------------------

::

  {
      "_id": "<system>-<datatype>-collect",
      "namespaced_identifiers": false,
      "source": {
        "datasets": [
          "<system>-<datatype>-all",
          "<system>-<datatype>-event2"
        ],
        "type": "merge_datasets"
      },
      "type": "pipe"
    }

A full connector example of ``-collect`` pipe can be found in the `Hubspot connector's playground branch <https://github.com/sesam-io/hubspot-connector/blob/playground>`__ in the `company template <https://github.com/sesam-io/hubspot-connector/blob/playground/templates/company.json>`__.
