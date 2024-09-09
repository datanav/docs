==============================
Webcrm to Businessnxt Dataflow
==============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Opportunities to Businessnxt Order
-----------------------------------------
Every Webcrm Opportunities will be synchronized with a Businessnxt Order.

Once a link between a Webcrm Opportunities and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Opportunities and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Webcrm Opportunities Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - OpportunityDiscount
     - totalDiscountAmountInCurrency
     - "string"


Webcrm Organisations to Businessnxt Address
-------------------------------------------
Every Webcrm Organisations will be synchronized with a Businessnxt Address.

Once a link between a Webcrm Organisations and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - OrganisationName
     - name
     - "string"
   * - OrganisationTelephone
     - phone
     - "string"


Webcrm Quotationline to Businessnxt Order
-----------------------------------------
Every Webcrm Quotationline will be synchronized with a Businessnxt Order.

Once a link between a Webcrm Quotationline and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Quotationline and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Webcrm Quotationline Property
     - Businessnxt Order Property
     - Businessnxt Data Type


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

