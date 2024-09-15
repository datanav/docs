==============================
SuperOffice to WebCRM Dataflow
==============================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to WebCRM Organisations
-------------------------------------------
Every SuperOffice Contact will be synchronized with a WebCRM Organisations.

Once a link between a SuperOffice Contact and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - Address.Postal.Address1
     - OrganisationAddress
     - "string"
   * - Address.Postal.Address1
     - OrganisationDeliveryAddress
     - "string"
   * - Address.Postal.City
     - OrganisationCity
     - "string"
   * - Address.Postal.City
     - OrganisationDeliveryCity
     - "string"
   * - Address.Postal.Zipcode
     - OrganisationDeliveryPostCode
     - "string"
   * - Address.Postal.Zipcode
     - OrganisationPostCode
     - "string"
   * - Address.Street.Address1
     - OrganisationAddress
     - "string"
   * - Address.Street.Address1
     - OrganisationDeliveryAddress
     - "string"
   * - Address.Street.City
     - OrganisationCity
     - "string"
   * - Address.Street.City
     - OrganisationDeliveryCity
     - "string"
   * - Address.Street.Zipcode
     - OrganisationDeliveryPostCode
     - "string"
   * - Address.Street.Zipcode
     - OrganisationPostCode
     - "string"
   * - ContactId
     - OrganisationId
     - "string"
   * - Name
     - OrganisationName
     - "string"
   * - Phones.Value
     - OrganisationTelephone
     - "string"


SuperOffice Product to WebCRM Products
--------------------------------------
Every SuperOffice Product will be synchronized with a WebCRM Products.

Once a link between a SuperOffice Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - UnitCost
     - ProductCostPrice
     - "string"
   * - UnitListPrice
     - ProductPrice
     - "string"
   * - VAT
     - ProductVatCode
     - "string"


SuperOffice Quoteline to WebCRM Quotationline
---------------------------------------------
Every SuperOffice Quoteline will be synchronized with a WebCRM Quotationline.

Once a link between a SuperOffice Quoteline and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
   * - DiscountPercent
     - QuotationLineDiscount
     - "string"
   * - ERPDiscountPercent
     - QuotationLineDiscount
     - "string"
   * - Quantity
     - QuotationLineQuantity
     - "string"
   * - QuoteAlternativeId
     - QuotationLineOpportunityId
     - "string"
   * - UnitListPrice
     - QuotationLinePrice
     - "string"
   * - VAT
     - QuotationLineVatPercentage
     - "string"


SuperOffice Sale to WebCRM Opportunities
----------------------------------------
Every SuperOffice Sale will be synchronized with a WebCRM Opportunities.

Once a link between a SuperOffice Sale and a WebCRM Opportunities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a WebCRM Opportunities:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - WebCRM Opportunities Property
     - WebCRM Data Type
   * - Contact.ContactId
     - OpportunityOrganisationId
     - "string"
   * - Currency.Id
     - OpportunityCurrencyName
     - "string"
   * - Person.PersonId
     - OpportunityOrganisationId
     - "string"


SuperOffice User to WebCRM Users
--------------------------------
Every SuperOffice User will be synchronized with a WebCRM Users.

Once a link between a SuperOffice User and a WebCRM Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a WebCRM Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - WebCRM Users Property
     - WebCRM Data Type
   * - personEmail
     - UserEmail
     - "string"

