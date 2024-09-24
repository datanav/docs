=========================
Invoiced to Wave Dataflow
=========================

Generated: 2024-09-24 13:32:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers (organisation data) to Wave Customer
-------------------------------------------------------
Every Invoiced Customers (organisation data) will be synchronized with a Wave Customer.

Once a link between a Invoiced Customers (organisation data) and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (organisation data) and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (organisation data) Property
     - Wave Customer Property
     - Wave Data Type
   * - name
     - name
     - N/A


Invoiced Customers (human data) to Wave Customer (human data)
-------------------------------------------------------------
Every Invoiced Customers (human data) will be synchronized with a Wave Customer (human data).

Once a link between a Invoiced Customers (human data) and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (human data) and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (human data) Property
     - Wave Customer (human data) Property
     - Wave Data Type


Invoiced Customers (organisation data) to Wave Customer
-------------------------------------------------------
Every Invoiced Customers (organisation data) will be synchronized with a Wave Customer.

Once a link between a Invoiced Customers (organisation data) and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (organisation data) and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (organisation data) Property
     - Wave Customer Property
     - Wave Data Type


Invoiced Customers (human data) to Wave Customer (human data)
-------------------------------------------------------------
Every Invoiced Customers (human data) will be synchronized with a Wave Customer (human data).

Once a link between a Invoiced Customers (human data) and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers (human data) and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Invoiced Customers (human data) Property
     - Wave Customer (human data) Property
     - Wave Data Type
   * - address1
     - address.addressLine1
     - "string"
   * - address1
     - shippingDetails.address.addressLine1
     - "string"
   * - address2
     - address.addressLine2
     - "string"
   * - address2
     - shippingDetails.address.addressLine2
     - "string"
   * - city
     - address.city
     - "string"
   * - city
     - shippingDetails.address.city
     - "string"
   * - country
     - address.country.code
     - "string"
   * - country
     - shippingDetails.address.country.code
     - "string"
   * - name
     - name
     - N/A
   * - postal_code
     - address.postalCode
     - "string"
   * - postal_code
     - shippingDetails.address.postalCode
     - "string"


Invoiced Invoices to Wave Invoice
---------------------------------
Every Invoiced Invoices will be synchronized with a Wave Invoice.

Once a link between a Invoiced Invoices and a Wave Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Wave Invoice:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Wave Invoice Property
     - Wave Data Type
   * - currency
     - currency.code
     - "string"
   * - customer
     - customer.id
     - "string"


Invoiced Items to Wave Product
------------------------------
Every Invoiced Items will be synchronized with a Wave Product.

Once a link between a Invoiced Items and a Wave Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Wave Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Wave Product Property
     - Wave Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"

