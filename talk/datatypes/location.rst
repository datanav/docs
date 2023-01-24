.. _location:

========
Location
========
A position, place or site that something is in or where something happens.

.. jinja:: talk_datatype_location
  :file: _jinja/datatype_mapping.jinja

Model properties
----------------

.. list-table::
   :header-rows: 1

   * - Property
     - Wikidata id
     - Description

   * - territorial_entity. reference_type
     - `P131 <https://www.wikidata.org/wiki/Property:P131>`_. `P3865 <https://www.wikidata.org/wiki/Property:P3865>`_
     - Type of teritorial entity

   * - territorial_entity. territorial_type
     - `P131 <https://www.wikidata.org/wiki/Property:P131>`_. `P132 <https://www.wikidata.org/wiki/Property:P132>`_
     - Type of teritorial entity

   * - country
     - `P17 <https://www.wikidata.org/wiki/Property:P17>`_
     - Country for this location

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - The type of the entity

   * - territorial_entity
     - `P131 <https://www.wikidata.org/wiki/Property:P131>`_
     - Located in the following teritorial entity

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - The source of the entity statement

   * - postal_code
     - `P281 <https://www.wikidata.org/wiki/Property:P281>`_
     - Identifier assigned by postal authorities

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - Time when an entity begins to exist

   * - coordinate_location
     - `P625 <https://www.wikidata.org/wiki/Property:P625>`_
     - Geocoordinates of the location in the WGS84 coordinating system

   * - addressee
     - `P1817 <https://www.wikidata.org/wiki/Property:P1817>`_
     - Person or organization to whom a location is connected

   * - post_town
     - `P4595 <https://www.wikidata.org/wiki/Property:P4595>`_
     - Town/city part of the postal address

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - Uniqe identifier used to merge entities with identical value and type

   * - unique_identifier. reference_type
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P3865 <https://www.wikidata.org/wiki/Property:P3865>`_
     - The type of the identifier

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - Date a entity is modified

   * - street_address
     - `P6375 <https://www.wikidata.org/wiki/Property:P6375>`_
     - Street address line for the location. Include building number or PO box.

   * - street_address. has_sorting
     - `P6375 <https://www.wikidata.org/wiki/Property:P6375>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - The index used to sort the street address

   * - related_category
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - A related catagory for the entity

   * - related_category. instance_of
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - The type of the category

   * - related_category. has_sorting
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - The index used to sort the category
