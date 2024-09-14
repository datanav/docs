==========================
HubSpot to WebCRM Dataflow
==========================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to WebCRM Organisations
---------------------------------------
Every HubSpot Company will be synchronized with a WebCRM Organisations.

Once a link between a HubSpot Company and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - properties.description
     - OrganisationCompanyDescription
     - "string"
   * - properties.name
     - OrganisationName
     - "string"
   * - properties.phone
     - OrganisationTelephone
     - "string"


HubSpot Deal to WebCRM Opportunities
------------------------------------
Every HubSpot Deal will be synchronized with a WebCRM Opportunities.

Once a link between a HubSpot Deal and a WebCRM Opportunities is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a WebCRM Opportunities:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - WebCRM Opportunities Property
     - WebCRM Data Type
   * - properties.deal_currency_code
     - OpportunityCurrencyName
     - "string"
   * - properties.description
     - OpportunityCurrencySymbol
     - "string"
   * - properties.hubspot_owner_id
     - OpportunityPersonId
     - "string"


HubSpot Lineitem to WebCRM Quotationline
----------------------------------------
Every HubSpot Lineitem will be synchronized with a WebCRM Quotationline.

Once a link between a HubSpot Lineitem and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
   * - properties.hs_discount_percentage
     - QuotationLineDiscount
     - "string"
   * - properties.price
     - QuotationLinePrice
     - "string"
   * - properties.quantity
     - QuotationLineQuantity
     - "string"


HubSpot Product to WebCRM Products
----------------------------------
Every HubSpot Product will be synchronized with a WebCRM Products.

Once a link between a HubSpot Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - properties.hs_cost_of_goods_sold
     - ProductCostPrice
     - "string"
   * - properties.price
     - ProductPrice
     - "string"


HubSpot User to WebCRM Users
----------------------------
Every HubSpot User will be synchronized with a WebCRM Users.

Once a link between a HubSpot User and a WebCRM Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a WebCRM Users:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - WebCRM Users Property
     - WebCRM Data Type
   * - email
     - UserEmail
     - "string"

