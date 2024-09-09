============================
Tripletex to Webcrm Dataflow
============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Webcrm Organisations
------------------------------------------
Every Tripletex Customer will be synchronized with a Webcrm Organisations.

Once a link between a Tripletex Customer and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Webcrm Organisations Property
     - Webcrm Data Type
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


Tripletex Department to Webcrm Organisations
--------------------------------------------
Every Tripletex Department will be synchronized with a Webcrm Organisations.

Once a link between a Tripletex Department and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - name
     - OrganisationName
     - "string"


Tripletex Contact to Webcrm Persons
-----------------------------------
Every Tripletex Contact will be synchronized with a Webcrm Persons.

Once a link between a Tripletex Contact and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     - Webcrm Persons Property
     - Webcrm Data Type
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


Tripletex Orderline to Webcrm Quotationline
-------------------------------------------
Every Tripletex Orderline will be synchronized with a Webcrm Quotationline.

Once a link between a Tripletex Orderline and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
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


Tripletex Product to Webcrm Products
------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Webcrm Products.

Once a link between a Tripletex Product and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Webcrm Products Property
     - Webcrm Data Type
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

