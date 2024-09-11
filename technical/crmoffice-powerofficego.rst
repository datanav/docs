===================================
CRMOffice to PowerOfficeGO Dataflow
===================================

Generated: 2024-09-11 09:13:48

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Activities to PowerOfficeGO Projectactivity
-----------------------------------------------------
Every CRMOffice Activities will be synchronized with a PowerOfficeGO Projectactivity.

Once a link between a CRMOffice Activities and a PowerOfficeGO Projectactivity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Activities and a PowerOfficeGO Projectactivity:

.. list-table::
   :header-rows: 1

   * - CRMOffice Activities Property
     - PowerOfficeGO Projectactivity Property
     - PowerOfficeGO Data Type
   * - subject
     - name
     - "string"


CRMOffice Contacts to PowerOfficeGO Contactperson
-------------------------------------------------
Every CRMOffice Contacts will be synchronized with a PowerOfficeGO Contactperson.

Once a link between a CRMOffice Contacts and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
   * - directPhone
     - phoneNumber
     - "string"
   * - familyName
     - lastName
     - "string"
   * - givenName
     - firstName
     - "string"

