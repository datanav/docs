=======================================
Powerofficego to PowerOfficeGo Dataflow
=======================================

Generated: 2023-08-01 14:01:16

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Supplier to PowerOfficeGo Address
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Supplier and a PowerOfficeGo Address must be established.

A Powerofficego Supplier will merge with a PowerOfficeGo Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Address Property
   * - MailAddress.Id
     - id

Once a link between a Powerofficego Supplier and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type


Powerofficego Customer to PowerOfficeGo Address
-----------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGo Address.

Once a link between a Powerofficego Customer and a PowerOfficeGo Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGo Address:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Address Property
     - PowerOfficeGo Data Type
   * - streetAddresses.address1
     - address1
     - "string"
   * - streetAddresses.address2
     - address2
     - "string"
   * - streetAddresses.address3
     - address3
     - "string"
   * - streetAddresses.city
     - city
     - "string"
   * - streetAddresses.countryCode
     - countryCode
     - "string"
   * - streetAddresses.lastChanged
     - lastChanged
     - "string"
   * - streetAddresses.zipCode
     - zipCode
     - "string"


Powerofficego Customer to PowerOfficeGo Contactperson
-----------------------------------------------------
Every Powerofficego Customer will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Powerofficego Customer and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastChanged
     - lastChanged
     - "string"
   * - mailAddress.city
     - city
     - "string"
   * - mailAddress.countryCode
     - residenceCountryCode
     - "string"
   * - mailAddress.zipCode
     - zipCode
     - "string"

