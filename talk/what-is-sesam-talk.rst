.. _what_is_sesam_talk:

==================
What is Sesam Talk
==================

Sesam Talk synchronizes a limited set of core types with a limited set of properties between the various :doc:`supported system <systems/index>`.

Sesam Talk merges data from the different systems on certain criteria. People are merged if they have the same email, organisations are merged if they have the exact same name.

.. Important::
  Sesam talk is currently an experimental free service. Use it at your own risk.

.. image:: images/dashboard-sesam-talk.jpg
  :width: 100%
  :alt: Alternative text

Person model
------------
A human being, regardless of role.

.. list-table::
   :header-rows: 1

   * - Property
     - Wikidata identifier
     - Description

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - Data type - that class of which this subject is a particular example and member

   * - employer
     - `P108 <https://www.wikidata.org/wiki/Property:P108>`_
     - person or organization for which the subject works or worked

   * - job_title
     - `P39 <https://www.wikidata.org/wiki/Property:P39>`_
     - A subjects role in an organisation

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - to be used in the references field to refer to the information document or database in which a claim is made; for qualifiers use P805; for the type of document in which a claim is made use P3865

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - related_category
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
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

   * - object_has_role
     - `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - phone_number
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_
     - telephone number in standard format (RFC3966), without 'tel:' prefix

   * - object_has_role
     - `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
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

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
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

Organisation model
------------------
Any type of group or association of individuals who are joined together either formally or legally.

.. list-table::
     :header-rows: 1

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

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - related_category
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - industry
     - `P452 <https://www.wikidata.org/wiki/Property:P452>`_
     - specific industry of company or organization

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
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

   * - object_has_role
     - `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - employees
     - `P1128 <https://www.wikidata.org/wiki/Property:P1128>`_
     - total number of employees of a company at a given \"point in time\" (P585). Most recent data would generally have preferred rank; data for previous years normal rank (not deprecated rank). Add data for recent years, don't overwrite

   * - phone_number
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_
     - telephone number in standard format (RFC3966), without 'tel:' prefix

   * - object_has_role
     - `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
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

   * - object_has_role
     - `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - (qualifier) role or generic identity of the value of a statement (\"object\") in the context of that statement; for the role of the item the statement is on (\"subject\"), use P2868

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - qualifier for subjects which may have different identities which are covered by different items, the identity to which the qualified statement applies

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

Classification model
--------------------
Classification and grouping used as controlled vocabularies.

.. list-table::
   :header-rows: 1

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
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - related_category
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - category is related to this item

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
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

   * - instance_of
     - `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - 

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - date a reference was modified, revised, or updated

   * - has_sorting
     - `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - entries are sorted by this in the appendix, list or table
Systems
-------
Sesam Talk can read and write data for several common cloud services.


.. list-table::
   :header-rows: 1

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
   :header-rows: 1

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
   :header-rows: 1

   * - System
     - Organisation
     - Person

   * - :ref:`bigquery`
     - Yes
     - Yes
