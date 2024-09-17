==================================
PowerOffice GO to HubSpot Dataflow
==================================

Generated: 2024-09-17 07:26:51

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


PowerOffice GO Contactperson to HubSpot Company
-----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a HubSpot Company must be established.

A new HubSpot Company will be created from a PowerOffice GO Contactperson if it is connected to a PowerOffice GO Powerofficego-quote that is synchronized into HubSpot.

Once a link between a PowerOffice GO Contactperson and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - HubSpot Company Property
     - HubSpot Data Type


PowerOffice GO Customers to HubSpot Company
-------------------------------------------
Every PowerOffice GO Customers will be synchronized with a HubSpot Company.

Once a link between a PowerOffice GO Customers and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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


PowerOffice GO Customers to HubSpot Contact
-------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers and a HubSpot Contact must be established.

A new HubSpot Contact will be created from a PowerOffice GO Customers if it is connected to a PowerOffice GO Powerofficego-quote that is synchronized into HubSpot.

Once a link between a PowerOffice GO Customers and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - MailAddress.CountryCode
     - properties.country
     - "string"


PowerOffice GO Product to HubSpot Product
-----------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Product and a HubSpot Product must be established.

A new HubSpot Product will be created from a PowerOffice GO Product if it is connected to a PowerOffice GO Powerofficego-salesorderlines that is synchronized into HubSpot.

Once a link between a PowerOffice GO Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - HubSpot Product Property
     - HubSpot Data Type


PowerOffice GO Departments to HubSpot Company
---------------------------------------------
Every PowerOffice GO Departments will be synchronized with a HubSpot Company.

Once a link between a PowerOffice GO Departments and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Name
     - properties.name
     - "string"


PowerOffice GO Employees to HubSpot Contact
-------------------------------------------
Every PowerOffice GO Employees will be synchronized with a HubSpot Contact.

Once a link between a PowerOffice GO Employees and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
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


PowerOffice GO Product to HubSpot Product
-----------------------------------------
Every PowerOffice GO Product will be synchronized with a HubSpot Product.

Once a link between a PowerOffice GO Product and a HubSpot Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Product and a HubSpot Product:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Product Property
     - HubSpot Product Property
     - HubSpot Data Type


PowerOffice GO Quote to HubSpot Quote
-------------------------------------
Every PowerOffice GO Quote will be synchronized with a HubSpot Quote.

Once a link between a PowerOffice GO Quote and a HubSpot Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Quote and a HubSpot Quote:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Quote Property
     - HubSpot Quote Property
     - HubSpot Data Type


PowerOffice GO Salesorderlines to HubSpot Lineitem
--------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a HubSpot Lineitem.

Once a link between a PowerOffice GO Salesorderlines and a HubSpot Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a HubSpot Lineitem:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - HubSpot Lineitem Property
     - HubSpot Data Type


PowerOffice GO Salesorderlines to HubSpot Lineitemdealassociationtype
---------------------------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a HubSpot Lineitemdealassociationtype.

Once a link between a PowerOffice GO Salesorderlines and a HubSpot Lineitemdealassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a HubSpot Lineitemdealassociationtype:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - HubSpot Lineitemdealassociationtype Property
     - HubSpot Data Type


PowerOffice GO Salesorderlines to HubSpot Lineitemquoteassociationtype
----------------------------------------------------------------------
Every PowerOffice GO Salesorderlines will be synchronized with a HubSpot Lineitemquoteassociationtype.

Once a link between a PowerOffice GO Salesorderlines and a HubSpot Lineitemquoteassociationtype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorderlines and a HubSpot Lineitemquoteassociationtype:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorderlines Property
     - HubSpot Lineitemquoteassociationtype Property
     - HubSpot Data Type


PowerOffice GO Salesorders to HubSpot Deal
------------------------------------------
Every PowerOffice GO Salesorders will be synchronized with a HubSpot Deal.

Once a link between a PowerOffice GO Salesorders and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Salesorders and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Salesorders Property
     - HubSpot Deal Property
     - HubSpot Data Type

