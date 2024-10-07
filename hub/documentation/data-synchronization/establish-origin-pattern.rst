.. _establish_origin_pattern:

Establish origin pattern
------------------------

In a :ref:`bidirectional synchronizaion <bidirectional-synchronization>` duplicate issues may arise if we no not know which entity from system *A* created which entity from system *B*. Without this relationship clearly established the new entity in system *B* might attempt to insert yet another entity into system *A* (because there might not be a connection between these two entities in the metadata).

In Sesam we solve this issue with the *establish origin pattern*. This pattern has one external requirement:

- When an entity is inserted into a system, the system's response has to include the new system specific primary key of the new entity. 

To be able to establish the origin of an inserted entity inserts into system *A* need to be done through the :ref:`capture response with transform pattern <capture_response_with_transform>` which allows us to capture the response from the system, including the newly generated primary key

Example:

::

  "transform": {
    "type": "dtl",
    "rules": {
      "default": [
        ["copy", "*"],
        ["merge-union",
          ["map",
            ["dict", "origin_entity", "_."],
            ["hops", {
              "datasets": ["<system>-<datatype>-share st"],
              "where": [
                ["eq", "_S.<primary-key", "st.<$generated_id>"]
              ],
              "track-dependencies": false
            }]
          ]
        ],
        ["add-if", "$origin", "_T.origin_entity.$origin"],
        ["remove", "origin_entity"]
      ]
    }
  }