===============================
SuperOffice to Shopify Dataflow
===============================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Shopify. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Shopify Customer
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Shopify Customer must be established.

A new Shopify Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Shopify.

Once a link between a SuperOffice Contact and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Shopify Customer Property
     - Shopify Data Type


SuperOffice Person to Shopify Customer
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Shopify Customer must be established.

A new Shopify Customer will be created from a SuperOffice Person if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Shopify.

Once a link between a SuperOffice Person and a Shopify Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Shopify Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Shopify Customer Property
     - Shopify Data Type
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - first_name
     - "string"
   * - Lastname
     - last_name
     - "string"
   * - MobilePhones.Value
     - phone
     - "string"
   * - OfficePhones.Value
     - default_address.phone
     - "string"
   * - OfficePhones.Value
     - phone
     - "string"


SuperOffice Product to Shopify Product
--------------------------------------
Before any synchronization can take place, a link between a SuperOffice Product and a Shopify Product must be established.

A new Shopify Product will be created from a SuperOffice Product if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Shopify.

Once a link between a SuperOffice Product and a Shopify Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Shopify Product:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Shopify Product Property
     - Shopify Data Type


SuperOffice Quotealternative to Shopify Order
---------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Shopify Order must be established.

A new Shopify Order will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Shopify.

Once a link between a SuperOffice Quotealternative and a Shopify Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Shopify Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Shopify Order Property
     - Shopify Data Type
   * - TotalPrice
     - current_total_price
     - "string"
   * - TotalPrice
     - total_price
     - "string"


SuperOffice Product to Shopify Sesamproduct
-------------------------------------------
Every SuperOffice Product will be synchronized with a Shopify Sesamproduct.

Once a link between a SuperOffice Product and a Shopify Sesamproduct is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Shopify Sesamproduct:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Shopify Sesamproduct Property
     - Shopify Data Type
   * - Description
     - variants.title
     - "string"
   * - Name
     - title
     - "string"
   * - UnitListPrice
     - sesam_priceExclVAT
     - "string"
   * - UnitListPrice
     - variants.price
     - "string"

