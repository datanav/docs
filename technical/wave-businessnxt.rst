============================
Wave to BusinessNxt Dataflow
============================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to BusinessNxt Address
------------------------------------
Every Wave Customer will be synchronized with a BusinessNxt Address.

Once a link between a Wave Customer and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
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


Wave Country to BusinessNxt Country
-----------------------------------
Every Wave Country will be synchronized with a BusinessNxt Country.

Once a link between a Wave Country and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - currency.code
     - currencyNo
     - "string"
   * - name
     - name
     - "string"


Wave Currency to BusinessNxt Currency
-------------------------------------
Every Wave Currency will be synchronized with a BusinessNxt Currency.

Once a link between a Wave Currency and a BusinessNxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a BusinessNxt Currency:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - BusinessNxt Currency Property
     - BusinessNxt Data Type
   * - name
     - name
     - "string"


Wave Invoice to BusinessNxt Order
---------------------------------
Every Wave Invoice will be synchronized with a BusinessNxt Order.

Once a link between a Wave Invoice and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - invoiceDate
     - invoiceDate
     - "string"
   * - title
     - name
     - "string"


Wave Invoice to BusinessNxt Orderline
-------------------------------------
Every Wave Invoice will be synchronized with a BusinessNxt Orderline.

Once a link between a Wave Invoice and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type
   * - id
     - orderNo
     - "string"


Wave Product to BusinessNxt Product
-----------------------------------
Every Wave Product will be synchronized with a BusinessNxt Product.

Once a link between a Wave Product and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
   * - description
     - description
     - "string"
   * - unitPrice
     - priceQuantity
     - "string"

