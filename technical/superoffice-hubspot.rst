===============================
SuperOffice to HubSpot Dataflow
===============================

Generated: 2023-06-23 11:19:50

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to HubSpot Contact
-------------------------------------
Every SuperOffice Person will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the SuperOffice Person will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A SuperOffice Person will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - HubSpot Contact Property
   * - Emails.Value
     - properties.email

Once a link between a SuperOffice Person and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - BirthDate
     - properties.date_of_birth
     - "string"
   * - Emails.Value
     - properties.email
     - "string"
   * - Firstname
     - properties.firstname
     - "string"
   * - Lastname
     - properties.lastname
     - "string"
   * - MobilePhones.Value
     - properties.mobilephone
     - "string"
   * - OfficePhones.Value
     - properties.phone
     - "string"


SuperOffice User to HubSpot Contact
-----------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a HubSpot Contact must be established.

A SuperOffice User will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - HubSpot Contact Property
   * - personEmail
     - properties.email

Once a link between a SuperOffice User and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - contactCategory
     - properties.country
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - personEmail
     - properties.email
     - "string"


SuperOffice Contact to HubSpot Company
--------------------------------------
Every SuperOffice Contact will be synchronized with a HubSpot Company.

Once a link between a SuperOffice Contact and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Address.Street.Address1
     - properties.address
     - "string"
   * - Address.Street.Address2
     - properties.address2
     - "string"
   * - Address.Street.City
     - properties.city
     - "string"
   * - Address.Street.Zipcode
     - properties.zip
     - "string"
   * - ContactId
     - id
     - "string"
   * - Country.CountryId
     - properties.country
     - "string"
   * - Domains
     - properties.website
     - "string"
   * - Name
     - properties.name
     - "string"
   * - Phones.Value
     - properties.phone
     - "string"


SuperOffice Sale classification status to HubSpot Pipelinedeal
--------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Sale classification status and a HubSpot Pipelinedeal must be established.

A new HubSpot Pipelinedeal will be created from a SuperOffice Sale classification status if it is connected to a SuperOffice Sale, Quote, Quoteline, or Quotealternative that is synchronized into HubSpot.

Once a link between a SuperOffice Sale classification status and a HubSpot Pipelinedeal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale classification status and a HubSpot Pipelinedeal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale classification status Property
     - HubSpot Pipelinedeal Property
     - HubSpot Data Type

