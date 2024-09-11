===========================
Wave to Custom CRM Dataflow
===========================

Generated: 2024-09-11 07:53:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Custom CRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Custom Contact
--------------------------------------
Every Wave Customer person will be synchronized with a Custom Contact.

Once a link between a Wave Customer person and a Custom Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Custom Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Custom Contact Property
     - Custom Data Type


Wave Customer to Custom Contact
-------------------------------
Every Wave Customer will be synchronized with a Custom Contact.

Once a link between a Wave Customer and a Custom Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Custom Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Custom Contact Property
     - Custom Data Type


Wave Customer to Custom Customer
--------------------------------
Every Wave Customer will be synchronized with a Custom Customer.

Once a link between a Wave Customer and a Custom Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Custom Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Custom Customer Property
     - Custom Data Type
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


Wave Invoice to Custom Order
----------------------------
Every Wave Invoice will be synchronized with a Custom Order.

Once a link between a Wave Invoice and a Custom Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Custom Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Custom Order Property
     - Custom Data Type


Wave Product to Custom Product
------------------------------
Every Wave Product will be synchronized with a Custom Product.

Once a link between a Wave Product and a Custom Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Custom Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Custom Product Property
     - Custom Data Type


Wave Vendor to Custom Contact
-----------------------------
Every Wave Vendor will be synchronized with a Custom Contact.

Once a link between a Wave Vendor and a Custom Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Custom Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Custom Contact Property
     - Custom Data Type

