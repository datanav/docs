====================================
Invoiced to Businesscentral Dataflow
====================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Businesscentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Businesscentral Companies
-------------------------------------------------------
Every Invoiced Customers company will be synchronized with a Businesscentral Companies.

Once a link between a Invoiced Customers company and a Businesscentral Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Businesscentral Companies:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Businesscentral Companies Property
     - Businesscentral Data Type


Invoiced Contacts to Businesscentral Contacts person
----------------------------------------------------
Every Invoiced Contacts will be synchronized with a Businesscentral Contacts person.

Once a link between a Invoiced Contacts and a Businesscentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Businesscentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Businesscentral Contacts person Property
     - Businesscentral Data Type
   * - address1
     - addressLine1
     - "string"
   * - address2
     - addressLine2
     - "string"
   * - city
     - city
     - "string"


Invoiced Customers company to Businesscentral Customers company
---------------------------------------------------------------
Every Invoiced Customers company will be synchronized with a Businesscentral Customers company.

Once a link between a Invoiced Customers company and a Businesscentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Businesscentral Customers company:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Businesscentral Customers company Property
     - Businesscentral Data Type
   * - name
     - displayName
     - "string"


Invoiced Customers person to Businesscentral Customers person
-------------------------------------------------------------
Every Invoiced Customers person will be synchronized with a Businesscentral Customers person.

Once a link between a Invoiced Customers person and a Businesscentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Businesscentral Customers person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Businesscentral Customers person Property
     - Businesscentral Data Type
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


Invoiced Invoices to Businesscentral Salesorders
------------------------------------------------
Every Invoiced Invoices will be synchronized with a Businesscentral Salesorders.

Once a link between a Invoiced Invoices and a Businesscentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Businesscentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Businesscentral Salesorders Property
     - Businesscentral Data Type
   * - currency
     - currencyId
     - "string"
   * - customer
     - customerId
     - "string"


Invoiced Items to Businesscentral Items
---------------------------------------
Every Invoiced Items will be synchronized with a Businesscentral Items.

Once a link between a Invoiced Items and a Businesscentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Businesscentral Items:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Businesscentral Items Property
     - Businesscentral Data Type
   * - name
     - displayName
     - "string"
   * - unit_cost
     - unitCost
     - N/A


Invoiced Lineitem to Businesscentral Salesorderlines
----------------------------------------------------
Every Invoiced Lineitem will be synchronized with a Businesscentral Salesorderlines.

Once a link between a Invoiced Lineitem and a Businesscentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Businesscentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Businesscentral Salesorderlines Property
     - Businesscentral Data Type
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

