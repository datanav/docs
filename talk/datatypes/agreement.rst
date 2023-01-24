.. _agreement:

=========
Agreement
=========
An agreement such as orders, invoices, that is intended to be enforceable by law.

.. jinja:: talk_datatype_agreement
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

   * - currency
     - `P38 <https://www.wikidata.org/wiki/Property:P38>`_
     - Currency used by item

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - The source of the entity statement

   * - part_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_
     - Part of agreement

   * - has_products
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_
     - Product lines

   * - has_products. point_in_time
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P585 <https://www.wikidata.org/wiki/Property:P585>`_
     - A point in time

   * - has_products. reference_type
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P585 <https://www.wikidata.org/wiki/Property:P585>`_
     - The type of the point in time

   * - has_products. quantity
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P1114 <https://www.wikidata.org/wiki/Property:P1114>`_
     - A specified number or amount

   * - has_products. title
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - A heading

   * - has_products. duration
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P2047 <https://www.wikidata.org/wiki/Property:P2047>`_
     - The period for the product line

   * - has_products. price
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P2284 <https://www.wikidata.org/wiki/Property:P2284>`_
     - The cost of the product

   * - has_products. vat
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P2855 <https://www.wikidata.org/wiki/Property:P2855>`_
     - Precentage of value added tax

   * - has_products. reference_type
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P3865 <https://www.wikidata.org/wiki/Property:P3865>`_
     - The type of the product line

   * - has_products. unit_symbol
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P5061 <https://www.wikidata.org/wiki/Property:P5061>`_
     - Identifier of the unit

   * - has_products. discount
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P7079 <https://www.wikidata.org/wiki/Property:P7079>`_
     - The discount for the product line

   * - has_products. ordered_by
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P8004 <https://www.wikidata.org/wiki/Property:P8004>`_
     - The subject that ordered the product line

   * - has_products. has_sorting
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - The index used to sort the product line

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - Time when an entity begins to exist

   * - point_in_time
     - `P585 <https://www.wikidata.org/wiki/Property:P585>`_
     - A point in time

   * - point_in_time. reference_type
     - `P585 <https://www.wikidata.org/wiki/Property:P585>`_. `P3865 <https://www.wikidata.org/wiki/Property:P3865>`_
     - The type of the point in time

   * - participant
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_
     - Person that actively takes/took part

   * - participant. object_has_role
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - The role of the participant

   * - description
     - `P921 <https://www.wikidata.org/wiki/Property:P921>`_
     - Description of the agreement

   * - email_address
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_
     - Email address

   * - email_address. reference_type
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_. `P3865 <https://www.wikidata.org/wiki/Property:P3865>`_
     - Type of email address

   * - title
     - `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - The title of the agreement

   * - duration
     - `P2047 <https://www.wikidata.org/wiki/Property:P2047>`_
     - Length of time of an event or process

   * - price
     - `P2284 <https://www.wikidata.org/wiki/Property:P2284>`_
     - The agreeed price

   * - url
     - `P2699 <https://www.wikidata.org/wiki/Property:P2699>`_
     - Location of a resource

   * - vat
     - `P2855 <https://www.wikidata.org/wiki/Property:P2855>`_
     - Percentage value-added tax

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - Uniqe identifier used to merge entities with identical value and type

   * - unique_identifier. reference_type
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P3865 <https://www.wikidata.org/wiki/Property:P3865>`_
     - The type of the identifier

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - Date a entity is modified

   * - discount
     - `P7079 <https://www.wikidata.org/wiki/Property:P7079>`_
     - The discount for the agreement

   * - related_category
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - A related catagory for the entity

   * - related_category. instance_of
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - The type of the category

   * - related_category. has_sorting
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - The index used to sort the category
