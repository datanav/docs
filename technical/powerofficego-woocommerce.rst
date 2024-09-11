=====================================
PowerOfficeGO to WooCommerce Dataflow
=====================================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to WooCommerce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGOPowerOffice GOPowerofficego Product to WooCommerceWoocommerce Product
----------------------------------------------------------------------------------
Every PowerOfficeGOPowerOffice GOPowerofficego Product will be synchronized with a WooCommerceWoocommerce Product.

Once a link between a PowerOfficeGOPowerOffice GOPowerofficego Product and a WooCommerceWoocommerce Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerOffice GOPowerofficego Product and a WooCommerceWoocommerce Product:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerOffice GOPowerofficego Product Property
     - WooCommerceWoocommerce Product Property
     - WooCommerceWoocommerce Data Type
   * - costPrice
     - price
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - sale_price
     - "string"


PowerOfficeGOPowerOffice GOPowerofficego Salesorders to WooCommerceWoocommerce Order
------------------------------------------------------------------------------------
Every PowerOfficeGOPowerOffice GOPowerofficego Salesorders will be synchronized with a WooCommerceWoocommerce Order.

Once a link between a PowerOfficeGOPowerOffice GOPowerofficego Salesorders and a WooCommerceWoocommerce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGOPowerOffice GOPowerofficego Salesorders and a WooCommerceWoocommerce Order:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGOPowerOffice GOPowerofficego Salesorders Property
     - WooCommerceWoocommerce Order Property
     - WooCommerceWoocommerce Data Type
   * - CurrencyCode
     - currency
     - "string"
   * - CustomerId
     - customer_id
     - "string"
   * - CustomerReferenceContactPersonId
     - customer_id
     - "string"

