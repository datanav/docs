==============================
Invoiced to CustomCRM Dataflow
==============================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to CustomCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers person to Custom Contact
-------------------------------------------
Every Invoiced Customers person will be synchronized with a Custom Contact.

Once a link between a Invoiced Customers person and a Custom Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Custom Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Custom Contact Property
     - Custom Data Type


Invoiced Lineitem to Custom Order
---------------------------------
Every Invoiced Lineitem will be synchronized with a Custom Order.

Once a link between a Invoiced Lineitem and a Custom Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Custom Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Custom Order Property
     - Custom Data Type


Invoiced Contacts to CustomCRM Contact
--------------------------------------
Every Invoiced Contacts will be synchronized with a CustomCRM Contact.

Once a link between a Invoiced Contacts and a CustomCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a CustomCRM Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - CustomCRM Contact Property
     - CustomCRM Data Type


Invoiced Customers company to CustomCRM Customer
------------------------------------------------
Every Invoiced Customers company will be synchronized with a CustomCRM Customer.

Once a link between a Invoiced Customers company and a CustomCRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a CustomCRM Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - CustomCRM Customer Property
     - CustomCRM Data Type
   * - address1
     - StreetAddress1
     - "string"
   * - address2
     - StreetAddress2
     - "string"
   * - city
     - City
     - "string"
   * - name
     - Name
     - "string"
   * - postal_code
     - ZipCode
     - "string"


Invoiced Invoices to CustomCRM Order
------------------------------------
Every Invoiced Invoices will be synchronized with a CustomCRM Order.

Once a link between a Invoiced Invoices and a CustomCRM Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a CustomCRM Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - CustomCRM Order Property
     - CustomCRM Data Type


Invoiced Items to CustomCRM Product
-----------------------------------
Every Invoiced Items will be synchronized with a CustomCRM Product.

Once a link between a Invoiced Items and a CustomCRM Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a CustomCRM Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - CustomCRM Product Property
     - CustomCRM Data Type

