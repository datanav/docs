========================
SuperOffice to  Dataflow
========================

Generated: 2024-09-05 10:48:08

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Organizations
-------------------------------------
Every SuperOffice Contact will be synchronized with a  Organizations.

Once a link between a SuperOffice Contact and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Organizations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Organizations Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - Urls.Value
     - website
     - "string"


SuperOffice Person to  Members
------------------------------
Every SuperOffice Person will be synchronized with a  Members.

Once a link between a SuperOffice Person and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Members:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Members Property
     -  Data Type
   * - Emails.Value
     - email
     - "string"

