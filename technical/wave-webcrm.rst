=======================
Wave to WebCRM Dataflow
=======================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to WebCRM Organisations
-------------------------------------
Every Wave Customer will be synchronized with a WebCRM Organisations.

Once a link between a Wave Customer and a WebCRM Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a WebCRM Organisations:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - WebCRM Organisations Property
     - WebCRM Data Type
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


Wave Customer to WebCRM Persons
-------------------------------
Every Wave Customer will be synchronized with a WebCRM Persons.

Once a link between a Wave Customer and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - WebCRM Persons Property
     - WebCRM Data Type
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


Wave Invoice to WebCRM Quotationline
------------------------------------
Every Wave Invoice will be synchronized with a WebCRM Quotationline.

Once a link between a Wave Invoice and a WebCRM Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a WebCRM Quotationline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     - WebCRM Quotationline Property
     - WebCRM Data Type
   * - id
     - QuotationLineOpportunityId
     - "string"
   * - items.price
     - QuotationLinePrice
     - "string"
   * - items.quantity
     - QuotationLineQuantity
     - "string"


Wave Product to WebCRM Products
-------------------------------
Every Wave Product will be synchronized with a WebCRM Products.

Once a link between a Wave Product and a WebCRM Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a WebCRM Products:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - WebCRM Products Property
     - WebCRM Data Type
   * - unitPrice
     - ProductPrice
     - "string"


Wave User to WebCRM Users
-------------------------
Every Wave User will be synchronized with a WebCRM Users.

Once a link between a Wave User and a WebCRM Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave User and a WebCRM Users:

.. list-table::
   :header-rows: 1

   * - Wave User Property
     - WebCRM Users Property
     - WebCRM Data Type


Wave Vendor to WebCRM Persons
-----------------------------
Every Wave Vendor will be synchronized with a WebCRM Persons.

Once a link between a Wave Vendor and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - WebCRM Persons Property
     - WebCRM Data Type
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

