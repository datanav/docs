==================================
PowerOffice GO to Hubspot Dataflow
==================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Contactperson to Hubspot Contact
--------------------------------------------
Every PowerOffice Contactperson will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the PowerOffice Contactperson will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A PowerOffice Contactperson will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Hubspot Contact Property
   * - emailAddress
     - properties.email

Once a link between a PowerOffice Contactperson and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


PowerOffice Customers person to Hubspot Contact
-----------------------------------------------
Every PowerOffice Customers person will be synchronized with a Hubspot Contact.

If a matching Hubspot Contact already exists, the PowerOffice Customers person will be merged with the existing one.
If no matching Hubspot Contact is found, a new Hubspot Contact will be created.

A PowerOffice Customers person will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - Hubspot Contact Property
   * - EmailAddress
     - properties.email

Once a link between a PowerOffice Customers person and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


PowerOffice Contactperson to Hubspot Company
--------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Contactperson and a Hubspot Company must be established.

A new Hubspot Company will be created from a PowerOffice Contactperson if it is connected to a PowerOffice Powerofficego-quote that is synchronized into Hubspot.

Once a link between a PowerOffice Contactperson and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Hubspot Company Property
     - Hubspot Data Type


PowerOffice Customers to Hubspot Company
----------------------------------------
Every PowerOffice Customers will be synchronized with a Hubspot Company.

Once a link between a PowerOffice Customers and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - Hubspot Company Property
     - Hubspot Data Type
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
   * - OrganizationNumber (Dependant on having NO in MailAddress.CountryCode)
     - properties.sesam_org_number_no
     - "string"
   * - OrganizationNumber (Dependant on having SE in MailAddress.CountryCode)
     - properties.sesam_org_number_se
     - "string"
   * - OrganizationNumber (Dependant on having  in MailAddress.CountryCodeDependant on having NO in MailAddress.CountryCode)
     - sync_org_nr
     - "string"
   * - PhoneNumber
     - properties.phone
     - "string"
   * - WebsiteUrl
     - properties.website
     - "string"


PowerOffice Customers to Hubspot Contact
----------------------------------------
Before any synchronization can take place, a link between a PowerOffice Customers and a Hubspot Contact must be established.

A new Hubspot Contact will be created from a PowerOffice Customers if it is connected to a PowerOffice Powerofficego-quote that is synchronized into Hubspot.

Once a link between a PowerOffice Customers and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - MailAddress.CountryCode
     - properties.country
     - "string"


Powerofficego Departments to Hubspot Company
--------------------------------------------
Every Powerofficego Departments will be synchronized with a Hubspot Company.

Once a link between a Powerofficego Departments and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Hubspot Company Property
     - Hubspot Data Type
   * - Name
     - properties.name
     - "string"


Powerofficego Employees to Hubspot Contact
------------------------------------------
Every Powerofficego Employees will be synchronized with a Hubspot Contact.

Once a link between a Powerofficego Employees and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


PowerOffice Product to Hubspot Product
--------------------------------------
Every PowerOffice Product will be synchronized with a Hubspot Product.

Once a link between a PowerOffice Product and a Hubspot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Product and a Hubspot Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice Product Property
     - Hubspot Product Property
     - Hubspot Data Type
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


PowerOffice Quote to Hubspot Quote
----------------------------------
Every PowerOffice Quote will be synchronized with a Hubspot Quote.

Once a link between a PowerOffice Quote and a Hubspot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Quote and a Hubspot Quote:

.. list-table::
   :header-rows: 1

   * - PowerOffice Quote Property
     - Hubspot Quote Property
     - Hubspot Data Type
   * - CreatedDate
     - properties.hs_createdate
     - "string"


PowerOffice Salesorderlines to Hubspot Lineitem
-----------------------------------------------
Every PowerOffice Salesorderlines will be synchronized with a Hubspot Lineitem.

Once a link between a PowerOffice Salesorderlines and a Hubspot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Salesorderlines and a Hubspot Lineitem:

.. list-table::
   :header-rows: 1

   * - PowerOffice Salesorderlines Property
     - Hubspot Lineitem Property
     - Hubspot Data Type
   * - Allowance
     - properties.hs_discount_percentage
     - "string"
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
     - N/A

