=========================
Invoiced to Wave Dataflow
=========================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Wave Customer
-------------------------------------------
Every Invoiced Customers company will be synchronized with a Wave Customer.

Once a link between a Invoiced Customers company and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Wave Customer Property
     - Wave Data Type
   * - name
     - name
     - N/A


Invoiced Customers person to Wave Customer person
-------------------------------------------------
Every Invoiced Customers person will be synchronized with a Wave Customer person.

Once a link between a Invoiced Customers person and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Wave Customer person Property
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

