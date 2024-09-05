=========================
Webcrm to Trello Dataflow
=========================

Generated: 2024-09-05 12:09:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Organisations to  Organizations
--------------------------------------
Every Webcrm Organisations will be synchronized with a  Organizations.

Once a link between a Webcrm Organisations and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Organisations and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Webcrm Organisations Property
     -  Organizations Property
     -  Data Type
   * - OrganisationCompanyDescription
     - desc
     - "string"
   * - OrganisationName
     - name
     - "string"


Webcrm Persons to  Members
--------------------------
Every Webcrm Persons will be synchronized with a  Members.

Once a link between a Webcrm Persons and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a  Members:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     -  Members Property
     -  Data Type
   * - PersonName
     - fullName
     - "string"


Webcrm Users to  Members
------------------------
Every Webcrm Users will be synchronized with a  Members.

Once a link between a Webcrm Users and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a  Members:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     -  Members Property
     -  Data Type

