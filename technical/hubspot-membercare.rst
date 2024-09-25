==============================
HubSpot to MemberCare Dataflow
==============================

Generated: 2024-09-25 00:34:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to MemberCare Countries
---------------------------------------
Every HubSpot Company will be synchronized with a MemberCare Countries.

Once a link between a HubSpot Company and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - properties.country
     - name
     - "string"
   * - properties.industry
     - name
     - "string"
   * - properties.state
     - name
     - "string"
   * - properties.type
     - name
     - "string"

