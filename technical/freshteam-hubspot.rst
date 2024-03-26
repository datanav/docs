=============================
Freshteam to Hubspot Dataflow
=============================

Generated: 2024-03-26 14:15:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Hubspot User
----------------------------------
Before any synchronization can take place, a link between a Freshteam Employee and a Hubspot User must be established.

A Freshteam Employee will merge with a Hubspot User if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Hubspot User Property
   * - official_email
     - email

Once a link between a Freshteam Employee and a Hubspot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Hubspot User:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Hubspot User Property
     - Hubspot Data Type
   * - official_email
     - email
     - "string"


Freshteam Department to  Company
--------------------------------
Every Freshteam Department will be synchronized with a  Company.

Once a link between a Freshteam Department and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Department and a  Company:

.. list-table::
   :header-rows: 1

   * - Freshteam Department Property
     -  Company Property
     -  Data Type
   * - name
     - properties.name
     - "string"


Freshteam Employee to  Contact
------------------------------
Every Freshteam Employee will be synchronized with a  Contact.

Once a link between a Freshteam Employee and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a  Contact:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     -  Contact Property
     -  Data Type
   * - Billing_Country
     - properties.country
     - "string"
   * - Billing_Country
     - properties.state
     - "string"
   * - Shipping_Country
     - properties.country
     - "string"
   * - Shipping_Country
     - properties.state
     - "string"
   * - address.country
     - properties.country
     - "string"
   * - address.country
     - properties.state
     - "string"
   * - communication_address.communication_country
     - properties.country
     - "string"
   * - communication_address.communication_country
     - properties.state
     - "string"
   * - date_of_birth
     - properties.date_of_birth
     - "string"
   * - first_name
     - properties.firstname
     - "string"
   * - last_name
     - properties.lastname
     - "string"
   * - official_email
     - properties.email
     - "string"
   * - official_email
     - properties.work_email
     - "string"
   * - personal_email
     - properties.email
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - properties.mobilephone
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.nameDependant on having wd:Q214995 in phone_numbers.name)
     - properties.phone
     - "string"

