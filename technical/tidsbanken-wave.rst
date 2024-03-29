===========================
Tidsbanken to Wave Dataflow
===========================

Generated: 2024-03-29 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Kunde to Wave Customer
---------------------------------
Every Tidsbanken Kunde will be synchronized with a Wave Customer.

Once a link between a Tidsbanken Kunde and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Wave Customer Property
     - Wave Data Type
   * - Gateadresse
     - address.addressLine1
     - "string"
   * - Gateadresse
     - shippingDetails.address.addressLine1
     - "string"
   * - LevPostNr
     - address.postalCode
     - "string"
   * - LevPostNr
     - shippingDetails.address.postalCode
     - "string"
   * - LevPoststed
     - address.city
     - "string"
   * - LevPoststed
     - shippingDetails.address.city
     - "string"
   * - Leveringsadresse
     - address.addressLine1
     - "string"
   * - Leveringsadresse
     - shippingDetails.address.addressLine1
     - "string"
   * - Leveringsadresse2
     - address.addressLine2
     - "string"
   * - Leveringsadresse2
     - shippingDetails.address.addressLine2
     - "string"
   * - Navn
     - name
     - N/A
   * - Postadresse
     - address.addressLine2
     - "string"
   * - Postadresse
     - shippingDetails.address.addressLine2
     - "string"
   * - Postnr
     - address.postalCode
     - "string"
   * - Postnr
     - shippingDetails.address.postalCode
     - "string"
   * - Poststed
     - address.city
     - "string"
   * - Poststed
     - shippingDetails.address.city
     - "string"
   * - Telefon
     - phone
     - "string"
   * - Url
     - website
     - "string"

