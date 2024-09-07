==============================
SuperOffice to Webcrm Dataflow
==============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Webcrm Organisations
-------------------------------------------
Every SuperOffice Contact will be synchronized with a Webcrm Organisations.

Once a link between a SuperOffice Contact and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Webcrm Organisations Property
     - Webcrm Data Type
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


SuperOffice Product to Webcrm Products
--------------------------------------
Every SuperOffice Product will be synchronized with a Webcrm Products.

Once a link between a SuperOffice Product and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - UnitCost
     - ProductCostPrice
     - "string"
   * - UnitListPrice
     - ProductPrice
     - "string"
   * - VAT
     - ProductVatCode
     - "string"


SuperOffice Quoteline to Webcrm Quotationline
---------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Webcrm Quotationline.

Once a link between a SuperOffice Quoteline and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
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


SuperOffice Sale to Webcrm Opportunities
----------------------------------------
Every SuperOffice Sale will be synchronized with a Webcrm Opportunities.

Once a link between a SuperOffice Sale and a Webcrm Opportunities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Webcrm Opportunities:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Webcrm Opportunities Property
     - Webcrm Data Type
   * - Contact.ContactId
     - OpportunityOrganisationId
     - "string"
   * - Currency.Id
     - OpportunityCurrencyName
     - "string"
   * - Person.PersonId
     - OpportunityOrganisationId
     - "string"


SuperOffice User to Webcrm Users
--------------------------------
Every SuperOffice User will be synchronized with a Webcrm Users.

Once a link between a SuperOffice User and a Webcrm Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Webcrm Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Webcrm Users Property
     - Webcrm Data Type
   * - personEmail
     - UserEmail
     - "string"

