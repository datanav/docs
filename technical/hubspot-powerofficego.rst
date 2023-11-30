====================
HubSpot to  Dataflow
====================

Generated: 2023-11-30 00:01:11

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
     - "datetime-format","%Y-%m-%d","_."]
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
     - "datetime-format","%Y-%m-%d","_."]
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


HubSpot Account to  Currency
----------------------------
Every HubSpot Account will be synchronized with a  Currency.

If a matching  Currency already exists, the HubSpot Account will be merged with the existing one.
If no matching  Currency is found, a new  Currency will be created.

A HubSpot Account will merge with a  Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     -  Currency Property
   * - companyCurrency
     - code

Once a link between a HubSpot Account and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a  Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     -  Currency Property
     -  Data Type


HubSpot Deal to  Currency
-------------------------
Every HubSpot Deal will be synchronized with a  Currency.

If a matching  Currency already exists, the HubSpot Deal will be merged with the existing one.
If no matching  Currency is found, a new  Currency will be created.

A HubSpot Deal will merge with a  Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Currency Property
   * - properties.deal_currency_code
     - code

Once a link between a HubSpot Deal and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a  Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     -  Currency Property
     -  Data Type


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
     - "if", "is-decimal", "decimal", "integer"]
   * - properties.quantity
     - Quantity
     - "integer"


HubSpot Lineitemdealassociation to  Salesorderlines
---------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a  Salesorderlines.

Once a link between a HubSpot Lineitemdealassociation and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     -  Salesorderlines Property
     -  Data Type
   * - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - sesam_SalesOrderId
     - "string"
   * - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - sesam_SalesOrdersId
     - "string"


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

