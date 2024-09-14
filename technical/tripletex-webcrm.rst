============================
Tripletex to WebCRM Dataflow
============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to WebCRM Organisations
------------------------------------------
Every Tripletex Customer will be synchronized with a WebCRM Organisations.

Once a link between a Tripletex Customer and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - deliveryAddress.addressLine1
     - OrganisationAddress
     - "string"
   * - deliveryAddress.addressLine1
     - OrganisationDeliveryAddress
     - "string"
   * - deliveryAddress.city
     - OrganisationCity
     - "string"
   * - deliveryAddress.city
     - OrganisationDeliveryCity
     - "string"
   * - deliveryAddress.postalCode
     - OrganisationDeliveryPostCode
     - "string"
   * - deliveryAddress.postalCode
     - OrganisationPostCode
     - "string"
   * - id
     - OrganisationId
     - "string"
   * - name
     - OrganisationName
     - "string"
   * - phoneNumber
     - OrganisationTelephone
     - "string"
   * - physicalAddress.addressLine1
     - OrganisationAddress
     - "string"
   * - physicalAddress.addressLine1
     - OrganisationDeliveryAddress
     - "string"
   * - physicalAddress.city
     - OrganisationCity
     - "string"
   * - physicalAddress.city
     - OrganisationDeliveryCity
     - "string"
   * - physicalAddress.postalCode
     - OrganisationDeliveryPostCode
     - "string"
   * - physicalAddress.postalCode
     - OrganisationPostCode
     - "string"
   * - postalAddress.addressLine1
     - OrganisationAddress
     - "string"
   * - postalAddress.addressLine1
     - OrganisationDeliveryAddress
     - "string"
   * - postalAddress.city
     - OrganisationCity
     - "string"
   * - postalAddress.city
     - OrganisationDeliveryCity
     - "string"
   * - postalAddress.postalCode
     - OrganisationDeliveryPostCode
     - "string"
   * - postalAddress.postalCode
     - OrganisationPostCode
     - "string"


Tripletex Department to WebCRM Organisations
--------------------------------------------
Every Tripletex Department will be synchronized with a WebCRM Organisations.

Once a link between a Tripletex Department and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - WebCRM Organisations Property
     - WebCRM Data Type
   * - name
     - OrganisationName
     - "string"


Tripletex Contact to WebCRM Persons
-----------------------------------
Every Tripletex Contact will be synchronized with a WebCRM Persons.

Once a link between a Tripletex Contact and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - customer.id
     - PersonOrganisationId
     - "string"
   * - firstName
     - PersonFirstName
     - "string"
   * - lastName
     - PersonLastName
     - "string"
   * - phoneNumberMobile
     - PersonMobilePhone
     - "string"
   * - phoneNumberWork
     - PersonDirectPhone
     - "string"


Tripletex Orderline to WebCRM Quotationline
-------------------------------------------
Every Tripletex Orderline will be synchronized with a WebCRM Quotationline.

Once a link between a Tripletex Orderline and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
   * - count
     - QuotationLineQuantity
     - "string"
   * - discount
     - QuotationLineDiscount
     - "string"
   * - order.id
     - QuotationLineOpportunityId
     - "string"
   * - unitCostCurrency
     - QuotationLineCostPrice
     - "string"
   * - unitPriceExcludingVatCurrency
     - QuotationLinePrice
     - "string"
   * - vatType.id
     - QuotationLineVatPercentage
     - "string"


Tripletex Product to WebCRM Products
------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a WebCRM Products.

Once a link between a Tripletex Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - costExcludingVatCurrency
     - ProductCostPrice
     - "string"
   * - priceExcludingVatCurrency
     - ProductPrice
     - "string"
   * - stockOfGoods
     - ProductQuantity
     - "string"
   * - vatType.id
     - ProductVatCode
     - "string"

