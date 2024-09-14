===========================
ZohoCRM to Zendesk Dataflow
===========================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Zendesk Organizations
----------------------------------------
Every ZohoCRM Account will be synchronized with a Zendesk Organizations.

Once a link between a ZohoCRM Account and a Zendesk Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Zendesk Organizations:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Zendesk Organizations Property
     - Zendesk Data Type
   * - Account_Name
     - name
     - "string"

