===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-08-31 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to  Contacts
---------------------------------
Every Wave Customer person will be synchronized with a  Contacts.

Once a link between a Wave Customer person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Contacts Property
     -  Data Type
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


Wave Invoice to  Quotations
---------------------------
Every Wave Invoice will be synchronized with a  Quotations.

Once a link between a Wave Invoice and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Quotations Property
     -  Data Type
   * - currency.code
     - Currency
     - "string"
   * - dueDate
     - DueDate
     - "string"
   * - memo
     - Description
     - "string"


Wave Currency to  Currencies
----------------------------
Every Wave Currency will be synchronized with a  Currencies.

Once a link between a Wave Currency and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a  Currencies:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     -  Currencies Property
     -  Data Type
   * - name
     - Description
     - "string"


Wave Customer to  Accounts
--------------------------
Every Wave Customer will be synchronized with a  Accounts.

Once a link between a Wave Customer and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Accounts Property
     -  Data Type
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


Wave Customer to  Contacts
--------------------------
Every Wave Customer will be synchronized with a  Contacts.

Once a link between a Wave Customer and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Contacts Property
     -  Data Type
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


Wave Customer person to  Addresses
----------------------------------
Every Wave Customer person will be synchronized with a  Addresses.

Once a link between a Wave Customer person and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Addresses Property
     -  Data Type
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


Wave Invoice to  Salesorderlines
--------------------------------
Every Wave Invoice will be synchronized with a  Salesorderlines.

Once a link between a Wave Invoice and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Salesorderlines Property
     -  Data Type
   * - id
     - OrderID
     - "string"
   * - items.product.id
     - Item
     - "string"


Wave Invoice to  Salesorders
----------------------------
Every Wave Invoice will be synchronized with a  Salesorders.

Once a link between a Wave Invoice and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Salesorders Property
     -  Data Type
   * - currency.code
     - Currency
     - "string"
   * - memo
     - Description
     - "string"


Wave Vendor to  Addresses
-------------------------
Every Wave Vendor will be synchronized with a  Addresses.

Once a link between a Wave Vendor and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Addresses Property
     -  Data Type
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


Wave Vendor to  Contacts
------------------------
Every Wave Vendor will be synchronized with a  Contacts.

Once a link between a Wave Vendor and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Contacts Property
     -  Data Type
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

