.. _time-based-masterdata-management:

=========================================
Time-based masterdata management in Sesam
=========================================

Summary
-------

Time-based master data management ensures that the most recently updated system becomes the master of a property, rather than assigning a specific system as the master for a given property. This approach is useful when no single system can be designated as the master for a particular type of data. In practice, it's often more important to have the latest version of the data—such as an employee's phone number or a customer's email address—regardless of which system it comes from. If a customer updates their phone number in one system, you don't want an outdated number from another system to override it. Time-based master data management always selects the most recent update as the master value, regardless of the source system.

This section covers best practices in how to implement time-based masterdata management in Sesam and the effects is has.

Claims
------

In order to do time-based masterdata management, every property needs a datetime corresponding to the date and time the property was last modified. In Sesam, the preferred way of implementing this is as ``claims``. A claim is a collection of metadata for each property. The property's value is one claim property, but also which entity/system the property originated from, the status of the claim (is it the newest one or an old claim) as well as a datetime property telling us when the property was last updated. We can now rewrite the key-value ``<property>: <value>`` as ``<property>: <claimDict>`` where ``claimDict`` is a dictionary containing the claim data. In the example below, ``claimDict`` contains the property's value, its $last-modified datetime, and the claim's end-time, which is when the claim got replaced by a newer claim. These are the ``claim properties``.

|start-h3| Example |end-h3|

::

  "<property>": 
    {
      "value": "value",
      "$last-modified": "~t1987-09-11:T06:55:07.456827Z",
      "end-time": "~t2024-09-20T07:18:20.698042Z"
    }

Last modified value
-------------------

In order to perform time-based masterdata management, each claim requires a datetime value describing when each specific property last changed in the source system. However, not every system has last modified datetime values for each property. Some systems might only have a datetime value on the entity as a whole, while some systems might not have any datetime value. In all three cases we need to be able to supply the claim with a near real-time datetime value in order to perform accurate time-based masterdata management. The different scenarios are described below in order of priority:

1. The system provides last modified datetime values for each individual property

  * In this case the system provided datetime values are directly added to each corresponding claim's ``$last-modified`` value

2. The system provides last modified datetime values for each entity

  * In this case we use the provided datetime value as the initial ``$last-modified`` but manually update the ``$last-modified`` value when the claim value changes 

3. The system does not provides any last modified datetime values on property or entity level

  * In this case we use Sesam's internal ``_ts`` value from the ``-collect`` pipe as initial $last-modified value and manually update the ``$last-modified`` value when the claim value changes 


A full DTL example on how to set and update $last-modified values in claims can be seen at the bottom of this page.

Masterdata management
---------------------

Now that we have up-to-date datetime values inside each property claim we can perform time-based masterdata management inside our :ref:`global pipes <whatis-global>`. Instead of using the :ref:`coalesce function <coalesce_dtl_function>` to set system priority we can sort claims by the newest ``$last-modified`` value and pick that claim value corresponding to the newest claim.

|start-h3| Example |end-h3|

::

  ["add", "<property>",
    ["path", "value",
      ["last",
        ["sorted", "_.$last-modified",
          ["filter",
            ["is-empty", "_.end-time"], "_T.<property>"]
        ]
      ]
    ]
  ]

DTL examples
------------

Set and update ``$last-modified``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::
  
  "transform": {
    "type": "dtl",
    "rules": {
      "default": [
        ["comment", "locating the last version of the entity in the sink dataset"],
        ["add", "_history",
          ["apply", {
            "datasets": ["<sink-dataset> t"],
            "where": [
              ["eq", "_S.<primary-key>", "t._id"]
            ],
            "track-dependencies": false
          }]
        ],
        ["merge",
          ["apply", "history",
            ["dict", "key", "age", "value", 
              ["dict", "value", "_S.age", "_S.$last-modified"]
            ]
          ]
        ]
      ],
      "history": [
        ["add", "_property", "_S.value"],
        ["add", "_pid", "_P._T._id"],
        ["comment", "locating the last version of the property"],
        ["add", "_property-history",
          ["path", "_S.key",
            ["if",
              ["and",
                ["eq",
                  ["count", "_R._T._history"], 1],
                ["is-empty", "_T._pid"]
              ],
              ["first", "_R._T._history"],
              ["filter",
                ["eq", "_._id", "_T._pid"], "_R._T._history"]
            ]
          ]
        ],
        ["add", "_property-history-newer",
          ["filter",
            ["gt", "_.$last-modified", "_R._T.$last-modified"], "_T._property-history"]
        ],
        ["if",
          ["eq",
            ["count", "_T._property-history"], 0],
          ["add", "_S.key", "_S.value"],
          [
            ["comment", "Ignore new data if older than history"],
            ["if",
              ["gt",
                ["count", "_T._property-history-newer"], 0],
              ["add", "_S.key", "_T._property-history"],
              [
                ["add", "_property-history-latest",
                  ["filter",
                    ["is-empty", "_.end-time"], "_T._property-history"]
                ],
                ["add", "_property-history-old",
                  ["filter",
                    ["is-not-empty", "_.end-time"], "_T._property-history"]
                ],
                ["add", "_property-compare",
                  ["map",
                    ["apply", "match-dict",
                      ["dict", "source", "_.", "target", "_T._property-history-latest"]
                    ], "_T._property"]
                ],
                ["add", "_property-history-compare",
                  ["map",
                    ["apply", "match-dict",
                      ["dict", "source", "_.", "target", "_T._property-compare.match"]
                    ], "_T._property-history-latest"]
                ],
                ["add", "_S.key",
                  ["combine",
                    ["apply", "add-end", "_T._property-history-compare.new"],
                    ["apply", "add-end", "_T._property-history-old"]
                  ]
                ]
              ]
            ],
            ["remove", "_property*"]
          ]
        ]
      ],
      "match-dict": [
        ["add", "key", "_P._S.key"],
        ["if",
          ["in", true,
            ["map",
              ["eq",
                ["apply", "strip-dates", "_S.source"],
                ["apply", "strip-dates", "_."]
              ], "_S.target"]
          ],
          ["add", "::match", "_S.source"],
          ["add", "::new", "_S.source"]
        ]
      ],
      "strip-dates": [
        ["copy", "ps:*"],
        ["if",
          ["neq", "_P._T.key", "end-time"],
          ["remove", "end-time"]
        ],
        ["if",
          ["neq", "_P._T.key", "$last-modified"],
          ["remove", "$last-modified"]
        ]
      ],
      "add-end": [
        ["copy", "*"],
        ["if",
          ["is-empty", "_S.end-time"],
          ["add", "end-time", "_R._T._$last-modified"]
        ],
        ["merge",
          ["dict",
            ["items", "_T."]
          ]
        ]
      ]
    }
  }


The example above also handles old claims and makes sure 

.. |start-h3| raw:: html

     <h3>

.. |end-h3| raw:: html

     </h3>