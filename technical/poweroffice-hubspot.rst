===============================
Poweroffice to HubSpot Dataflow
===============================

Generated: 2023-08-01 14:00:16

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Contactperson to HubSpot Contact
--------------------------------------------
Every Poweroffice Contactperson will be synchronized with a HubSpot Contact.

Once a link between a Poweroffice Contactperson and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Contactperson and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Poweroffice Contactperson Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - emailAddress
     - properties.work_email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"


Poweroffice Customer to HubSpot Company
---------------------------------------
Every Poweroffice Customer will be synchronized with a HubSpot Company.

Once a link between a Poweroffice Customer and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - LegalName
     - properties.name
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"


Poweroffice Employee to HubSpot Contact
---------------------------------------
Every Poweroffice Employee will be synchronized with a HubSpot Contact.

Once a link between a Poweroffice Employee and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Employee and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Poweroffice Employee Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - DateOfBirth
     - properties.date_of_birth
     - "string"
   * - EmailAddress
     - properties.work_email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - LastName
     - properties.lastname
     - "string"


Poweroffice Supplier to HubSpot Company
---------------------------------------
Every Poweroffice Supplier will be synchronized with a HubSpot Company.

Once a link between a Poweroffice Supplier and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Supplier and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - LegalName
     - properties.name
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"

