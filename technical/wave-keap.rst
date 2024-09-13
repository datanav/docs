=====================
Wave to Keap Dataflow
=====================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Keap Companies
-------------------------------
Every Wave Customer will be synchronized with a Keap Companies.

Once a link between a Wave Customer and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Keap Companies Property
     - Keap Data Type
   * - address.city
     - address.locality
     - "string"
   * - address.postalCode
     - address.zip_code
     - "string"
   * - id
     - id
     - "string"
   * - name
     - company_name
     - "string"
   * - shippingDetails.address.city
     - address.locality
     - "string"
   * - shippingDetails.address.postalCode
     - address.zip_code
     - "string"


Wave Vendor to Keap Companies
-----------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Keap Companies must be established.

A new Keap Companies will be created from a Wave Vendor if it is connected to a Wave Customer-person that is synchronized into Keap.

Once a link between a Wave Vendor and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Keap Companies Property
     - Keap Data Type
   * - address.city
     - address.locality
     - "string"
   * - address.postalCode
     - address.zip_code
     - "string"
   * - id
     - id
     - "string"
   * - name
     - company_name
     - "string"


Wave Customer person to Keap Contacts
-------------------------------------
Every Wave Customer person will be synchronized with a Keap Contacts.

Once a link between a Wave Customer person and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Keap Contacts Property
     - Keap Data Type


Wave Product to Keap Product
----------------------------
Every Wave Product will be synchronized with a Keap Product.

Once a link between a Wave Product and a Keap Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Keap Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Keap Product Property
     - Keap Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - unitPrice
     - product_price
     - "string"

