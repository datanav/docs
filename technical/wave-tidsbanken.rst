=====================================
Wave Financial to Tidsbanken Dataflow
=====================================

Generated: 2024-07-02 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Tidsbanken Ansatt
-----------------------------------------
Before any synchronization can take place, a link between a Wave Customer person and a Tidsbanken Ansatt must be established.

A Wave Customer person will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Tidsbanken Ansatt Property
   * - email
     - Epost

Once a link between a Wave Customer person and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - address.addressLine1
     - Adresse
     - "string"
   * - address.city
     - Poststed
     - "string"
   * - address.postalCode
     - Postnummer
     - "string"
   * - firstName
     - Fornavn
     - "string"
   * - id
     - Id
     - "integer"
   * - lastName
     - Etternavn
     - "string"
   * - mobile
     - Mobil
     - "string"
   * - name
     - Navn
     - "string"
   * - shippingDetails.address.addressLine1
     - Adresse
     - "string"
   * - shippingDetails.address.city
     - Poststed
     - "string"
   * - shippingDetails.address.postalCode
     - Postnummer
     - "string"


Wave Customer to Tidsbanken Ansatt
----------------------------------
Before any synchronization can take place, a link between a Wave Customer and a Tidsbanken Ansatt must be established.

A Wave Customer will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tidsbanken Ansatt Property
   * - email
     - Epost

Once a link between a Wave Customer and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - address.addressLine1
     - Adresse
     - "string"
   * - address.city
     - Poststed
     - "string"
   * - address.postalCode
     - Postnummer
     - "string"
   * - id
     - Id
     - "integer"
   * - shippingDetails.address.addressLine1
     - Adresse
     - "string"
   * - shippingDetails.address.city
     - Poststed
     - "string"
   * - shippingDetails.address.postalCode
     - Postnummer
     - "string"


Wave Vendor to Tidsbanken Ansatt
--------------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Tidsbanken Ansatt must be established.

A Wave Vendor will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Tidsbanken Ansatt Property
   * - email
     - Epost

Once a link between a Wave Vendor and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
   * - address.addressLine1
     - Adresse
     - "string"
   * - address.city
     - Poststed
     - "string"
   * - address.postalCode
     - Postnummer
     - "string"
   * - id
     - Id
     - "integer"


Wave Customer to Tidsbanken Kunde
---------------------------------
Every Wave Customer will be synchronized with a Tidsbanken Kunde.

Once a link between a Wave Customer and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type
   * - address.addressLine1
     - Gateadresse
     - "string"
   * - address.addressLine1
     - Leveringsadresse
     - "string"
   * - address.addressLine1
     - Postadresse
     - "string"
   * - address.addressLine2
     - Gateadresse
     - "string"
   * - address.addressLine2
     - Leveringsadresse2
     - "string"
   * - address.addressLine2
     - Postadresse
     - "string"
   * - address.city
     - LevPoststed
     - "string"
   * - address.city
     - Poststed
     - "string"
   * - address.postalCode
     - LevPostNr
     - "string"
   * - address.postalCode
     - Postnr
     - "string"
   * - id
     - Id
     - "string"
   * - name
     - Navn
     - "string"
   * - phone
     - Telefon
     - "string"
   * - shippingDetails.address.addressLine1
     - Gateadresse
     - "string"
   * - shippingDetails.address.addressLine1
     - Leveringsadresse
     - "string"
   * - shippingDetails.address.addressLine1
     - Postadresse
     - "string"
   * - shippingDetails.address.addressLine2
     - Gateadresse
     - "string"
   * - shippingDetails.address.addressLine2
     - Leveringsadresse2
     - "string"
   * - shippingDetails.address.addressLine2
     - Postadresse
     - "string"
   * - shippingDetails.address.city
     - LevPoststed
     - "string"
   * - shippingDetails.address.city
     - Poststed
     - "string"
   * - shippingDetails.address.postalCode
     - LevPostNr
     - "string"
   * - shippingDetails.address.postalCode
     - Postnr
     - "string"
   * - shippingDetails.phone
     - Telefon
     - "string"
   * - website
     - Url
     - "string"

