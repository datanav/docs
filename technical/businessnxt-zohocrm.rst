===============================
BusinessNxt to ZohoCRM Dataflow
===============================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

BusinessNxt Address to ZohoCRM Account
--------------------------------------
Every BusinessNxt Address will be synchronized with a ZohoCRM Account.

Once a link between a BusinessNxt Address and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Address and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Address Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - fax
     - Fax
     - "string"
   * - name
     - Account_Name
     - "string"
   * - phone
     - Phone
     - "string"


BusinessNxt Company to ZohoCRM Account
--------------------------------------
Every BusinessNxt Company will be synchronized with a ZohoCRM Account.

Once a link between a BusinessNxt Company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"

