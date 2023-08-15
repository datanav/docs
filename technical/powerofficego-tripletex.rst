===================================
Powerofficego to Tripletex Dataflow
===================================

Generated: 2023-08-15 08:52:57

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
Every Powerofficego Customers will be synchronized with a Tripletex Contact.

Once a link between a Powerofficego Customers and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
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
   * - emailAddress
     - email
     - "string"
   * - firstName
     - firstName
     - "string"


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
   * - InvoiceEmailAddressCC
     - invoiceEmail
     - "string"
   * - id
     - id
     - "integer"
   * - legalName
     - name
     - "string"
   * - mailAddress.address1
     - postalAddress.addressLine1
     - "string"
   * - mailAddress.address2
     - postalAddress.addressLine2
     - "string"
   * - mailAddress.addressLine1
     - postalAddress.addressLine1
     - "string"
   * - mailAddress.addressLine2
     - postalAddress.addressLine2
     - "string"
   * - mailAddress.city
     - postalAddress.city
     - "string"
   * - mailAddress.countryCode
     - postalAddress.country.id
     - "integer"
   * - mailAddress.zipCode
     - postalAddress.postalCode
     - "string"
   * - ourReferenceEmployeeCode
     - accountManager.id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - streetAddresses.address1
     - physicalAddress.addressLine1
     - "string"
   * - streetAddresses.address2
     - physicalAddress.addressLine2
     - "string"
   * - streetAddresses.city
     - physicalAddress.city
     - "string"
   * - streetAddresses.countryCode
     - physicalAddress.country.id
     - "integer"
   * - streetAddresses.zipCode
     - physicalAddress.postalCode
     - "string"
   * - vatNumber (Dependant on having NO in mailAddress.countryCodeDependant on having NO in mailAddress.countryCode)
     - organizationNumber
     - "replace"," ","", "string"]


Powerofficego Employees to Tripletex Employee
---------------------------------------------
Every Powerofficego Employees will be synchronized with a Tripletex Employee.

If a matching Tripletex Employee already exists, the Powerofficego Employees will be merged with the existing one.
If no matching Tripletex Employee is found, a new Tripletex Employee will be created.

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
   * - DateOfBirth
     - dateOfBirth
     - "datetime-format","%Y-%m-%d","_."]
   * - FirstName
     - firstName
     - "string"
   * - LastName
     - lastName
     - "string"


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


Powerofficego Suppliers to Tripletex Supplier
---------------------------------------------
Every Powerofficego Suppliers will be synchronized with a Tripletex Supplier.

Once a link between a Powerofficego Suppliers and a Tripletex Supplier is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a Tripletex Supplier:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - Tripletex Supplier Property
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
   * - PhoneNumber
     - phoneNumber
     - "string"

