Feedback loop
-------------
Expensive hops or external transforms is best to do in a separate dataflow. This allows you to optimise what you process using subsets, the primary dataflow does not have to wait for this data, it will be processed later if it applied to the entity. Entities might be processed twice if the feedback affected the entity. Use the ``_id`` of the merge source as the identifier. Make sure the feedback is marked as deleted when the data that produced it no longer exists (otherwise entities will never be deleted due to the feedback entity itself).

Example feedback pipe:

.. code::
  
  {
    "_id": "test-feedback",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-test"
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          [
            "if",
            [
              "matches",
              "test-feedback:*",
              "_S._id"
            ],
            [
              "filter"
            ],
            [
              "add",
              "_id",
              [
                "concat",
                "test-feedback:",
                "_S._id"
              ]
            ]
          ],
          [
            "add",
            "$ids",
            "_S.$ids"
          ],
          [
            "add",
            "example-property",
            "foo"
          ]
        ]
      }
    }
  }

And how it's used in the connect pipe:

.. code::

 {
    "_id": "global-test",
    "type": "pipe",
    "source": {
      "type": "merge",
      "datasets": [
        "test-a a",
        "test-b b",
        "test-feedback f"
      ],
      "equality_sets": [
        [
          "a.$ids",
          "b.$ids",
          "f.$ids"
        ]
      ],
      "identity": "first",
      "strategy": "compact",
      "version": 2
    },
    "transform": {
      "type": "dtl",
      "rules": {
        "default": [
          [
            "copy",
            "*"
          ],
          [
            "if",
            [
              "matches",
              "test-feedback:*",
              "_S._id"
            ],
            [
              "filter",
              false
            ]
          ]
        ]
      }
    }
  }
