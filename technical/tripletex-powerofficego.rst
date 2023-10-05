===================================
Tripletex to PowerOfficeGo Dataflow
===================================

Generated: 2023-10-05 06:16:43

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Currency to PowerOfficeGo Currency
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Currency and a PowerOfficeGo Currency must be established.

A Tripletex Currency will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - PowerOfficeGo Currency Property
   * - code
     - Code

Once a link between a Tripletex Currency and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


Tripletex Employee to PowerOfficeGo Employees
---------------------------------------------
Before any synchronization can take place, a link between a Tripletex Employee and a PowerOfficeGo Employees must be established.

A Tripletex Employee will merge with a PowerOfficeGo Employees if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Employees Property
   * - nationalIdentityNumber
     - SocialSecurityNumber

Once a link between a Tripletex Employee and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Employee and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - Tripletex Employee Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type


Tripletex Contact to PowerOfficeGo Customers person
---------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Contact and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - email
     - EmailAddress
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - phoneNumberWork
     - PhoneNumber
     - "string"


Tripletex Contact to PowerOfficeGo Customers
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Contact and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Tripletex Contact if it is connected to a Tripletex Order that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Contact and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type


Tripletex Customer to PowerOfficeGo Customers person
----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Customer if it is connected to a Tripletex Order, or Contact that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - deliveryAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - id
     - Id
     - "string"
   * - physicalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - physicalAddress.city
     - MailAddress.City
     - "string"
   * - physicalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - physicalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"


Tripletex Customer to PowerOfficeGo Customers
---------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Tripletex Customer if it is connected to a Tripletex Order, or Contact that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - deliveryAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - deliveryAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - deliveryAddress.city
     - MailAddress.City
     - "string"
   * - deliveryAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - deliveryAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - email
     - EmailAddress
     - "string"
   * - id
     - Id
     - "string"
   * - invoiceEmail
     - InvoiceEmailAddress
     - "string"
   * - name
     - Name
     - "string"
   * - organizationNumber
     - OrganizationNumber (Dependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCodeDependant on having NO in MailAddress.countryCode)
     - "string"
   * - phoneNumber
     - Number
     - "string"
   * - phoneNumber
     - PhoneNumber
     - "string"
   * - physicalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - physicalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - physicalAddress.city
     - MailAddress.City
     - "string"
   * - physicalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - physicalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.AddressLine1
     - "string"
   * - postalAddress.addressLine1
     - MailAddress.addressLine1
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.AddressLine2
     - "string"
   * - postalAddress.addressLine2
     - MailAddress.addressLine2
     - "string"
   * - postalAddress.city
     - MailAddress.City
     - "string"
   * - postalAddress.city
     - MailAddress.city
     - "string"
   * - postalAddress.country.id
     - MailAddress.CountryCode
     - "string"
   * - postalAddress.country.id
     - MailAddress.countryCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.ZipCode
     - "string"
   * - postalAddress.postalCode
     - MailAddress.zipCode
     - "string"


Tripletex Customer to PowerOfficeGo Departments
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a PowerOfficeGo Departments must be established.

A new PowerOfficeGo Departments will be created from a Tripletex Customer if it is connected to a Tripletex Employee that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Customer and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - changes.timestamp
     - CreatedDateTimeOffset
     - "string"
   * - name
     - Name
     - "string"


Tripletex Department to PowerOfficeGo Customers person
------------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Tripletex Department if it is connected to a Tripletex Contact that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Department and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type


Tripletex Department to PowerOfficeGo Customers
-----------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Tripletex Department if it is connected to a Tripletex Contact that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Department and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - name
     - Name
     - "string"


Tripletex Department to PowerOfficeGo Departments
-------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Department and a PowerOfficeGo Departments must be established.

A new PowerOfficeGo Departments will be created from a Tripletex Department if it is connected to a Tripletex Employee that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Department and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type


Tripletex Order to PowerOfficeGo Salesorders
--------------------------------------------
Before any synchronization can take place, a link between a Tripletex Order and a PowerOfficeGo Salesorders must be established.

A new PowerOfficeGo Salesorders will be created from a Tripletex Order if it is connected to a Tripletex Order, or Orderline that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Order and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type


Tripletex Productgroup to PowerOfficeGo Productgroup
----------------------------------------------------
Before any synchronization can take place, a link between a Tripletex Productgroup and a PowerOfficeGo Productgroup must be established.

A new PowerOfficeGo Productgroup will be created from a Tripletex Productgroup if it is connected to a Tripletex Product that is synchronized into PowerOfficeGo.

Once a link between a Tripletex Productgroup and a PowerOfficeGo Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a PowerOfficeGo Productgroup:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - PowerOfficeGo Productgroup Property
     - PowerOfficeGo Data Type


Tripletex Order to PowerOfficeGo Outgoinginvoices
-------------------------------------------------
Every Tripletex Order will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Tripletex Order and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - changes.timestamp
     - createdDateTimeOffset
     - "string"
   * - contact.id
     - customerId
     - "string"
   * - currency.id
     - CurrencyCode
     - "string"
   * - customer.id
     - customerId
     - "string"
   * - deliveryDate
     - DeliveryDate
     - "string"
   * - deliveryDate
     - sentDateTimeOffset
     - "string"
   * - orderDate
     - OrderDate
     - "string"


Tripletex Orderline to PowerOfficeGo Outgoinginvoices
-----------------------------------------------------
Every Tripletex Orderline will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Tripletex Orderline and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - changes.timestamp
     - createdDateTimeOffset
     - "string"
   * - currency.id
     - CurrencyCode
     - "string"
   * - order.id
     - OrderNo
     - "string"


Tripletex Contact to PowerOfficeGo Contactperson
------------------------------------------------
Every Tripletex Contact will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Tripletex Contact and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - customer.id
     - partyCustomerCode
     - "string"
   * - customer.id
     - partyId
     - "string"
   * - customer.id
     - partySupplierCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - lastName
     - lastName
     - "string"
   * - phoneNumberWork
     - phoneNumber
     - "string"

