===================================
Wave to Visma Business Nxt Dataflow
===================================

Generated: 2024-09-11 07:53:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Businessnxt Address
------------------------------------
Every Wave Customer will be synchronized with a Businessnxt Address.

Once a link between a Wave Customer and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - fax
     - fax
     - "string"
   * - name
     - name
     - "string"
   * - phone
     - phone
     - "string"
   * - shippingDetails.phone
     - phone
     - "string"


Wave Country to Visma Country
-----------------------------
Every Wave Country will be synchronized with a Visma Country.

Once a link between a Wave Country and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - Visma Country Property
     - Visma Data Type
   * - currency.code
     - currencyNo
     - "string"
   * - name
     - name
     - "string"


Wave Currency to Visma Currency
-------------------------------
Every Wave Currency will be synchronized with a Visma Currency.

Once a link between a Wave Currency and a Visma Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a Visma Currency:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Visma Currency Property
     - Visma Data Type
   * - name
     - name
     - "string"


Wave Invoice to Visma Order
---------------------------
Every Wave Invoice will be synchronized with a Visma Order.

Once a link between a Wave Invoice and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Visma Order Property
     - Visma Data Type
   * - invoiceDate
     - invoiceDate
     - "string"
   * - title
     - name
     - "string"


Wave Invoice to Visma Orderline
-------------------------------
Every Wave Invoice will be synchronized with a Visma Orderline.

Once a link between a Wave Invoice and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Visma Orderline Property
     - Visma Data Type
   * - id
     - orderNo
     - "string"


Wave Product to Visma Product
-----------------------------
Every Wave Product will be synchronized with a Visma Product.

Once a link between a Wave Product and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Visma Product Property
     - Visma Data Type
   * - description
     - description
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"

