==============================
HubSpot to Salesforce Dataflow
==============================

Generated: 2024-09-25 00:34:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


HubSpot Lineitemdealassociationtype to Salesforce Invoiceline
-------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Salesforce Invoiceline.

Once a link between a HubSpot Lineitemdealassociationtype and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type


HubSpot Lineitemdealassociationtype to Salesforce Orderitem
-----------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Salesforce Orderitem.

Once a link between a HubSpot Lineitemdealassociationtype and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Salesforce Orderitem Property
     - Salesforce Data Type


HubSpot Lineitemdealassociationtype to Salesforce Quotelineitem
---------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Salesforce Quotelineitem.

Once a link between a HubSpot Lineitemdealassociationtype and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type


HubSpot Lineitemquoteassociationtype to Salesforce Invoiceline
--------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Salesforce Invoiceline.

Once a link between a HubSpot Lineitemquoteassociationtype and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type


HubSpot Lineitemquoteassociationtype to Salesforce Orderitem
------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Salesforce Orderitem.

Once a link between a HubSpot Lineitemquoteassociationtype and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Salesforce Orderitem Property
     - Salesforce Data Type


HubSpot Lineitemquoteassociationtype to Salesforce Quotelineitem
----------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Salesforce Quotelineitem.

Once a link between a HubSpot Lineitemquoteassociationtype and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type


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

