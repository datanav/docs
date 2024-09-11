==============================
WebCRM to SuperOffice Dataflow
==============================

Generated: 2024-09-11 07:56:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


WebCRM Opportunities to SuperOffice Sale
----------------------------------------
Every WebCRM Opportunities will be synchronized with a SuperOffice Sale.

Once a link between a WebCRM Opportunities and a SuperOffice Sale is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a SuperOffice Sale:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - SuperOffice Sale Property
     - SuperOffice Data Type
   * - OpportunityCurrencyName
     - Currency.Id
     - "integer"


WebCRM Products to SuperOffice Product
--------------------------------------
Every WebCRM Products will be synchronized with a SuperOffice Product.

Once a link between a WebCRM Products and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - ProductCostPrice
     - UnitCost
     - "string"
   * - ProductPrice
     - UnitListPrice
     - N/A
   * - ProductVatCode
     - VAT
     - N/A


WebCRM Quotationline to SuperOffice Quoteline
---------------------------------------------
Every WebCRM Quotationline will be synchronized with a SuperOffice Quoteline.

Once a link between a WebCRM Quotationline and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type

