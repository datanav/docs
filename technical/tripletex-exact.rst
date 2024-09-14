==================================
Tripletex to Exact Online Dataflow
==================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer person to Exact Online Contacts
--------------------------------------------------
Every Tripletex Customer person will be synchronized with a Exact Online Contacts.

Once a link between a Tripletex Customer person and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Tripletex Department to Exact Online Accounts
---------------------------------------------
Every Tripletex Department will be synchronized with a Exact Online Accounts.

Once a link between a Tripletex Department and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Exact Online Accounts Property
     - Exact Online Data Type
   * - name
     - Name
     - "string"


Tripletex Employee to Exact Online Contacts
-------------------------------------------
Every Tripletex Employee will be synchronized with a Exact Online Contacts.

Once a link between a Tripletex Employee and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Tripletex Order to Exact Online Quotations
------------------------------------------
Every Tripletex Order will be synchronized with a Exact Online Quotations.

Once a link between a Tripletex Order and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - currency.id
     - Currency
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"


Tripletex Orderline to Exact Online Quotations
----------------------------------------------
Every Tripletex Orderline will be synchronized with a Exact Online Quotations.

Once a link between a Tripletex Orderline and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Exact Online Quotations Property
     - Exact Online Data Type
   * - currency.id
     - Currency
     - "string"


Tripletex Contact to Exact Online Contacts
------------------------------------------
Every Tripletex Contact will be synchronized with a Exact Online Contacts.

Once a link between a Tripletex Contact and a Exact Online Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Exact Online Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Exact Online Contacts Property
     - Exact Online Data Type
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


Tripletex Currency to Exact Online Currencies
---------------------------------------------
Every Tripletex Currency will be synchronized with a Exact Online Currencies.

Once a link between a Tripletex Currency and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - displayName
     - Description
     - "string"


Tripletex Customer to Exact Online Accounts
-------------------------------------------
removed person customers for now until that pattern is resolved, it  will be synchronized with a Exact Online Accounts.

Once a link between a Tripletex Customer and a Exact Online Accounts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Exact Online Accounts:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Exact Online Accounts Property
     - Exact Online Data Type
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


Tripletex Customer person to Exact Online Addresses
---------------------------------------------------
Every Tripletex Customer person will be synchronized with a Exact Online Addresses.

Once a link between a Tripletex Customer person and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer person and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer person Property
     - Exact Online Addresses Property
     - Exact Online Data Type
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


Tripletex Department to Exact Online Departments
------------------------------------------------
Every Tripletex Department will be synchronized with a Exact Online Departments.

If a matching Exact Online Departments already exists, the Tripletex Department will be merged with the existing one.
If no matching Exact Online Departments is found, a new Exact Online Departments will be created.

A Tripletex Department will merge with a Exact Online Departments if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Exact Online Departments Property
   * - departmentNumber
     - Code

Once a link between a Tripletex Department and a Exact Online Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Exact Online Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Exact Online Departments Property
     - Exact Online Data Type
   * - departmentNumber
     - Code
     - "string"


Tripletex Employee to Exact Online Addresses
--------------------------------------------
Every Tripletex Employee will be synchronized with a Exact Online Addresses.

Once a link between a Tripletex Employee and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
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
   * - address.country.id
     - Country
     - "string"


Tripletex Employee to Exact Online Employees
--------------------------------------------
Every Tripletex Employee will be synchronized with a Exact Online Employees.

Once a link between a Tripletex Employee and a Exact Online Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a Exact Online Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - Exact Online Employees Property
     - Exact Online Data Type
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


Tripletex Invoice to Exact Online Salesinvoices
-----------------------------------------------
Every Tripletex Invoice will be synchronized with a Exact Online Salesinvoices.

Once a link between a Tripletex Invoice and a Exact Online Salesinvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Invoice and a Exact Online Salesinvoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Invoice Property
     - Exact Online Salesinvoices Property
     - Exact Online Data Type
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


Tripletex Order to Exact Online Salesorders
-------------------------------------------
Every Tripletex Order will be synchronized with a Exact Online Salesorders.

Once a link between a Tripletex Order and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - currency.id
     - Currency
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - orderDate
     - OrderDate
     - "string"


Tripletex Orderline to Exact Online Salesorderlines
---------------------------------------------------
Every Tripletex Orderline will be synchronized with a Exact Online Salesorderlines.

Once a link between a Tripletex Orderline and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type
   * - order.id
     - OrderID
     - "string"
   * - product.id
     - Item
     - "string"
   * - unitCostCurrency
     - CostPriceFC
     - "string"


Tripletex Product to Exact Online Items
---------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Exact Online Items.

Once a link between a Tripletex Product and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Exact Online Items Property
     - Exact Online Data Type


Tripletex Productunit to Exact Online Units
-------------------------------------------
Every Tripletex Productunit will be synchronized with a Exact Online Units.

Once a link between a Tripletex Productunit and a Exact Online Units is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productunit and a Exact Online Units:

.. list-table::
   :header-rows: 1

   * - Tripletex Productunit Property
     - Exact Online Units Property
     - Exact Online Data Type
   * - commonCode
     - Code
     - "string"
   * - name
     - Description
     - "string"


Tripletex Vattype to Exact Online Vatcodes
------------------------------------------
Every Tripletex Vattype will be synchronized with a Exact Online Vatcodes.

Once a link between a Tripletex Vattype and a Exact Online Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Vattype and a Exact Online Vatcodes:

.. list-table::
   :header-rows: 1

   * - Tripletex Vattype Property
     - Exact Online Vatcodes Property
     - Exact Online Data Type
   * - number
     - Code
     - "string"

