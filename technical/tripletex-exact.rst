======================
Tripletex to  Dataflow
======================

Generated: 2024-08-29 12:52:26

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to  Contacts
--------------------------------------
Every Tripletex Customer person will be synchronized with a  Contacts.

Once a link between a Tripletex Customer person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Contacts Property
     -  Data Type
   * - deliveryAddress.city
     - City
     - "string"
   * - deliveryAddress.country.id
     - Country
     - "string"
   * - email
     - Email
     - "string"
   * - name
     - FullName
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - phoneNumberMobile
     - Mobile
     - "string"
   * - physicalAddress.city
     - City
     - "string"
   * - physicalAddress.country.id
     - Country
     - "string"
   * - postalAddress.city
     - City
     - "string"
   * - postalAddress.country.id
     - Country
     - "string"


Tripletex Department to  Accounts
---------------------------------
Every Tripletex Department will be synchronized with a  Accounts.

Once a link between a Tripletex Department and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Accounts Property
     -  Data Type
   * - name
     - Name
     - "string"


Tripletex Employee to  Contacts
-------------------------------
Every Tripletex Employee will be synchronized with a  Contacts.

Once a link between a Tripletex Employee and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Contacts Property
     -  Data Type
   * - address.city
     - City
     - "string"
   * - address.country.id
     - Country
     - "string"
   * - dateOfBirth
     - BirthDate
     - "string"
   * - email
     - BusinessEmail
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberMobile
     - Mobile
     - "string"
   * - phoneNumberWork
     - Phone
     - "string"


Tripletex Order to  Quotations
------------------------------
Every Tripletex Order will be synchronized with a  Quotations.

Once a link between a Tripletex Order and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     -  Quotations Property
     -  Data Type
   * - currency.id
     - Currency
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"


Tripletex Orderline to  Quotations
----------------------------------
Every Tripletex Orderline will be synchronized with a  Quotations.

Once a link between a Tripletex Orderline and a  Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a  Quotations:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     -  Quotations Property
     -  Data Type
   * - currency.id
     - Currency
     - "string"


Tripletex Contact to  Contacts
------------------------------
Every Tripletex Contact will be synchronized with a  Contacts.

Once a link between a Tripletex Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Contacts Property
     -  Data Type
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberMobile
     - Mobile
     - "string"
   * - phoneNumberWork
     - Phone
     - "string"


Tripletex Currency to  Currencies
---------------------------------
Every Tripletex Currency will be synchronized with a  Currencies.

Once a link between a Tripletex Currency and a  Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a  Currencies:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     -  Currencies Property
     -  Data Type
   * - displayName
     - Description
     - "string"


Tripletex Customer to  Accounts
-------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a  Accounts.

Once a link between a Tripletex Customer and a  Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Accounts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Accounts Property
     -  Data Type
   * - deliveryAddress.addressLine1
     - AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - AddressLine2
     - "string"
   * - deliveryAddress.city
     - City
     - "string"
   * - deliveryAddress.country.id
     - Country
     - "string"
   * - deliveryAddress.postalCode
     - Postcode
     - "string"
   * - name
     - Name
     - "string"
   * - phoneNumber
     - Phone
     - "string"
   * - physicalAddress.addressLine1
     - AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - AddressLine2
     - "string"
   * - physicalAddress.city
     - City
     - "string"
   * - physicalAddress.country.id
     - Country
     - "string"
   * - physicalAddress.postalCode
     - Postcode
     - "string"
   * - postalAddress.addressLine1
     - AddressLine1
     - "string"
   * - postalAddress.addressLine2
     - AddressLine2
     - "string"
   * - postalAddress.city
     - City
     - "string"
   * - postalAddress.country.id
     - Country
     - "string"
   * - postalAddress.postalCode
     - Postcode
     - "string"
   * - website
     - Website
     - "string"


Tripletex Customer person to  Addresses
---------------------------------------
Every Tripletex Customer person will be synchronized with a  Addresses.

Once a link between a Tripletex Customer person and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     -  Addresses Property
     -  Data Type
   * - deliveryAddress.addressLine1
     - AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - AddressLine2
     - "string"
   * - deliveryAddress.city
     - City
     - "string"
   * - deliveryAddress.country.id
     - Country
     - "string"
   * - physicalAddress.addressLine1
     - AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - AddressLine2
     - "string"
   * - physicalAddress.city
     - City
     - "string"
   * - physicalAddress.country.id
     - Country
     - "string"
   * - postalAddress.addressLine1
     - AddressLine1
     - "string"
   * - postalAddress.addressLine2
     - AddressLine2
     - "string"
   * - postalAddress.city
     - City
     - "string"
   * - postalAddress.country.id
     - Country
     - "string"


Tripletex Employee to  Addresses
--------------------------------
Every Tripletex Employee will be synchronized with a  Addresses.

Once a link between a Tripletex Employee and a  Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Addresses:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
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
   * - address.country.id
     - Country
     - "string"


Tripletex Employee to  Employees
--------------------------------
Every Tripletex Employee will be synchronized with a  Employees.

Once a link between a Tripletex Employee and a  Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a  Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     -  Employees Property
     -  Data Type
   * - address.addressLine1
     - AddressStreet
     - "string"
   * - address.addressLine2
     - AddressLine2
     - "string"
   * - address.city
     - City
     - "string"
   * - address.country.id
     - Country
     - "string"
   * - address.postalCode
     - Postcode
     - "string"
   * - id
     - ID
     - "string"

