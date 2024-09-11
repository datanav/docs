=============================
Wave to Business Nxt Dataflow
=============================

Generated: 2024-09-11 12:17:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Business Nxt Address
-------------------------------------
Every Wave Customer will be synchronized with a Business Nxt Address.

Once a link between a Wave Customer and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Business Nxt Address Property
     - Business Nxt Data Type
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


Wave Country to Business Nxt Country
------------------------------------
Every Wave Country will be synchronized with a Business Nxt Country.

Once a link between a Wave Country and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - currency.code
     - currencyNo
     - "string"
   * - name
     - name
     - "string"


Wave Currency to Business Nxt Currency
--------------------------------------
Every Wave Currency will be synchronized with a Business Nxt Currency.

Once a link between a Wave Currency and a Business Nxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a Business Nxt Currency:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Business Nxt Currency Property
     - Business Nxt Data Type
   * - name
     - name
     - "string"


Wave Invoice to Business Nxt Order
----------------------------------
Every Wave Invoice will be synchronized with a Business Nxt Order.

Once a link between a Wave Invoice and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - invoiceDate
     - invoiceDate
     - "string"
   * - title
     - name
     - "string"


Wave Invoice to Business Nxt Orderline
--------------------------------------
Every Wave Invoice will be synchronized with a Business Nxt Orderline.

Once a link between a Wave Invoice and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type
   * - id
     - orderNo
     - "string"


Wave Product to Business Nxt Product
------------------------------------
Every Wave Product will be synchronized with a Business Nxt Product.

Once a link between a Wave Product and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - description
     - description
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"

