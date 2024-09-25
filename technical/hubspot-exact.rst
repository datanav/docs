================================
HubSpot to Exact Online Dataflow
================================

Generated: 2024-09-25 00:34:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Exact Online. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Account to Exact Online Currencies
------------------------------------------
Every HubSpot Account will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Account and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - accountType
     - Code
     - "string"


HubSpot Contact to Exact Online Addresses
-----------------------------------------
Every HubSpot Contact will be synchronized with a Exact Online Addresses.

Once a link between a HubSpot Contact and a Exact Online Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Exact Online Addresses:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Exact Online Addresses Property
     - Exact Online Data Type
   * - properties.city
     - City
     - "string"
   * - properties.country
     - Country
     - "string"


HubSpot Deal to Exact Online Currencies
---------------------------------------
Every HubSpot Deal will be synchronized with a Exact Online Currencies.

Once a link between a HubSpot Deal and a Exact Online Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Exact Online Currencies:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Exact Online Currencies Property
     - Exact Online Data Type
   * - properties.deal_currency_code
     - Code
     - "string"


HubSpot Deal to Exact Online Salesorders
----------------------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Exact Online Salesorders.

Once a link between a HubSpot Deal and a Exact Online Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Exact Online Salesorders:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Exact Online Salesorders Property
     - Exact Online Data Type
   * - properties.deal_currency_code
     - Currency
     - "string"
   * - properties.description
     - Description
     - "string"


HubSpot Lineitem to Exact Online Salesorderlines
------------------------------------------------
Every HubSpot Lineitem will be synchronized with a Exact Online Salesorderlines.

Once a link between a HubSpot Lineitem and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitem and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitem Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type


HubSpot Lineitemdealassociationtype to Exact Online Salesorderlines
-------------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Exact Online Salesorderlines.

Once a link between a HubSpot Lineitemdealassociationtype and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type


HubSpot Lineitemquoteassociationtype to Exact Online Salesorderlines
--------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Exact Online Salesorderlines.

Once a link between a HubSpot Lineitemquoteassociationtype and a Exact Online Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Exact Online Salesorderlines:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Exact Online Salesorderlines Property
     - Exact Online Data Type


HubSpot Product to Exact Online Items
-------------------------------------
Every HubSpot Product will be synchronized with a Exact Online Items.

Once a link between a HubSpot Product and a Exact Online Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Exact Online Items:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Exact Online Items Property
     - Exact Online Data Type


HubSpot Quote to Exact Online Quotations
----------------------------------------
Every HubSpot Quote will be synchronized with a Exact Online Quotations.

Once a link between a HubSpot Quote and a Exact Online Quotations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quote and a Exact Online Quotations:

.. list-table::
   :header-rows: 1

   * - HubSpot Quote Property
     - Exact Online Quotations Property
     - Exact Online Data Type

