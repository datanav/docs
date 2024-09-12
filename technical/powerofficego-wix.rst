==============================
PowerOffice GO to Wix Dataflow
==============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Wix Members
-------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Wix Members must be established.

A PowerOffice GO Contactperson will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Wix Members Property
   * - emailAddress
     - loginEmail

Once a link between a PowerOffice GO Contactperson and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Wix Members:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Wix Members Property
     - Wix Data Type
   * - emailAddress
     - loginEmail
     - "string"


PowerOffice GO Customers person to Wix Contacts
-----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Wix Contacts must be established.

A PowerOffice GO Customers person will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Wix Contacts Property
   * - EmailAddress
     - primaryInfo.email

Once a link between a PowerOffice GO Customers person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
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


PowerOffice GO Customers person to Wix Members
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Wix Members must be established.

A PowerOffice GO Customers person will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Wix Members Property
   * - EmailAddress
     - loginEmail

Once a link between a PowerOffice GO Customers person and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Wix Members:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Wix Members Property
     - Wix Data Type


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


PowerOffice GO Contactperson to Wix Contacts
--------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the PowerOffice GO Contactperson will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A PowerOffice GO Contactperson will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Wix Contacts Property
   * - emailAddress
     - primaryInfo.email

Once a link between a PowerOffice GO Contactperson and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
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


PowerOffice GO Currency to Wix Currencies
-----------------------------------------
Every PowerOffice GO Currency will be synchronized with a Wix Currencies.

If a matching Wix Currencies already exists, the PowerOffice GO Currency will be merged with the existing one.
If no matching Wix Currencies is found, a new Wix Currencies will be created.

A PowerOffice GO Currency will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Currency Property
     - Wix Currencies Property
   * - code
     - code

Once a link between a PowerOffice GO Currency and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Currency and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Currency Property
     - Wix Currencies Property
     - Wix Data Type


PowerOffice GO Product to Wix Products
--------------------------------------
Every PowerOffice GO Product will be synchronized with a Wix Products.

Once a link between a PowerOffice GO Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
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


PowerOffice GO Salesorders to Wix Orders
----------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a Wix Orders.

Once a link between a PowerOffice GO Salesorders and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - Wix Orders Property
     - Wix Data Type
   * - CurrencyCode
     - currency
     - "string"
   * - TotalAmount
     - totals.total
     - "string"


PowerOffice GO Suppliers person to Wix Contacts
-----------------------------------------------
Every PowerOffice GO Suppliers person will be synchronized with a Wix Contacts.

Once a link between a PowerOffice GO Suppliers person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
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

