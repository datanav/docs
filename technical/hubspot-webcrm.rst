==========================
HubSpot to Webcrm Dataflow
==========================

Generated: 2024-09-10 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Webcrm Organisations
---------------------------------------
Every HubSpot Company will be synchronized with a Webcrm Organisations.

Once a link between a HubSpot Company and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - properties.description
     - OrganisationCompanyDescription
     - "string"
   * - properties.name
     - OrganisationName
     - "string"
   * - properties.phone
     - OrganisationTelephone
     - "string"


HubSpot Deal to Webcrm Opportunities
------------------------------------
Every HubSpot Deal will be synchronized with a Webcrm Opportunities.

Once a link between a HubSpot Deal and a Webcrm Opportunities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Webcrm Opportunities:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Webcrm Opportunities Property
     - Webcrm Data Type
   * - properties.deal_currency_code
     - OpportunityCurrencyName
     - "string"
   * - properties.description
     - OpportunityCurrencySymbol
     - "string"
   * - properties.hubspot_owner_id
     - OpportunityPersonId
     - "string"


HubSpot Lineitem to Webcrm Quotationline
----------------------------------------
Every HubSpot Lineitem will be synchronized with a Webcrm Quotationline.

Once a link between a HubSpot Lineitem and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
   * - properties.hs_discount_percentage
     - QuotationLineDiscount
     - "string"
   * - properties.price
     - QuotationLinePrice
     - "string"
   * - properties.quantity
     - QuotationLineQuantity
     - "string"


HubSpot Product to Webcrm Products
----------------------------------
Every HubSpot Product will be synchronized with a Webcrm Products.

Once a link between a HubSpot Product and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - properties.hs_cost_of_goods_sold
     - ProductCostPrice
     - "string"
   * - properties.price
     - ProductPrice
     - "string"


HubSpot User to Webcrm Users
----------------------------
Every HubSpot User will be synchronized with a Webcrm Users.

Once a link between a HubSpot User and a Webcrm Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Webcrm Users:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Webcrm Users Property
     - Webcrm Data Type
   * - email
     - UserEmail
     - "string"

