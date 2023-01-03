Golden property based on last updated
-------------------------------------
Make sure you have a reliable timestamp from the source that you propagate. Think about feedback loops if data is synced back. Can be good to standardise on e.g. ``$last_updated``.

Example enrich pipe:

.. code::

 {
  "_id": "test-enrich",
  "type": "pipe",
  "source": {
    "type": "dataset",
    "dataset": "test",
    "include_previous_versions": true
  },
  "sink": {
    "set_initial_offset": "onload"
  },
  "transform": {
    "type": "dtl",
    "rules": {
      "default": [
        ["copy", "*"],
        ["add", "$updated",
          ["dict",
            ["flatten",
              ["list",
                ["items",
                  ["first",
                    ["hops", {
                      "datasets": ["test-enrich t"],
                      "where": [
                        ["eq", "_S._id", "t._id"]
                      ],
                      "return": "t.$updated",
                      "track-dependencies": false
                    }]
                  ]
                ],
                ["items",
                  ["apply", "is-changed",
                    ["filter",
                      ["not",
                        ["matches", "_*", "_.key"]
                      ],
                      ["key-values", "_S."]
                    ]
                  ]
                ]
              ]
            ]
          ]
        ]
      ],
      "is-changed": [
        ["if",
          ["is-changed",
            ["path", "_P._S.key", "_."]
          ],
          ["discard"],
          ["add", "_S.", "_P._S.$last-update"]
        ]
      ]
    }
  },
  "batch_size": 1,
  "namespaces": {
    "identity": "test",
    "property": "test"
  }
 }
 
Example connect pipe:

.. code::

 {
  "_id": "global-test",
  "type": "pipe",
  "source": {
    "type": "merge",
    "datasets": ["test-update t", "test-update2 t2"],
    "equality_sets": [
      [
        ["ni-id",
          ["ni", "t._id"]
        ],
        ["ni-id",
          ["ni", "t2._id"]
        ]
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
        ["add", "$updated",
          ["dict",
            ["items", "_S.$updated"]
          ]
        ],
        ["add", "x",
          ["first",
            ["values",
              ["apply", "newest",
                ["list",
                  ["list", "test:x", "test2:x"]
                ]
              ]
            ]
          ]
        ],
        ["add", "y",
          ["first",
            ["values",
              ["apply", "newest",
                ["list",
                  ["list", "test:y", "test2:y"]
                ]
              ]
            ]
          ]
        ]
      ],
      "newest": [
        ["add", "_x",
          ["first",
            ["sorted-descending", "_.value",
              ["key-values",
                ["map-dict",
                  ["if",
                    ["in", "_.", "_S."], "_."], "_.", "_R._T.$updated"]
              ]
            ]
          ]
        ],
        ["add", "_x",
          ["first",
            ["values",
              ["map-dict",
                ["if",
                  ["eq", "_.", "_T._x.key"], "_."], "_.", "_R._S"]
            ]
          ]
        ]
      ]
    }
  },
  "metadata": {
    "global": true
  }
 }
