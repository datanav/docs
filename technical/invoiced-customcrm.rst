==============================
Invoiced to Customcrm Dataflow
==============================

Generated: 2024-09-10 14:15:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Customcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Contacts to Customcrm Contact
--------------------------------------
Every Invoiced Contacts will be synchronized with a Customcrm Contact.

Once a link between a Invoiced Contacts and a Customcrm Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Customcrm Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Customcrm Contact Property
     - Customcrm Data Type


Invoiced Contacts to Customcrm Product
--------------------------------------
Every Invoiced Contacts will be synchronized with a Customcrm Product.

Once a link between a Invoiced Contacts and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Customcrm Product Property
     - Customcrm Data Type


Invoiced Customers company to Customcrm Customer
------------------------------------------------
Every Invoiced Customers company will be synchronized with a Customcrm Customer.

Once a link between a Invoiced Customers company and a Customcrm Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Customcrm Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Customcrm Customer Property
     - Customcrm Data Type
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


Invoiced Invoices to Customcrm Order
------------------------------------
Every Invoiced Invoices will be synchronized with a Customcrm Order.

Once a link between a Invoiced Invoices and a Customcrm Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Customcrm Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Customcrm Order Property
     - Customcrm Data Type


Invoiced Items to Customcrm Product
-----------------------------------
Every Invoiced Items will be synchronized with a Customcrm Product.

Once a link between a Invoiced Items and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Customcrm Product Property
     - Customcrm Data Type

