Registering webhooks
====================
.. _registering_webhooks:

The pipe should be called ``-registerwebhook``.

Example: -registerwebhook pipe
------------------------------

::

   {
      "_id": "xxxxxx-datatype-registerwebhook",
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
            "_id": "datatype-create",
            "_updated": 0,
            "properties": {
              "webhook": {
                "address": "$ENV(service_url)/receivers/xxxxxx-datatype-event/entities",
                "topic": "datatype/create"
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
                        "xxxxxx-datatype-registerwebhook sink"
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
          "system": "xxxxxx",
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
                "comment",
                "TODO: we should compare the state of the actual object vs our desired state."
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
          "system": "xxxxxx",
          "type": "rest"
        }
      ],
      "type": "pipe"
    }

* ``webhook-insert`` operation should be added to the system configuration.