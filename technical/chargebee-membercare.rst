================================
Chargebee to MemberCare Dataflow
================================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Currency to MemberCare Companycategories
--------------------------------------------------
Every Chargebee Currency will be synchronized with a MemberCare Companycategories.

Once a link between a Chargebee Currency and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Currency and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Chargebee Currency Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


Chargebee Customer to MemberCare Persons
----------------------------------------
Every Chargebee Customer will be synchronized with a MemberCare Persons.

Once a link between a Chargebee Customer and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - first_name
     - firstname
     - "string"
   * - last_name
     - lastname
     - "string"


Chargebee Item to MemberCare Products
-------------------------------------
Every Chargebee Item will be synchronized with a MemberCare Products.

Once a link between a Chargebee Item and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - MemberCare Products Property
     - MemberCare Data Type


Chargebee Item_family to MemberCare Companycategories
-----------------------------------------------------
Every Chargebee Item_family will be synchronized with a MemberCare Companycategories.

Once a link between a Chargebee Item_family and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item_family and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Chargebee Item_family Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


Chargebee Order to MemberCare Invoices
--------------------------------------
Every Chargebee Order will be synchronized with a MemberCare Invoices.

Once a link between a Chargebee Order and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - order_line_items.amount
     - invoiceItems.quantity
     - "string"
   * - order_line_items.description
     - invoiceItems.description
     - "string"
   * - order_line_items.unit_price
     - invoiceItems.unitPrice
     - "string"


Chargebee Address to MemberCare Countries
-----------------------------------------
Every Chargebee Address will be synchronized with a MemberCare Countries.

Once a link between a Chargebee Address and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - country
     - name
     - "string"


Chargebee Business_entity to MemberCare Companies
-------------------------------------------------
Every Chargebee Business_entity will be synchronized with a MemberCare Companies.

Once a link between a Chargebee Business_entity and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - name
     - companyName
     - "string"


Chargebee Customer to MemberCare Countries
------------------------------------------
Every Chargebee Customer will be synchronized with a MemberCare Countries.

Once a link between a Chargebee Customer and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - billing_address.country
     - name
     - "string"

