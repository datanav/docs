============================
WebCRM to Tripletex Dataflow
============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Organisations to Tripletex Country
-----------------------------------------
Every WebCRM Organisations will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the WebCRM Organisations will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A WebCRM Organisations will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Tripletex Country Property
   * - OrganisationCountryData.CodeISO
     - isoAlpha2Code

Once a link between a WebCRM Organisations and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - Tripletex Country Property
     - Tripletex Data Type


WebCRM Persons to Tripletex Contact
-----------------------------------
Every WebCRM Persons will be synchronized with a Tripletex Contact.

Once a link between a WebCRM Persons and a Tripletex Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a Tripletex Contact:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - Tripletex Contact Property
     - Tripletex Data Type
   * - PersonDirectPhone
     - phoneNumberWork
     - "string"
   * - PersonFirstName
     - firstName
     - "string"
   * - PersonLastName
     - lastName
     - "string"
   * - PersonMobilePhone
     - phoneNumberMobile
     - N/A
   * - PersonOrganisationId
     - customer.id
     - "integer"


WebCRM Products to Tripletex Product
------------------------------------
Every WebCRM Products will be synchronized with a Tripletex Product.

Once a link between a WebCRM Products and a Tripletex Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a Tripletex Product:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - Tripletex Product Property
     - Tripletex Data Type
   * - ProductCostPrice
     - costExcludingVatCurrency
     - "float"
   * - ProductPrice
     - priceExcludingVatCurrency
     - "float"
   * - ProductQuantity
     - stockOfGoods
     - "integer"
   * - ProductVatCode
     - vatType.id
     - "integer"


WebCRM Quotationline to Tripletex Orderline
-------------------------------------------
Every WebCRM Quotationline will be synchronized with a Tripletex Orderline.

Once a link between a WebCRM Quotationline and a Tripletex Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Quotationline and a Tripletex Orderline:

.. list-table::
   :header-rows: 1

   * - WebCRM Quotationline Property
     - Tripletex Orderline Property
     - Tripletex Data Type

