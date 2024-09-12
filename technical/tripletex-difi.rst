==========================
Tripletex to Difi Dataflow
==========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Difi. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Difi Enhetsregisteret
-------------------------------------------
Before any synchronization can take place, a link between a Tripletex Customer and a Difi Enhetsregisteret must be established.

A Tripletex Customer will merge with a Difi Enhetsregisteret if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Difi Enhetsregisteret Property
   * - organizationNumber
     - orgnr

Once a link between a Tripletex Customer and a Difi Enhetsregisteret is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Difi Enhetsregisteret:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Difi Enhetsregisteret Property
     - Difi Data Type


Tripletex Supplier to Difi Enhetsregisteret
-------------------------------------------
Before any synchronization can take place, a link between a Tripletex Supplier and a Difi Enhetsregisteret must be established.

A Tripletex Supplier will merge with a Difi Enhetsregisteret if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Difi Enhetsregisteret Property
   * - organizationNumber
     - orgnr

Once a link between a Tripletex Supplier and a Difi Enhetsregisteret is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Supplier and a Difi Enhetsregisteret:

.. list-table::
   :header-rows: 1

   * - Tripletex Supplier Property
     - Difi Enhetsregisteret Property
     - Difi Data Type

