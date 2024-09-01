===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-09-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to  Customers company
-----------------------------------
Every Wave Customer will be synchronized with a  Customers company.

Once a link between a Wave Customer and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Customers company Property
     -  Data Type
   * - name
     - name
     - "string"


Wave Customer person to  Customers person
-----------------------------------------
Every Wave Customer person will be synchronized with a  Customers person.

Once a link between a Wave Customer person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Customers person Property
     -  Data Type
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


Wave Invoice to  Invoices
-------------------------
Every Wave Invoice will be synchronized with a  Invoices.

Once a link between a Wave Invoice and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Invoices:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Invoices Property
     -  Data Type
   * - currency.code
     - currency
     - "string"
   * - customer.id
     - customer
     - "string"


Wave Invoice to  Lineitem
-------------------------
Every Wave Invoice will be synchronized with a  Lineitem.

Once a link between a Wave Invoice and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Lineitem Property
     -  Data Type
   * - items.description
     - items.description
     - "string"
   * - items.price
     - items.amount
     - "string"
   * - items.quantity
     - items.quantity
     - "string"


Wave Product to  Items
----------------------
Every Wave Product will be synchronized with a  Items.

Once a link between a Wave Product and a  Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Items Property
     -  Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"

