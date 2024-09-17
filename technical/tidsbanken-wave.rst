===========================
Tidsbanken to Wave Dataflow
===========================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Wave Customer person
-----------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Wave Customer person must be established.

A Tidsbanken Ansatt will merge with a Wave Customer person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Wave Customer person Property
   * - Epost
     - email

Once a link between a Tidsbanken Ansatt and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Wave Customer person Property
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
   * - Navn
     - name
     - N/A
   * - Telefon
     - phone
     - "string"
   * - Url
     - website
     - "string"


Tidsbanken Kunde to Wave Customer person
----------------------------------------
Every Tidsbanken Kunde will be synchronized with a Wave Customer person.

Once a link between a Tidsbanken Kunde and a Wave Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Wave Customer person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Wave Customer person Property
     - Wave Data Type

