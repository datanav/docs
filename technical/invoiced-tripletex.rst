==============================
Invoiced to Tripletex Dataflow
==============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Contacts to Tripletex Contact
--------------------------------------
Every Invoiced Contacts will be synchronized with a Tripletex Contact.

Once a link between a Invoiced Contacts and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - email
     - email
     - "string"
   * - phone
     - phoneNumberMobile
     - N/A


Invoiced Customers company to Tripletex Customer
------------------------------------------------
Every Invoiced Customers company will be synchronized with a Tripletex Customer.

Once a link between a Invoiced Customers company and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - address1
     - deliveryAddress.addressLine1
     - "string"
   * - address1
     - physicalAddress.addressLine1
     - "string"
   * - address1
     - postalAddress.addressLine1
     - "string"
   * - address2
     - deliveryAddress.addressLine2
     - "string"
   * - address2
     - physicalAddress.addressLine2
     - "string"
   * - address2
     - postalAddress.addressLine2
     - "string"
   * - city
     - deliveryAddress.city
     - "string"
   * - city
     - physicalAddress.city
     - "string"
   * - city
     - postalAddress.city
     - "string"
   * - country
     - deliveryAddress.country.id
     - "string"
   * - country
     - physicalAddress.country.id
     - "integer"
   * - country
     - postalAddress.country.id
     - "integer"
   * - id
     - id
     - "integer"
   * - name
     - name
     - "string"
   * - postal_code
     - deliveryAddress.postalCode
     - "string"
   * - postal_code
     - physicalAddress.postalCode
     - "string"
   * - postal_code
     - postalAddress.postalCode
     - "string"


Invoiced Customers person to Tripletex Customer person
------------------------------------------------------
Every Invoiced Customers person will be synchronized with a Tripletex Customer person.

Once a link between a Invoiced Customers person and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - address1
     - deliveryAddress.addressLine1
     - "string"
   * - address1
     - physicalAddress.addressLine1
     - "string"
   * - address1
     - postalAddress.addressLine1
     - "string"
   * - address2
     - deliveryAddress.addressLine2
     - "string"
   * - address2
     - physicalAddress.addressLine2
     - "string"
   * - address2
     - postalAddress.addressLine2
     - "string"
   * - city
     - deliveryAddress.city
     - "string"
   * - city
     - physicalAddress.city
     - "string"
   * - city
     - postalAddress.city
     - "string"
   * - country
     - deliveryAddress.country.id
     - "string"
   * - country
     - physicalAddress.country.id
     - "integer"
   * - country
     - postalAddress.country.id
     - "integer"
   * - id
     - id
     - "integer"
   * - name
     - name
     - "string"
   * - postal_code
     - deliveryAddress.postalCode
     - "string"
   * - postal_code
     - physicalAddress.postalCode
     - "string"
   * - postal_code
     - postalAddress.postalCode
     - "string"


Invoiced Invoices to Tripletex Order
------------------------------------
Every Invoiced Invoices will be synchronized with a Tripletex Order.

Once a link between a Invoiced Invoices and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Tripletex Order Property
     - Tripletex Data Type
   * - currency
     - currency.id
     - "integer"
   * - customer
     - contact.id
     - "integer"
   * - customer
     - customer.id
     - "integer"


Invoiced Items to Tripletex Product
-----------------------------------
Every Invoiced Items will be synchronized with a Tripletex Product.

Once a link between a Invoiced Items and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - currency
     - currency.id
     - "integer"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unit_cost
     - costExcludingVatCurrency
     - "float"


Invoiced Lineitem to Tripletex Orderline
----------------------------------------
Every Invoiced Lineitem will be synchronized with a Tripletex Orderline.

Once a link between a Invoiced Lineitem and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Tripletex Orderline Property
     - Tripletex Data Type
   * - $original_id
     - order.id
     - "integer"
   * - items.amount
     - unitPriceExcludingVatCurrency
     - "float"
   * - items.description
     - description
     - "string"
   * - items.discounts
     - discount
     - "float"
   * - items.quantity
     - count
     - N/A

