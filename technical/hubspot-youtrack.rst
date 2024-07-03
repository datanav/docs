============================
HubSpot to Youtrack Dataflow
============================

Generated: 2024-07-03 00:00:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Youtrack Users
---------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Youtrack Users must be established.

A HubSpot Contact will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Youtrack Users Property
   * - properties.email
     - profile.email.email

Once a link between a HubSpot Contact and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - properties.email
     - profile.email
     - "string"
   * - properties.email
     - profile.email.email
     - "string"
   * - properties.work_email
     - profile.email.email
     - "string"


HubSpot Company to Youtrack Groups
----------------------------------
Every HubSpot Company will be synchronized with a Youtrack Groups.

Once a link between a HubSpot Company and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - properties.name
     - name
     - "string"


HubSpot Contactcompanyassociationtype to Youtrack Organizationroles
-------------------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a Youtrack Organizationroles.

Once a link between a HubSpot Contactcompanyassociationtype and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


HubSpot Dealcompanyassociationtype to Youtrack Organizationroles
----------------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a Youtrack Organizationroles.

Once a link between a HubSpot Dealcompanyassociationtype and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


HubSpot Dealcontactassociationtype to Youtrack Organizationroles
----------------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a Youtrack Organizationroles.

Once a link between a HubSpot Dealcontactassociationtype and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


HubSpot Lineitemdealassociationtype to Youtrack Organizationroles
-----------------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a Youtrack Organizationroles.

Once a link between a HubSpot Lineitemdealassociationtype and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


HubSpot Lineitemquoteassociationtype to Youtrack Organizationroles
------------------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a Youtrack Organizationroles.

Once a link between a HubSpot Lineitemquoteassociationtype and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


HubSpot Quotecompanyassociationtype to Youtrack Organizationroles
-----------------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a Youtrack Organizationroles.

Once a link between a HubSpot Quotecompanyassociationtype and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


HubSpot Quotecontactassociationtype to Youtrack Organizationroles
-----------------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a Youtrack Organizationroles.

Once a link between a HubSpot Quotecontactassociationtype and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


HubSpot Quotedealassociationtype to Youtrack Organizationroles
--------------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a Youtrack Organizationroles.

Once a link between a HubSpot Quotedealassociationtype and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


HubSpot Quotequotetemplateassociationtype to Youtrack Organizationroles
-----------------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a Youtrack Organizationroles.

Once a link between a HubSpot Quotequotetemplateassociationtype and a Youtrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a Youtrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     - Youtrack Organizationroles Property
     - Youtrack Data Type


HubSpot Ticket to Youtrack Issues
---------------------------------
Every HubSpot Ticket will be synchronized with a Youtrack Issues.

Once a link between a HubSpot Ticket and a Youtrack Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a Youtrack Issues:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     - Youtrack Issues Property
     - Youtrack Data Type
   * - properties.hubspot_owner_id
     - reporter.id
     - "string"


HubSpot User to Youtrack Users
------------------------------
Every HubSpot User will be synchronized with a Youtrack Users.

Once a link between a HubSpot User and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - email
     - profile.email.email
     - "string"

