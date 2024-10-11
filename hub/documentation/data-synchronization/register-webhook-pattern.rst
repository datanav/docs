Registering webhooks
====================
.. _registering_webhooks:

The pipe should be called ``-registerwebhook``.

Example: -registerwebhook pipe
------------------------------

::

   {
      "_id": "<system>-<datatype>-registerwebhook",
      "namespaced_identifiers": false,
      "pump": {
        "run_at_startup_if_not_populated": true
      },
      "sink": {
        "deletion_tracking": false,
        "set_initial_offset": "onload"
      },
      "source": {
        "entities": [
          {
            "_id": "<datatype>-create",
            "_updated": 0,
            "properties": {
              "webhook": {
                "address": "<service_url>/receivers/<system>-<datatype>-event/entities",
                "topic": "<datatype>/create"
              }
            }
          }
          }
        ],
        "supports_since": true,
        "type": "embedded"
      },
      "transform": [
        {
          "rules": {
            "default": [
              [
                "copy",
                "properties"
              ],
              [
                "add",
                "id",
                [
                  "first",
                  [
                    "hops",
                    {
                      "datasets": [
                        "<system>-<datatype>-registerwebhook sink"
                      ],
                      "return": [
                        "first",
                        "sink.insert_response.value.id"
                      ],
                      "where": [
                        [
                          "eq",
                          "_S._id",
                          "sink._id"
                        ]
                      ]
                    }
                  ]
                ]
              ],
              [
                "add",
                "$operation",
                [
                  "if",
                  [
                    "is-not-null",
                    "_T.id"
                  ],
                  "lookup",
                  "insert"
                ]
              ]
            ]
          },
          "type": "dtl"
        },
        {
          "allowed_status_codes": "200,404",
          "operation": "webhook-lookup",
          "replace_entity": false,
          "response_property": "lookup_response",
          "response_status_property": "lookup_status_code",
          "side_effects": false,
          "system": "<system>",
          "trace": true,
          "trigger_on": {
            "key": "$operation",
            "value": "lookup"
          },
          "type": "rest"
        },
        {
          "rules": {
            "default": [
              [
                "add",
                "payload",
                [
                  "dict",
                  "webhook",
                  "_S.properties.webhook"
                ]
              ],
              [
                "copy",
                "*"
              ],
              [
                "discard",
                [
                  "or",
                  [
                    "eq",
                    404,
                    "_T.lookup_status_code"
                  ],
                  [
                    "eq",
                    "_S.$operation",
                    "insert"
                  ]
                ]
              ]
            ]
          },
          "type": "dtl"
        },
        {
          "allowed_status_codes": "200,201",
          "operation": "webhook-insert",
          "replace_entity": false,
          "response_property": "insert_response",
          "response_status_property": "insert_status_code",
          "side_effects": true,
          "system": "<system>",
          "type": "rest"
        }
      ],
      "type": "pipe"
    }

* ``webhook-insert`` operation should be added to the system configuration. Make sure to set webhook_secret if necessary.
* A full connector example of ``-registerwebhook`` pipe can be found in the `Shopify connector's playground branch <https://github.com/sesam-io/shopify-connector/blob/playground>`__ in the `order template <https://github.com/sesam-io/shopify-connector/blob/playground/templates/order.json>`__.

Wiping webhooks
---------------

The pipe to wipe webhooks should be called ``-wipe``.

Example: -wipe pipe
-------------------

::

     {
    "_id": "<system>-<datatype>-wipe",
    "namespaced_identifiers": false,
    "pump": {
      "mode": "manual",
      "run_at_startup_if_not_populated": true
    },
    "source": {
      "dataset": "<system>-<datatype>-collect",
      "type": "dataset"
    },
    "transform": [
      {
        "rules": {
          "default": [
            [
              "copy",
              "*"
            ],
            [
              "discard",
              [
                "matches",
                "https://*.sesam.cloud/*",
                "_S.address"
              ]
            ]
          ]
        },
        "type": "dtl"
      },
      {
        "operation": "<datatype>-delete",
        "response_status_property": "status_code",
        "system": "<system>",
        "trace": true,
        "trigger_on": {
          "key": "_deleted",
          "value": false
        },
        "type": "rest"
      }
    ],
    "type": "pipe"
  }

A full connector example of ``-wipe`` pipe can be found in the `Shopify connector's playground branch <https://github.com/sesam-io/shopify-connector/blob/playground>`__ in the `webhook template <https://github.com/sesam-io/shopify-connector/blob/playground/templates/webhook.json>`__.
