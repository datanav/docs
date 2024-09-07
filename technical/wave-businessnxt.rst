======================================
Wave Financial to Businessnxt Dataflow
======================================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Wave Country to Businessnxt Country
-----------------------------------
Every Wave Country will be synchronized with a Businessnxt Country.

Once a link between a Wave Country and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - currency.code
     - currencyNo
     - "string"
   * - name
     - name
     - "string"


Wave Currency to Businessnxt Currency
-------------------------------------
Every Wave Currency will be synchronized with a Businessnxt Currency.

Once a link between a Wave Currency and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Businessnxt Currency Property
     - Businessnxt Data Type
   * - name
     - name
     - "string"


Wave Invoice to Businessnxt Order
---------------------------------
Every Wave Invoice will be synchronized with a Businessnxt Order.

Once a link between a Wave Invoice and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - invoiceDate
     - invoiceDate
     - "string"
   * - title
     - name
     - "string"


Wave Invoice to Businessnxt Orderline
-------------------------------------
Every Wave Invoice will be synchronized with a Businessnxt Orderline.

Once a link between a Wave Invoice and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type
   * - id
     - orderNo
     - "string"


Wave Product to Businessnxt Product
-----------------------------------
Every Wave Product will be synchronized with a Businessnxt Product.

Once a link between a Wave Product and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - description
     - description
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"

