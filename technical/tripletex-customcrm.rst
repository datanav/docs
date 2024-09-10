===============================
Tripletex to Customcrm Dataflow
===============================

Generated: 2024-09-10 14:16:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Customcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Contact to Customcrm Contact
--------------------------------------
Every Tripletex Contact will be synchronized with a Customcrm Contact.

Once a link between a Tripletex Contact and a Customcrm Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Customcrm Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Customcrm Contact Property
     - Customcrm Data Type


Tripletex Contact to Customcrm Product
--------------------------------------
Every Tripletex Contact will be synchronized with a Customcrm Product.

Once a link between a Tripletex Contact and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Customcrm Product Property
     - Customcrm Data Type


Tripletex Customer to Customcrm Customer
----------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Customcrm Customer.

Once a link between a Tripletex Customer and a Customcrm Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Customcrm Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Customcrm Customer Property
     - Customcrm Data Type
   * - deliveryAddress.addressLine1
     - StreetAddress1
     - "string"
   * - deliveryAddress.addressLine2
     - StreetAddress2
     - "string"
   * - deliveryAddress.city
     - City
     - "string"
   * - deliveryAddress.postalCode
     - ZipCode
     - "string"
   * - name
     - Name
     - "string"
   * - phoneNumberMobile
     - Phone
     - "string"
   * - physicalAddress.addressLine1
     - StreetAddress1
     - "string"
   * - physicalAddress.addressLine2
     - StreetAddress2
     - "string"
   * - physicalAddress.city
     - City
     - "string"
   * - physicalAddress.postalCode
     - ZipCode
     - "string"
   * - postalAddress.addressLine1
     - StreetAddress1
     - "string"
   * - postalAddress.addressLine2
     - StreetAddress2
     - "string"
   * - postalAddress.city
     - City
     - "string"
   * - postalAddress.postalCode
     - ZipCode
     - "string"
   * - website
     - Website
     - "string"


Tripletex Order to Customcrm Order
----------------------------------
Every Tripletex Order will be synchronized with a Customcrm Order.

Once a link between a Tripletex Order and a Customcrm Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Customcrm Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Customcrm Order Property
     - Customcrm Data Type


Tripletex Order to Customcrm User
---------------------------------
Every Tripletex Order will be synchronized with a Customcrm User.

Once a link between a Tripletex Order and a Customcrm User is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Customcrm User:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Customcrm User Property
     - Customcrm Data Type


Tripletex Product to Customcrm Product
--------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Customcrm Product.

Once a link between a Tripletex Product and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Customcrm Product Property
     - Customcrm Data Type

