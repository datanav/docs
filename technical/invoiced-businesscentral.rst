=====================================
Invoiced to Business Central Dataflow
=====================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Business Central Companies
--------------------------------------------------------
Every Invoiced Customers company will be synchronized with a Business Central Companies.

Once a link between a Invoiced Customers company and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Business Central Companies Property
     - Business Central Data Type


Invoiced Contacts to Business Central Contacts person
-----------------------------------------------------
Every Invoiced Contacts will be synchronized with a Business Central Contacts person.

Once a link between a Invoiced Contacts and a Business Central Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Business Central Contacts person:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Business Central Contacts person Property
     - Business Central Data Type
   * - address1
     - addressLine1
     - "string"
   * - address2
     - addressLine2
     - "string"
   * - city
     - city
     - "string"
   * - email
     - email
     - "string"
   * - name
     - displayName
     - "string"
   * - phone
     - mobilePhoneNumber
     - "string"
   * - postal_code
     - postalCode
     - "string"


Invoiced Customers company to Business Central Customers company
----------------------------------------------------------------
Every Invoiced Customers company will be synchronized with a Business Central Customers company.

Once a link between a Invoiced Customers company and a Business Central Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Business Central Customers company:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Business Central Customers company Property
     - Business Central Data Type
   * - name
     - displayName
     - "string"


Invoiced Customers person to Business Central Customers person
--------------------------------------------------------------
Every Invoiced Customers person will be synchronized with a Business Central Customers person.

Once a link between a Invoiced Customers person and a Business Central Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Business Central Customers person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Business Central Customers person Property
     - Business Central Data Type
   * - address1
     - addressLine1
     - "string"
   * - address2
     - addressLine2
     - "string"
   * - city
     - city
     - "string"
   * - country
     - country
     - "string"
   * - id
     - id
     - "string"
   * - name
     - displayName
     - "string"
   * - postal_code
     - postalCode
     - "string"


Invoiced Invoices to Business Central Salesorders
-------------------------------------------------
Every Invoiced Invoices will be synchronized with a Business Central Salesorders.

Once a link between a Invoiced Invoices and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Business Central Salesorders Property
     - Business Central Data Type
   * - currency
     - currencyId
     - "string"
   * - customer
     - customerId
     - "string"


Invoiced Items to Business Central Items
----------------------------------------
Every Invoiced Items will be synchronized with a Business Central Items.

Once a link between a Invoiced Items and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Business Central Items Property
     - Business Central Data Type
   * - name
     - displayName
     - "string"
   * - unit_cost
     - unitCost
     - N/A


Invoiced Lineitem to Business Central Salesorderlines
-----------------------------------------------------
Every Invoiced Lineitem will be synchronized with a Business Central Salesorderlines.

Once a link between a Invoiced Lineitem and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Business Central Salesorderlines Property
     - Business Central Data Type
   * - $original_id
     - documentId
     - "string"
   * - items.amount
     - unitPrice
     - "float"
   * - items.discounts
     - discountPercent
     - N/A
   * - items.name
     - description
     - "string"
   * - items.quantity
     - quantity
     - N/A

