====================
HubSpot to  Dataflow
====================

Generated: 2024-09-02 14:00:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to  Companycategories
-------------------------------------
Every HubSpot Company will be synchronized with a  Companycategories.

Once a link between a HubSpot Company and a  Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Companycategories:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Companycategories Property
     -  Data Type
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


HubSpot Company to  Countries
-----------------------------
Every HubSpot Company will be synchronized with a  Countries.

Once a link between a HubSpot Company and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Countries:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Countries Property
     -  Data Type
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

