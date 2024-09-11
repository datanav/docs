=================================
HubSpot to PowerOfficeGO Dataflow
=================================

Generated: 2024-09-11 11:28:31

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to PowerOfficeGO Contactperson
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGO Contactperson must be established.

A new PowerOfficeGO Contactperson will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into PowerOfficeGO.

A HubSpot Contact will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGO Contactperson Property
   * - properties.email
     - emailAddress

Once a link between a HubSpot Contact and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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


HubSpot Contact to PowerOfficeGO Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGO Customers person must be established.

A new PowerOfficeGO Customers person will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOfficeGO.

A HubSpot Contact will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGO Customers person Property
   * - properties.email
     - EmailAddress

Once a link between a HubSpot Contact and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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


HubSpot Company to PowerOfficeGO Contactperson
----------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a PowerOfficeGO Contactperson must be established.

A new PowerOfficeGO Contactperson will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into PowerOfficeGO.

Once a link between a HubSpot Company and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type


HubSpot Company to PowerOfficeGO Customers
------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a PowerOfficeGO Customers must be established.

A new PowerOfficeGO Customers will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOfficeGO.

Once a link between a HubSpot Company and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
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


HubSpot Company to PowerOfficeGO Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a PowerOfficeGO Customers person must be established.

A new PowerOfficeGO Customers person will be created from a HubSpot Company if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOfficeGO.

Once a link between a HubSpot Company and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
   * - properties.country
     - MailAddress.CountryCode
     - "string"
   * - properties.industry
     - MailAddress.CountryCode
     - "string"
   * - properties.type
     - MailAddress.CountryCode
     - "string"


HubSpot Contact to PowerOfficeGO Customers
------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGO Customers must be established.

A new PowerOfficeGO Customers will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOfficeGO.

Once a link between a HubSpot Contact and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
   * - properties.country
     - MailAddress.CountryCode
     - "string"


HubSpot Deal to PowerOfficeGO Salesorders
-----------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOfficeGO Salesorders.

Once a link between a HubSpot Deal and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
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


HubSpot Lineitem to PowerOfficeGO Salesorderlines
-------------------------------------------------
Every HubSpot Lineitem will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a HubSpot Lineitem and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
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


HubSpot Product to PowerOfficeGO Product
----------------------------------------
Every HubSpot Product will be synchronized with a PowerOfficeGO Product.

Once a link between a HubSpot Product and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
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

