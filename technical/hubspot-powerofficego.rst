==================================
HubSpot to PowerOffice GO Dataflow
==================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to PowerOffice Contactperson
--------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOffice Contactperson must be established.

A new PowerOffice Contactperson will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into PowerOffice.

A HubSpot Contact will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOffice Contactperson Property
   * - properties.email
     - emailAddress

Once a link between a HubSpot Contact and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - id
     - id
     - "integer"
   * - properties.address
     - address1
     - "string"
   * - properties.city
     - city
     - "string"
   * - properties.country
     - residenceCountryCode
     - "string"
   * - properties.date_of_birth
     - dateOfBirth
     - N/A
   * - properties.email
     - emailAddress
     - "string"
   * - properties.firstname
     - firstName
     - "string"
   * - properties.lastname
     - lastName
     - "string"
   * - properties.phone
     - phoneNumber
     - "string"
   * - properties.zip
     - zipCode
     - "string"


HubSpot Contact to PowerOffice Customers person
-----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOffice Customers person must be established.

A new PowerOffice Customers person will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOffice.

A HubSpot Contact will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOffice Customers person Property
   * - properties.email
     - EmailAddress

Once a link between a HubSpot Contact and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
   * - id
     - Id
     - "integer"
   * - properties.address
     - MailAddress.AddressLine1
     - "string"
   * - properties.city
     - MailAddress.City
     - "string"
   * - properties.country
     - MailAddress.CountryCode
     - "string"
   * - properties.date_of_birth
     - DateOfBirth
     - N/A
   * - properties.email
     - EmailAddress
     - "string"
   * - properties.firstname
     - FirstName
     - "string"
   * - properties.lastname
     - LastName
     - "string"
   * - properties.phone
     - PhoneNumber
     - "string"
   * - properties.zip
     - MailAddress.ZipCode
     - "string"


HubSpot Company to Powerofficego Contactperson
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Powerofficego Contactperson must be established.

A new Powerofficego Contactperson will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into Powerofficego.

Once a link between a HubSpot Company and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type


HubSpot Company to Powerofficego Customers
------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Powerofficego Customers must be established.

A new Powerofficego Customers will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Powerofficego.

Once a link between a HubSpot Company and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
   * - id
     - Id
     - "integer"
   * - properties.address
     - MailAddress.AddressLine1
     - "string"
   * - properties.address2
     - MailAddress.AddressLine2
     - "string"
   * - properties.city
     - MailAddress.City
     - "string"
   * - properties.country
     - MailAddress.CountryCode
     - "string"
   * - properties.country
     - MailAddress.countryCode
     - "string"
   * - properties.industry
     - MailAddress.CountryCode
     - "string"
   * - properties.industry
     - MailAddress.countryCode
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.phone
     - Number
     - "string"
   * - properties.phone
     - PhoneNumber
     - "string"
   * - properties.sesam_org_number_no
     - OrganizationNumber (Dependant on having NO in MailAddress.CountryCode)
     - "string"
   * - properties.sesam_org_number_se
     - OrganizationNumber (Dependant on having SE in MailAddress.CountryCode)
     - "string"
   * - properties.type
     - MailAddress.CountryCode
     - "string"
   * - properties.type
     - MailAddress.countryCode
     - "string"
   * - properties.website
     - WebsiteUrl
     - "string"
   * - properties.zip
     - MailAddress.ZipCode
     - "string"


HubSpot Company to Powerofficego Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a Powerofficego Customers person must be established.

A new Powerofficego Customers person will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Powerofficego.

Once a link between a HubSpot Company and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
   * - properties.country
     - MailAddress.CountryCode
     - "string"
   * - properties.industry
     - MailAddress.CountryCode
     - "string"
   * - properties.type
     - MailAddress.CountryCode
     - "string"


HubSpot Contact to Powerofficego Customers
------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Powerofficego Customers must be established.

A new Powerofficego Customers will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into Powerofficego.

Once a link between a HubSpot Contact and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
   * - properties.country
     - MailAddress.CountryCode
     - "string"


HubSpot Deal to PowerOffice Salesorders
---------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOffice Salesorders.

Once a link between a HubSpot Deal and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
   * - properties.amount
     - NetAmount
     - "string"
   * - properties.amount
     - TotalAmount
     - "string"
   * - properties.closedate
     - OrderDate
     - "string"
   * - properties.closedate
     - SalesOrderDate
     - "string"
   * - properties.createdate
     - CreatedDateTimeOffset
     - "string"
   * - properties.deal_currency_code
     - CurrencyCode
     - "string"


HubSpot Lineitem to PowerOffice Salesorderlines
-----------------------------------------------
Every HubSpot Lineitem will be synchronized with a PowerOffice Salesorderlines.

Once a link between a HubSpot Lineitem and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
   * - properties.hs_discount_percentage
     - Allowance
     - "float"
   * - properties.hs_product_id
     - ProductCode
     - "string"
   * - properties.hs_product_id
     - ProductId
     - "integer"
   * - properties.name
     - Description
     - "string"
   * - properties.price
     - ProductUnitPrice
     - N/A
   * - properties.quantity
     - Quantity
     - N/A


HubSpot Product to PowerOffice Product
--------------------------------------
Every HubSpot Product will be synchronized with a PowerOffice Product.

Once a link between a HubSpot Product and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.description
     - description
     - "string"
   * - properties.hs_cost_of_goods_sold
     - CostPrice
     - "string"
   * - properties.hs_cost_of_goods_sold
     - costPrice
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.name
     - name
     - "string"
   * - properties.price
     - SalesPrice
     - "string"
   * - properties.price
     - salesPrice
     - "string"

