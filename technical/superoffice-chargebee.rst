========================
SuperOffice to  Dataflow
========================

Generated: 2024-09-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Customer
--------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a  Customer must be established.

A new  Customer will be created from a SuperOffice Contact if it is connected to a SuperOffice Sale, Quoteline, or Quotealternative that is synchronized into .

Once a link between a SuperOffice Contact and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Customer Property
     -  Data Type


SuperOffice Person to  Customer
-------------------------------
Every SuperOffice Person will be synchronized with a  Customer.

Once a link between a SuperOffice Person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Customer:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Customer Property
     -  Data Type
   * - Emails.Value
     - email
     - "string"
   * - Firstname
     - first_name
     - "string"
   * - Lastname
     - last_name
     - "string"


SuperOffice Contact to  Business_entity
---------------------------------------
Every SuperOffice Contact will be synchronized with a  Business_entity.

Once a link between a SuperOffice Contact and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Business_entity Property
     -  Data Type
   * - Name
     - name
     - "string"


SuperOffice Quotealternative to  Order
--------------------------------------
Every SuperOffice Quotealternative will be synchronized with a  Order.

Once a link between a SuperOffice Quotealternative and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a  Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     -  Order Property
     -  Data Type


SuperOffice Quoteline to  Order
-------------------------------
Every SuperOffice Quoteline will be synchronized with a  Order.

Once a link between a SuperOffice Quoteline and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a  Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     -  Order Property
     -  Data Type
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


SuperOffice Sale to  Order
--------------------------
Every SuperOffice Sale will be synchronized with a  Order.

Once a link between a SuperOffice Sale and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a  Order:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     -  Order Property
     -  Data Type
   * - Contact.ContactId
     - customer_id
     - "string"
   * - Currency.Id
     - currency_code
     - "string"
   * - Person.PersonId
     - customer_id
     - "string"


SuperOffice Product to  Item
----------------------------
Every SuperOffice Product will be synchronized with a  Item.

Once a link between a SuperOffice Product and a  Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a  Item:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     -  Item Property
     -  Data Type
   * - Name
     - name
     - "string"

