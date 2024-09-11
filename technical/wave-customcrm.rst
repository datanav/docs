==========================
Wave to CustomCRM Dataflow
==========================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to CustomCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to CustomCRM Contact
-----------------------------------------
Every Wave Customer person will be synchronized with a CustomCRM Contact.

Once a link between a Wave Customer person and a CustomCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a CustomCRM Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - CustomCRM Contact Property
     - CustomCRM Data Type


Wave Customer to CustomCRM Contact
----------------------------------
Every Wave Customer will be synchronized with a CustomCRM Contact.

Once a link between a Wave Customer and a CustomCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a CustomCRM Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - CustomCRM Contact Property
     - CustomCRM Data Type


Wave Customer to CustomCRM Customer
-----------------------------------
Every Wave Customer will be synchronized with a CustomCRM Customer.

Once a link between a Wave Customer and a CustomCRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a CustomCRM Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - CustomCRM Customer Property
     - CustomCRM Data Type
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


Wave Invoice to CustomCRM Order
-------------------------------
Every Wave Invoice will be synchronized with a CustomCRM Order.

Once a link between a Wave Invoice and a CustomCRM Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a CustomCRM Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - CustomCRM Order Property
     - CustomCRM Data Type


Wave Product to CustomCRM Product
---------------------------------
Every Wave Product will be synchronized with a CustomCRM Product.

Once a link between a Wave Product and a CustomCRM Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a CustomCRM Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - CustomCRM Product Property
     - CustomCRM Data Type


Wave Vendor to CustomCRM Contact
--------------------------------
Every Wave Vendor will be synchronized with a CustomCRM Contact.

Once a link between a Wave Vendor and a CustomCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a CustomCRM Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - CustomCRM Contact Property
     - CustomCRM Data Type

