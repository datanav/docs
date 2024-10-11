.. _verify_deletes:

Verify deletes
==============

For different reasons source systems may return unreliable results, e.g. :ref:`empty responses <sporadic-empty-response>`. Often :ref:`circuit breakers <circuit_breakers>` may help to remedy these situations, but they do not catch all potential scenarios. 

Incorrect deletes are especially problematic as they could propagate delete requests to other systems. By *verifying deletes* we can ensure that entities registered as deleted in Sesam are actually deleted in the source system. 

We do this by performing a *lookup* operation for each specific entity in the source system. We use the lookup to check if the entity exists and set the ``_deleted`` value accordingly.

Example:

::

  {
    "transform": [{
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["if",
            ["eq", "_S._deleted", true],
            ["if",
              ["is-not-empty",
                ["hops", {
                  "datasets": ["<system>-<datatype>-collect s"],
                  "where": [
                    ["eq", "_S._id", "s._id"]
                  ],
                  "track-dependencies": false
                }]
              ],
              ["add", "$operation", "lookup-delete"]
            ]
          ]
        ]
      }
    },
      {
      "type": "rest",
      "system": "<system>",
      "allowed_status_codes": "200,404",
      "operation": "<datatype>-lookup",
      "replace_entity": false,
      "response_property": "response_body",
      "response_status_property": "response_status",
      "side_effects": false,
      "trigger_on": {
        "key": "$operation",
        "value": "lookup-delete"
      }
    },
      {
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*",
            ["list", "response_body", "response_status", "$operation"]
          ],
          ["if",
            ["and",
              ["eq", "_S.$operation", "lookup-delete"],
              ["eq", "_S.response_status", 200]
            ],
            ["add", "_deleted", false]
          ]
        ]
      }
    }]
  }   

This pattern is also available in the :ref:`collect template <template_transform_collect_rest>` by adding the ``operation_lookup_delete`` and ``rest_system`` properties.