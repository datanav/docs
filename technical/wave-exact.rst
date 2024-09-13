=============================
Wave to Exact Online Dataflow
=============================

Generated: 2024-09-13 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Exact Online Contacts
---------------------------------------------
Every Wave Customer person will be synchronized with a Exact Online Contacts.

Once a link between a Wave Customer person and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Wave Invoice to Exact Online Quotations
---------------------------------------
Every Wave Invoice will be synchronized with a Exact Online Quotations.

Once a link between a Wave Invoice and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - currency.code
     - Currency
     - "string"
   * - dueDate
     - DueDate
     - "string"
   * - memo
     - Description
     - "string"


Wave Currency to Exact Online Currencies
----------------------------------------
Every Wave Currency will be synchronized with a Exact Online Currencies.

Once a link between a Wave Currency and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - name
     - Description
     - "string"


Wave Customer to Exact Online Accounts
--------------------------------------
Every Wave Customer will be synchronized with a Exact Online Accounts.

Once a link between a Wave Customer and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Exact Online Accounts Property
     - Exact Online Data Type
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


Wave Customer to Exact Online Contacts
--------------------------------------
Every Wave Customer will be synchronized with a Exact Online Contacts.

Once a link between a Wave Customer and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Wave Customer person to Exact Online Addresses
----------------------------------------------
Every Wave Customer person will be synchronized with a Exact Online Addresses.

Once a link between a Wave Customer person and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Exact Online Addresses Property
     - Exact Online Data Type
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


Wave Invoice to Exact Online Salesorderlines
--------------------------------------------
Every Wave Invoice will be synchronized with a Exact Online Salesorderlines.

Once a link between a Wave Invoice and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - id
     - OrderID
     - "string"
   * - items.product.id
     - Item
     - "string"


Wave Invoice to Exact Online Salesorders
----------------------------------------
Every Wave Invoice will be synchronized with a Exact Online Salesorders.

Once a link between a Wave Invoice and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - currency.code
     - Currency
     - "string"
   * - memo
     - Description
     - "string"


Wave Product to Exact Online Items
----------------------------------
Every Wave Product will be synchronized with a Exact Online Items.

Once a link between a Wave Product and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Exact Online Items Property
     - Exact Online Data Type


Wave Vendor to Exact Online Addresses
-------------------------------------
Every Wave Vendor will be synchronized with a Exact Online Addresses.

Once a link between a Wave Vendor and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Exact Online Addresses Property
     - Exact Online Data Type
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


Wave Vendor to Exact Online Contacts
------------------------------------
Every Wave Vendor will be synchronized with a Exact Online Contacts.

Once a link between a Wave Vendor and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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

