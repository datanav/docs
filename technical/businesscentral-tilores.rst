====================================
Business Central to Tilores Dataflow
====================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessCentral Contacts person to Tilores Human
------------------------------------------------
Every BusinessCentral Contacts person will be synchronized with a Tilores Human.

Once a link between a BusinessCentral Contacts person and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Contacts person and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Contacts person Property
     - Tilores Human Property
     - Tilores Data Type
   * - city
     - city
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - mobilePhoneNumber
     - phoneNumber
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - postalCode
     - "string"


BusinessCentral Customers person to Tilores Human
-------------------------------------------------
Every BusinessCentral Customers person will be synchronized with a Tilores Human.

Once a link between a BusinessCentral Customers person and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Customers person and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Customers person Property
     - Tilores Human Property
     - Tilores Data Type
   * - city
     - city
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - postalCode
     - postalCode
     - "string"


BusinessCentral Employees to Tilores Human
------------------------------------------
Every BusinessCentral Employees will be synchronized with a Tilores Human.

Once a link between a BusinessCentral Employees and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessCentral Employees and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - BusinessCentral Employees Property
     - Tilores Human Property
     - Tilores Data Type
   * - birthDate
     - dateOfBirth
     - "string"
   * - city
     - city
     - "string"
   * - email
     - email
     - "string"
   * - givenName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - personalEmail
     - email
     - "string"
   * - postalCode
     - postalCode
     - "string"
   * - surname
     - lastName
     - "string"

