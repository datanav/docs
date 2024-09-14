===============================
WebCRM to Business Nxt Dataflow
===============================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Opportunities to Business Nxt Order
------------------------------------------
Every WebCRM Opportunities will be synchronized with a Business Nxt Order.

Once a link between a WebCRM Opportunities and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - OpportunityDiscount
     - totalDiscountAmountInCurrency
     - "string"


WebCRM Organisations to Business Nxt Address
--------------------------------------------
Every WebCRM Organisations will be synchronized with a Business Nxt Address.

Once a link between a WebCRM Organisations and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - OrganisationName
     - name
     - "string"
   * - OrganisationTelephone
     - phone
     - "string"


WebCRM Quotationline to Business Nxt Order
------------------------------------------
Every WebCRM Quotationline will be synchronized with a Business Nxt Order.

Once a link between a WebCRM Quotationline and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Business Nxt Order Property
     - Business Nxt Data Type


WebCRM Organisations to Business Nxt Country
--------------------------------------------
Every WebCRM Organisations will be synchronized with a Business Nxt Country.

Once a link between a WebCRM Organisations and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Business Nxt Country Property
     - Business Nxt Data Type
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


WebCRM Products to Business Nxt Product
---------------------------------------
Every WebCRM Products will be synchronized with a Business Nxt Product.

Once a link between a WebCRM Products and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - ProductPrice
     - priceQuantity
     - "string"
   * - ProductQuantity
     - quantityPerUnit
     - "string"


WebCRM Quotationline to Business Nxt Orderline
----------------------------------------------
Every WebCRM Quotationline will be synchronized with a Business Nxt Orderline.

Once a link between a WebCRM Quotationline and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type

