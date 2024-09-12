=================================
SuperOffice to Chargebee Dataflow
=================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Chargebee Customer
-----------------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Chargebee Customer must be established.

A new Chargebee Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, Quoteline, or Quotealternative that is synchronized into Chargebee.

Once a link between a SuperOffice Contact and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Chargebee Customer Property
     - Chargebee Data Type


SuperOffice Person to Chargebee Customer
----------------------------------------
Every SuperOffice Person will be synchronized with a Chargebee Customer.

Once a link between a SuperOffice Person and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - first_name
     - "string"
   * - Lastname
     - last_name
     - "string"


SuperOffice Contact to Chargebee Business_entity
------------------------------------------------
Every SuperOffice Contact will be synchronized with a Chargebee Business_entity.

Once a link between a SuperOffice Contact and a Chargebee Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Chargebee Business_entity:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Chargebee Business_entity Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"


SuperOffice Quotealternative to Chargebee Order
-----------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Chargebee Order.

Once a link between a SuperOffice Quotealternative and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Chargebee Order Property
     - Chargebee Data Type


SuperOffice Quoteline to Chargebee Order
----------------------------------------
Every SuperOffice Quoteline will be synchronized with a Chargebee Order.

Once a link between a SuperOffice Quoteline and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - Description
     - order_line_items.description
     - "string"
   * - Quantity
     - order_line_items.amount
     - "string"
   * - UnitListPrice
     - order_line_items.unit_price
     - "string"
   * - VAT
     - order_line_items.tax_amount
     - "string"


SuperOffice Sale to Chargebee Order
-----------------------------------
Every SuperOffice Sale will be synchronized with a Chargebee Order.

Once a link between a SuperOffice Sale and a Chargebee Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Chargebee Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Chargebee Order Property
     - Chargebee Data Type
   * - Contact.ContactId
     - customer_id
     - "string"
   * - Currency.Id
     - currency_code
     - "string"
   * - Person.PersonId
     - customer_id
     - "string"


SuperOffice Product to Chargebee Item
-------------------------------------
Every SuperOffice Product will be synchronized with a Chargebee Item.

Once a link between a SuperOffice Product and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Chargebee Item Property
     - Chargebee Data Type
   * - Name
     - name
     - "string"

