====================
HubSpot to  Dataflow
====================

Generated: 2024-03-26 00:00:20

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to  Contactperson
---------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Contactperson must be established.

A new  Contactperson will be created from a HubSpot Contact if it is connected to a HubSpot Deal that is synchronized into .

A HubSpot Contact will merge with a  Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Contactperson Property
   * - properties.email
     - emailAddress

Once a link between a HubSpot Contact and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Contactperson Property
     -  Data Type
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
     - "if","gt","abs","datetime-diff", "year", "_.","now"]]], 100], "1935-01-01","datetime-format", "%Y-%m-%d"]
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


HubSpot Company to  Contactperson
---------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a  Contactperson must be established.

A new  Contactperson will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into .

Once a link between a HubSpot Company and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Contactperson Property
     -  Data Type


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


HubSpot Contact to PowerOfficeGo Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a HubSpot Contact if it is connected to a HubSpot Deal, Quote, Lineitem, Quotedealassociation, Dealcompanyassociation, Dealcontactassociation, Lineitemdealassociation, Quotecompanyassociation, Quotecontactassociation, Lineitemquoteassociation, Ticketcompanyassociation, or Quotequotetemplateassociation that is synchronized into PowerOfficeGo.

Once a link between a HubSpot Contact and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
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
     - "if","gt","abs","datetime-diff", "year", "_.","now"]]], 100], "1935-01-01","datetime-format", "%Y-%m-%d"]
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


HubSpot Deal to  Salesorders
----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a  Salesorders.

Once a link between a HubSpot Deal and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Salesorders Property
     -  Data Type
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


HubSpot Lineitem to  Salesorderlines
------------------------------------
Every HubSpot Lineitem will be synchronized with a  Salesorderlines.

Once a link between a HubSpot Lineitem and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     -  Salesorderlines Property
     -  Data Type
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
     - "if", "is-decimal", "decimal", "float", "decimal"]]
   * - properties.quantity
     - Quantity
     - "integer", "decimal"]


HubSpot Product to  Product
---------------------------
Every HubSpot Product will be synchronized with a  Product.

Once a link between a HubSpot Product and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a  Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     -  Product Property
     -  Data Type
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

