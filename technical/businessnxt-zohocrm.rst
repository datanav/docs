===============================
Businessnxt to ZohoCRM Dataflow
===============================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to ZohoCRM Account
--------------------------------------
Every Businessnxt Address will be synchronized with a ZohoCRM Account.

Once a link between a Businessnxt Address and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
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


Businessnxt Company to ZohoCRM Account
--------------------------------------
Every Businessnxt Company will be synchronized with a ZohoCRM Account.

Once a link between a Businessnxt Company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"

