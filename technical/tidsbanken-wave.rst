===========================
Tidsbanken to Wave Dataflow
===========================

Generated: 2024-10-19 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Wave Customer
----------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Wave Customer must be established.

A Tidsbanken Ansatt will merge with a Wave Customer if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Wave Customer Property
   * - Epost
     - email

Once a link between a Tidsbanken Ansatt and a Wave Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Wave Customer:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Wave Customer Property
     - Wave Data Type
   * - Adresse
     - address.addressLine1
     - "string"
   * - Adresse
     - shippingDetails.address.addressLine1
     - "string"
   * - Etternavn
     - lastName
     - N/A
   * - Fornavn
     - firstName
     - "string"
   * - Mobil
     - mobile
     - "string"
   * - Navn
     - name
     - N/A
   * - Postnummer
     - address.postalCode
     - "string"
   * - Postnummer
     - shippingDetails.address.postalCode
     - "string"
   * - Poststed
     - address.city
     - "string"
   * - Poststed
     - shippingDetails.address.city
     - "string"


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


Tidsbanken Kunde to Wave Customer (human data)
----------------------------------------------
Every Tidsbanken Kunde will be synchronized with a Wave Customer (human data).

Once a link between a Tidsbanken Kunde and a Wave Customer (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Wave Customer (human data):

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Wave Customer (human data) Property
     - Wave Data Type

