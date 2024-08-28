===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-08-28 10:47:44

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

