===============================
Poweroffice to Tilores Dataflow
===============================

Generated: 2023-05-15 08:58:56

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Contactperson to Tilores Human
------------------------------------------
Every Poweroffice Contactperson will be synchronized with a Tilores Human.

Once a link between a Poweroffice Contactperson and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Contactperson and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Poweroffice Contactperson Property
     - Tilores Human Property
     - Tilores Data Type
   * - Address1
     - street
     - "string"
   * - DateOfBirth
     - dateOfBirth
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"


Poweroffice Customer to Tilores Human
-------------------------------------
Every Poweroffice Customer will be synchronized with a Tilores Human.

Once a link between a Poweroffice Customer and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - Tilores Human Property
     - Tilores Data Type
   * - DateOfBirth
     - dateOfBirth
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - Id
     - id
     - "string"
   * - LastName
     - lastName
     - "string"
   * - Name
     - firstName
     - "string"


Poweroffice Employee to Tilores Human
-------------------------------------
Every Poweroffice Employee will be synchronized with a Tilores Human.

Once a link between a Poweroffice Employee and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Employee and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - Tilores Human Property
     - Tilores Data Type
   * - DateOfBirth
     - dateOfBirth
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - Id
     - id
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MailAddress.City
     - city
     - "string"
   * - MailAddress.ZipCode
     - postalCode
     - "string"
   * - StreetAddresses.City
     - city
     - "string"
   * - StreetAddresses.ZipCode
     - postalCode
     - "string"

