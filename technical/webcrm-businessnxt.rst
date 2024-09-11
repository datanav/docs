==============================
WebCRM to BusinessNxt Dataflow
==============================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Opportunities to BusinessNxt Order
-----------------------------------------
Every WebCRM Opportunities will be synchronized with a BusinessNxt Order.

Once a link between a WebCRM Opportunities and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - OpportunityDiscount
     - totalDiscountAmountInCurrency
     - "string"


WebCRM Organisations to BusinessNxt Address
-------------------------------------------
Every WebCRM Organisations will be synchronized with a BusinessNxt Address.

Once a link between a WebCRM Organisations and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
   * - OrganisationName
     - name
     - "string"
   * - OrganisationTelephone
     - phone
     - "string"


WebCRM Quotationline to BusinessNxt Order
-----------------------------------------
Every WebCRM Quotationline will be synchronized with a BusinessNxt Order.

Once a link between a WebCRM Quotationline and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type


WebCRM Organisations to BusinessNxt Country
-------------------------------------------
Every WebCRM Organisations will be synchronized with a BusinessNxt Country.

Once a link between a WebCRM Organisations and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - OrganisationCountryData
     - isoCode
     - "string"
   * - OrganisationCountryData
     - name
     - "string"
   * - OrganisationCountryData.CodeISO
     - isoCode
     - "string"
   * - OrganisationCountryData.Name
     - name
     - "string"


WebCRM Products to BusinessNxt Product
--------------------------------------
Every WebCRM Products will be synchronized with a BusinessNxt Product.

Once a link between a WebCRM Products and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
   * - ProductPrice
     - priceQuantity
     - "string"
   * - ProductQuantity
     - quantityPerUnit
     - "string"


WebCRM Quotationline to BusinessNxt Orderline
---------------------------------------------
Every WebCRM Quotationline will be synchronized with a BusinessNxt Orderline.

Once a link between a WebCRM Quotationline and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type

