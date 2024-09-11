=====================================
WebCRM to Visma Business Nxt Dataflow
=====================================

Generated: 2024-09-11 07:48:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Opportunities to Businessnxt Order
-----------------------------------------
Every Webcrm Opportunities will be synchronized with a Businessnxt Order.

Once a link between a Webcrm Opportunities and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Opportunities and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Webcrm Opportunities Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - OpportunityDiscount
     - totalDiscountAmountInCurrency
     - "string"


Webcrm Organisations to Businessnxt Address
-------------------------------------------
Every Webcrm Organisations will be synchronized with a Businessnxt Address.

Once a link between a Webcrm Organisations and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - OrganisationName
     - name
     - "string"
   * - OrganisationTelephone
     - phone
     - "string"


Webcrm Quotationline to Businessnxt Order
-----------------------------------------
Every Webcrm Quotationline will be synchronized with a Businessnxt Order.

Once a link between a Webcrm Quotationline and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Businessnxt Order Property
     - Businessnxt Data Type


WebCRM Organisations to Visma Country
-------------------------------------
Every WebCRM Organisations will be synchronized with a Visma Country.

Once a link between a WebCRM Organisations and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Visma Country:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Visma Country Property
     - Visma Data Type
   * - OrganisationCountryData
     - isoCode
     - "string"
   * - OrganisationCountryData
     - name
     - "string"
   * - OrganisationCountryData.CodeISO
     - isoCode
     - "string"
   * - OrganisationCountryData.Name
     - name
     - "string"


WebCRM Products to Visma Product
--------------------------------
Every WebCRM Products will be synchronized with a Visma Product.

Once a link between a WebCRM Products and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Visma Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Visma Product Property
     - Visma Data Type
   * - ProductPrice
     - priceQuantity
     - "string"
   * - ProductQuantity
     - quantityPerUnit
     - "string"


WebCRM Quotationline to Visma Orderline
---------------------------------------
Every WebCRM Quotationline will be synchronized with a Visma Orderline.

Once a link between a WebCRM Quotationline and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Visma Orderline Property
     - Visma Data Type

