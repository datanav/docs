============================
Asana to MemberCare Dataflow
============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Asana to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Asana Teams to MemberCare Companies
-----------------------------------
Every Asana Teams will be synchronized with a MemberCare Companies.

Once a link between a Asana Teams and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Teams and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Asana Teams Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - name
     - companyName
     - "string"
   * - name
     - name
     - "string"
   * - permalink_url
     - url
     - "string"


Asana Workspaces to MemberCare Companies
----------------------------------------
Every Asana Workspaces will be synchronized with a MemberCare Companies.

Once a link between a Asana Workspaces and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Asana Workspaces and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Asana Workspaces Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - email_domains
     - url
     - "string"
   * - name
     - companyName
     - "string"
   * - name
     - name
     - "string"

