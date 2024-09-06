===============================
Invoiced to Salesforce Dataflow
===============================

Generated: 2024-09-06 11:53:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Salesforce Division
-------------------------------------------------
Every Invoiced Customers company will be synchronized with a Salesforce Division.

Once a link between a Invoiced Customers company and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Invoiced Customers company to Salesforce Organization
-----------------------------------------------------
Every Invoiced Customers company will be synchronized with a Salesforce Organization.

Once a link between a Invoiced Customers company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"


Invoiced Invoices to Salesforce Invoice
---------------------------------------
Every Invoiced Invoices will be synchronized with a Salesforce Invoice.

Once a link between a Invoiced Invoices and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - currency
     - CurrencyIsoCode
     - "string"


Invoiced Lineitem to Salesforce Invoice
---------------------------------------
Every Invoiced Lineitem will be synchronized with a Salesforce Invoice.

Once a link between a Invoiced Lineitem and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Salesforce Invoice Property
     - Salesforce Data Type


Invoiced Contacts to Salesforce Contact
---------------------------------------
Every Invoiced Contacts will be synchronized with a Salesforce Contact.

Once a link between a Invoiced Contacts and a Salesforce Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Salesforce Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Salesforce Contact Property
     - Salesforce Data Type


Invoiced Customers person to Salesforce Customer
------------------------------------------------
Every Invoiced Customers person will be synchronized with a Salesforce Customer.

Once a link between a Invoiced Customers person and a Salesforce Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Salesforce Customer:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Salesforce Customer Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Invoiced Items to Salesforce Product2
-------------------------------------
Every Invoiced Items will be synchronized with a Salesforce Product2.

Once a link between a Invoiced Items and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - description
     - Description	
     - "string"
   * - name
     - Name	
     - "string"

