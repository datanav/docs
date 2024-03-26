============================
HubSpot to Youtrack Dataflow
============================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to  Users
-------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Users must be established.

A HubSpot Contact will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Users Property
   * - properties.email
     - profile.email.email

Once a link between a HubSpot Contact and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Users:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Users Property
     -  Data Type
   * - properties.email
     - profile.email
     - "string"
   * - properties.email
     - profile.email.email
     - "string"
   * - properties.work_email
     - profile.email.email
     - "string"


HubSpot Company to  Groups
--------------------------
Every HubSpot Company will be synchronized with a  Groups.

Once a link between a HubSpot Company and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a  Groups:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     -  Groups Property
     -  Data Type
   * - properties.name
     - name
     - "string"


HubSpot Contactcompanyassociationtype to  Organizationroles
-----------------------------------------------------------
Every HubSpot Contactcompanyassociationtype will be synchronized with a  Organizationroles.

Once a link between a HubSpot Contactcompanyassociationtype and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociationtype and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociationtype Property
     -  Organizationroles Property
     -  Data Type


HubSpot Dealcompanyassociationtype to  Organizationroles
--------------------------------------------------------
Every HubSpot Dealcompanyassociationtype will be synchronized with a  Organizationroles.

Once a link between a HubSpot Dealcompanyassociationtype and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcompanyassociationtype and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcompanyassociationtype Property
     -  Organizationroles Property
     -  Data Type


HubSpot Dealcontactassociationtype to  Organizationroles
--------------------------------------------------------
Every HubSpot Dealcontactassociationtype will be synchronized with a  Organizationroles.

Once a link between a HubSpot Dealcontactassociationtype and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Dealcontactassociationtype and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Dealcontactassociationtype Property
     -  Organizationroles Property
     -  Data Type


HubSpot Lineitemdealassociationtype to  Organizationroles
---------------------------------------------------------
Every HubSpot Lineitemdealassociationtype will be synchronized with a  Organizationroles.

Once a link between a HubSpot Lineitemdealassociationtype and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemdealassociationtype and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemdealassociationtype Property
     -  Organizationroles Property
     -  Data Type


HubSpot Lineitemquoteassociationtype to  Organizationroles
----------------------------------------------------------
Every HubSpot Lineitemquoteassociationtype will be synchronized with a  Organizationroles.

Once a link between a HubSpot Lineitemquoteassociationtype and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Lineitemquoteassociationtype and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Lineitemquoteassociationtype Property
     -  Organizationroles Property
     -  Data Type


HubSpot Quotecompanyassociationtype to  Organizationroles
---------------------------------------------------------
Every HubSpot Quotecompanyassociationtype will be synchronized with a  Organizationroles.

Once a link between a HubSpot Quotecompanyassociationtype and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecompanyassociationtype and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecompanyassociationtype Property
     -  Organizationroles Property
     -  Data Type


HubSpot Quotecontactassociationtype to  Organizationroles
---------------------------------------------------------
Every HubSpot Quotecontactassociationtype will be synchronized with a  Organizationroles.

Once a link between a HubSpot Quotecontactassociationtype and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotecontactassociationtype and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotecontactassociationtype Property
     -  Organizationroles Property
     -  Data Type


HubSpot Quotedealassociationtype to  Organizationroles
------------------------------------------------------
Every HubSpot Quotedealassociationtype will be synchronized with a  Organizationroles.

Once a link between a HubSpot Quotedealassociationtype and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotedealassociationtype and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotedealassociationtype Property
     -  Organizationroles Property
     -  Data Type


HubSpot Quotequotetemplateassociationtype to  Organizationroles
---------------------------------------------------------------
Every HubSpot Quotequotetemplateassociationtype will be synchronized with a  Organizationroles.

Once a link between a HubSpot Quotequotetemplateassociationtype and a  Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Quotequotetemplateassociationtype and a  Organizationroles:

.. list-table::
   :header-rows: 1

   * - HubSpot Quotequotetemplateassociationtype Property
     -  Organizationroles Property
     -  Data Type


HubSpot Ticket to  Issues
-------------------------
Every HubSpot Ticket will be synchronized with a  Issues.

Once a link between a HubSpot Ticket and a  Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Ticket and a  Issues:

.. list-table::
   :header-rows: 1

   * - HubSpot Ticket Property
     -  Issues Property
     -  Data Type
   * - properties.hubspot_owner_id
     - reporter.id
     - "string"


HubSpot User to  Users
----------------------
Every HubSpot User will be synchronized with a  Users.

Once a link between a HubSpot User and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a  Users:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     -  Users Property
     -  Data Type
   * - email
     - profile.email.email
     - "string"

