=================================
Powerofficego to HubSpot Dataflow
=================================

Generated: 2023-09-07 10:57:04

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to HubSpot Company
------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a HubSpot Company must be established.

A new HubSpot Company will be created from a Powerofficego Customers if it is connected to a Powerofficego Quote that is synchronized into HubSpot.

Once a link between a Powerofficego Customers and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Name
     - properties.name
     - "string"
   * - Number
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"


Powerofficego Contactperson to HubSpot Contact
----------------------------------------------
Every Powerofficego Contactperson will be synchronized with a HubSpot Contact.

Once a link between a Powerofficego Contactperson and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - address1
     - properties.address
     - "string"
   * - city
     - properties.city
     - "string"
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - emailAddress
     - properties.email
     - "string"
   * - emailAddress
     - properties.work_email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - id
     - id
     - "string"
   * - lastName
     - properties.lastname
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - residenceCountryCode
     - properties.country
     - "string"
   * - zipCode
     - properties.zip
     - "string"


Powerofficego Customer to HubSpot Company
-----------------------------------------
Every Powerofficego Customer will be synchronized with a HubSpot Company.

Once a link between a Powerofficego Customer and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - LegalName
     - properties.name
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"
   * - id
     - id
     - "string"
   * - legalName
     - properties.name
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - phoneNumberMobile
     - properties.phone
     - "string"
   * - streetAddresses.address1
     - properties.address
     - "string"
   * - streetAddresses.address2
     - properties.address2
     - "string"
   * - streetAddresses.city
     - properties.city
     - "string"
   * - streetAddresses.countryCode
     - properties.country
     - "string"
   * - streetAddresses.zipCode
     - properties.zip
     - "string"
   * - websiteUrl
     - properties.website
     - "string"


Powerofficego Customer to HubSpot Contact
-----------------------------------------
Every Powerofficego Customer will be synchronized with a HubSpot Contact.

Once a link between a Powerofficego Customer and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - LastName
     - properties.lastname
     - "string"
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - emailAddress
     - properties.email
     - "string"
   * - emailAddress
     - properties.work_email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - id
     - id
     - "string"
   * - mailAddress.countryCode
     - properties.country
     - "string"
   * - streetAddresses.address1
     - properties.address
     - "string"
   * - streetAddresses.city
     - properties.city
     - "string"
   * - streetAddresses.countryCode
     - properties.country
     - "string"
   * - streetAddresses.zipCode
     - properties.zip
     - "string"


Powerofficego Customers to HubSpot Contact
------------------------------------------
Every Powerofficego Customers will be synchronized with a HubSpot Contact.

Once a link between a Powerofficego Customers and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - DateOfBirth
     - properties.date_of_birth
     - "string"
   * - EmailAddress
     - properties.email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - LastName
     - properties.lastname
     - "string"
   * - MailAddress.countryCode
     - properties.country
     - "string"
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - emailAddress
     - properties.email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - mailAddress.countryCode
     - properties.country
     - "string"
   * - streetAddresses.countryCode
     - properties.country
     - "string"


Powerofficego Departments to HubSpot Company
--------------------------------------------
Every Powerofficego Departments will be synchronized with a HubSpot Company.

Once a link between a Powerofficego Departments and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Name
     - properties.name
     - "string"


Powerofficego Employee to HubSpot Contact
-----------------------------------------
Every Powerofficego Employee will be synchronized with a HubSpot Contact.

Once a link between a Powerofficego Employee and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employee and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employee Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - DateOfBirth
     - properties.date_of_birth
     - "string"
   * - EmailAddress
     - properties.work_email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - LastName
     - properties.lastname
     - "string"
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - emailAddress
     - properties.work_email
     - "string"


Powerofficego Employees to HubSpot Contact
------------------------------------------
Every Powerofficego Employees will be synchronized with a HubSpot Contact.

Once a link between a Powerofficego Employees and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - DateOfBirth
     - properties.date_of_birth
     - "string"
   * - EmailAddress
     - properties.work_email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - LastName
     - properties.lastname
     - "string"
   * - MailAddress.countryCode
     - properties.country
     - "string"
   * - PhoneNumber
     - properties.mobilephone
     - "string"
   * - dateOfBirth
     - properties.date_of_birth
     - "string"
   * - emailAddress
     - properties.work_email
     - "string"
   * - firstName
     - properties.firstname
     - "string"
   * - lastName
     - properties.lastname
     - "string"


Powerofficego Supplier to HubSpot Company
-----------------------------------------
Every Powerofficego Supplier will be synchronized with a HubSpot Company.

Once a link between a Powerofficego Supplier and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Supplier and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Supplier Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - LegalName
     - properties.name
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"


Powerofficego Suppliers to HubSpot Company
------------------------------------------
Every Powerofficego Suppliers will be synchronized with a HubSpot Company.

Once a link between a Powerofficego Suppliers and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - LegalName
     - properties.name
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"


Powerofficego Suppliers to HubSpot Contact
------------------------------------------
Every Powerofficego Suppliers will be synchronized with a HubSpot Contact.

Once a link between a Powerofficego Suppliers and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - EmailAddress
     - properties.work_email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"


Powerofficego Product to HubSpot Product
----------------------------------------
Every Powerofficego Product will be synchronized with a HubSpot Product.

Once a link between a Powerofficego Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - HubSpot Product Property
     - HubSpot Data Type
   * - CostPrice
     - properties.hs_cost_of_goods_sold
     - "string"
   * - Description
     - properties.description
     - "string"
   * - Name
     - properties.name
     - "string"
   * - SalesPrice
     - properties.price
     - "string"
   * - costPrice
     - properties.hs_cost_of_goods_sold
     - "string"
   * - description
     - properties.description
     - "string"
   * - name
     - properties.name
     - "string"
   * - salesPrice
     - properties.price
     - "string"


Powerofficego Quote to HubSpot Quote
------------------------------------
Every Powerofficego Quote will be synchronized with a HubSpot Quote.

Once a link between a Powerofficego Quote and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Quote and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - Powerofficego Quote Property
     - HubSpot Quote Property
     - HubSpot Data Type


Powerofficego Salesorderline to HubSpot Lineitemdealassociation
---------------------------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a HubSpot Lineitemdealassociation.

Once a link between a Powerofficego Salesorderline and a HubSpot Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a HubSpot Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - HubSpot Lineitemdealassociation Property
     - HubSpot Data Type

