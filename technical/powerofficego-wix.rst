=============================
Powerofficego to Wix Dataflow
=============================

Generated: 2024-07-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - PhoneNumber
     - primaryInfo.phone
     - "string"


Powerofficego Customers to Wix Contacts
---------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Wix Contacts must be established.

A new Wix Contacts will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorders, Salesorderline, Salesorderlines, or Outgoinginvoices that is synchronized into Wix.

Once a link between a Powerofficego Customers and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
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
   * - phoneNumber
     - primaryInfo.phone
     - "string"
   * - residenceCountryCode
     - info.addresses.items.address.country
     - "string"
   * - zipCode
     - info.addresses.items.address.postalCode
     - "string"


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
     - costAndProfitData.itemCost
     - N/A
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
     - N/A


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
   * - LastName
     - info.name.last
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
   * - PhoneNumber
     - primaryInfo.phone
     - "string"

