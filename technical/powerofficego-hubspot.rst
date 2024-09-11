==================================
PowerOffice GO to HubSpot Dataflow
==================================

Generated: 2024-09-11 11:39:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to HubSpot Contact
-----------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the PowerOffice GO Contactperson will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A PowerOffice GO Contactperson will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - HubSpot Contact Property
   * - emailAddress
     - properties.email

Once a link between a PowerOffice GO Contactperson and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
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


PowerOffice GO Customers person to HubSpot Contact
--------------------------------------------------
Every PowerOffice GO Customers person will be synchronized with a HubSpot Contact.

If a matching HubSpot Contact already exists, the PowerOffice GO Customers person will be merged with the existing one.
If no matching HubSpot Contact is found, a new HubSpot Contact will be created.

A PowerOffice GO Customers person will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - HubSpot Contact Property
   * - EmailAddress
     - properties.email

Once a link between a PowerOffice GO Customers person and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
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


PowerOfficeGO Contactperson to HubSpot Company
----------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Contactperson and a HubSpot Company must be established.

A new HubSpot Company will be created from a PowerOfficeGO Contactperson if it is connected to a PowerOfficeGO Quote that is synchronized into HubSpot.

Once a link between a PowerOfficeGO Contactperson and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - HubSpot Company Property
     - HubSpot Data Type


PowerOfficeGO Customers to HubSpot Company
------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a HubSpot Company.

Once a link between a PowerOfficeGO Customers and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - HubSpot Company Property
     - HubSpot Data Type
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


PowerOfficeGO Customers to HubSpot Contact
------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Customers and a HubSpot Contact must be established.

A new HubSpot Contact will be created from a PowerOfficeGO Customers if it is connected to a PowerOfficeGO Quote that is synchronized into HubSpot.

Once a link between a PowerOfficeGO Customers and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - MailAddress.CountryCode
     - properties.country
     - "string"


PowerOfficeGO Departments to HubSpot Company
--------------------------------------------
Every PowerOfficeGO Departments will be synchronized with a HubSpot Company.

Once a link between a PowerOfficeGO Departments and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Departments and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Departments Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Name
     - properties.name
     - "string"


PowerOfficeGO Employees to HubSpot Contact
------------------------------------------
Every PowerOfficeGO Employees will be synchronized with a HubSpot Contact.

Once a link between a PowerOfficeGO Employees and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Employees and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Employees Property
     - HubSpot Contact Property
     - HubSpot Data Type
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


PowerOfficeGO Product to HubSpot Product
----------------------------------------
Every PowerOfficeGO Product will be synchronized with a HubSpot Product.

Once a link between a PowerOfficeGO Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Product Property
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


PowerOfficeGO Quote to HubSpot Quote
------------------------------------
Every PowerOfficeGO Quote will be synchronized with a HubSpot Quote.

Once a link between a PowerOfficeGO Quote and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Quote and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Quote Property
     - HubSpot Quote Property
     - HubSpot Data Type
   * - CreatedDate
     - properties.hs_createdate
     - "string"


PowerOfficeGO Salesorderlines to HubSpot Lineitem
-------------------------------------------------
Every PowerOfficeGO Salesorderlines will be synchronized with a HubSpot Lineitem.

Once a link between a PowerOfficeGO Salesorderlines and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Salesorderlines and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Salesorderlines Property
     - HubSpot Lineitem Property
     - HubSpot Data Type
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

