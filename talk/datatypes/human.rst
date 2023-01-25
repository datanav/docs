.. _human:

=====
Human
=====
A human being, regardless of role.

.. jinja:: talk_datatype_human
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

   * - employer
     - `P108 <https://www.wikidata.org/wiki/Property:P108>`_
     - Organization for which the person works or worked

   * - employer. job_title
     - `P108 <https://www.wikidata.org/wiki/Property:P108>`_. `P39 <https://www.wikidata.org/wiki/Property:P39>`_
     - A persons role at the employer

   * - creator
     - `P170 <https://www.wikidata.org/wiki/Property:P170>`_
     - Created by

   * - stated_in
     - `P248 <https://www.wikidata.org/wiki/Property:P248>`_
     - The source of the entity statement

   * - date_of_birth
     - `P569 <https://www.wikidata.org/wiki/Property:P569>`_
     - Date on which the person was born

   * - created
     - `P571 <https://www.wikidata.org/wiki/Property:P571>`_
     - Time when an entity begins to exist

   * - last_name
     - `P734 <https://www.wikidata.org/wiki/Property:P734>`_
     - Lest name of person

   * - first_name
     - `P735 <https://www.wikidata.org/wiki/Property:P735>`_
     - First name or another given name of this person

   * - email_address
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_
     - Email address

   * - email_address. object_has_role
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - The role of the email address

   * - email_address. has_sorting
     - `P968 <https://www.wikidata.org/wiki/Property:P968>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - The index used to sort the email address

   * - phone_number
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_
     - Telephone number

   * - phone_number. object_has_role
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_. `P3831 <https://www.wikidata.org/wiki/Property:P3831>`_
     - The role of the phone number

   * - phone_number. has_sorting
     - `P1329 <https://www.wikidata.org/wiki/Property:P1329>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - The index used to sort the phone number

   * - twitter_username
     - `P2002 <https://www.wikidata.org/wiki/Property:P2002>`_
     - Twitter username

   * - faceboook_id
     - `P2013 <https://www.wikidata.org/wiki/Property:P2013>`_
     - Facebook username

   * - unique_identifier
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_
     - Uniqe identifier used to merge entities with identical value and type

   * - unique_identifier. reference_type
     - `P4649 <https://www.wikidata.org/wiki/Property:P4649>`_. `P3865 <https://www.wikidata.org/wiki/Property:P3865>`_
     - The type of the identifier

   * - updated
     - `P5017 <https://www.wikidata.org/wiki/Property:P5017>`_
     - Date a entity is modified

   * - resident_of
     - `P5389 <https://www.wikidata.org/wiki/Property:P5389>`_
     - Country  where a person is resident

   * - linkedIn_id
     - `P6634 <https://www.wikidata.org/wiki/Property:P6634>`_
     - Linkedin username

   * - related_category
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_
     - A related catagory for the entity

   * - related_category. instance_of
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_. `P31 <https://www.wikidata.org/wiki/Property:P31>`_
     - The type of the category

   * - related_category. has_sorting
     - `P7084 <https://www.wikidata.org/wiki/Property:P7084>`_. `P8307 <https://www.wikidata.org/wiki/Property:P8307>`_
     - The index used to sort the category

   * - reports_to
     - `P10645 <https://www.wikidata.org/wiki/Property:P10645>`_
     - The subject position reports to this position
