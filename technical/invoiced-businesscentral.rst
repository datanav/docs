====================================
Invoiced to BusinessCentral Dataflow
====================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to BusinessCentral. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Invoiced Contacts to BusinessCentral Contacts person
----------------------------------------------------
Every Invoiced Contacts will be synchronized with a BusinessCentral Contacts person.

Once a link between a Invoiced Contacts and a BusinessCentral Contacts person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a BusinessCentral Contacts person:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - BusinessCentral Contacts person Property
     - BusinessCentral Data Type
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


Invoiced Customers company to BusinessCentral Customers company
---------------------------------------------------------------
Every Invoiced Customers company will be synchronized with a BusinessCentral Customers company.

Once a link between a Invoiced Customers company and a BusinessCentral Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a BusinessCentral Customers company:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - BusinessCentral Customers company Property
     - BusinessCentral Data Type
   * - name
     - displayName
     - "string"


Invoiced Customers person to BusinessCentral Customers person
-------------------------------------------------------------
Every Invoiced Customers person will be synchronized with a BusinessCentral Customers person.

Once a link between a Invoiced Customers person and a BusinessCentral Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a BusinessCentral Customers person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - BusinessCentral Customers person Property
     - BusinessCentral Data Type
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


Invoiced Invoices to BusinessCentral Salesorders
------------------------------------------------
Every Invoiced Invoices will be synchronized with a BusinessCentral Salesorders.

Once a link between a Invoiced Invoices and a BusinessCentral Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a BusinessCentral Salesorders:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - BusinessCentral Salesorders Property
     - BusinessCentral Data Type
   * - currency
     - currencyId
     - "string"
   * - customer
     - customerId
     - "string"


Invoiced Items to BusinessCentral Items
---------------------------------------
Every Invoiced Items will be synchronized with a BusinessCentral Items.

Once a link between a Invoiced Items and a BusinessCentral Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a BusinessCentral Items:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - BusinessCentral Items Property
     - BusinessCentral Data Type
   * - name
     - displayName
     - "string"
   * - unit_cost
     - unitCost
     - N/A


Invoiced Lineitem to BusinessCentral Salesorderlines
----------------------------------------------------
Every Invoiced Lineitem will be synchronized with a BusinessCentral Salesorderlines.

Once a link between a Invoiced Lineitem and a BusinessCentral Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a BusinessCentral Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - BusinessCentral Salesorderlines Property
     - BusinessCentral Data Type
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

