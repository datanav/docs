==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-08-29 10:35:42

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Contacts
----------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Contacts.

Once a link between a Powerofficego Contactperson and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Contacts Property
     -  Data Type
   * - city
     - City
     - "string"
   * - dateOfBirth
     - BirthDate
     - "string"
   * - emailAddress
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - residenceCountryCode
     - Country
     - "string"


Powerofficego Suppliers person to  Contacts
-------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a  Contacts.

Once a link between a Powerofficego Suppliers person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     -  Contacts Property
     -  Data Type
   * - DateOfBirth
     - BirthDate
     - "string"
   * - EmailAddress
     - Email
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - LastName
     - LastName
     - "string"
   * - MailAddress.City
     - City
     - "string"
   * - MailAddress.CountryCode
     - Country
     - "string"
   * - PhoneNumber
     - Phone
     - "string"

