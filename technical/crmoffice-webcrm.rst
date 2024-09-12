============================
CRMOffice to WebCRM Dataflow
============================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to WebCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Contacts to WebCRM Persons
------------------------------------
Every CRMOffice Contacts will be synchronized with a WebCRM Persons.

Once a link between a CRMOffice Contacts and a WebCRM Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a WebCRM Persons:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - WebCRM Persons Property
     - WebCRM Data Type
   * - directPhone
     - PersonDirectPhone
     - "string"
   * - familyName
     - PersonLastName
     - "string"
   * - givenName
     - PersonFirstName
     - "string"
   * - mobilePhone
     - PersonMobilePhone
     - "string"

