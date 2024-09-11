=================================
Tripletex to ExactOnline Dataflow
=================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to ExactOnline. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to ExactOnline Contacts
-------------------------------------------------
Every Tripletex Customer person will be synchronized with a ExactOnline Contacts.

Once a link between a Tripletex Customer person and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


Tripletex Department to ExactOnline Accounts
--------------------------------------------
Every Tripletex Department will be synchronized with a ExactOnline Accounts.

Once a link between a Tripletex Department and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
   * - name
     - Name
     - "string"


Tripletex Employee to ExactOnline Contacts
------------------------------------------
Every Tripletex Employee will be synchronized with a ExactOnline Contacts.

Once a link between a Tripletex Employee and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


Tripletex Order to ExactOnline Quotations
-----------------------------------------
Every Tripletex Order will be synchronized with a ExactOnline Quotations.

Once a link between a Tripletex Order and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - currency.id
     - Currency
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"


Tripletex Orderline to ExactOnline Quotations
---------------------------------------------
Every Tripletex Orderline will be synchronized with a ExactOnline Quotations.

Once a link between a Tripletex Orderline and a ExactOnline Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a ExactOnline Quotations:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - ExactOnline Quotations Property
     - ExactOnline Data Type
   * - currency.id
     - Currency
     - "string"


Tripletex Contact to ExactOnline Contacts
-----------------------------------------
Every Tripletex Contact will be synchronized with a ExactOnline Contacts.

Once a link between a Tripletex Contact and a ExactOnline Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a ExactOnline Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - ExactOnline Contacts Property
     - ExactOnline Data Type
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


Tripletex Currency to ExactOnline Currencies
--------------------------------------------
Every Tripletex Currency will be synchronized with a ExactOnline Currencies.

Once a link between a Tripletex Currency and a ExactOnline Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a ExactOnline Currencies:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - ExactOnline Currencies Property
     - ExactOnline Data Type
   * - displayName
     - Description
     - "string"


Tripletex Customer to ExactOnline Accounts
------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a ExactOnline Accounts.

Once a link between a Tripletex Customer and a ExactOnline Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a ExactOnline Accounts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - ExactOnline Accounts Property
     - ExactOnline Data Type
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


Tripletex Customer person to ExactOnline Addresses
--------------------------------------------------
Every Tripletex Customer person will be synchronized with a ExactOnline Addresses.

Once a link between a Tripletex Customer person and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - ExactOnline Addresses Property
     - ExactOnline Data Type
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


Tripletex Department to ExactOnline Departments
-----------------------------------------------
Every Tripletex Department will be synchronized with a ExactOnline Departments.

If a matching ExactOnline Departments already exists, the Tripletex Department will be merged with the existing one.
If no matching ExactOnline Departments is found, a new ExactOnline Departments will be created.

A Tripletex Department will merge with a ExactOnline Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - ExactOnline Departments Property
   * - departmentNumber
     - Code

Once a link between a Tripletex Department and a ExactOnline Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a ExactOnline Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - ExactOnline Departments Property
     - ExactOnline Data Type
   * - departmentNumber
     - Code
     - "string"


Tripletex Employee to ExactOnline Addresses
-------------------------------------------
Every Tripletex Employee will be synchronized with a ExactOnline Addresses.

Once a link between a Tripletex Employee and a ExactOnline Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a ExactOnline Addresses:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
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
   * - address.country.id
     - Country
     - "string"


Tripletex Employee to ExactOnline Employees
-------------------------------------------
Every Tripletex Employee will be synchronized with a ExactOnline Employees.

Once a link between a Tripletex Employee and a ExactOnline Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a ExactOnline Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - ExactOnline Employees Property
     - ExactOnline Data Type
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
   * - dateOfBirth
     - BirthDate
     - "string"
   * - email
     - BusinessEmail
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - id
     - ID
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberHome
     - Mobile
     - "string"
   * - phoneNumberMobile
     - BusinessMobile
     - "string"
   * - phoneNumberWork
     - Phone
     - "string"


Tripletex Invoice to ExactOnline Salesinvoices
----------------------------------------------
Every Tripletex Invoice will be synchronized with a ExactOnline Salesinvoices.

Once a link between a Tripletex Invoice and a ExactOnline Salesinvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a ExactOnline Salesinvoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - ExactOnline Salesinvoices Property
     - ExactOnline Data Type
   * - currency.id
     - Currency
     - "string"
   * - invoiceDate
     - InvoiceDate
     - "string"
   * - invoiceDueDate
     - DueDate
     - "string"
   * - invoiceNumber
     - InvoiceNumber
     - "string"


Tripletex Order to ExactOnline Salesorders
------------------------------------------
Every Tripletex Order will be synchronized with a ExactOnline Salesorders.

Once a link between a Tripletex Order and a ExactOnline Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a ExactOnline Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - ExactOnline Salesorders Property
     - ExactOnline Data Type
   * - currency.id
     - Currency
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - orderDate
     - OrderDate
     - "string"


Tripletex Orderline to ExactOnline Salesorderlines
--------------------------------------------------
Every Tripletex Orderline will be synchronized with a ExactOnline Salesorderlines.

Once a link between a Tripletex Orderline and a ExactOnline Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a ExactOnline Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - ExactOnline Salesorderlines Property
     - ExactOnline Data Type
   * - order.id
     - OrderID
     - "string"
   * - product.id
     - Item
     - "string"
   * - unitCostCurrency
     - CostPriceFC
     - "string"


Tripletex Product to ExactOnline Items
--------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a ExactOnline Items.

Once a link between a Tripletex Product and a ExactOnline Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a ExactOnline Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - ExactOnline Items Property
     - ExactOnline Data Type


Tripletex Productunit to ExactOnline Units
------------------------------------------
Every Tripletex Productunit will be synchronized with a ExactOnline Units.

Once a link between a Tripletex Productunit and a ExactOnline Units is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productunit and a ExactOnline Units:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     - ExactOnline Units Property
     - ExactOnline Data Type
   * - commonCode
     - Code
     - "string"
   * - name
     - Description
     - "string"


Tripletex Vattype to ExactOnline Vatcodes
-----------------------------------------
Every Tripletex Vattype will be synchronized with a ExactOnline Vatcodes.

Once a link between a Tripletex Vattype and a ExactOnline Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Vattype and a ExactOnline Vatcodes:

.. list-table::
   :header-rows: 1

   * - Tripletex Vattype Property
     - ExactOnline Vatcodes Property
     - ExactOnline Data Type
   * - number
     - Code
     - "string"

