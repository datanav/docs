==============================
Webcrm to Businessnxt Dataflow
==============================

Generated: 2024-09-03 09:02:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Organisations to Businessnxt Country
-------------------------------------------
Every Webcrm Organisations will be synchronized with a Businessnxt Country.

Once a link between a Webcrm Organisations and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - OrganisationCountryData
     - isoCode
     - "string"
   * - OrganisationCountryData
     - name
     - "string"


Webcrm Products to Businessnxt Product
--------------------------------------
Every Webcrm Products will be synchronized with a Businessnxt Product.

Once a link between a Webcrm Products and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - ProductPrice
     - priceQuantity
     - "string"
   * - ProductQuantity
     - quantityPerUnit
     - "string"


Webcrm Quotationline to Businessnxt Orderline
---------------------------------------------
Every Webcrm Quotationline will be synchronized with a Businessnxt Orderline.

Once a link between a Webcrm Quotationline and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type

