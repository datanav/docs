======================
Chargebee to  Dataflow
======================

Generated: 2024-09-03 08:57:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Address to  Countries
-------------------------------
Every Chargebee Address will be synchronized with a  Countries.

Once a link between a Chargebee Address and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a  Countries:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     -  Countries Property
     -  Data Type
   * - country
     - name
     - "string"


Chargebee Business_entity to  Companies
---------------------------------------
Every Chargebee Business_entity will be synchronized with a  Companies.

Once a link between a Chargebee Business_entity and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a  Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     -  Companies Property
     -  Data Type
   * - name
     - companyName
     - "string"


Chargebee Customer to  Countries
--------------------------------
Every Chargebee Customer will be synchronized with a  Countries.

Once a link between a Chargebee Customer and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a  Countries:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     -  Countries Property
     -  Data Type
   * - billing_address.country
     - name
     - "string"

