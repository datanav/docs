===================================
Powerofficego to Customcrm Dataflow
===================================

Generated: 2024-09-10 14:11:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Customcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Customcrm Contact
------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Customcrm Contact.

Once a link between a Powerofficego Contactperson and a Customcrm Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Customcrm Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Customcrm Contact Property
     - Customcrm Data Type


Powerofficego Contactperson to Customcrm Product
------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Customcrm Product.

Once a link between a Powerofficego Contactperson and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Customcrm Product Property
     - Customcrm Data Type


Powerofficego Customers to Customcrm Customer
---------------------------------------------
Every Powerofficego Customers will be synchronized with a Customcrm Customer.

Once a link between a Powerofficego Customers and a Customcrm Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Customcrm Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Customcrm Customer Property
     - Customcrm Data Type
   * - MailAddress.AddressLine1
     - StreetAddress1
     - "string"
   * - MailAddress.AddressLine2
     - StreetAddress2
     - "string"
   * - MailAddress.City
     - City
     - "string"
   * - MailAddress.ZipCode
     - ZipCode
     - "string"
   * - Name
     - Name
     - "string"
   * - WebsiteUrl
     - Website
     - "string"


Powerofficego Suppliers person to Customcrm Contact
---------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Customcrm Contact.

Once a link between a Powerofficego Suppliers person and a Customcrm Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Customcrm Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Customcrm Contact Property
     - Customcrm Data Type


Powerofficego Suppliers person to Customcrm Product
---------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Customcrm Product.

Once a link between a Powerofficego Suppliers person and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Customcrm Product Property
     - Customcrm Data Type

