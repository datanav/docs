===================================
Poweroffice to PowerOffice Dataflow
===================================

Generated: 2023-05-22 22:53:47

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Supplier to PowerOffice Address
-------------------------------------------
Before any synchronization can take place, a link between a Poweroffice Supplier and a PowerOffice Address must be established.

A Poweroffice Supplier will merge with a PowerOffice Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - PowerOffice Address Property
   * - MailAddress.Id
     - id

Once a link between a Poweroffice Supplier and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Supplier and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - PowerOffice Address Property
     - PowerOffice Data Type


Poweroffice Customer to PowerOffice Contactperson
-------------------------------------------------
Every Poweroffice Customer will be synchronized with a PowerOffice Contactperson.

Once a link between a Poweroffice Customer and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - DateOfBirth
     - DateOfBirth
     - "string"
   * - DateOfBirth
     - dateOfBirth
     - "string"
   * - EmailAddress
     - EmailAddress
     - "string"
   * - EmailAddress
     - emailAddress
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - Id
     - Id
     - "integer"
   * - Id
     - id
     - "integer"
   * - InternationalIdCountryCode
     - ResidenceCountryCode
     - "string"
   * - LastChanged
     - LastChanged
     - "string"
   * - LastChanged
     - lastChanged
     - "string"
   * - LastName
     - LastName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - MailAddress.City
     - city
     - "string"
   * - MailAddress.CountryCode
     - residenceCountryCode
     - "string"
   * - MailAddress.ZipCode
     - zipCode
     - "string"
   * - Name
     - FirstName
     - "string"
   * - Name
     - firstName
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
   * - mailaddress.city
     - city
     - "string"
   * - streetAddresses.city
     - city
     - "string"
   * - streetAddresses.countryCode
     - residenceCountryCode
     - "string"
   * - streetAddresses.zipCode
     - zipCode
     - "string"

