============================
ZohoCRM to Wikidata Dataflow
============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Wikidata. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Wikidata Country
-----------------------------------
Before any synchronization can take place, a link between a ZohoCRM Account and a Wikidata Country must be established.

A ZohoCRM Account will merge with a Wikidata Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Wikidata Country Property
   * - Billing_Country
     - ps:P1476
   * - Shipping_Country
     - ps:P1476

Once a link between a ZohoCRM Account and a Wikidata Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Wikidata Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Wikidata Country Property
     - Wikidata Data Type


ZohoCRM Contact to Wikidata Country
-----------------------------------
Before any synchronization can take place, a link between a ZohoCRM Contact and a Wikidata Country must be established.

A ZohoCRM Contact will merge with a Wikidata Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Wikidata Country Property
   * - Other_Country
     - ps:P1476
   * - Mailing_Country
     - ps:P1476

Once a link between a ZohoCRM Contact and a Wikidata Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Wikidata Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Wikidata Country Property
     - Wikidata Data Type

