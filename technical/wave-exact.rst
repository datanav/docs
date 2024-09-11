============================
Wave to ExactOnline Dataflow
============================

Generated: 2024-09-11 11:13:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to ExactOnline Contacts
--------------------------------------------
Every Wave Customer person will be synchronized with a ExactOnline Contacts.

Once a link between a Wave Customer person and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


Wave Invoice to ExactOnline Quotations
--------------------------------------
Every Wave Invoice will be synchronized with a ExactOnline Quotations.

Once a link between a Wave Invoice and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - currency.code
     - Currency
     - "string"
   * - dueDate
     - DueDate
     - "string"
   * - memo
     - Description
     - "string"


Wave Currency to ExactOnline Currencies
---------------------------------------
Every Wave Currency will be synchronized with a ExactOnline Currencies.

Once a link between a Wave Currency and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - name
     - Description
     - "string"


Wave Customer to ExactOnline Accounts
-------------------------------------
Every Wave Customer will be synchronized with a ExactOnline Accounts.

Once a link between a Wave Customer and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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


Wave Customer to ExactOnline Contacts
-------------------------------------
Every Wave Customer will be synchronized with a ExactOnline Contacts.

Once a link between a Wave Customer and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


Wave Customer person to ExactOnline Addresses
---------------------------------------------
Every Wave Customer person will be synchronized with a ExactOnline Addresses.

Once a link between a Wave Customer person and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
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


Wave Invoice to ExactOnline Salesorderlines
-------------------------------------------
Every Wave Invoice will be synchronized with a ExactOnline Salesorderlines.

Once a link between a Wave Invoice and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - id
     - OrderID
     - "string"
   * - items.product.id
     - Item
     - "string"


Wave Invoice to ExactOnline Salesorders
---------------------------------------
Every Wave Invoice will be synchronized with a ExactOnline Salesorders.

Once a link between a Wave Invoice and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
   * - currency.code
     - Currency
     - "string"
   * - memo
     - Description
     - "string"


Wave Product to ExactOnline Items
---------------------------------
Every Wave Product will be synchronized with a ExactOnline Items.

Once a link between a Wave Product and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - ExactOnline Items Property
     - ExactOnline Data Type


Wave Vendor to ExactOnline Addresses
------------------------------------
Every Wave Vendor will be synchronized with a ExactOnline Addresses.

Once a link between a Wave Vendor and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
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


Wave Vendor to ExactOnline Contacts
-----------------------------------
Every Wave Vendor will be synchronized with a ExactOnline Contacts.

Once a link between a Wave Vendor and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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

