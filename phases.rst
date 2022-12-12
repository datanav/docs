.. guide_phases

======
Phases
======

This document describes the various phases that entities which are
read from and written to connectors go through. The document also
defines properties that are used to manage the lifecycle of data in
these phases.

-------
Collect
-------

A connector collects raw entities from systems into collect
datasets. These entities do not have any namespaces on them.

------
Enrich
------

Add ``$share_id`` property
--------------------------

::

    ["add", "share_id",
      ["flatten",
        ["hops", {
          "datasets": ["hubspot-26626063-hubspot-company-share-insert chi"],
          "where": [
            ["eq", "_S.$share_id", "chi.$share_id"]
          ],
          "return": "chi.$share_id"
        }]
      ]
    ],

Add ``$modified`` property
--------------------------

::

     ["add", "$modified",
      ["dict",
        ["flatten",
          ["list",
            ["items",
              ["first",
                ["hops", {
                  "datasets": ["hubspot-26626063-hubspot-company-enrich t"],
                  "where": [
                    ["eq", "_S._id", "t._id"]
                  ],
                  "return": "t.$modified",
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

The referenced ``is-changed`` named rule:

::

    "is-changed": [
      ["if",
        ["is-not-empty", "_P._T._prefix"],
        ["add", "_prefix",
          ["concat", "_P._T._prefix", ".", "_S.key"]
        ],
        ["add", "_prefix", "_S.key"]
      ],
      ["if",
        ["eq",
          ["is-changed",
            ["path", "_T._prefix", "_."]
          ], false],
        ["discard"],
        ["add", "_T._prefix", "_R._S.$last-modified"]
      ],
      ["if",
        ["is-dict", "_S.value"],
        ["merge-union",
          ["apply", "is-changed",
            ["key-values", "_S.value"]
          ]
        ]
      ]
    ]

-------
Connect
-------

Inbound property mapping
------------------------

- This phase is where entities from different connectors's types get
  merged and where inbound mapping rules are applied to produce global
  datasets with golden properties.

---------
Transform
---------

Outbound property mapping
-------------------------

- The *transform* phase project global properties down to only the
  properties specified in the connector type's
  ``share_properties``. The projection uses the *inverse mapping* of
  the global properties.

Split duplicates into separate entities
---------------------------------------

- If the source entity has more than one system specific id then it
  must be split up into multiple entities — one per id, so that
  updates can be made for each of them individually. The system
  specific ids can probably be inferred from ``$ids`` by extracting
  those with the enrich phase namespace.


TODO: How to rewrite property values, i.e. enums?

TODO: If entity is a merge of multiple entities from this particular system, then the transform phase must split them into separate entities.

-----
Share
-----

The *share* phase takes the desired state defined in the *transform*
phase and applies it to the connector's system. It also keeps track of
identifiers that get created in the insert path defined below. These
identifiers are used to keep track of the system specific identities
of entities, and also used to keep a mapping of them across systems
when they refer to the same thing.


Inserts
-------

- Discard ``_deleted=true``. Deletes should be handled by the delete path.

  ::

      ["discard",
        ["not", "_S._deleted"]
      ],

- Discard if system specific primary id exists, e.g. ``id``. The object has already been inserted.

  ::

      ["discard",
        ["is-null", "_S.id"]
      ],

- Discard if entity already exists in the insert sink dataset (join
  key is ``$share_id``) – unless we want to recreate it that is.

  ::

     ["discard",
       ["is-empty",
         ["hops", {
           "datasets": ["hubspot-26626063-hubspot-company-share-insert chi"],
           "where": [
             ["eq", "_S.$share_id", "chi.$share_id"]
           ],
           "track-dependencies": false
         }]
       ]
     ],

- Prepare REST insert payload

  ::

      ["add", "::payload",
        ["dict", "properties", "_S.properties"]
      ],
      ["copy", "$share-id"]

- Insert payload through REST transform

  .. NOTE::

     What to do if we get a conflict? Discard it?

  ::

      {
          "type": "rest",
          "system": "hubspot-26626063-hubspot",
          "operation": "insert",
          "properties": {
            "url": "companies"
          },
          "replace_entity": false,
          "side_effects": true
      }

- Save response in sink dataset with a specific shape: ``$share_id``,
  ``_id`` bound to system primary id, and the response payload.

  Ideally we should store the entire response, including status
  code, headers and body, so that we know what happened.

  ::

     {
       "type": "dtl",
       "rules": {
         "default": [
           ["copy", "$sesam-id"],
           ["merge-union", "_S.response"],
           ["add", "_id", "_T.id"]
         ]
       }
     }

Updates
-------

- Discard ``_deleted=true``.  Deletes should be handled by the delete path.

  ::

      ["discard",
        ["not", "_S._deleted"]
      ],

- Discard if system specific primary id does not exist,
  e.g. ``id``. The entity does not exist in the system, and this
  should be handled by the insert path.

  ::

      ["discard",
        ["is-not-empty", "_S.id"]
      ],

- Prepare REST lookup payload

  ::

      ["add", "::properties",
        ["dict", "url",
          ["concat", "companies/", "_S.id", "?properties=hs_analytics_first_timestamp,hs_analytics_last_timestamp,hs_analytics_last_visit_timestamp,hs_analytics_num_page_views,hs_analytics_num_visits,engagements_last_meeting_booked,engagements_last_meeting_booked_campaign,engagements_last_meeting_booked_source,hs_last_booked_meeting_date,hs_last_logged_call_date,hs_last_open_task_date,hs_last_sales_activity_timestamp,hs_lastmodifieddate,notes_last_contacted,notes_last_updated,notes_next_activity_date,num_contacted_notes,about_us,address,address2,annualrevenue,city,closedate,country,createdate,days_to_close,description,domain,engagements_last_meeting_booked_medium,first_contact_createdate,founded_year,hs_analytics_last_touch_converting_campaign,hs_analytics_source,hs_analytics_source_data_1,hs_analytics_source_data_2,hs_createdate,hs_num_child_companies,hs_object_id,hs_parent_company_id,industry,is_public,lifecyclestage,name,num_associated_contacts,numberofemployees,phone,state,timezone,total_money_raised,total_revenue,type,web_technologies,website,zip,hs_analytics_first_touch_converting_campaign,hs_analytics_first_visit_timestamp,first_deal_created_date,hs_num_open_deals,hs_total_deal_value,num_associated_deals,recent_deal_amount,recent_deal_close_date,hs_lead_status,hubspot_owner_assigneddate,hubspot_owner_id,hubspot_team_id,facebook_company_page,facebookfans,googleplus_page,linkedin_company_page,linkedinbio,twitterbio,twitterfollowers,twitterhandle,hs_ideal_customer_profile,hs_is_target_account,hs_num_blockers,hs_num_contacts_with_buying_roles,hs_num_decision_makers&"]
        ]
      ],
      ["add", "entity", "_S."]

- Send it through REST transform to look up existing version

  ::

      {
        "type": "rest",
        "system": "hubspot-26626063-hubspot",
        "operation": "get",
        "replace_entity": false
      }

- Perform logic to decide if update can proceed or if we should
  discard the update (here we can use the new
  ``<collect-namespace>:$based_on`` property).

- Prepare REST update payload + send it to the REST sink to perform the
  update.

  ::

      "sink": {
        "type": "rest",
        "system": "hubspot-26626063-hubspot",
        "operation": "update"
      },

- TODO: Should we update the insert sink dataset?

Deletes
-------

- Discard ``_deleted=false``. Entity is not deleted, so should be handled by insert or update paths.

  .. NOTE::

     Are we sure we get ``_deleted=true`` for all the to be deleted entities?

  ::

      ["discard",
        "_S._deleted"
      ],

- Discard if system specific primary id does not exist,
  e.g. ``id``. The entity does not exist in the system, and this
  should be handled by the insert path.

  ::

      ["discard",
        ["is-not-empty", "_S.id"]
      ],

- TODO: do we actually have to look up the entity in the target system, or do we just blindly delete it? UPDATE: do GET and make decision on the $based_on.

- DELETE: prepare REST payload + send it to the REST sink to perform the
  update

- TODO: Should we update the insert sink dataset?

------
Issues
------

- How to handle adding new systems later? There might be problems with the last modified strategy. Is the new data considered more recently updated than the data that has previously been imported from other systems. Suspect that we'll have to set last modified to be in the past on initial load.

----------
Properties
----------

.. list-table::
   :header-rows: 1
   :widths: 20, 80

   * - Property
     - Description

   * - ``<collect-namespace>:$based_on``
     - Contains the raw properties needed in the *share*
       dataset. The property is created in the *enrich* phase and
       flows downstream all the way to the *share* phase.

       .. NOTE::

          Should consider if the property is created in the collect
          phase already as it is really the connector's job to define
          it. That becomes clear as it is being used in the *share*
          phase later, which is also managed by the connector.

       It is used to compare against the response from the id lookup
       in the system to determine if there has been an update since
       the last time. The property must contain the exact same
       structure as in the collect and transform datasets, but only
       for the subset of properties needed in the *share* phase.

       .. NOTE::

          The connector needs to convey what properties are needed in
          transform via the ``share_properties`` manifest
          property. That same list of properties should be used to
          construct the ``<collect-namespace>:$based_on`` property.


   * - ``$last_modified``
     - Added in the collect phase, alternatively use ``_ts`` from
       enrich instead.

       .. NOTE::

          It currently called ``$last-modified``.

          The timestamp id entity wide, so it might not be granular
          enough causing lost writes.

   * - ``$modified``
     - This one is added in the *enrich* phase. It used to figure out
       what properties where modified last for use with the last
       modified strategy used in globals.

       .. NOTE::

          It currently seems to include namespaces, but that should be
          unnecessary.

   * - ``<collect-namespace>:$share_id``
     - The property is used to hold a reference to the id of the
       entity that caused it to be created in this system. It should
       never be touched again unless it's deleted and inserted again,
       will default to use _id if $share_id is not explicitly set.

       It is also used to merge entities across systems in
       globals.

       .. NOTE::

          It currently called ``sesam-id``.

   * - ``$original_id``
     - This property is added to the entity when the ``_id`` of the
       source entity is rewritten. The value is the original id.

   * - ``$type``
     - This property is used to define the type of the entity,
       e.g. ``hubspot:company``.

       .. NOTE::

          It currently called ``rdf:type``.
