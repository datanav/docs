======================================
Wave Financial to Businessnxt Dataflow
======================================

Generated: 2024-09-03 08:55:46

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to  Address
-------------------------
Every Wave Customer will be synchronized with a  Address.

Once a link between a Wave Customer and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Address Property
     -  Data Type
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


Wave Country to  Country
------------------------
Every Wave Country will be synchronized with a  Country.

Once a link between a Wave Country and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a  Country:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     -  Country Property
     -  Data Type
   * - currency.code
     - currencyNo
     - "string"
   * - name
     - name
     - "string"


Wave Currency to  Currency
--------------------------
Every Wave Currency will be synchronized with a  Currency.

Once a link between a Wave Currency and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a  Currency:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     -  Currency Property
     -  Data Type
   * - name
     - name
     - "string"


Wave Invoice to  Order
----------------------
Every Wave Invoice will be synchronized with a  Order.

Once a link between a Wave Invoice and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Order Property
     -  Data Type
   * - invoiceDate
     - invoiceDate
     - "string"
   * - title
     - name
     - "string"


Wave Invoice to  Orderline
--------------------------
Every Wave Invoice will be synchronized with a  Orderline.

Once a link between a Wave Invoice and a  Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Orderline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Orderline Property
     -  Data Type
   * - id
     - orderNo
     - "string"


Wave Product to  Product
------------------------
Every Wave Product will be synchronized with a  Product.

Once a link between a Wave Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Product Property
     -  Data Type
   * - description
     - description
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"

