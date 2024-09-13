==================================
HubSpot to PowerOffice GO Dataflow
==================================

Generated: 2024-09-13 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to PowerOffice GO Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into PowerOffice GO.

A HubSpot Contact will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOffice GO Contactperson Property
   * - properties.email
     - emailAddress

Once a link between a HubSpot Contact and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
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


HubSpot Contact to PowerOffice GO Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOffice GO Customers person must be established.

A new PowerOffice GO Customers person will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOffice GO.

A HubSpot Contact will merge with a PowerOffice GO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOffice GO Customers person Property
   * - properties.email
     - EmailAddress

Once a link between a HubSpot Contact and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type
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


HubSpot Company to PowerOffice GO Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into PowerOffice GO.

Once a link between a HubSpot Company and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type


HubSpot Company to PowerOfficeGo Customers
------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOfficeGo.

Once a link between a HubSpot Company and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
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


HubSpot Company to PowerOfficeGo Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOfficeGo.

Once a link between a HubSpot Company and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - properties.country
     - MailAddress.CountryCode
     - "string"
   * - properties.industry
     - MailAddress.CountryCode
     - "string"
   * - properties.type
     - MailAddress.CountryCode
     - "string"


HubSpot Contact to PowerOfficeGo Customers
------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOfficeGo.

Once a link between a HubSpot Contact and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - properties.country
     - MailAddress.CountryCode
     - "string"


HubSpot Deal to PowerOffice GO Salesorders
------------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOffice GO Salesorders.

Once a link between a HubSpot Deal and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
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


HubSpot Lineitem to PowerOffice GO Salesorderlines
--------------------------------------------------
Every HubSpot Lineitem will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a HubSpot Lineitem and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type
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


HubSpot Product to PowerOffice GO Product
-----------------------------------------
Every HubSpot Product will be synchronized with a PowerOffice GO Product.

Once a link between a HubSpot Product and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
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

