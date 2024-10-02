.. _namespace_split:

Namespace split pattern
------------------------

When multiple entities from different systems merge in a :ref:`global pipe <whatis-global>` we end up with an ``$ids`` array containing the ``_id`` values of the merged entities. The new ``_id`` value of the entity is determined by the order of the datasets in the ``datasets`` property in the global pipes :ref:`merge source <merge_source>`. 

If two entities, *a* from system *A* and *b* from system *B* merge in a global pipe only one if the ``_id`` values will be kept as the new ``_id`` (with default merge source settings). The result is that an entity with ``_id`` from system *A* can update data in system *B*, which is not semantically correct and could cause some potential duplicate issues when doing :ref:`bidirectional synchronization <bidirectional-synchronization>`.

The ``namespace split pattern`` is a pattern for releasing the correct version of the entity to each ``-transform`` pipe by adding a ``-transform-split`` between the global pipe and the ``-transform`` pipe which in turn output the source entity with the correct ``_id`` value.

Example:

::

  {
    "_id": "<system>-<datatype>-transform-split",
    "type": "pipe",
    "source": {
      "type": "dataset",
      "dataset": "global-<global-datatype>"
    },
    "transform": [{
      "type": "dtl",
      "rules": {
        "default": [
          ["copy", "*"],
          ["if",
            ["in", "<system>-<datatype>",
              ["map",
                ["ni-ns", "_."], "_S.$ids"]
            ],
            [
              ["create",
                ["apply", "emit",
                  ["filter",
                    ["eq",
                      ["ni-ns", "_."], "<system>-<datatype>"], "_S.$ids"]
                ]
              ]
            ],
            [
              ["create",
                ["apply", "emit-new",
                  ["list", "_S.$ids"]
                ]
              ]
            ]
          ],
          ["discard"]
        ],
        "emit": [
          ["merge-union", "_R._T"],
          ["add", "_id",
            ["string", "_S."]
          ],
          ["add", "$ids", "_R._S.$ids"],
          ["add", "<system>-<datatype>:id",
           ["ni-id", "_S."]
          ],
          ["add", "_deleted", "_R._S._deleted"]
        ],
        "emit-new": [
          ["merge-union", "_R._T"],
          ["add", "_id", "_R._S._id"],
          ["add", "_deleted", "_R._S._deleted"]
        ]
      }
    }],
    "add_namespaces": false
  }
