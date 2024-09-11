=================================
PowerOfficeGO to Tilores Dataflow
=================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Contactperson to Tilores Human
------------------------------------------
Every PowerOffice Contactperson will be synchronized with a Tilores Human.

Once a link between a PowerOffice Contactperson and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Tilores Human Property
     - Tilores Data Type
   * - address1
     - street
     - "string"
   * - address2
     - street
     - "string"
   * - city
     - city
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - lastName
     - "string"
   * - zipCode
     - postalCode
     - "string"


PowerOffice Customers person to Tilores Human
---------------------------------------------
Every PowerOffice Customers person will be synchronized with a Tilores Human.

Once a link between a PowerOffice Customers person and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - Tilores Human Property
     - Tilores Data Type
   * - DateOfBirth
     - dateOfBirth
     - "string"
   * - EmailAddress
     - email
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


PowerOffice Employees to Tilores Human
--------------------------------------
Every PowerOffice Employees will be synchronized with a Tilores Human.

Once a link between a PowerOffice Employees and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Employees and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - PowerOffice Employees Property
     - Tilores Human Property
     - Tilores Data Type
   * - DateOfBirth
     - dateOfBirth
     - "string"
   * - EmailAddress
     - email
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
   * - MailAddress.city
     - city
     - "string"
   * - MailAddress.zipCode
     - postalCode
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - lastName
     - "string"
   * - streetAddresses.city
     - city
     - "string"
   * - streetAddresses.zipCode
     - postalCode
     - "string"

