==============================
HubSpot to Salesforce Dataflow
==============================

Generated: 2024-09-12 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to Salesforce Division
--------------------------------------
Every HubSpot Company will be synchronized with a Salesforce Division.

Once a link between a HubSpot Company and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - properties.name
     - Name
     - "string"


HubSpot Contactcompanyassociationtype to Salesforce Currencytype
----------------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Contactcompanyassociationtype and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


HubSpot Deal to Salesforce Invoice
----------------------------------
Every HubSpot Deal will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Deal and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - properties.amount
     - TotalAmount
     - "string"
   * - properties.closedate
     - FullSettlementDate
     - "string"
   * - properties.deal_currency_code
     - CurrencyIsoCode
     - "string"
   * - properties.description
     - Description
     - "string"


HubSpot Dealcompanyassociation to Salesforce Invoice
----------------------------------------------------
Every HubSpot Dealcompanyassociation will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Dealcompanyassociation and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociation and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociation Property
     - Salesforce Invoice Property
     - Salesforce Data Type


HubSpot Dealcompanyassociationtype to Salesforce Currencytype
-------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Dealcompanyassociationtype and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


HubSpot Dealcontactassociation to Salesforce Invoice
----------------------------------------------------
Every HubSpot Dealcontactassociation will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Dealcontactassociation and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociation and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociation Property
     - Salesforce Invoice Property
     - Salesforce Data Type


HubSpot Dealcontactassociationtype to Salesforce Currencytype
-------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Dealcontactassociationtype and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


HubSpot Lineitem to Salesforce Invoice
--------------------------------------
Every HubSpot Lineitem will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Lineitem and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Salesforce Invoice Property
     - Salesforce Data Type


HubSpot Lineitemdealassociation to Salesforce Invoice
-----------------------------------------------------
Every HubSpot Lineitemdealassociation will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Lineitemdealassociation and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociation and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociation Property
     - Salesforce Invoice Property
     - Salesforce Data Type


HubSpot Lineitemdealassociationtype to Salesforce Currencytype
--------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Lineitemdealassociationtype and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


HubSpot Lineitemquoteassociation to Salesforce Invoice
------------------------------------------------------
Every HubSpot Lineitemquoteassociation will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Lineitemquoteassociation and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociation and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociation Property
     - Salesforce Invoice Property
     - Salesforce Data Type


HubSpot Lineitemquoteassociationtype to Salesforce Currencytype
---------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Lineitemquoteassociationtype and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


HubSpot Quote to Salesforce Invoice
-----------------------------------
Every HubSpot Quote will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Quote and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - properties.hs_quote_amount
     - TotalAmount
     - "string"


HubSpot Quotecompanyassociation to Salesforce Invoice
-----------------------------------------------------
Every HubSpot Quotecompanyassociation will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Quotecompanyassociation and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociation and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociation Property
     - Salesforce Invoice Property
     - Salesforce Data Type


HubSpot Quotecompanyassociationtype to Salesforce Currencytype
--------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Quotecompanyassociationtype and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


HubSpot Quotecontactassociation to Salesforce Invoice
-----------------------------------------------------
Every HubSpot Quotecontactassociation will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Quotecontactassociation and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociation and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociation Property
     - Salesforce Invoice Property
     - Salesforce Data Type


HubSpot Quotecontactassociationtype to Salesforce Currencytype
--------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Quotecontactassociationtype and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


HubSpot Quotedealassociation to Salesforce Invoice
--------------------------------------------------
Every HubSpot Quotedealassociation will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Quotedealassociation and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociation and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociation Property
     - Salesforce Invoice Property
     - Salesforce Data Type


HubSpot Quotedealassociationtype to Salesforce Currencytype
-----------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Quotedealassociationtype and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


HubSpot Quotequotetemplateassociation to Salesforce Invoice
-----------------------------------------------------------
Every HubSpot Quotequotetemplateassociation will be synchronized with a Salesforce Invoice.

Once a link between a HubSpot Quotequotetemplateassociation and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociation and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociation Property
     - Salesforce Invoice Property
     - Salesforce Data Type


HubSpot Quotequotetemplateassociationtype to Salesforce Currencytype
--------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


HubSpot Account to Salesforce Currencytype
------------------------------------------
Every HubSpot Account will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Account and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - accountType
     - IsoCode
     - "string"


HubSpot Deal to Salesforce Currencytype
---------------------------------------
Every HubSpot Deal will be synchronized with a Salesforce Currencytype.

Once a link between a HubSpot Deal and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Salesforce Currencytype Property
     - Salesforce Data Type
   * - properties.deal_currency_code
     - IsoCode
     - "string"


HubSpot Deal to Salesforce Order
--------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Salesforce Order.

Once a link between a HubSpot Deal and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - properties.amount
     - TotalAmount
     - "string"
   * - properties.closedate
     - EffectiveDate
     - "string"
   * - properties.closedate
     - EndDate
     - "string"
   * - properties.closedate
     - OrderedDate
     - "string"
   * - properties.deal_currency_code
     - CurrencyIsoCode
     - "string"
   * - properties.dealname
     - Name
     - "string"
   * - properties.description
     - Description
     - "string"


HubSpot Lineitem to Salesforce Invoiceline
------------------------------------------
Every HubSpot Lineitem will be synchronized with a Salesforce Invoiceline.

Once a link between a HubSpot Lineitem and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.price
     - UnitPrice
     - "string"
   * - properties.quantity
     - Quantity
     - "string"


HubSpot Lineitem to Salesforce Orderitem
----------------------------------------
Every HubSpot Lineitem will be synchronized with a Salesforce Orderitem.

Once a link between a HubSpot Lineitem and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - properties.price
     - TotalPrice
     - "string"
   * - properties.quantity
     - Quantity
     - "string"


HubSpot Lineitem to Salesforce Quotelineitem
--------------------------------------------
Every HubSpot Lineitem will be synchronized with a Salesforce Quotelineitem.

Once a link between a HubSpot Lineitem and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.hs_discount_percentage
     - Discount
     - "string"
   * - properties.price
     - TotalPriceWithTax
     - "string"
   * - properties.quantity
     - Quantity
     - "string"


HubSpot Product to Salesforce Product2
--------------------------------------
Every HubSpot Product will be synchronized with a Salesforce Product2.

Once a link between a HubSpot Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - properties.description
     - Description
     - "string"
   * - properties.description
     - Description	
     - "string"
   * - properties.name
     - Name
     - "string"
   * - properties.name
     - Name	
     - "string"


HubSpot Quote to Salesforce Quote
---------------------------------
Every HubSpot Quote will be synchronized with a Salesforce Quote.

Once a link between a HubSpot Quote and a Salesforce Quote is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Salesforce Quote:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Salesforce Quote Property
     - Salesforce Data Type
   * - properties.hs_quote_amount
     - TotalPriceWithTax
     - "string"
   * - properties.hs_title
     - Name
     - "string"

