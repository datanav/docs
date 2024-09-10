====================================
Wave Financial to Customcrm Dataflow
====================================

Generated: 2024-09-10 14:15:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Customcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Customcrm Contact
----------------------------------
Every Wave Customer will be synchronized with a Customcrm Contact.

Once a link between a Wave Customer and a Customcrm Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Customcrm Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Customcrm Contact Property
     - Customcrm Data Type


Wave Customer to Customcrm Customer
-----------------------------------
Every Wave Customer will be synchronized with a Customcrm Customer.

Once a link between a Wave Customer and a Customcrm Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Customcrm Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Customcrm Customer Property
     - Customcrm Data Type
   * - address.addressLine1
     - StreetAddress1
     - "string"
   * - address.addressLine2
     - StreetAddress2
     - "string"
   * - address.city
     - City
     - "string"
   * - address.postalCode
     - ZipCode
     - "string"
   * - fax
     - Fax
     - "string"
   * - internalNotes
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - shippingDetails.address.addressLine1
     - StreetAddress1
     - "string"
   * - shippingDetails.address.addressLine2
     - StreetAddress2
     - "string"
   * - shippingDetails.address.city
     - City
     - "string"
   * - shippingDetails.address.postalCode
     - ZipCode
     - "string"
   * - website
     - Website
     - "string"


Wave Customer to Customcrm Product
----------------------------------
Every Wave Customer will be synchronized with a Customcrm Product.

Once a link between a Wave Customer and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Customcrm Product Property
     - Customcrm Data Type


Wave Invoice to Customcrm Order
-------------------------------
Every Wave Invoice will be synchronized with a Customcrm Order.

Once a link between a Wave Invoice and a Customcrm Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Customcrm Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Customcrm Order Property
     - Customcrm Data Type


Wave Product to Customcrm Product
---------------------------------
Every Wave Product will be synchronized with a Customcrm Product.

Once a link between a Wave Product and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Customcrm Product Property
     - Customcrm Data Type


Wave Vendor to Customcrm Contact
--------------------------------
Every Wave Vendor will be synchronized with a Customcrm Contact.

Once a link between a Wave Vendor and a Customcrm Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Customcrm Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Customcrm Contact Property
     - Customcrm Data Type


Wave Vendor to Customcrm Product
--------------------------------
Every Wave Vendor will be synchronized with a Customcrm Product.

Once a link between a Wave Vendor and a Customcrm Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Customcrm Product:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Customcrm Product Property
     - Customcrm Data Type

