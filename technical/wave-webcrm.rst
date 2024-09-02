===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-09-02 08:11:38

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to  Organisations
-------------------------------
Every Wave Customer will be synchronized with a  Organisations.

Once a link between a Wave Customer and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Organisations:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Organisations Property
     -  Data Type
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


Wave Customer to  Persons
-------------------------
Every Wave Customer will be synchronized with a  Persons.

Once a link between a Wave Customer and a  Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Persons:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Persons Property
     -  Data Type
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


Wave Invoice to  Quotationline
------------------------------
Every Wave Invoice will be synchronized with a  Quotationline.

Once a link between a Wave Invoice and a  Quotationline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Invoice and a  Quotationline:

.. list-table::
   :header-rows: 1

   * - Wave Invoice Property
     -  Quotationline Property
     -  Data Type
   * - id
     - QuotationLineOpportunityId
     - "string"
   * - items.price
     - QuotationLinePrice
     - "string"
   * - items.quantity
     - QuotationLineQuantity
     - "string"


Wave Product to  Products
-------------------------
Every Wave Product will be synchronized with a  Products.

Once a link between a Wave Product and a  Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a  Products:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     -  Products Property
     -  Data Type
   * - unitPrice
     - ProductPrice
     - "string"


Wave User to  Users
-------------------
Every Wave User will be synchronized with a  Users.

Once a link between a Wave User and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave User and a  Users:

.. list-table::
   :header-rows: 1

   * - Wave User Property
     -  Users Property
     -  Data Type


Wave Vendor to  Persons
-----------------------
Every Wave Vendor will be synchronized with a  Persons.

Once a link between a Wave Vendor and a  Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Persons:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Persons Property
     -  Data Type
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

