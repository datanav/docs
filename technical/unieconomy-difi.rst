===========================
Unieconomy to Difi Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Difi. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Companies to Difi Enhetsregisteret
---------------------------------------------
Before any synchronization can take place, a link between a Unieconomy Companies and a Difi Enhetsregisteret must be established.

A Unieconomy Companies will merge with a Difi Enhetsregisteret if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Difi Enhetsregisteret Property
   * - OrganizationNumber
     - orgnr

Once a link between a Unieconomy Companies and a Difi Enhetsregisteret is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Companies and a Difi Enhetsregisteret:

.. list-table::
   :header-rows: 1

   * - Unieconomy Companies Property
     - Difi Enhetsregisteret Property
     - Difi Data Type


Unieconomy Customers to Difi Enhetsregisteret
---------------------------------------------
Before any synchronization can take place, a link between a Unieconomy Customers and a Difi Enhetsregisteret must be established.

A Unieconomy Customers will merge with a Difi Enhetsregisteret if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Difi Enhetsregisteret Property
   * - OrgNumber
     - orgnr

Once a link between a Unieconomy Customers and a Difi Enhetsregisteret is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Customers and a Difi Enhetsregisteret:

.. list-table::
   :header-rows: 1

   * - Unieconomy Customers Property
     - Difi Enhetsregisteret Property
     - Difi Data Type

