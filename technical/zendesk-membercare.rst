==============================
Zendesk to MemberCare Dataflow
==============================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to MemberCare Companies
---------------------------------------------
Every Zendesk Organizations will be synchronized with a MemberCare Companies.

Once a link between a Zendesk Organizations and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - name
     - companyName
     - "string"


Zendesk Users to MemberCare Persons
-----------------------------------
Every Zendesk Users will be synchronized with a MemberCare Persons.

Once a link between a Zendesk Users and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - email
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - name
     - name
     - "string"

