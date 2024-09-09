=================================
Wave Financial to Webcrm Dataflow
=================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Webcrm. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Webcrm Organisations
-------------------------------------
Every Wave Customer will be synchronized with a Webcrm Organisations.

Once a link between a Wave Customer and a Webcrm Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Webcrm Organisations:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Webcrm Organisations Property
     - Webcrm Data Type
   * - address.addressLine1
     - OrganisationAddress
     - "string"
   * - address.addressLine1
     - OrganisationDeliveryAddress
     - "string"
   * - address.city
     - OrganisationCity
     - "string"
   * - address.city
     - OrganisationDeliveryCity
     - "string"
   * - address.postalCode
     - OrganisationDeliveryPostCode
     - "string"
   * - address.postalCode
     - OrganisationPostCode
     - "string"
   * - address.province.code
     - OrganisationDeliveryState
     - "string"
   * - id
     - OrganisationId
     - "string"
   * - internalNotes
     - OrganisationCompanyDescription
     - "string"
   * - name
     - OrganisationName
     - "string"
   * - phone
     - OrganisationTelephone
     - "string"
   * - shippingDetails.address.addressLine1
     - OrganisationAddress
     - "string"
   * - shippingDetails.address.addressLine1
     - OrganisationDeliveryAddress
     - "string"
   * - shippingDetails.address.city
     - OrganisationCity
     - "string"
   * - shippingDetails.address.city
     - OrganisationDeliveryCity
     - "string"
   * - shippingDetails.address.postalCode
     - OrganisationDeliveryPostCode
     - "string"
   * - shippingDetails.address.postalCode
     - OrganisationPostCode
     - "string"
   * - shippingDetails.address.province.code
     - OrganisationDeliveryState
     - "string"
   * - shippingDetails.phone
     - OrganisationTelephone
     - "string"


Wave Customer to Webcrm Persons
-------------------------------
Every Wave Customer will be synchronized with a Webcrm Persons.

Once a link between a Wave Customer and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Webcrm Persons Property
     - Webcrm Data Type
   * - firstName
     - PersonFirstName
     - "string"
   * - id
     - PersonOrganisationId
     - "string"
   * - lastName
     - PersonLastName
     - "string"
   * - mobile
     - PersonMobilePhone
     - "string"


Wave Invoice to Webcrm Quotationline
------------------------------------
Every Wave Invoice will be synchronized with a Webcrm Quotationline.

Once a link between a Wave Invoice and a Webcrm Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a Webcrm Quotationline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - Webcrm Quotationline Property
     - Webcrm Data Type
   * - id
     - QuotationLineOpportunityId
     - "string"
   * - items.price
     - QuotationLinePrice
     - "string"
   * - items.quantity
     - QuotationLineQuantity
     - "string"


Wave Product to Webcrm Products
-------------------------------
Every Wave Product will be synchronized with a Webcrm Products.

Once a link between a Wave Product and a Webcrm Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Webcrm Products:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Webcrm Products Property
     - Webcrm Data Type
   * - unitPrice
     - ProductPrice
     - "string"


Wave User to Webcrm Users
-------------------------
Every Wave User will be synchronized with a Webcrm Users.

Once a link between a Wave User and a Webcrm Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave User and a Webcrm Users:

.. list-table::
   :header-rows: 1

   * - Wave User Property
     - Webcrm Users Property
     - Webcrm Data Type


Wave Vendor to Webcrm Persons
-----------------------------
Every Wave Vendor will be synchronized with a Webcrm Persons.

Once a link between a Wave Vendor and a Webcrm Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Webcrm Persons:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Webcrm Persons Property
     - Webcrm Data Type
   * - firstName
     - PersonFirstName
     - "string"
   * - id
     - PersonOrganisationId
     - "string"
   * - lastName
     - PersonLastName
     - "string"
   * - mobile
     - PersonMobilePhone
     - "string"
   * - phone
     - PersonDirectPhone
     - "string"

