=============================
Powerofficego to Wix Dataflow
=============================

Generated: 2023-09-05 13:37:57

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Employees to Wix Contacts
---------------------------------------
Every Powerofficego Employees will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Employees and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Wix Contacts Property
     - Wix Data Type
   * - FirstName
     - info.name.first
     - "string"
   * - LastName
     - info.name.last
     - "string"
   * - PhoneNumber
     - info.phones
     - "string"
   * - PhoneNumber
     - primaryInfo.phone
     - "string"


Powerofficego Contactperson to Wix Contacts
-------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Contactperson and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wix Contacts Property
     - Wix Data Type
   * - emailAddress
     - info.emails
     - "string"
   * - emailAddress
     - primaryInfo.email
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"


Powerofficego Customers to Wix Contacts
---------------------------------------
Every Powerofficego Customers will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Customers and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Wix Contacts Property
     - Wix Data Type
   * - EmailAddress
     - info.emails
     - "string"
   * - EmailAddress
     - primaryInfo.email
     - "string"
   * - FirstName
     - info.name.first
     - "string"
   * - LastName
     - info.name.last
     - "string"

