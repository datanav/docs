================================
Tripletex to Custom CRM Dataflow
================================

Generated: 2024-09-11 07:44:14

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Custom CRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to Custom Contact
-------------------------------------------
Every Tripletex Customer person will be synchronized with a Custom Contact.

Once a link between a Tripletex Customer person and a Custom Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Custom Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Custom Contact Property
     - Custom Data Type


Tripletex Department to Custom Customer
---------------------------------------
Every Tripletex Department will be synchronized with a Custom Customer.

Once a link between a Tripletex Department and a Custom Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Custom Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Custom Customer Property
     - Custom Data Type


Tripletex Employee to Custom Contact
------------------------------------
Every Tripletex Employee will be synchronized with a Custom Contact.

Once a link between a Tripletex Employee and a Custom Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Custom Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Custom Contact Property
     - Custom Data Type


Tripletex Orderline to Custom Order
-----------------------------------
Every Tripletex Orderline will be synchronized with a Custom Order.

Once a link between a Tripletex Orderline and a Custom Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Custom Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Custom Order Property
     - Custom Data Type


Tripletex Contact to Custom Contact
-----------------------------------
Every Tripletex Contact will be synchronized with a Custom Contact.

Once a link between a Tripletex Contact and a Custom Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Custom Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Custom Contact Property
     - Custom Data Type


Tripletex Customer to Custom Customer
-------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Custom Customer.

Once a link between a Tripletex Customer and a Custom Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Custom Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Custom Customer Property
     - Custom Data Type
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


Tripletex Order to Custom Order
-------------------------------
Every Tripletex Order will be synchronized with a Custom Order.

Once a link between a Tripletex Order and a Custom Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Custom Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Custom Order Property
     - Custom Data Type


Tripletex Product to Custom Product
-----------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Custom Product.

Once a link between a Tripletex Product and a Custom Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Custom Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Custom Product Property
     - Custom Data Type

