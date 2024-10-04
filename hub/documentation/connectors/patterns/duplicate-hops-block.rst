.. _duplicate-hops-block:

Duplicate hops block
====================

When performing inserts, especially when doing it while implementing the :ref:`namespace split pattern <namespace_split>`, its important to ensure that en entity can only go through the :ref:`insert pattern <insert_pattern>` once. 

The idea behind the namespace split pattern is to always have the correct ``_id`` value in entities coming into the ``-share`` pipe. However, once you shift the ``_id`` the old entity (which is now ``_deleted: true`` and ``$replaced": true``) will still propagate the ``-share`` pipe. 

As a safety measure to ensure an entity is only inserted once we add a :ref:`hops <hops>` in the share pipe to the pipe's sink dataset. If the entity exists in the sink dataset as a successful insert we know we should not attempt to insert it again.

Example:

::

  {    
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          ["if",
            ["is-not-empty",
              ["filter",["is-not-null", "_."],
                ["hops", {
                  "datasets": ["<sink-dataset> st"],
                    "where": [
                      ["eq", "_S.$ids",
                        ["ni", "st._id"]
                      ]     
                    ],
                    "return": "st.<previous-insert-response>",
                    "track-dependencies": false
                }]
              ]
            ],
            ["add", "$discard", "already-inserted"]
          ]
        ]
      }
    }
  }