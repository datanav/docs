==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Human
-------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Human.

Once a link between a Powerofficego Contactperson and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Human:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Human Property
     -  Data Type
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


Powerofficego Employees to  Human
---------------------------------
Every Powerofficego Employees will be synchronized with a  Human.

Once a link between a Powerofficego Employees and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Human:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Human Property
     -  Data Type
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

