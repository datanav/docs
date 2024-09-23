=====================================
Invoiced to Business Central Dataflow
=====================================

Generated: 2024-09-23 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers (organisation data) to Business Central Companies
--------------------------------------------------------------------
Every Invoiced Customers (organisation data) will be synchronized with a Business Central Companies.

Once a link between a Invoiced Customers (organisation data) and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (organisation data) and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (organisation data) Property
     - Business Central Companies Property
     - Business Central Data Type


Invoiced Contacts to Business Central Contacts (human data)
-----------------------------------------------------------
Every Invoiced Contacts will be synchronized with a Business Central Contacts (human data).

Once a link between a Invoiced Contacts and a Business Central Contacts (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Business Central Contacts (human data):

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Business Central Contacts (human data) Property
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


Invoiced Customers (organisation data) to Business Central Customers (organisation data)
----------------------------------------------------------------------------------------
Every Invoiced Customers (organisation data) will be synchronized with a Business Central Customers (organisation data).

Once a link between a Invoiced Customers (organisation data) and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (organisation data) and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (organisation data) Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type


Invoiced Customers (human data) to Business Central Customers (human data)
--------------------------------------------------------------------------
Every Invoiced Customers (human data) will be synchronized with a Business Central Customers (human data).

Once a link between a Invoiced Customers (human data) and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (human data) and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (human data) Property
     - Business Central Customers (human data) Property
     - Business Central Data Type


Invoiced Customers (organisation data) to Business Central Customers (organisation data)
----------------------------------------------------------------------------------------
Every Invoiced Customers (organisation data) will be synchronized with a Business Central Customers (organisation data).

Once a link between a Invoiced Customers (organisation data) and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (organisation data) and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (organisation data) Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type


Invoiced Customers (human data) to Business Central Customers (human data)
--------------------------------------------------------------------------
Every Invoiced Customers (human data) will be synchronized with a Business Central Customers (human data).

Once a link between a Invoiced Customers (human data) and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (human data) and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (human data) Property
     - Business Central Customers (human data) Property
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

