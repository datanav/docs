.. _task:

====
Task
====
A piece of work to be done.

.. jinja:: talk_datatype_task
  :file: _jinja/datatype_mapping.jinja

Model properties
----------------

.. list-table::
   :header-rows: 1

   * - Property
     - Wikidata id
     - Description

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - The type of the entity

   * - owned_by
     - `P127 <https://www.wikidata.org/wiki/Property:P127>`_
     - Owner of the task

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - The source of the entity statement

   * - location
     - `P276 <https://www.wikidata.org/wiki/Property:P276>`_
     - Location of the task

   * - part_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_
     - Object of which the task is a part of

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - Time when an entity begins to exist

   * - participant
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_
     - Person, or organization that actively takes/took part of the task

   * - participant. instance_of
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - The type of the participant

   * - earliest_date
     - `P1319 <https://www.wikidata.org/wiki/Property:P1319>`_
     - Earliest date at which a task can happen

   * - latest_date
     - `P1326 <https://www.wikidata.org/wiki/Property:P1326>`_
     - Latest possible time that something can occurr

   * - title
     - `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - Task title

   * - duration
     - `P2047 <https://www.wikidata.org/wiki/Property:P2047>`_
     - Length of time of the task

   * - intended_public
     - `P2360 <https://www.wikidata.org/wiki/Property:P2360>`_
     - This task is tergeted for, or has been designed to that person or organization 

   * - budget
     - `P2769 <https://www.wikidata.org/wiki/Property:P2769>`_
     - Assigned monetary amount for the task

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - Uniqe identifier used to merge entities with identical value and type

   * - unique_identifier. reference_type
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P3865 <https://www.wikidata.org/wiki/Property:P3865>`_
     - The type of the identifier

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - Date a entity is modified

   * - related_category
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - A related catagory for the entity

   * - related_category. instance_of
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - The type of the category

   * - related_category. has_sorting
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - The index used to sort the category

   * - ordered_by
     - `P8004 <https://www.wikidata.org/wiki/Property:P8004>`_
     - Subject that ordered the task
