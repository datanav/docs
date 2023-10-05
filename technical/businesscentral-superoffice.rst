=======================================
Businesscentral to SuperOffice Dataflow
=======================================

Generated: 2023-10-05 06:51:09

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Company to SuperOffice Contact
----------------------------------------------
Every Businesscentral Company will be synchronized with a SuperOffice Contact.

Once a link between a Businesscentral Company and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Company and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Company Property
     - SuperOffice Contact Property
     - SuperOffice Data Type


Businesscentral Contact company to SuperOffice Contact
------------------------------------------------------
Every Businesscentral Contact company will be synchronized with a SuperOffice Contact.

Once a link between a Businesscentral Contact company and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact company and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact company Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - addressLine1
     - Address.Postal.Address1
     - "string"
   * - addressLine1
     - Address.Street.Address1
     - "string"
   * - addressLine2
     - Address.Postal.Address2
     - "string"
   * - addressLine2
     - Address.Street.Address2
     - "string"
   * - city
     - Address.Postal.City
     - "string"
   * - city
     - Address.Street.City
     - "string"
   * - country
     - Country.CountryId
     - "integer"
   * - id
     - ContactId
     - "integer"
   * - phoneNumber
     - Phones.Value
     - "string"
   * - postalCode
     - Address.Postal.Zipcode
     - "string"
   * - postalCode
     - Address.Street.Zipcode
     - "string"


Businesscentral Contact to SuperOffice Person
---------------------------------------------
Every Businesscentral Contact will be synchronized with a SuperOffice Person.

Once a link between a Businesscentral Contact and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact Property
     - SuperOffice Person Property
     - SuperOffice Data Type

