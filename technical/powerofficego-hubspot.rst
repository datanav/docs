==========================
Powerofficego to  Dataflow
==========================

Generated: 2023-11-29 23:45:21

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Contact
---------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Contact.

If a matching  Contact already exists, the Powerofficego Contactperson will be merged with the existing one.
If no matching  Contact is found, a new  Contact will be created.

A Powerofficego Contactperson will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Contact Property
   * - emailAddress
     - properties.email

Once a link between a Powerofficego Contactperson and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Contact Property
     -  Data Type
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


Powerofficego Customers person to  Contact
------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a  Contact must be established.

A Powerofficego Customers person will merge with a  Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Contact Property
   * - EmailAddress
     - properties.email

Once a link between a Powerofficego Customers person and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Contact Property
     -  Data Type
   * - DateOfBirth
     - properties.date_of_birth
     - "string"
   * - EmailAddress
     - properties.email
     - "string"
   * - FirstName
     - properties.firstname
     - "string"
   * - Id
     - id
     - "string"
   * - LastName
     - properties.lastname
     - "string"
   * - MailAddress.AddressLine1
     - properties.address
     - "string"
   * - MailAddress.City
     - properties.city
     - "string"
   * - MailAddress.CountryCode
     - properties.country
     - "string"
   * - MailAddress.ZipCode
     - properties.zip
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"


Powerofficego Contactperson to  Company
---------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a  Company must be established.

A new  Company will be created from a Powerofficego Contactperson if it is connected to a Powerofficego Quote that is synchronized into .

Once a link between a Powerofficego Contactperson and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Company Property
     -  Data Type


Powerofficego Customers to  Company
-----------------------------------
Every Powerofficego Customers will be synchronized with a  Company.

Once a link between a Powerofficego Customers and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Company Property
     -  Data Type
   * - Id
     - id
     - "string"
   * - MailAddress.AddressLine1
     - properties.address
     - "string"
   * - MailAddress.AddressLine2
     - properties.address2
     - "string"
   * - MailAddress.City
     - properties.city
     - "string"
   * - MailAddress.CountryCode
     - properties.country
     - "string"
   * - MailAddress.ZipCode
     - properties.zip
     - "string"
   * - Name
     - properties.name
     - "string"
   * - Number
     - properties.phone
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"


Powerofficego Customers to  Contact
-----------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a  Contact must be established.

A new  Contact will be created from a Powerofficego Customers if it is connected to a Powerofficego Quote that is synchronized into .

Once a link between a Powerofficego Customers and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Contact Property
     -  Data Type
   * - MailAddress.CountryCode
     - properties.country
     - "string"


Powerofficego Departments to  Company
-------------------------------------
Every Powerofficego Departments will be synchronized with a  Company.

Once a link between a Powerofficego Departments and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Company Property
     -  Data Type
   * - Name
     - properties.name
     - "string"


Powerofficego Employees to  Contact
-----------------------------------
Every Powerofficego Employees will be synchronized with a  Contact.

Once a link between a Powerofficego Employees and a  Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a  Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     -  Contact Property
     -  Data Type
   * - DateOfBirth
     - properties.date_of_birth
     - "string"
   * - EmailAddress
     - properties.email
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
   * - MailAddress.CountryCode
     - properties.country
     - "string"
   * - MailAddress.CountryCode
     - properties.state
     - "string"
   * - MailAddress.countryCode
     - properties.country
     - "string"
   * - MailAddress.countryCode
     - properties.state
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


Powerofficego Product to  Product
---------------------------------
Every Powerofficego Product will be synchronized with a  Product.

Once a link between a Powerofficego Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a  Product:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     -  Product Property
     -  Data Type
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


Powerofficego Quote to  Quote
-----------------------------
Every Powerofficego Quote will be synchronized with a  Quote.

Once a link between a Powerofficego Quote and a  Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Quote and a  Quote:

.. list-table::
   :header-rows: 1

   * - Powerofficego Quote Property
     -  Quote Property
     -  Data Type
   * - CreatedDate
     - properties.hs_createdate
     - "string"


Powerofficego Salesorderlines to  Lineitem
------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Lineitem.

Once a link between a Powerofficego Salesorderlines and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Lineitem Property
     -  Data Type
   * - Description
     - properties.name
     - "string"
   * - ProductCode
     - properties.hs_product_id
     - "string"
   * - ProductId
     - properties.hs_product_id
     - "string"
   * - ProductUnitPrice
     - properties.price
     - "string"
   * - Quantity
     - properties.quantity
     - "integer"


Powerofficego Salesorderlines to  Lineitemdealassociation
---------------------------------------------------------
Every Powerofficego Salesorderlines will be synchronized with a  Lineitemdealassociation.

Once a link between a Powerofficego Salesorderlines and a  Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderlines and a  Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderlines Property
     -  Lineitemdealassociation Property
     -  Data Type
   * - sesam_SalesOrderId
     - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - "string"
   * - sesam_SalesOrdersId
     - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - "string"

