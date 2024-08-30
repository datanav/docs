======================
Tripletex to  Dataflow
======================

Generated: 2024-08-30 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Customers company
----------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customers company.

Once a link between a Tripletex Customer and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Customers company Property
     -  Data Type
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


Tripletex Customer person to  Customers person
----------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Customers person.

Once a link between a Tripletex Customer person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Customers person Property
     -  Data Type
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


Tripletex Order to  Invoices
----------------------------
Every Tripletex Order will be synchronized with a  Invoices.

Once a link between a Tripletex Order and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Invoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Invoices Property
     -  Data Type
   * - contact.id
     - customer
     - "string"
   * - currency.id
     - currency
     - "string"
   * - customer.id
     - customer
     - "string"


Tripletex Orderline to  Lineitem
--------------------------------
Every Tripletex Orderline will be synchronized with a  Lineitem.

Once a link between a Tripletex Orderline and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     -  Lineitem Property
     -  Data Type
   * - count
     - items.quantity
     - "string"
   * - description
     - items.description
     - "string"
   * - discount
     - items.discounts
     - "string"
   * - unitPriceExcludingVatCurrency
     - items.amount
     - "string"


Tripletex Product to  Items
---------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a  Items.

Once a link between a Tripletex Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Items Property
     -  Data Type
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

