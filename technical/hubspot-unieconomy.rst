==============================
HubSpot to Unieconomy Dataflow
==============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Unieconomy Countries
---------------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Unieconomy Countries must be established.

A HubSpot Contact will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Unieconomy Countries Property
   * - properties.country
     - Name

Once a link between a HubSpot Contact and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


HubSpot Account to Unieconomy Currencycodes
-------------------------------------------
Every HubSpot Account will be synchronized with a Unieconomy Currencycodes.

If a matching Unieconomy Currencycodes already exists, the HubSpot Account will be merged with the existing one.
If no matching Unieconomy Currencycodes is found, a new Unieconomy Currencycodes will be created.

A HubSpot Account will merge with a Unieconomy Currencycodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Unieconomy Currencycodes Property
   * - companyCurrency
     - Code

Once a link between a HubSpot Account and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Account and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - HubSpot Account Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type


HubSpot Company to Unieconomy Countries
---------------------------------------
Every HubSpot Company will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the HubSpot Company will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A HubSpot Company will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Unieconomy Countries Property
   * - properties.country
     - Name

Once a link between a HubSpot Company and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


HubSpot Deal to Unieconomy Currencycodes
----------------------------------------
Every HubSpot Deal will be synchronized with a Unieconomy Currencycodes.

If a matching Unieconomy Currencycodes already exists, the HubSpot Deal will be merged with the existing one.
If no matching Unieconomy Currencycodes is found, a new Unieconomy Currencycodes will be created.

A HubSpot Deal will merge with a Unieconomy Currencycodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Unieconomy Currencycodes Property
   * - properties.deal_currency_code
     - Code

Once a link between a HubSpot Deal and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type


HubSpot Dealcompanyassociationtype to Unieconomy Dimensions
-----------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Unieconomy Dimensions.

Once a link between a HubSpot Dealcompanyassociationtype and a Unieconomy Dimensions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Unieconomy Dimensions:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Unieconomy Dimensions Property
     - Unieconomy Data Type


HubSpot Dealcontactassociationtype to Unieconomy Dimensions
-----------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Unieconomy Dimensions.

Once a link between a HubSpot Dealcontactassociationtype and a Unieconomy Dimensions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Unieconomy Dimensions:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Unieconomy Dimensions Property
     - Unieconomy Data Type


HubSpot Quotecompanyassociationtype to Unieconomy Dimensions
------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Unieconomy Dimensions.

Once a link between a HubSpot Quotecompanyassociationtype and a Unieconomy Dimensions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Unieconomy Dimensions:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Unieconomy Dimensions Property
     - Unieconomy Data Type


HubSpot Quotecontactassociationtype to Unieconomy Dimensions
------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Unieconomy Dimensions.

Once a link between a HubSpot Quotecontactassociationtype and a Unieconomy Dimensions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Unieconomy Dimensions:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Unieconomy Dimensions Property
     - Unieconomy Data Type


HubSpot Quotedealassociationtype to Unieconomy Dimensions
---------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Unieconomy Dimensions.

Once a link between a HubSpot Quotedealassociationtype and a Unieconomy Dimensions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Unieconomy Dimensions:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Unieconomy Dimensions Property
     - Unieconomy Data Type


HubSpot Quotequotetemplateassociationtype to Unieconomy Dimensions
------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Unieconomy Dimensions.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Unieconomy Dimensions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Unieconomy Dimensions:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Unieconomy Dimensions Property
     - Unieconomy Data Type


HubSpot Ticketcompanyassociationtype to Unieconomy Dimensions
-------------------------------------------------------------
Every HubSpot Ticketcompanyassociationtype will be synchronized with a Unieconomy Dimensions.

Once a link between a HubSpot Ticketcompanyassociationtype and a Unieconomy Dimensions is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticketcompanyassociationtype and a Unieconomy Dimensions:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticketcompanyassociationtype Property
     - Unieconomy Dimensions Property
     - Unieconomy Data Type

