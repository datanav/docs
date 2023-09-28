=================================
HubSpot to PowerOfficeGo Dataflow
=================================

Generated: 2023-09-28 09:17:28

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to PowerOfficeGo Customers
------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into PowerOfficeGo.

Once a link between a HubSpot Company and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
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


HubSpot Company to PowerOfficeGo Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a HubSpot Company and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a HubSpot Company if it is connected to a HubSpot Deal that is synchronized into PowerOfficeGo.

Once a link between a HubSpot Company and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type


HubSpot Deal to PowerOfficeGo Outgoinginvoices
----------------------------------------------
Every HubSpot Deal will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Deal and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - properties.amount
     - NetAmount
     - "string"
   * - properties.closedate
     - DeliveryDate
     - "string"
   * - properties.closedate
     - OrderDate
     - "string"
   * - properties.closedate
     - sentDateTimeOffset
     - "string"
   * - properties.createdate
     - createdDateTimeOffset
     - "string"
   * - properties.deal_currency_code
     - CurrencyCode
     - "string"


HubSpot Dealcompanyassociation to PowerOfficeGo Outgoinginvoices
----------------------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Dealcompanyassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customerId
     - "string"


HubSpot Dealcontactassociation to PowerOfficeGo Outgoinginvoices
----------------------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Dealcontactassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customerId
     - "string"


HubSpot Lineitem to PowerOfficeGo Outgoinginvoices
--------------------------------------------------
Every HubSpot Lineitem will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Lineitem and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - properties.createdate
     - createdDateTimeOffset
     - "string"


HubSpot Lineitemdealassociation to PowerOfficeGo Outgoinginvoices
-----------------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Lineitemdealassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - OrderNo
     - "string"


HubSpot Lineitemquoteassociation to PowerOfficeGo Outgoinginvoices
------------------------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Lineitemquoteassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - OrderNo
     - "string"


HubSpot Quote to PowerOfficeGo Outgoinginvoices
-----------------------------------------------
Every HubSpot Quote will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Quote and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - associations.companies.results.id
     - customerId
     - "string"
   * - createdAt
     - createdDateTimeOffset
     - "string"
   * - properties.hs_quote_amount
     - NetAmount
     - "string"


HubSpot Quotecompanyassociation to PowerOfficeGo Outgoinginvoices
-----------------------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Quotecompanyassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customerId
     - "string"


HubSpot Quotecontactassociation to PowerOfficeGo Outgoinginvoices
-----------------------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Quotecontactassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customerId
     - "string"


HubSpot Quotedealassociation to PowerOfficeGo Outgoinginvoices
--------------------------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Quotedealassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - OrderNo
     - "string"


HubSpot Quotequotetemplateassociation to PowerOfficeGo Outgoinginvoices
-----------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Quotequotetemplateassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypesDependant on having wd:Q566889 in sesam_simpleAssociationTypes)
     - OrderNo
     - "string"


HubSpot Ticketcompanyassociation to PowerOfficeGo Outgoinginvoices
------------------------------------------------------------------
Every HubSpot Ticketcompanyassociation will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a HubSpot Ticketcompanyassociation and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociation and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociation Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - toObjectId (Dependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypesDependant on having wd:Q852835 in sesam_simpleAssociationTypes)
     - customerId
     - "string"


HubSpot Account to PowerOfficeGo Currency
-----------------------------------------
Every HubSpot Account will be synchronized with a PowerOfficeGo Currency.

If a matching PowerOfficeGo Currency already exists, the HubSpot Account will be merged with the existing one.
If no matching PowerOfficeGo Currency is found, a new PowerOfficeGo Currency will be created.

A HubSpot Account will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - PowerOfficeGo Currency Property
   * - companyCurrency
     - Code

Once a link between a HubSpot Account and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


HubSpot Contact to PowerOfficeGo Location
-----------------------------------------
Every HubSpot Contact will be synchronized with a PowerOfficeGo Location.

Once a link between a HubSpot Contact and a PowerOfficeGo Location is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a PowerOfficeGo Location:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - PowerOfficeGo Location Property
     - PowerOfficeGo Data Type
   * - properties.address
     - address1
     - "string"
   * - properties.city
     - city
     - "string"
   * - properties.country
     - countryCode
     - "string"
   * - properties.zip
     - zipCode
     - "string"


HubSpot Deal to PowerOfficeGo Currency
--------------------------------------
Every HubSpot Deal will be synchronized with a PowerOfficeGo Currency.

If a matching PowerOfficeGo Currency already exists, the HubSpot Deal will be merged with the existing one.
If no matching PowerOfficeGo Currency is found, a new PowerOfficeGo Currency will be created.

A HubSpot Deal will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGo Currency Property
   * - properties.deal_currency_code
     - Code

Once a link between a HubSpot Deal and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


HubSpot Deal to PowerOfficeGo Salesorders
-----------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a PowerOfficeGo Salesorders.

Once a link between a HubSpot Deal and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type
   * - properties.amount
     - NetAmount
     - "string"
   * - properties.amount
     - TotalAmount
     - "string"
   * - properties.closedate
     - OrderDate
     - "string"
   * - properties.createdate
     - CreatedDateTimeOffset
     - "string"
   * - properties.deal_currency_code
     - CurrencyCode
     - "string"


HubSpot Lineitemdealassociation to PowerOfficeGo Salesorderline
---------------------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a PowerOfficeGo Salesorderline.

Once a link between a HubSpot Lineitemdealassociation and a PowerOfficeGo Salesorderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a PowerOfficeGo Salesorderline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - PowerOfficeGo Salesorderline Property
     - PowerOfficeGo Data Type


HubSpot Product to PowerOfficeGo Product
----------------------------------------
Every HubSpot Product will be synchronized with a PowerOfficeGo Product.

Once a link between a HubSpot Product and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type
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

