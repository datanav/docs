===========================
SuperOffice to Wix Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Wix Contacts
----------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Wix Contacts must be established.

A new Wix Contacts will be created from a SuperOffice Person if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Wix.

A SuperOffice Person will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Contacts Property
   * - Emails.Value
     - primaryInfo.email

Once a link between a SuperOffice Person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Contacts Property
     - Wix Data Type
   * - Address.Street.Address1
     - info.addresses.items.address.addressLine
     - "string"
   * - Address.Street.Address2
     - info.addresses.items.address.addressLine2
     - "string"
   * - Address.Street.City
     - info.addresses.items.address.city
     - "string"
   * - Address.Street.Zipcode
     - info.addresses.items.address.postalCode
     - "string"
   * - Emails.Value
     - info.emails
     - "string"
   * - Emails.Value
     - primaryInfo.email
     - "string"
   * - Firstname
     - info.name.first
     - "string"
   * - Lastname
     - info.name.last
     - "string"
   * - MobilePhones.Value
     - info.phones
     - "string"
   * - MobilePhones.Value
     - primaryInfo.phone
     - "string"
   * - OfficePhones.Value
     - primaryInfo.phone
     - "string"
   * - PersonId
     - id
     - "string"


SuperOffice Person to Wix Members
---------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Wix Members must be established.

A SuperOffice Person will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Members Property
   * - Emails.Value
     - loginEmail

Once a link between a SuperOffice Person and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Wix Members:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Members Property
     - Wix Data Type
   * - Emails.Value
     - loginEmail
     - "string"


SuperOffice Pricelist to Wix Currencies
---------------------------------------
Before any synchronization can take place, a link between a SuperOffice Pricelist and a Wix Currencies must be established.

A SuperOffice Pricelist will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - Wix Currencies Property
   * - Currency
     - code

Once a link between a SuperOffice Pricelist and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Pricelist and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Pricelist Property
     - Wix Currencies Property
     - Wix Data Type


SuperOffice User to Wix Contacts
--------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Wix Contacts must be established.

A SuperOffice User will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Contacts Property
   * - personEmail
     - primaryInfo.email

Once a link between a SuperOffice User and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Contacts Property
     - Wix Data Type
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - personEmail
     - info.emails
     - "string"
   * - personEmail
     - primaryInfo.email
     - "string"


SuperOffice User to Wix Members
-------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Wix Members must be established.

A SuperOffice User will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Members Property
   * - personEmail
     - loginEmail

Once a link between a SuperOffice User and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Wix Members:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Members Property
     - Wix Data Type
   * - personEmail
     - loginEmail
     - "string"


SuperOffice Contact to Wix Contacts
-----------------------------------
Before any synchronization can take place, a link between a SuperOffice Contact and a Wix Contacts must be established.

A new Wix Contacts will be created from a SuperOffice Contact if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Wix.

Once a link between a SuperOffice Contact and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Wix Contacts Property
     - Wix Data Type
   * - Address.Postal.Address1
     - info.addresses.items.address.addressLine
     - "string"
   * - Address.Postal.Address2
     - info.addresses.items.address.addressLine2
     - "string"
   * - Address.Postal.City
     - info.addresses.items.address.city
     - "string"
   * - Address.Postal.Zipcode
     - info.addresses.items.address.postalCode
     - "string"
   * - Address.Street.Address1
     - info.addresses.items.address.addressLine
     - "string"
   * - Address.Street.Address2
     - info.addresses.items.address.addressLine2
     - "string"
   * - Address.Street.City
     - info.addresses.items.address.city
     - "string"
   * - Address.Street.Zipcode
     - info.addresses.items.address.postalCode
     - "string"
   * - ContactId
     - id
     - "string"


SuperOffice Quotealternative to Wix Orders
------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Quotealternative and a Wix Orders must be established.

A new Wix Orders will be created from a SuperOffice Quotealternative if it is connected to a SuperOffice Quoteline, or Quotealternative that is synchronized into Wix.

Once a link between a SuperOffice Quotealternative and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Wix Orders Property
     - Wix Data Type
   * - TotalPrice
     - totals.total
     - "string"


SuperOffice Listcurrencyitems to Wix Currencies
-----------------------------------------------
Every SuperOffice Listcurrencyitems will be synchronized with a Wix Currencies.

If a matching Wix Currencies already exists, the SuperOffice Listcurrencyitems will be merged with the existing one.
If no matching Wix Currencies is found, a new Wix Currencies will be created.

A SuperOffice Listcurrencyitems will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Wix Currencies Property
   * - Name
     - code

Once a link between a SuperOffice Listcurrencyitems and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcurrencyitems and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcurrencyitems Property
     - Wix Currencies Property
     - Wix Data Type


SuperOffice Product to Wix Products
-----------------------------------
Every SuperOffice Product will be synchronized with a Wix Products.

Once a link between a SuperOffice Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - Wix Products Property
     - Wix Data Type
   * - Description
     - description
     - "string"
   * - ERPPriceListKey
     - price.currency
     - "string"
   * - ERPPriceListKey
     - priceData.currency
     - "string"
   * - Name
     - name
     - "string"
   * - UnitCost
     - costAndProfitData.itemCost
     - N/A
   * - UnitCost
     - costRange.maxValue
     - "string"
   * - UnitListPrice
     - price.price
     - "string"
   * - UnitListPrice
     - priceData.price
     - N/A

