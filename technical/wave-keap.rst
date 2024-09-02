===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-09-02 13:38:44

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to  Companies
---------------------------
Every Wave Customer will be synchronized with a  Companies.

Once a link between a Wave Customer and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Companies Property
     -  Data Type
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


Wave Customer person to  Contacts
---------------------------------
Every Wave Customer person will be synchronized with a  Contacts.

Once a link between a Wave Customer person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Contacts Property
     -  Data Type


Wave Product to  Product
------------------------
Every Wave Product will be synchronized with a  Product.

Once a link between a Wave Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Product Property
     -  Data Type
   * - description
     - product_desc
     - "string"
   * - name
     - product_name
     - "string"
   * - unitPrice
     - product_price
     - "string"

