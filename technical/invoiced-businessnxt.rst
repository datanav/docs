================================
Invoiced to BusinessNxt Dataflow
================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Businessnxt Address
-------------------------------------------------
Every Invoiced Customers company will be synchronized with a Businessnxt Address.

Once a link between a Invoiced Customers company and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - name
     - name
     - "string"


Invoiced Lineitem to Businessnxt Order
--------------------------------------
Every Invoiced Lineitem will be synchronized with a Businessnxt Order.

Once a link between a Invoiced Lineitem and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Invoiced Invoices to BusinessNxt Order
--------------------------------------
Every Invoiced Invoices will be synchronized with a BusinessNxt Order.

Once a link between a Invoiced Invoices and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - discounts
     - totalDiscountAmountInCurrency
     - "string"


Invoiced Items to BusinessNxt Product
-------------------------------------
Every Invoiced Items will be synchronized with a BusinessNxt Product.

Once a link between a Invoiced Items and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
   * - description
     - description
     - "string"


Invoiced Lineitem to BusinessNxt Orderline
------------------------------------------
Every Invoiced Lineitem will be synchronized with a BusinessNxt Orderline.

Once a link between a Invoiced Lineitem and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type
   * - $original_id
     - orderNo
     - "string"

