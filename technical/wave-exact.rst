================================
Wave Financial to Exact Dataflow
================================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Exact Contacts
--------------------------------------
Every Wave Customer person will be synchronized with a Exact Contacts.

Once a link between a Wave Customer person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Exact Contacts Property
     - Exact Data Type
   * - address.city
     - City
     - "string"
   * - address.country.code
     - Country
     - "string"
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - mobile
     - Mobile
     - "string"
   * - name
     - FullName
     - "string"
   * - phone
     - Phone
     - "string"
   * - shippingDetails.address.city
     - City
     - "string"
   * - shippingDetails.address.country.code
     - Country
     - "string"
   * - shippingDetails.phone
     - Phone
     - "string"


Wave Invoice to Exact Quotations
--------------------------------
Every Wave Invoice will be synchronized with a Exact Quotations.

Once a link between a Wave Invoice and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Exact Quotations Property
     - Exact Data Type
   * - currency.code
     - Currency
     - "string"
   * - dueDate
     - DueDate
     - "string"
   * - memo
     - Description
     - "string"


Wave Currency to Exact Currencies
---------------------------------
Every Wave Currency will be synchronized with a Exact Currencies.

Once a link between a Wave Currency and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Exact Currencies Property
     - Exact Data Type
   * - name
     - Description
     - "string"


Wave Customer to Exact Accounts
-------------------------------
Every Wave Customer will be synchronized with a Exact Accounts.

Once a link between a Wave Customer and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Exact Accounts Property
     - Exact Data Type
   * - address.addressLine1
     - AddressLine1
     - "string"
   * - address.addressLine2
     - AddressLine2
     - "string"
   * - address.city
     - City
     - "string"
   * - address.country.code
     - Country
     - "string"
   * - address.postalCode
     - Postcode
     - "string"
   * - name
     - Name
     - "string"
   * - phone
     - Phone
     - "string"
   * - shippingDetails.address.addressLine1
     - AddressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - AddressLine2
     - "string"
   * - shippingDetails.address.city
     - City
     - "string"
   * - shippingDetails.address.country.code
     - Country
     - "string"
   * - shippingDetails.address.postalCode
     - Postcode
     - "string"
   * - shippingDetails.phone
     - Phone
     - "string"
   * - website
     - Website
     - "string"


Wave Customer to Exact Contacts
-------------------------------
Every Wave Customer will be synchronized with a Exact Contacts.

Once a link between a Wave Customer and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Exact Contacts Property
     - Exact Data Type
   * - address.city
     - City
     - "string"
   * - address.country.code
     - Country
     - "string"
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - mobile
     - Mobile
     - "string"
   * - shippingDetails.address.city
     - City
     - "string"
   * - shippingDetails.address.country.code
     - Country
     - "string"


Wave Customer person to Exact Addresses
---------------------------------------
Every Wave Customer person will be synchronized with a Exact Addresses.

Once a link between a Wave Customer person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Exact Addresses Property
     - Exact Data Type
   * - address.addressLine1
     - AddressLine1
     - "string"
   * - address.addressLine2
     - AddressLine2
     - "string"
   * - address.city
     - City
     - "string"
   * - address.country.code
     - Country
     - "string"
   * - shippingDetails.address.addressLine1
     - AddressLine1
     - "string"
   * - shippingDetails.address.addressLine2
     - AddressLine2
     - "string"
   * - shippingDetails.address.city
     - City
     - "string"
   * - shippingDetails.address.country.code
     - Country
     - "string"


Wave Invoice to Exact Salesorderlines
-------------------------------------
Every Wave Invoice will be synchronized with a Exact Salesorderlines.

Once a link between a Wave Invoice and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - id
     - OrderID
     - "string"
   * - items.product.id
     - Item
     - "string"


Wave Invoice to Exact Salesorders
---------------------------------
Every Wave Invoice will be synchronized with a Exact Salesorders.

Once a link between a Wave Invoice and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Exact Salesorders Property
     - Exact Data Type
   * - currency.code
     - Currency
     - "string"
   * - memo
     - Description
     - "string"


Wave Product to Exact Items
---------------------------
Every Wave Product will be synchronized with a Exact Items.

Once a link between a Wave Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Exact Items Property
     - Exact Data Type


Wave Vendor to Exact Addresses
------------------------------
Every Wave Vendor will be synchronized with a Exact Addresses.

Once a link between a Wave Vendor and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Exact Addresses Property
     - Exact Data Type
   * - address.addressLine1
     - AddressLine1
     - "string"
   * - address.addressLine2
     - AddressLine2
     - "string"
   * - address.city
     - City
     - "string"
   * - address.country.code
     - Country
     - "string"


Wave Vendor to Exact Contacts
-----------------------------
Every Wave Vendor will be synchronized with a Exact Contacts.

Once a link between a Wave Vendor and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Exact Contacts Property
     - Exact Data Type
   * - address.city
     - City
     - "string"
   * - address.country.code
     - Country
     - "string"
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - mobile
     - Mobile
     - "string"
   * - phone
     - Phone
     - "string"

