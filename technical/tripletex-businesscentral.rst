======================================
Tripletex to Business Central Dataflow
======================================

Generated: 2024-09-24 00:00:36

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Business Central. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Product to Business Central Items
-------------------------------------------
Before any synchronization can take place, a link between a Tripletex Product and a Business Central Items must be established.

A new Business Central Items will be created from a Tripletex Product if it is connected to a Tripletex Orderline that is synchronized into Business Central.

A Tripletex Product will merge with a Business Central Items if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Business Central Items Property
   * - ean
     - gtin

Once a link between a Tripletex Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Business Central Items Property
     - Business Central Data Type
   * - costExcludingVatCurrency
     - unitCost
     - N/A
   * - ean
     - gtin
     - "string"
   * - name
     - displayName
     - "string"
   * - priceExcludingVatCurrency
     - unitPrice
     - N/A


Tripletex Customer to Business Central Companies
------------------------------------------------
Every Tripletex Customer will be synchronized with a Business Central Companies.

Once a link between a Tripletex Customer and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Business Central Companies Property
     - Business Central Data Type


Tripletex Department to Business Central Companies
--------------------------------------------------
Every Tripletex Department will be synchronized with a Business Central Companies.

Once a link between a Tripletex Department and a Business Central Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Business Central Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Business Central Companies Property
     - Business Central Data Type


Tripletex Contact to Business Central Contacts (human data)
-----------------------------------------------------------
Every Tripletex Contact will be synchronized with a Business Central Contacts (human data).

Once a link between a Tripletex Contact and a Business Central Contacts (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Business Central Contacts (human data):

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Business Central Contacts (human data) Property
     - Business Central Data Type
   * - email
     - email
     - "string"
   * - phoneNumberMobile
     - mobilePhoneNumber
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Customer to Business Central Customers (organisation data)
--------------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Business Central Customers (organisation data).

Once a link between a Tripletex Customer and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type
   * - deliveryAddress.addressLine1
     - addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - addressLine2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postalCode
     - "string"
   * - id
     - id
     - "string"
   * - name
     - displayName
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - addressLine2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postalCode
     - "string"
   * - postalAddress.addressLine1
     - addressLine1
     - "string"
   * - postalAddress.addressLine2
     - addressLine2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postalCode
     - "string"
   * - website
     - website
     - "string"


Tripletex Customer to Business Central Customers (human data)
-------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Business Central Customers (human data).

Once a link between a Tripletex Customer and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Business Central Customers (human data) Property
     - Business Central Data Type


Tripletex Customer (classification data) to Business Central Contacts (classification data)
-------------------------------------------------------------------------------------------
Every Tripletex Customer (classification data) will be synchronized with a Business Central Contacts (classification data).

Once a link between a Tripletex Customer (classification data) and a Business Central Contacts (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (classification data) and a Business Central Contacts (classification data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (classification data) Property
     - Business Central Contacts (classification data) Property
     - Business Central Data Type
   * - deliveryAddress.addressLine1
     - addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - addressLine2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - isPrivateIndividual
     - type
     - "string"
   * - name
     - displayName
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - phoneNumberMobile
     - mobilePhoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - addressLine2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postalCode
     - "string"
   * - postalAddress.addressLine1
     - addressLine1
     - "string"
   * - postalAddress.addressLine2
     - addressLine2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postalCode
     - "string"


Tripletex Customer (organisation data) to Business Central Customers (organisation data)
----------------------------------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Business Central Customers (organisation data).

Once a link between a Tripletex Customer (organisation data) and a Business Central Customers (organisation data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (organisation data) and a Business Central Customers (organisation data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (organisation data) Property
     - Business Central Customers (organisation data) Property
     - Business Central Data Type
   * - deliveryAddress.addressLine1
     - addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - addressLine2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postalCode
     - "string"
   * - id
     - id
     - "string"
   * - physicalAddress.addressLine1
     - addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - addressLine2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postalCode
     - "string"
   * - postalAddress.addressLine1
     - addressLine1
     - "string"
   * - postalAddress.addressLine2
     - addressLine2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postalCode
     - "string"


Tripletex Customer (classification data) to Business Central Customers (classification data)
--------------------------------------------------------------------------------------------
Every Tripletex Customer (classification data) will be synchronized with a Business Central Customers (classification data).

Once a link between a Tripletex Customer (classification data) and a Business Central Customers (classification data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (classification data) and a Business Central Customers (classification data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (classification data) Property
     - Business Central Customers (classification data) Property
     - Business Central Data Type


Tripletex Customer (human data) to Business Central Customers (human data)
--------------------------------------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Business Central Customers (human data).

Once a link between a Tripletex Customer (human data) and a Business Central Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer (human data) and a Business Central Customers (human data):

.. list-table::
   :header-rows: 1

   * - Tripletex Customer (human data) Property
     - Business Central Customers (human data) Property
     - Business Central Data Type
   * - deliveryAddress.addressLine1
     - addressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - addressLine2
     - "string"
   * - deliveryAddress.city
     - city
     - "string"
   * - deliveryAddress.country.id
     - country
     - "string"
   * - deliveryAddress.postalCode
     - postalCode
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - isPrivateIndividual
     - type
     - "string"
   * - name
     - displayName
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - addressLine1
     - "string"
   * - physicalAddress.addressLine2
     - addressLine2
     - "string"
   * - physicalAddress.city
     - city
     - "string"
   * - physicalAddress.country.id
     - country
     - "string"
   * - physicalAddress.postalCode
     - postalCode
     - "string"
   * - postalAddress.addressLine1
     - addressLine1
     - "string"
   * - postalAddress.addressLine2
     - addressLine2
     - "string"
   * - postalAddress.city
     - city
     - "string"
   * - postalAddress.country.id
     - country
     - "string"
   * - postalAddress.postalCode
     - postalCode
     - "string"


Tripletex Employee to Business Central Employees
------------------------------------------------
Every Tripletex Employee will be synchronized with a Business Central Employees.

Once a link between a Tripletex Employee and a Business Central Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Business Central Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Business Central Employees Property
     - Business Central Data Type
   * - address.addressLine1
     - addressLine1
     - "string"
   * - address.addressLine2
     - addressLine2
     - "string"
   * - address.city
     - city
     - "string"
   * - address.country.id
     - country
     - "string"
   * - address.postalCode
     - postalCode
     - "string"
   * - dateOfBirth
     - birthDate
     - "string"
   * - email
     - email
     - "string"
   * - firstName
     - givenName
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - surname
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"


Tripletex Order to Business Central Salesorders
-----------------------------------------------
Every Tripletex Order will be synchronized with a Business Central Salesorders.

Once a link between a Tripletex Order and a Business Central Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Business Central Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Business Central Salesorders Property
     - Business Central Data Type


Tripletex Orderline to Business Central Salesorderlines
-------------------------------------------------------
Every Tripletex Orderline will be synchronized with a Business Central Salesorderlines.

Once a link between a Tripletex Orderline and a Business Central Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Business Central Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Business Central Salesorderlines Property
     - Business Central Data Type


Tripletex Product to Business Central Items
-------------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Business Central Items.

Once a link between a Tripletex Product and a Business Central Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Business Central Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Business Central Items Property
     - Business Central Data Type

