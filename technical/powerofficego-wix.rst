=============================
Powerofficego to Wix Dataflow
=============================

Generated: 2023-11-29 14:42:03

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Wix Members
------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Wix Members must be established.

A Powerofficego Contactperson will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wix Members Property
   * - emailAddress
     - loginEmail

Once a link between a Powerofficego Contactperson and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wix Members Property
     - Wix Data Type
   * - emailAddress
     - loginEmail
     - "string"


Powerofficego Customers person to Wix Contacts
----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a Wix Contacts must be established.

A Powerofficego Customers person will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Wix Contacts Property
   * - EmailAddress
     - primaryInfo.email

Once a link between a Powerofficego Customers person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Wix Contacts Property
     - Wix Data Type
   * - Id
     - id
     - "string"
   * - MailAddress.AddressLine1
     - info.addresses.items.address.addressLine
     - "string"
   * - MailAddress.AddressLine2
     - info.addresses.items.address.addressLine2
     - "string"
   * - MailAddress.City
     - info.addresses.items.address.city
     - "string"
   * - MailAddress.CountryCode
     - info.addresses.items.address.country
     - "string"
   * - MailAddress.ZipCode
     - info.addresses.items.address.postalCode
     - "string"


Powerofficego Customers person to Wix Members
---------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a Wix Members must be established.

A Powerofficego Customers person will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Wix Members Property
   * - EmailAddress
     - loginEmail

Once a link between a Powerofficego Customers person and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Wix Members Property
     - Wix Data Type


Powerofficego Customers to Wix Contacts
---------------------------------------
Every Powerofficego Customers will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Customers and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Wix Contacts Property
     - Wix Data Type
   * - EmailAddress
     - info.emails
     - "string"
   * - Id
     - id
     - "string"
   * - MailAddress.AddressLine1
     - info.addresses.items.address.addressLine
     - "string"
   * - MailAddress.AddressLine2
     - info.addresses.items.address.addressLine2
     - "string"
   * - MailAddress.City
     - info.addresses.items.address.city
     - "string"
   * - MailAddress.CountryCode
     - info.addresses.items.address.country
     - "string"
   * - MailAddress.ZipCode
     - info.addresses.items.address.postalCode
     - "string"


Powerofficego Customers to Wix Members
--------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Wix Members must be established.

A new Wix Members will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorders, Salesorderline, or Outgoinginvoices that is synchronized into Wix.

Once a link between a Powerofficego Customers and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Wix Members Property
     - Wix Data Type
   * - EmailAddress
     - loginEmail
     - "string"


Powerofficego Employees to Wix Contacts
---------------------------------------
Every Powerofficego Employees will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Employees and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Wix Contacts Property
     - Wix Data Type
   * - EmailAddress
     - primaryInfo.email
     - "string"
   * - FirstName
     - info.name.first
     - "string"
   * - Id
     - id
     - "string"
   * - LastName
     - info.name.last
     - "string"
   * - MailAddress.Address1
     - info.addresses.items.address.addressLine
     - "string"
   * - MailAddress.Address2
     - info.addresses.items.address.addressLine2
     - "string"
   * - MailAddress.City
     - info.addresses.items.address.city
     - "string"
   * - MailAddress.ZipCode
     - info.addresses.items.address.postalCode
     - "string"
   * - PhoneNumber
     - info.phones
     - "string"
   * - PhoneNumber
     - primaryInfo.phone
     - "string"


Powerofficego Contactperson to Wix Contacts
-------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the Powerofficego Contactperson will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A Powerofficego Contactperson will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wix Contacts Property
   * - emailAddress
     - primaryInfo.email

Once a link between a Powerofficego Contactperson and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wix Contacts Property
     - Wix Data Type
   * - address1
     - info.addresses.items.address.addressLine
     - "string"
   * - address2
     - info.addresses.items.address.addressLine2
     - "string"
   * - city
     - info.addresses.items.address.city
     - "string"
   * - emailAddress
     - info.emails
     - "string"
   * - emailAddress
     - primaryInfo.email
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - residenceCountryCode
     - info.addresses.items.address.country
     - "string"
   * - zipCode
     - info.addresses.items.address.postalCode
     - "string"


Powerofficego Product to Wix Inventory
--------------------------------------
Every Powerofficego Product will be synchronized with a Wix Inventory.

Once a link between a Powerofficego Product and a Wix Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Wix Inventory:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Wix Inventory Property
     - Wix Data Type
   * - availableStock
     - lastUpdated
     - "string"
   * - availableStock
     - variants.quantity
     - "integer"


Powerofficego Product to Wix Products
-------------------------------------
Every Powerofficego Product will be synchronized with a Wix Products.

Once a link between a Powerofficego Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Wix Products Property
     - Wix Data Type
   * - costPrice
     - costRange.maxValue
     - "string"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - price.price
     - "string"
   * - salesPrice
     - priceData.price
     - "decimal"


Powerofficego Suppliers person to Wix Contacts
----------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Suppliers person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Wix Contacts Property
     - Wix Data Type
   * - EmailAddress
     - primaryInfo.email
     - "string"
   * - FirstName
     - info.name.first
     - "string"
   * - Id
     - id
     - "string"
   * - MailAddress.AddressLine1
     - info.addresses.items.address.addressLine
     - "string"
   * - MailAddress.AddressLine2
     - info.addresses.items.address.addressLine2
     - "string"
   * - MailAddress.City
     - info.addresses.items.address.city
     - "string"
   * - MailAddress.CountryCode
     - info.addresses.items.address.country
     - "string"
   * - MailAddress.ZipCode
     - info.addresses.items.address.postalCode
     - "string"

