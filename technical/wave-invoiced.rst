=========================
Wave to Invoiced Dataflow
=========================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Invoiced. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Invoiced Customers company
-------------------------------------------
Every Wave Customer will be synchronized with a Invoiced Customers company.

Once a link between a Wave Customer and a Invoiced Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Invoiced Customers company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Invoiced Customers company Property
     - Invoiced Data Type
   * - name
     - name
     - "string"


Wave Customer person to Invoiced Customers person
-------------------------------------------------
Every Wave Customer person will be synchronized with a Invoiced Customers person.

Once a link between a Wave Customer person and a Invoiced Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Invoiced Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Invoiced Customers person Property
     - Invoiced Data Type
   * - address.addressLine1
     - address1
     - "string"
   * - address.addressLine2
     - address2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.code
     - country
     - "string"
   * - address.postalCode
     - postal_code
     - "string"
   * - id
     - id
     - "string"
   * - name
     - name
     - "string"
   * - shippingDetails.address.addressLine1
     - address1
     - "string"
   * - shippingDetails.address.addressLine2
     - address2
     - "string"
   * - shippingDetails.address.city
     - city
     - "string"
   * - shippingDetails.address.country.code
     - country
     - "string"
   * - shippingDetails.address.postalCode
     - postal_code
     - "string"


Wave Invoice to Invoiced Invoices
---------------------------------
Every Wave Invoice will be synchronized with a Invoiced Invoices.

Once a link between a Wave Invoice and a Invoiced Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Invoiced Invoices:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Invoiced Invoices Property
     - Invoiced Data Type
   * - currency.code
     - currency
     - "string"
   * - customer.id
     - customer
     - "string"


Wave Invoice to Invoiced Lineitem
---------------------------------
Every Wave Invoice will be synchronized with a Invoiced Lineitem.

Once a link between a Wave Invoice and a Invoiced Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Invoiced Lineitem:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Invoiced Lineitem Property
     - Invoiced Data Type
   * - items.description
     - items.description
     - "string"
   * - items.price
     - items.amount
     - "string"
   * - items.quantity
     - items.quantity
     - "string"


Wave Product to Invoiced Items
------------------------------
Every Wave Product will be synchronized with a Invoiced Items.

Once a link between a Wave Product and a Invoiced Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Invoiced Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Invoiced Items Property
     - Invoiced Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"

