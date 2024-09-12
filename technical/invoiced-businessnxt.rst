=================================
Invoiced to Business Nxt Dataflow
=================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Business Nxt Address
--------------------------------------------------
Every Invoiced Customers company will be synchronized with a Business Nxt Address.

Once a link between a Invoiced Customers company and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - name
     - name
     - "string"


Invoiced Lineitem to Business Nxt Order
---------------------------------------
Every Invoiced Lineitem will be synchronized with a Business Nxt Order.

Once a link between a Invoiced Lineitem and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Business Nxt Order Property
     - Business Nxt Data Type


Invoiced Invoices to Business Nxt Order
---------------------------------------
Every Invoiced Invoices will be synchronized with a Business Nxt Order.

Once a link between a Invoiced Invoices and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - discounts
     - totalDiscountAmountInCurrency
     - "string"


Invoiced Items to Business Nxt Product
--------------------------------------
Every Invoiced Items will be synchronized with a Business Nxt Product.

Once a link between a Invoiced Items and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - description
     - description
     - "string"


Invoiced Lineitem to Business Nxt Orderline
-------------------------------------------
Every Invoiced Lineitem will be synchronized with a Business Nxt Orderline.

Once a link between a Invoiced Lineitem and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type
   * - $original_id
     - orderNo
     - "string"

