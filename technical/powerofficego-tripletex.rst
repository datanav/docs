===================================
Powerofficego to Tripletex Dataflow
===================================

Generated: 2023-10-05 06:16:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Employee to Tripletex Employee
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Employee and a Tripletex Employee must be established.

A Powerofficego Employee will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - Tripletex Employee Property
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Powerofficego Employee and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - Tripletex Employee Property
     - Tripletex Data Type


Powerofficego Employees to Tripletex Employee
---------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Employees and a Tripletex Employee must be established.

A Powerofficego Employees will merge with a Tripletex Employee if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Tripletex Employee Property
   * - SocialSecurityNumber
     - nationalIdentityNumber

Once a link between a Powerofficego Employees and a Tripletex Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Tripletex Employee:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Tripletex Employee Property
     - Tripletex Data Type


Powerofficego Product to Tripletex Productunit
----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Product and a Tripletex Productunit must be established.

A Powerofficego Product will merge with a Tripletex Productunit if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Tripletex Productunit Property
   * - unitOfMeasureCode
     - name

Once a link between a Powerofficego Product and a Tripletex Productunit is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Tripletex Productunit:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Tripletex Productunit Property
     - Tripletex Data Type


Powerofficego Customer to Tripletex Customer
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a Tripletex Customer must be established.

A new Tripletex Customer will be created from a Powerofficego Customer if it is connected to a Powerofficego Customer, Customers, or Contactperson that is synchronized into Tripletex.

Once a link between a Powerofficego Customer and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - Tripletex Customer Property
     - Tripletex Data Type


Powerofficego Customer to Tripletex Department
----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customer and a Tripletex Department must be established.

A new Tripletex Department will be created from a Powerofficego Customer if it is connected to a Powerofficego Employee, or Employees that is synchronized into Tripletex.

Once a link between a Powerofficego Customer and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - Tripletex Department Property
     - Tripletex Data Type


Powerofficego Customers to Tripletex Contact
--------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Tripletex Contact must be established.

A new Tripletex Contact will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorder, or Salesorders that is synchronized into Tripletex.

Once a link between a Powerofficego Customers and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Contact Property
     - Tripletex Data Type


Powerofficego Customers to Tripletex Customer
---------------------------------------------
Every Powerofficego Customers will be synchronized with a Tripletex Customer.

Once a link between a Powerofficego Customers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Customer Property
     - Tripletex Data Type


Powerofficego Customers to Tripletex Department
-----------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Tripletex Department must be established.

A new Tripletex Department will be created from a Powerofficego Customers if it is connected to a Powerofficego Employee, or Employees that is synchronized into Tripletex.

Once a link between a Powerofficego Customers and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Tripletex Department Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to Tripletex Customer
-----------------------------------------------
Every Powerofficego Departments will be synchronized with a Tripletex Customer.

Once a link between a Powerofficego Departments and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to Tripletex Department
-------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Departments and a Tripletex Department must be established.

A new Tripletex Department will be created from a Powerofficego Departments if it is connected to a Powerofficego Employee, or Employees that is synchronized into Tripletex.

Once a link between a Powerofficego Departments and a Tripletex Department is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Tripletex Department:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Tripletex Department Property
     - Tripletex Data Type


Powerofficego Salesorder to Tripletex Order
-------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Salesorder and a Tripletex Order must be established.

A new Tripletex Order will be created from a Powerofficego Salesorder if it is connected to a Powerofficego Salesorderline that is synchronized into Tripletex.

Once a link between a Powerofficego Salesorder and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorder and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorder Property
     - Tripletex Order Property
     - Tripletex Data Type


Powerofficego Salesorders to Tripletex Order
--------------------------------------------
Every Powerofficego Salesorders will be synchronized with a Tripletex Order.

Once a link between a Powerofficego Salesorders and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Tripletex Order Property
     - Tripletex Data Type


Powerofficego Currency to Tripletex Customercategory
----------------------------------------------------
Every Powerofficego Currency will be synchronized with a Tripletex Customercategory.

