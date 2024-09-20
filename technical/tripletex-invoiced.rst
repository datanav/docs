==============================
Tripletex to Invoiced Dataflow
==============================

Generated: 2024-09-20 13:11:59

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Invoiced Customers (organisation data)
------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Invoiced Customers (organisation data).

Once a link between a Tripletex Customer and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type
   * - deliveryAddress.addressLine1
     - address1
     - "string"
   * - deliveryAddress.addressLine2
     - address2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postal_code
     - "string"
   * - id
     - id
     - "string"
   * - name
     - name
     - "string"
   * - physicalAddress.addressLine1
     - address1
     - "string"
   * - physicalAddress.addressLine2
     - address2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postal_code
     - "string"
   * - postalAddress.addressLine1
     - address1
     - "string"
   * - postalAddress.addressLine2
     - address2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postal_code
     - "string"


Tripletex Customer to Invoiced Customers (human data)
-----------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Invoiced Customers (human data).

Once a link between a Tripletex Customer and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Invoiced Customers (human data) Property
     - Invoiced Data Type


Tripletex Customer (organisation data) to Invoiced Customers (organisation data)
--------------------------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Invoiced Customers (organisation data).

Once a link between a Tripletex Customer (organisation data) and a Invoiced Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (organisation data) and a Invoiced Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (organisation data) Property
     - Invoiced Customers (organisation data) Property
     - Invoiced Data Type


Tripletex Customer (human data) to Invoiced Customers (human data)
------------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Invoiced Customers (human data).

Once a link between a Tripletex Customer (human data) and a Invoiced Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (human data) and a Invoiced Customers (human data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (human data) Property
     - Invoiced Customers (human data) Property
     - Invoiced Data Type
   * - deliveryAddress.addressLine1
     - address1
     - "string"
   * - deliveryAddress.addressLine2
     - address2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postal_code
     - "string"
   * - id
     - id
     - "string"
   * - name
     - name
     - "string"
   * - physicalAddress.addressLine1
     - address1
     - "string"
   * - physicalAddress.addressLine2
     - address2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postal_code
     - "string"
   * - postalAddress.addressLine1
     - address1
     - "string"
   * - postalAddress.addressLine2
     - address2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postal_code
     - "string"


Tripletex Order to Invoiced Invoices
------------------------------------
Every Tripletex Order will be synchronized with a Invoiced Invoices.

Once a link between a Tripletex Order and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Invoiced Invoices Property
     - Invoiced Data Type


Tripletex Orderline to Invoiced Lineitem
----------------------------------------
Every Tripletex Orderline will be synchronized with a Invoiced Lineitem.

Once a link between a Tripletex Orderline and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Invoiced Lineitem Property
     - Invoiced Data Type


Tripletex Product to Invoiced Items
-----------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Invoiced Items.

Once a link between a Tripletex Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - costExcludingVatCurrency
     - unit_cost
     - "string"
   * - currency.id
     - currency
     - "string"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"

