===========================
Tripletex to Exact Dataflow
===========================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to Exact Contacts
-------------------------------------------
Every Tripletex Customer person will be synchronized with a Exact Contacts.

Once a link between a Tripletex Customer person and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Exact Contacts Property
     - Exact Data Type
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


Tripletex Department to Exact Accounts
--------------------------------------
Every Tripletex Department will be synchronized with a Exact Accounts.

Once a link between a Tripletex Department and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Exact Accounts Property
     - Exact Data Type
   * - name
     - Name
     - "string"


Tripletex Employee to Exact Contacts
------------------------------------
Every Tripletex Employee will be synchronized with a Exact Contacts.

Once a link between a Tripletex Employee and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Exact Contacts Property
     - Exact Data Type
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


Tripletex Order to Exact Quotations
-----------------------------------
Every Tripletex Order will be synchronized with a Exact Quotations.

Once a link between a Tripletex Order and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Exact Quotations Property
     - Exact Data Type
   * - currency.id
     - Currency
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"


Tripletex Orderline to Exact Quotations
---------------------------------------
Every Tripletex Orderline will be synchronized with a Exact Quotations.

Once a link between a Tripletex Orderline and a Exact Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Exact Quotations:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Exact Quotations Property
     - Exact Data Type
   * - currency.id
     - Currency
     - "string"


Tripletex Contact to Exact Contacts
-----------------------------------
Every Tripletex Contact will be synchronized with a Exact Contacts.

Once a link between a Tripletex Contact and a Exact Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Exact Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Exact Contacts Property
     - Exact Data Type
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


Tripletex Currency to Exact Currencies
--------------------------------------
Every Tripletex Currency will be synchronized with a Exact Currencies.

Once a link between a Tripletex Currency and a Exact Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a Exact Currencies:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Exact Currencies Property
     - Exact Data Type
   * - displayName
     - Description
     - "string"


Tripletex Customer to Exact Accounts
------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Exact Accounts.

Once a link between a Tripletex Customer and a Exact Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Exact Accounts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Exact Accounts Property
     - Exact Data Type
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


Tripletex Customer person to Exact Addresses
--------------------------------------------
Every Tripletex Customer person will be synchronized with a Exact Addresses.

Once a link between a Tripletex Customer person and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Exact Addresses Property
     - Exact Data Type
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


Tripletex Department to Exact Departments
-----------------------------------------
Every Tripletex Department will be synchronized with a Exact Departments.

If a matching Exact Departments already exists, the Tripletex Department will be merged with the existing one.
If no matching Exact Departments is found, a new Exact Departments will be created.

A Tripletex Department will merge with a Exact Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Exact Departments Property
   * - departmentNumber
     - Code

Once a link between a Tripletex Department and a Exact Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Exact Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Exact Departments Property
     - Exact Data Type
   * - departmentNumber
     - Code
     - "string"


Tripletex Employee to Exact Addresses
-------------------------------------
Every Tripletex Employee will be synchronized with a Exact Addresses.

Once a link between a Tripletex Employee and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Exact Addresses Property
     - Exact Data Type
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


Tripletex Employee to Exact Employees
-------------------------------------
Every Tripletex Employee will be synchronized with a Exact Employees.

Once a link between a Tripletex Employee and a Exact Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Exact Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Exact Employees Property
     - Exact Data Type
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


Tripletex Invoice to Exact Salesinvoices
----------------------------------------
Every Tripletex Invoice will be synchronized with a Exact Salesinvoices.

Once a link between a Tripletex Invoice and a Exact Salesinvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a Exact Salesinvoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - Exact Salesinvoices Property
     - Exact Data Type
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


Tripletex Order to Exact Salesorders
------------------------------------
Every Tripletex Order will be synchronized with a Exact Salesorders.

Once a link between a Tripletex Order and a Exact Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Exact Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Exact Salesorders Property
     - Exact Data Type
   * - currency.id
     - Currency
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - orderDate
     - OrderDate
     - "string"


Tripletex Orderline to Exact Salesorderlines
--------------------------------------------
Every Tripletex Orderline will be synchronized with a Exact Salesorderlines.

Once a link between a Tripletex Orderline and a Exact Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Exact Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Exact Salesorderlines Property
     - Exact Data Type
   * - order.id
     - OrderID
     - "string"
   * - product.id
     - Item
     - "string"
   * - unitCostCurrency
     - CostPriceFC
     - "string"


Tripletex Product to Exact Items
--------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Exact Items.

Once a link between a Tripletex Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Exact Items Property
     - Exact Data Type


Tripletex Productunit to Exact Units
------------------------------------
Every Tripletex Productunit will be synchronized with a Exact Units.

Once a link between a Tripletex Productunit and a Exact Units is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productunit and a Exact Units:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     - Exact Units Property
     - Exact Data Type
   * - commonCode
     - Code
     - "string"
   * - name
     - Description
     - "string"


Tripletex Vattype to Exact Vatcodes
-----------------------------------
Every Tripletex Vattype will be synchronized with a Exact Vatcodes.

Once a link between a Tripletex Vattype and a Exact Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Vattype and a Exact Vatcodes:

.. list-table::
   :header-rows: 1

   * - Tripletex Vattype Property
     - Exact Vatcodes Property
     - Exact Data Type
   * - number
     - Code
     - "string"

