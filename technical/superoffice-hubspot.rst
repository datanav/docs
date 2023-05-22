===============================
SuperOffice to HubSpot Dataflow
===============================

Generated: 2023-05-22 22:30:21

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - Address.Postal.Address1
     - properties.address
     - "string"
   * - Address.Postal.Address2
     - properties.address2
     - "string"
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
   * - Urls.Value
     - properties.website
     - "string"


SuperOffice Person to HubSpot Contact
-------------------------------------
Every SuperOffice Person will be synchronized with a HubSpot Contact.

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


SuperOffice Product to HubSpot Product
--------------------------------------
Every SuperOffice Product will be synchronized with a HubSpot Product.

Once a link between a SuperOffice Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - Description
     - properties.description
     - "string"
   * - ERPProductKey
     - properties.hs_sku
     - "string"
   * - Name
     - properties.name
     - "string"
   * - UnitCost
     - properties.hs_cost_of_goods_sold
     - "string"
   * - UnitListPrice
     - properties.price
     - "string"


SuperOffice Quotealternative to HubSpot Quote
---------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a HubSpot Quote.

Once a link between a SuperOffice Quotealternative and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - HubSpot Quote Property
     - HubSpot Data Type
   * - Name
     - properties.hs_title
     - "string"
   * - TotalPrice
     - properties.hs_quote_amount
     - "string"


SuperOffice Quoteline to HubSpot Lineitem
-----------------------------------------
Every SuperOffice Quoteline will be synchronized with a HubSpot Lineitem.

Once a link between a SuperOffice Quoteline and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
   * - Name
     - properties.name
     - "string"
   * - Quantity
     - properties.quantity
     - "string"
   * - UnitListPrice
     - properties.price
     - "string"


SuperOffice Sale to HubSpot Deal
--------------------------------
When a Superoffice Sale gets the status "Sold", it  will be synchronized with a HubSpot Deal.

Once a link between a SuperOffice Sale and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - Amount
     - properties.amount
     - "string"
   * - CreatedDate
     - properties.createdate
     - "string"
   * - Currency.Id
     - properties.deal_currency_code
     - "string"
   * - SaleText
     - properties.dealname
     - "string"
   * - SaleText
     - properties.description
     - "string"
   * - Saledate
     - properties.closedate
     - "string"
   * - Status
     - properties.dealstage
     - "string"


SuperOffice Ticket to HubSpot Ticket
------------------------------------
Every SuperOffice Ticket will be synchronized with a HubSpot Ticket.

Once a link between a SuperOffice Ticket and a HubSpot Ticket is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ticket and a HubSpot Ticket:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ticket Property
     - HubSpot Ticket Property
     - HubSpot Data Type
   * - CreatedAt
     - properties.createdate
     - "string"
   * - OwnedBy.AssociateId
     - properties.hubspot_owner_id
     - "string"
   * - Title
     - properties.subject
     - "string"


SuperOffice User to HubSpot User
--------------------------------
Every SuperOffice User will be synchronized with a HubSpot User.

Once a link between a SuperOffice User and a HubSpot User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a HubSpot User:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - HubSpot User Property
     - HubSpot Data Type

