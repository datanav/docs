.. _what_is_sesam_talk:

==================
What is Sesam Talk
==================

Sesam Talk synchronizes a limited set of core types with a limited set of properties between the various :doc:`supported system <systems/index>`.

Sesam Talk merges data from the different systems on certain criteria. People are merged if they have the same email, organisations are merged if they have the exact same name.

.. Important::
  Sesam talk is currently in Beta. Use it at your own risk.

.. image:: images/dashboard-sesam-talk.jpg
  :width: 100%
  :alt: Alternative text

Asset model
-----------
Items or resources, such as valubales, machinery, or real estate

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - arranged_by
     - `P88 <https://www.wikidata.org/wiki/Property:P88>`_
     - person or organization that commissioned this work

   * - maintained_by
     - `P126 <https://www.wikidata.org/wiki/Property:P126>`_
     - person or organization in charge of keeping the subject (for instance an infrastructure) in functioning order

   * - owned_by
     - `P127 <https://www.wikidata.org/wiki/Property:P127>`_
     - owner of the subject

   * - operator
     - `P137 <https://www.wikidata.org/wiki/Property:P137>`_
     - person, profession, or organization that operates the equipment, facility, or service

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - manufacturer
     - `P176 <https://www.wikidata.org/wiki/Property:P176>`_
     - manufacturer or producer of this product

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - location
     - `P276 <https://www.wikidata.org/wiki/Property:P276>`_
     - location of the object, structure or event. In the case of an administrative entity as containing item use P131. For statistical entities use P8138. In the case of a geographic entity use P706. Use P7153 for locations associated with the object.

   * - part_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_
     - object of which the subject is a part (if this subject is already part of object A which is a part of object B, then please only make the subject part of object A). Inverse property of \"has part\" (P527, see also \"has parts of the class\" (P2670)).

   * - part_of.instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - part_of.related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - part_of.has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - service_entry
     - `P729 <https://www.wikidata.org/wiki/Property:P729>`_
     - date or point in time on which a piece or class of equipment entered operational service

   * - end_of_service
     - `P730 <https://www.wikidata.org/wiki/Property:P730>`_
     - date or point in time on which a piece or class of equipment was retired of pulled out from operational service

   * - description
     - `P921 <https://www.wikidata.org/wiki/Property:P921>`_
     - Description of primary topic of a work (see also P180: depicts)

   * - described_by_source
     - `P1343 <https://www.wikidata.org/wiki/Property:P1343>`_
     - work where this item is described

   * - described_by_source.instance_of
     - `P1343 <https://www.wikidata.org/wiki/Property:P1343>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - replaced_by
     - `P1366 <https://www.wikidata.org/wiki/Property:P1366>`_
     - other person or item which continues the item by replacing it in its role. Use P156 (\"followed by\") if the item is not replaced nor identical, but adds to the series (e.g. books in a series).

   * - total_equity
     - `P2137 <https://www.wikidata.org/wiki/Property:P2137>`_
     - amount of equity value for an entity

   * - serial_number
     - `P2598 <https://www.wikidata.org/wiki/Property:P2598>`_
     - an identifier for a specific object among the same product. Not a product code or model number

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

Classification model
--------------------
Classification and grouping used as controlled vocabularies.

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - description
     - `P921 <https://www.wikidata.org/wiki/Property:P921>`_
     - Description of primary topic of a work (see also P180: depicts)

   * - title
     - `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - published name of a work, such as a newspaper article, a literary work, piece of music, a website, or a performance work

   * - url
     - `P2699 <https://www.wikidata.org/wiki/Property:P2699>`_
     - location of a resource

   * - code
     - `P3295 <https://www.wikidata.org/wiki/Property:P3295>`_
     - code used to represent a specific concept in a given encoding

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

Agreement model
---------------
An agreement such as orders, invoices, that is intended to be enforceable by law

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - invoice
     - `Q190581 <https://www.wikidata.org/wiki/Property:Q190581>`_
     - commercial document issued by a seller to a buyer, relating to a sale transaction and indicating the products, quantities, and agreed prices for products or services the seller has provided the buyer

   * - email_address.instance_of
     - `(P968) <https://www.wikidata.org/wiki/Property:(P968)>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - email_address
     - `(P968) <https://www.wikidata.org/wiki/Property:(P968)>`_
     - email address, prefixed with mailto:

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - currency
     - `P38 <https://www.wikidata.org/wiki/Property:P38>`_
     - currency used by item

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - part_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_
     - object of which the subject is a part (if this subject is already part of object A which is a part of object B, then please only make the subject part of object A). Inverse property of \"has part\" (P527, see also \"has parts of the class\" (P2670)).

   * - part_of.instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - part_of.related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - part_of.has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - details
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_
     - part of this subject; inverse property of \"part of\" (P361). See also \"has parts of the class\" (P2670).

   * - details.instance_of
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - details.point_in_time
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P585 <https://www.wikidata.org/wiki/Property:P585>`_
     - Done at this time

   * - details.instance_of
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P585 <https://www.wikidata.org/wiki/Property:P585>`_
     - 

   * - details.quantity
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P1114 <https://www.wikidata.org/wiki/Property:P1114>`_
     - A specified number or amount

   * - details.title
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - A heading

   * - details.duration
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P2047 <https://www.wikidata.org/wiki/Property:P2047>`_
     - A specified period of time something lasts

   * - details.price
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P2284 <https://www.wikidata.org/wiki/Property:P2284>`_
     - The cost of an object or service

   * - details.vat
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P2855 <https://www.wikidata.org/wiki/Property:P2855>`_
     - Precentage of value added tax

   * - details.unit_symbol
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P5061 <https://www.wikidata.org/wiki/Property:P5061>`_
     - 

   * - details.discount
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P7079 <https://www.wikidata.org/wiki/Property:P7079>`_
     - reduction in the size of something, or the process of becoming smaller, typically when a material return to room temperature after heating

   * - details.ordered_by
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P8004 <https://www.wikidata.org/wiki/Property:P8004>`_
     - 

   * - details.has_sorting
     - `P527 <https://www.wikidata.org/wiki/Property:P527>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - point_in_time
     - `P585 <https://www.wikidata.org/wiki/Property:P585>`_
     - time and date something took place, existed or a statement was true

   * - point_in_time.instance_of
     - `P585 <https://www.wikidata.org/wiki/Property:P585>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - participant
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_
     - person, group of people or organization (object) that actively takes/took part in an event or process (subject). Preferably qualify with \"object has role\" (P3831). Use P1923 for participants that are teams.

   * - participant.object_has_role
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - 

   * - description
     - `P921 <https://www.wikidata.org/wiki/Property:P921>`_
     - Description of primary topic of a work (see also P180: depicts)

   * - title
     - `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - published name of a work, such as a newspaper article, a literary work, piece of music, a website, or a performance work

   * - duration
     - `P2047 <https://www.wikidata.org/wiki/Property:P2047>`_
     - length of time of an event or process

   * - price
     - `P2284 <https://www.wikidata.org/wiki/Property:P2284>`_
     - published price listed or paid for a product (use with unit of currency)

   * - url
     - `P2699 <https://www.wikidata.org/wiki/Property:P2699>`_
     - location of a resource

   * - vat
     - `P2855 <https://www.wikidata.org/wiki/Property:P2855>`_
     - percentage value-added tax in this country or region. Do not use for sales tax. For specialised rates, use qualifiers

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

   * - discount
     - `P7079 <https://www.wikidata.org/wiki/Property:P7079>`_
     - reduction in the size of something, or the process of becoming smaller, typically when a material return to room temperature after heating

Documentation model
-------------------
A permanent record of information in written, photographic, or other form.

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - owned_by
     - `P127 <https://www.wikidata.org/wiki/Property:P127>`_
     - owner of the subject

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - part_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_
     - object of which the subject is a part (if this subject is already part of object A which is a part of object B, then please only make the subject part of object A). Inverse property of \"has part\" (P527, see also \"has parts of the class\" (P2670)).

   * - part_of.instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - part_of.related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - part_of.has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - title
     - `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - published name of a work, such as a newspaper article, a literary work, piece of music, a website, or a performance work

   * - subtitle
     - `P1680 <https://www.wikidata.org/wiki/Property:P1680>`_
     - A secondary or subordinate title

   * - url
     - `P2699 <https://www.wikidata.org/wiki/Property:P2699>`_
     - A URL is the address of a given unique resource on the Web

   * - file_format
     - `P2701 <https://www.wikidata.org/wiki/Property:P2701>`_
     - file format, compression type, or ontology used in a file

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

   * - modified_version_of
     - `P5059 <https://www.wikidata.org/wiki/Property:P5059>`_
     - indicates the work or one of its versions which served as a basis for the adaptation or arrangement resulting in the given version of the work

Event model
-----------
Something that occurs in a certain place during a particular interval of time.

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - location
     - `P276 <https://www.wikidata.org/wiki/Property:P276>`_
     - Location of an object

   * - instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - start_time
     - `P580 <https://www.wikidata.org/wiki/Property:P580>`_
     - time a time period starts

   * - end_time
     - `P582 <https://www.wikidata.org/wiki/Property:P582>`_
     - time a time period ends

   * - point_in_time
     - `P585 <https://www.wikidata.org/wiki/Property:P585>`_
     - time and date something took place, existed or a statement was true

   * - participant
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_
     - person, group of people or organization (object) that actively takes/took part in an event or process (subject). Preferably qualify with \"object has role\" (P3831). Use P1923 for participants that are teams.

   * - participant.object_has_role
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - 

   * - description
     - `P921 <https://www.wikidata.org/wiki/Property:P921>`_
     - Description of primary topic of a work (see also P180: depicts)

   * - title
     - `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - published name of a work

   * - duration
     - `P2047 <https://www.wikidata.org/wiki/Property:P2047>`_
     - length of time of an event or process

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

Location model
--------------
A position, place or site that something is in or where something happens.

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - country
     - `P17 <https://www.wikidata.org/wiki/Property:P17>`_
     - sovereign state of this item (not to be used for human beings)

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - located_in_the_administrative_territorial_entity
     - `P131 <https://www.wikidata.org/wiki/Property:P131>`_
     - the item is located on the territory of the following administrative entity. Use P276 for specifying locations that are non-administrative places and for items about events. Use P1382 if the item falls only partially into the administrative entity.

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - postal_code
     - `P281 <https://www.wikidata.org/wiki/Property:P281>`_
     - identifier assigned by postal authorities 

   * - instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - coordinate_location
     - `P625 <https://www.wikidata.org/wiki/Property:P625>`_
     - geocoordinates of the subject. For Earth, please note that only WGS84 coordinating system is supported at the moment

   * - addressee
     - `P1817 <https://www.wikidata.org/wiki/Property:P1817>`_
     - person or organization to whom a letter or note is addressed

   * - post_town
     - `P4595 <https://www.wikidata.org/wiki/Property:P4595>`_
     - town/city part of the postal address, can be different from administrative location

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

   * - street_address
     - `P6375 <https://www.wikidata.org/wiki/Property:P6375>`_
     - full street address where subject is located. Include building number, city/locality, post code, but not country; use also P669 if the street has its own separate item

   * - street_address.has_sorting
     - `P6375 <https://www.wikidata.org/wiki/Property:P6375>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

Organisation model
------------------
Any type of group or association of individuals who are joined together either formally or legally.

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - chief_executive_officer
     - `P169 <https://www.wikidata.org/wiki/Property:P169>`_
     - highest-ranking corporate officer appointed as the CEO within an organization

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - ticker_symbol
     - `P249 <https://www.wikidata.org/wiki/Property:P249>`_
     - identifier for a publicly traded share of a particular stock on a particular stock market or that of a cryptocurrency

   * - location
     - `P276 <https://www.wikidata.org/wiki/Property:P276>`_
     - location of the object, structure or event. In the case of an administrative entity as containing item use P131. For statistical entities use P8138. In the case of a geographic entity use P706. Use P7153 for locations associated with the object.

   * - part_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_
     - object of which the subject is a part (if this subject is already part of object A which is a part of object B, then please only make the subject part of object A). Inverse property of \"has part\" (P527, see also \"has parts of the class\" (P2670)).

   * - part_of.instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - part_of.related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - part_of.has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - industry
     - `P452 <https://www.wikidata.org/wiki/Property:P452>`_
     - specific industry of company or organization

   * - industry.instance_of
     - `P452 <https://www.wikidata.org/wiki/Property:P452>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - official_website
     - `P856 <https://www.wikidata.org/wiki/Property:P856>`_
     -  A group of World Wide Web pages usually containing links to each other and made available online by an individual, company, or organization

   * - description
     - `P921 <https://www.wikidata.org/wiki/Property:P921>`_
     - Description of primary topic of a work (see also P180: depicts)

   * - email_address
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_
     - An email address identifies an email box to which messages are delivered. 

   * - email_address.object_has_role
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - email_address.has_sorting
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - employees
     - `P1128 <https://www.wikidata.org/wiki/Property:P1128>`_
     - total number of employees of a company at a given \"point in time\" (P585). Most recent data would generally have preferred rank; data for previous years normal rank (not deprecated rank). Add data for recent years, don't overwrite

   * - phone_number
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_
     - telephone number in standard format (RFC3966), without 'tel:' prefix

   * - phone_number.object_has_role
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - phone_number.has_sorting
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - official_name
     - `P1448 <https://www.wikidata.org/wiki/Property:P1448>`_
     - official name of the subject in its official language(s)

   * - total_revenue
     - `P2139 <https://www.wikidata.org/wiki/Property:P2139>`_
     - income gained by an organization during a given time frame. Not to be confused with fiscal revenue

   * - fax_number
     - `P2900 <https://www.wikidata.org/wiki/Property:P2900>`_
     - telephone number of a facsimile line

   * - fax_number.object_has_role
     - `P2900 <https://www.wikidata.org/wiki/Property:P2900>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - fax_number.has_sorting
     - `P2900 <https://www.wikidata.org/wiki/Property:P2900>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

Person model
------------
A human being, regardless of role.

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - employer
     - `P108 <https://www.wikidata.org/wiki/Property:P108>`_
     - person or organization for which the subject works or worked

   * - employer.job_title
     - `P108 <https://www.wikidata.org/wiki/Property:P108>`_. `P39 <https://www.wikidata.org/wiki/Property:P39>`_
     - A subjects role in an organisation

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - date_of_birth
     - `P569 <https://www.wikidata.org/wiki/Property:P569>`_
     - date on which the subject was born

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - last_name
     - `P734 <https://www.wikidata.org/wiki/Property:P734>`_
     - part of full name of person

   * - first_name
     - `P735 <https://www.wikidata.org/wiki/Property:P735>`_
     - first name or another given name of this person; values used with the property should not link disambiguations nor family names

   * - email_address
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_
     - email address, prefixed with mailto:

   * - email_address.object_has_role
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - email_address.has_sorting
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - phone_number
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_
     - telephone number in standard format (RFC3966), without 'tel:' prefix

   * - phone_number.object_has_role
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - phone_number.has_sorting
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - twitter_username
     - `P2002 <https://www.wikidata.org/wiki/Property:P2002>`_
     - Twitter username

   * - faceboook_id
     - `P2013 <https://www.wikidata.org/wiki/Property:P2013>`_
     - facebook username

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

   * - permanent_resident_of
     - `P5389 <https://www.wikidata.org/wiki/Property:P5389>`_
     - country or region where a person has the legal status of permanent resident

   * - linkedIn_personal_profile_id
     - `P6634 <https://www.wikidata.org/wiki/Property:P6634>`_
     - Linkedin username

   * - reports_to
     - `P10645 <https://www.wikidata.org/wiki/Property:P10645>`_
     - the subject position reports to this position

Product model
-------------
A product is the item offered for sale. A product can be a service or an item.

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - image
     - `P18 <https://www.wikidata.org/wiki/Property:P18>`_
     - image of relevant illustration of the subject; if available, also use more specific properties (sample: coat of arms image, locator map, flag image, signature image, logo image, collage image)

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - currency
     - `P38 <https://www.wikidata.org/wiki/Property:P38>`_
     - currency used by item

   * - owned_by
     - `P127 <https://www.wikidata.org/wiki/Property:P127>`_
     - owner of the subject

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - manufacturer
     - `P176 <https://www.wikidata.org/wiki/Property:P176>`_
     - manufacturer or producer of this product

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - country_of_origin
     - `P495 <https://www.wikidata.org/wiki/Property:P495>`_
     - country of origin of this item (creative work, food, phrase, product, etc.)

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - description
     - `P921 <https://www.wikidata.org/wiki/Property:P921>`_
     - Description of primary topic of a work (see also P180: depicts)

   * - quantity
     - `P1114 <https://www.wikidata.org/wiki/Property:P1114>`_
     - number of instances of this subject

   * - described_by_source
     - `P1343 <https://www.wikidata.org/wiki/Property:P1343>`_
     - work where this item is described

   * - described_by_source.instance_of
     - `P1343 <https://www.wikidata.org/wiki/Property:P1343>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - title
     - `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - published name of a work

   * - price
     - `P2284 <https://www.wikidata.org/wiki/Property:P2284>`_
     - published price listed or paid for a product (use with unit of currency)

   * - discontinued_date
     - `P2669 <https://www.wikidata.org/wiki/Property:P2669>`_
     - date that the availability of a product was discontinued; see also \"dissolved, abolished or demolished\" (P576)

   * - url
     - `P2699 <https://www.wikidata.org/wiki/Property:P2699>`_
     - A URL is the address of a given unique resource on the Web

   * - vat
     - `P2855 <https://www.wikidata.org/wiki/Property:P2855>`_
     - percentage value-added tax in this country or region. Do not use for sales tax. For specialised rates, use qualifiers

   * - code
     - `P3295 <https://www.wikidata.org/wiki/Property:P3295>`_
     - code used to represent a specific concept in a given encoding

   * - global_trade_item_number
     - `P3962 <https://www.wikidata.org/wiki/Property:P3962>`_
     - GTIN (or EAN, UCC) is used to identify products via their barcodes

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

   * - unit symbol
     - `P5061 <https://www.wikidata.org/wiki/Property:P5061>`_
     - abbreviation of a unit for each language; if not provided, then it should default to English

Task model
----------
A piece of work to be done.

.. list-table::

   * - Property
     - Wikidata identifier
     - Description

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - owned_by
     - `P127 <https://www.wikidata.org/wiki/Property:P127>`_
     - owner of the subject

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - location
     - `P276 <https://www.wikidata.org/wiki/Property:P276>`_
     - location of the object, structure or event. In the case of an administrative entity as containing item use P131. For statistical entities use P8138. In the case of a geographic entity use P706. Use P7153 for locations associated with the object.

   * - part_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_
     - object of which the subject is a part (if this subject is already part of object A which is a part of object B, then please only make the subject part of object A). Inverse property of \"has part\" (P527, see also \"has parts of the class\" (P2670)).

   * - part_of.instance_of
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - part_of.related_category
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - part_of.has_sorting
     - `P361 <https://www.wikidata.org/wiki/Property:P361>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table


   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - time when an entity begins to exist; for date of official opening use P1619

   * - participant
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_
     - person, group of people or organization (object) that actively takes/took part in an event or process (subject). Preferably qualify with \"object has role\" (P3831). Use P1923 for participants that are teams.

   * - participant.instance_of
     - `P710 <https://www.wikidata.org/wiki/Property:P710>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - object has role

   * - earliest_date
     - `P1319 <https://www.wikidata.org/wiki/Property:P1319>`_
     - earliest date at which an event could have happened. Use as qualifier for other date properties

   * - latest_date
     - `P1326 <https://www.wikidata.org/wiki/Property:P1326>`_
     - latest possible time that something could have occurred. Use as qualifier for other date properties

   * - title
     - `P1476 <https://www.wikidata.org/wiki/Property:P1476>`_
     - published name of a work, such as a newspaper article, a literary work, piece of music, a website, or a performance work

   * - duration
     - `P2047 <https://www.wikidata.org/wiki/Property:P2047>`_
     - length of time of an event or process

   * - intended_public
     - `P2360 <https://www.wikidata.org/wiki/Property:P2360>`_
     - this work, product, object or event is intended for, or has been designed to that person or group of people, animals, plants, etc

   * - budget
     - `P2769 <https://www.wikidata.org/wiki/Property:P2769>`_
     - assigned monetary amount for a project (for the estimated cost of a film, also commonly referred to as budget, use P2130)

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - unique_identifier.instance_of
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

   * - orderd_by
     - `P8004 <https://www.wikidata.org/wiki/Property:P8004>`_
     - subject that ordered the act

Systems
-------
Sesam Talk can read and write data for several common cloud services.


.. list-table::

   * - System
     - Type of system
     - Organisation
     - Person

   * - :ref:`wave`
     - Accounting
     - Yes
     - Yes (primary contact from companies)

   * - :ref:`hubspot`
     - CRM
     - Yes
     - Yes

   * - :ref:`freshteam`
     - CRM
     - Yes
     - Yes

Enhancement systems
-------------------
Sesam Talk has support for systems that enhances your data.

.. list-table::
  
   * - System
     - Organisation
     - Person

   * - :ref:`opensesam`
     - Yes
     - N/A

Analytic systems
----------------
Sesam Talk can write and keep all your data up-to-date in your analytic solution.

.. list-table::

   * - System
     - Organisation
     - Person

   * - :ref:`bigquery`
     - Yes
     - Yes
