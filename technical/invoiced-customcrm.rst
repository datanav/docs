===============================
Invoiced to Custom CRM Dataflow
===============================

Generated: 2024-09-11 11:41:16

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Custom CRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers person to CustomCRM Contact
----------------------------------------------
Every Invoiced Customers person will be synchronized with a CustomCRM Contact.

Once a link between a Invoiced Customers person and a CustomCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a CustomCRM Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - CustomCRM Contact Property
     - CustomCRM Data Type


Invoiced Lineitem to CustomCRM Order
------------------------------------
Every Invoiced Lineitem will be synchronized with a CustomCRM Order.

Once a link between a Invoiced Lineitem and a CustomCRM Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a CustomCRM Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - CustomCRM Order Property
     - CustomCRM Data Type


Invoiced Contacts to Custom CRM Contact
---------------------------------------
Every Invoiced Contacts will be synchronized with a Custom CRM Contact.

Once a link between a Invoiced Contacts and a Custom CRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Custom CRM Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Custom CRM Contact Property
     - Custom CRM Data Type


Invoiced Customers company to Custom CRM Customer
-------------------------------------------------
Every Invoiced Customers company will be synchronized with a Custom CRM Customer.

Once a link between a Invoiced Customers company and a Custom CRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Custom CRM Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Custom CRM Customer Property
     - Custom CRM Data Type
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


Invoiced Invoices to Custom CRM Order
-------------------------------------
Every Invoiced Invoices will be synchronized with a Custom CRM Order.

Once a link between a Invoiced Invoices and a Custom CRM Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Custom CRM Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Custom CRM Order Property
     - Custom CRM Data Type


Invoiced Items to Custom CRM Product
------------------------------------
Every Invoiced Items will be synchronized with a Custom CRM Product.

Once a link between a Invoiced Items and a Custom CRM Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Custom CRM Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Custom CRM Product Property
     - Custom CRM Data Type

