====================
HubSpot to  Dataflow
====================

Generated: 2024-08-26 15:42:47

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to  Company
---------------------------
Every HubSpot Company will be synchronized with a  Company.

Once a link between a HubSpot Company and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Company:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Company Property
     -  Data Type
   * - properties.name
     - name
     - "string"


HubSpot Contactcompanyassociationtype to  Country
-------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a  Country.

Once a link between a HubSpot Contactcompanyassociationtype and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a  Country:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     -  Country Property
     -  Data Type
   * - label
     - name
     - "string"


HubSpot Company to  Country
---------------------------
Every HubSpot Company will be synchronized with a  Country.

Once a link between a HubSpot Company and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Country:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Country Property
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

