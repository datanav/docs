===========================
Wave to Custom CRM Dataflow
===========================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Custom CRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Custom CRM Contact
------------------------------------------
Every Wave Customer person will be synchronized with a Custom CRM Contact.

Once a link between a Wave Customer person and a Custom CRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Custom CRM Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Custom CRM Contact Property
     - Custom CRM Data Type


Wave Customer to Custom CRM Contact
-----------------------------------
Every Wave Customer will be synchronized with a Custom CRM Contact.

Once a link between a Wave Customer and a Custom CRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Custom CRM Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Custom CRM Contact Property
     - Custom CRM Data Type


Wave Customer to Custom CRM Customer
------------------------------------
Every Wave Customer will be synchronized with a Custom CRM Customer.

Once a link between a Wave Customer and a Custom CRM Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Custom CRM Customer:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Custom CRM Customer Property
     - Custom CRM Data Type
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


Wave Invoice to Custom CRM Order
--------------------------------
Every Wave Invoice will be synchronized with a Custom CRM Order.

Once a link between a Wave Invoice and a Custom CRM Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Custom CRM Order:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Custom CRM Order Property
     - Custom CRM Data Type


Wave Product to Custom CRM Product
----------------------------------
Every Wave Product will be synchronized with a Custom CRM Product.

Once a link between a Wave Product and a Custom CRM Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Custom CRM Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Custom CRM Product Property
     - Custom CRM Data Type


Wave Vendor to Custom CRM Contact
---------------------------------
Every Wave Vendor will be synchronized with a Custom CRM Contact.

Once a link between a Wave Vendor and a Custom CRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Custom CRM Contact:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Custom CRM Contact Property
     - Custom CRM Data Type

