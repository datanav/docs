==============================
Webcrm to Superoffice Dataflow
==============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Organisations to Superoffice Contact
-------------------------------------------
Every Webcrm Organisations will be synchronized with a Superoffice Contact.

Once a link between a Webcrm Organisations and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - OrganisationAddress
     - Address.Postal.Address1
     - "string"
   * - OrganisationAddress
     - Address.Street.Address1
     - "string"
   * - OrganisationCity
     - Address.Postal.City
     - "string"
   * - OrganisationCity
     - Address.Street.City
     - "string"
   * - OrganisationDeliveryAddress
     - Address.Postal.Address1
     - "string"
   * - OrganisationDeliveryAddress
     - Address.Street.Address1
     - "string"
   * - OrganisationDeliveryCity
     - Address.Postal.City
     - "string"
   * - OrganisationDeliveryCity
     - Address.Street.City
     - "string"
   * - OrganisationDeliveryPostCode
     - Address.Postal.Zipcode
     - "string"
   * - OrganisationDeliveryPostCode
     - Address.Street.Zipcode
     - "string"
   * - OrganisationId
     - ContactId
     - "integer"
   * - OrganisationName
     - Name
     - "string"
   * - OrganisationPostCode
     - Address.Postal.Zipcode
     - "string"
   * - OrganisationPostCode
     - Address.Street.Zipcode
     - "string"
   * - OrganisationTelephone
     - Phones.Value
     - "string"


Webcrm Persons to Superoffice Person
------------------------------------
Every Webcrm Persons will be synchronized with a Superoffice Person.

Once a link between a Webcrm Persons and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - PersonDirectPhone
     - OfficePhones.Value
     - "string"
   * - PersonFirstName
     - Firstname
     - "string"
   * - PersonLastName
     - Lastname
     - "string"
   * - PersonMobilePhone
     - MobilePhones.Value
     - "string"
   * - PersonOrganisationId
     - Contact.ContactId
     - "integer"
   * - document_number
     - BirthDate
     - N/A


Webcrm Users to Superoffice Person
----------------------------------
Every Webcrm Users will be synchronized with a Superoffice Person.

Once a link between a Webcrm Users and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - UserMobilePhone
     - MobilePhones.Value
     - "string"
   * - UserTelephone
     - OfficePhones.Value
     - "string"


Webcrm Opportunities to Superoffice Sale
----------------------------------------
Every Webcrm Opportunities will be synchronized with a Superoffice Sale.

Once a link between a Webcrm Opportunities and a Superoffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Opportunities and a Superoffice Sale:

.. list-table::
   :header-rows: 1

   * - Webcrm Opportunities Property
     - Superoffice Sale Property
     - Superoffice Data Type
   * - OpportunityCurrencyName
     - Currency.Id
     - "integer"


Webcrm Products to Superoffice Product
--------------------------------------
Every Webcrm Products will be synchronized with a Superoffice Product.

Once a link between a Webcrm Products and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - ProductCostPrice
     - UnitCost
     - "string"
   * - ProductPrice
     - UnitListPrice
     - N/A
   * - ProductVatCode
     - VAT
     - N/A


Webcrm Quotationline to Superoffice Quoteline
---------------------------------------------
Every Webcrm Quotationline will be synchronized with a Superoffice Quoteline.

Once a link between a Webcrm Quotationline and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Superoffice Quoteline Property
     - Superoffice Data Type

