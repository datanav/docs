===============================
Tripletex to CustomCRM Dataflow
===============================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to CustomCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to CustomCRM Contact
----------------------------------------------
Every Tripletex Customer person will be synchronized with a CustomCRM Contact.

Once a link between a Tripletex Customer person and a CustomCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a CustomCRM Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - CustomCRM Contact Property
     - CustomCRM Data Type


Tripletex Department to CustomCRM Customer
------------------------------------------
Every Tripletex Department will be synchronized with a CustomCRM Customer.

Once a link between a Tripletex Department and a CustomCRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a CustomCRM Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - CustomCRM Customer Property
     - CustomCRM Data Type


Tripletex Employee to CustomCRM Contact
---------------------------------------
Every Tripletex Employee will be synchronized with a CustomCRM Contact.

Once a link between a Tripletex Employee and a CustomCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a CustomCRM Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - CustomCRM Contact Property
     - CustomCRM Data Type


Tripletex Orderline to CustomCRM Order
--------------------------------------
Every Tripletex Orderline will be synchronized with a CustomCRM Order.

Once a link between a Tripletex Orderline and a CustomCRM Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a CustomCRM Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - CustomCRM Order Property
     - CustomCRM Data Type


Tripletex Contact to CustomCRM Contact
--------------------------------------
Every Tripletex Contact will be synchronized with a CustomCRM Contact.

Once a link between a Tripletex Contact and a CustomCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a CustomCRM Contact:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - CustomCRM Contact Property
     - CustomCRM Data Type


Tripletex Customer to CustomCRM Customer
----------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a CustomCRM Customer.

Once a link between a Tripletex Customer and a CustomCRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a CustomCRM Customer:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - CustomCRM Customer Property
     - CustomCRM Data Type
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


Tripletex Order to CustomCRM Order
----------------------------------
Every Tripletex Order will be synchronized with a CustomCRM Order.

Once a link between a Tripletex Order and a CustomCRM Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a CustomCRM Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - CustomCRM Order Property
     - CustomCRM Data Type


Tripletex Product to CustomCRM Product
--------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a CustomCRM Product.

Once a link between a Tripletex Product and a CustomCRM Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a CustomCRM Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - CustomCRM Product Property
     - CustomCRM Data Type

