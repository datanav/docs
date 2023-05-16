===================================
Poweroffice to PowerOffice Dataflow
===================================

Generated: 2023-05-16 12:34:10

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
     - Id

Once a link between a Poweroffice Supplier and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Supplier and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - PowerOffice Address Property
     - PowerOffice Data Type


Poweroffice Contactperson to PowerOffice Customer
-------------------------------------------------
Every Poweroffice Contactperson will be synchronized with a PowerOffice Customer.

Once a link between a Poweroffice Contactperson and a PowerOffice Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Contactperson and a PowerOffice Customer:

.. list-table::
   :header-rows: 1

   * - Poweroffice Contactperson Property
     - PowerOffice Customer Property
     - PowerOffice Data Type
   * - DateOfBirth
     - DateOfBirth
     - "string"
   * - EmailAddress
     - EmailAddress
     - "string"
   * - FirstName
     - FirstName
     - "string"
   * - FirstName
     - Name
     - "string"
   * - LastChanged
     - LastChanged
     - "string"
   * - LastName
     - LastName
     - "string"
   * - ResidenceCountryCode
     - InternationalIdCountryCode
     - "string"
   * - dateOfBirth
     - DateOfBirth
     - "string"
   * - emailAddress
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - firstName
     - Name
     - "string"
   * - lastChanged
     - LastChanged
     - "string"
   * - lastName
     - LastName
     - "string"


Poweroffice Customer to PowerOffice Address
-------------------------------------------
Every Poweroffice Customer will be synchronized with a PowerOffice Address.

If a matching PowerOffice Address already exists, the Poweroffice Customer will be merged with the existing one.
If no matching PowerOffice Address is found, a new PowerOffice Address will be created.

A Poweroffice Customer will merge with a PowerOffice Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - PowerOffice Address Property
   * - MailAddress.Id
     - Id
   * - StreetAddresses.Id
     - Id

Once a link between a Poweroffice Customer and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
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
   * - Name
     - FirstName
     - "string"
   * - Name
     - firstName
     - "string"