Once a link between a Powerofficego Currency and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - Tripletex Customercategory Property
     - Tripletex Data Type


Powerofficego Outgoinginvoices to Tripletex Order
-------------------------------------------------
Every Powerofficego Outgoinginvoices will be synchronized with a Tripletex Order.

Once a link between a Powerofficego Outgoinginvoices and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoices and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoices Property
     - Tripletex Order Property
     - Tripletex Data Type


Powerofficego Product to Tripletex Product
------------------------------------------
Every Powerofficego Product will be synchronized with a Tripletex Product.

Once a link between a Powerofficego Product and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Tripletex Product Property
     - Tripletex Data Type


Powerofficego Productgroup to Tripletex Customercategory
--------------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a Tripletex Customercategory.

Once a link between a Powerofficego Productgroup and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - Tripletex Customercategory Property
     - Tripletex Data Type


Powerofficego Salesorderlines to Tripletex Order
------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a Tripletex Order.

Once a link between a Powerofficego Salesorderlines and a Tripletex Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a Tripletex Order:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     - Tripletex Order Property
     - Tripletex Data Type


Powerofficego Suppliers to Tripletex Customer
---------------------------------------------
Every Powerofficego Suppliers will be synchronized with a Tripletex Customer.

Once a link between a Powerofficego Suppliers and a Tripletex Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a Tripletex Customer:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - Tripletex Customer Property
     - Tripletex Data Type
   * - EmailAddress
     - email
     - "string"
   * - Id
     - id
     - "integer"
   * - LegalName
     - name
     - "string"
   * - MailAddress.AddressLine1
     - deliveryAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - physicalAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine1
     - postalAddress.addressLine1
     - "string"
   * - MailAddress.AddressLine2
     - deliveryAddress.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - physicalAddress.addressLine2
     - "string"
   * - MailAddress.AddressLine2
     - postalAddress.addressLine2
     - "string"
   * - MailAddress.City
     - deliveryAddress.city
     - "string"
   * - MailAddress.City
     - physicalAddress.city
     - "string"
   * - MailAddress.City
     - postalAddress.city
     - "string"
   * - MailAddress.CountryCode
     - deliveryAddress.country.id
     - "string"
   * - MailAddress.CountryCode
     - physicalAddress.country.id
     - "integer"
   * - MailAddress.CountryCode
     - postalAddress.country.id
     - "integer"
   * - MailAddress.ZipCode
     - deliveryAddress.postalCode
     - "string"
   * - MailAddress.ZipCode
     - physicalAddress.postalCode
     - "string"
   * - MailAddress.ZipCode
     - postalAddress.postalCode
     - "string"
   * - PhoneNumber
     - phoneNumber
     - "string"


Powerofficego Vatcodes to Tripletex Customercategory
----------------------------------------------------
Every Powerofficego Vatcodes will be synchronized with a Tripletex Customercategory.

Once a link between a Powerofficego Vatcodes and a Tripletex Customercategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Vatcodes and a Tripletex Customercategory:

.. list-table::
   :header-rows: 1

   * - Powerofficego Vatcodes Property
     - Tripletex Customercategory Property
     - Tripletex Data Type


Powerofficego Contactperson to Tripletex Contact
------------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Tripletex Contact.

Once a link between a Powerofficego Contactperson and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - partyCustomerCode
     - customer.id
     - "integer"
   * - partyId
     - customer.id
     - "integer"
   * - partySupplierCode
     - customer.id
     - "integer"
   * - phoneNumber
     - phoneNumberWork
     - "string"


Powerofficego Customers person to Tripletex Contact
---------------------------------------------------
Every Powerofficego Customers person will be synchronized with a Tripletex Contact.

Once a link between a Powerofficego Customers person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - EmailAddress
     - email
     - "string"
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"
   * - PhoneNumber
     - phoneNumberWork
     - "string"


Powerofficego Suppliers person to Tripletex Contact
---------------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Tripletex Contact.

Once a link between a Powerofficego Suppliers person and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - FirstName
     - firstName
     - "string"
   * - PhoneNumber
     - phoneNumberWork
     - "string"

