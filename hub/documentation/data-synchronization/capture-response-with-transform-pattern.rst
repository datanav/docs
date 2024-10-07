.. _capture_response_with_transform:

Capture response with transform
-------------------------------

When using a sink to communicate with an external system the response from the system is not captured. This can cause problems when you are dependent of a response for further logic, e.g. doing :ref:`bidirectional synchronizaion <bidirectional-synchronization>`. In these cases we should use the transform instead of the sink to communicate with the system. The response from the system can now be stored in the sink dataset instead and be available for further logic when required. This also helps in troubleshooting as many system respond is both error codes and error messages describing the current issue.

This pipe needs to be durable to avoid reprocessing in case of data loss and the batch size needs to be set to 1 to avoid duplicates as this is not transactional. Also, do not mix dependency tracking in this pipe as it can cause duplicates. 

Be wary of previewing non idempotent operations (such as inserts) as this will trigger the transform (the :ref:`rest transform <REST_transform>` has the property :ref:`side_effects <REST_transform_properties>` for this reason).

REST transform example:

::
  
    {
      "transform": {
          "type": "chained",
          "transforms": [
          {
              "rules": {
              "default": [
                  ["copy", "_id"],
                  ["add", "$payload", "_S."]
                  ["if",
                  ["all",
                      ["is-null", "_."],
                      ["map",
                      ["path", "_.", "_S."],
                      ["literal", "id"]
                      ]
                  ],
                  ["add", "$operation", "inserts"]
                  ]
              ]
              },
              "type": "dtl"
          },
          {
              "type": "rest",
              "system": "<system>",
              "allowed_status_codes": "100-428,430-599",
              "operation": "<datatype>-insert",
              "replace_entity": false,
              "response_property": "response_body",
              "response_status_property": "response_status",
              "side_effects": true,
              "trigger_on": {
              "key": "$operation",
              "value": "insert"
              }
          },
          {
              "type": "dtl",
              "rules": {
              "default": [
                  ["copy", "*"],
                  ["if",
                  ["not",
                      ["in", "_S.response_status", 
                      ["list", 200, 201, 204]
                      ]
                  ],
                  ["add", "$error", "error-insert"],
                      [
                      ["add", "$generated_id", 
                          ["first", "_S.response_body.<primary-key>"]
                      ],
                      ["if",
                          ["any", 
                          ["is-null", "_."], "_T.$generated_id"],
                          [
                          "trip!",
                          "Generated primary key is incomplete or not found"
                          ]
                      ]
                      ]
                  ]
                  ]
              ]
              }
          }
          ]
      },
      "namespaced_identifiers": false
    }