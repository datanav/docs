==============================
Salesforce to ZohoCRM Dataflow
==============================

Generated: 2024-09-13 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Division to ZohoCRM Account
--------------------------------------
Every Salesforce Division will be synchronized with a ZohoCRM Account.

Once a link between a Salesforce Division and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Name
     - Account_Name
     - "string"


Salesforce Organization to ZohoCRM Account
------------------------------------------
Every Salesforce Organization will be synchronized with a ZohoCRM Account.

Once a link between a Salesforce Organization and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - Fax
     - Fax
     - "string"
   * - Fax	
     - Fax
     - "string"
   * - Name
     - Account_Name
     - "string"
   * - Name	
     - Account_Name
     - "string"
   * - Phone
     - Phone
     - "string"
   * - Phone	
     - Phone
     - "string"


Salesforce Customer to ZohoCRM Contact
--------------------------------------
Every Salesforce Customer will be synchronized with a ZohoCRM Contact.

Once a link between a Salesforce Customer and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - Name
     - Full_Name
     - "string"

