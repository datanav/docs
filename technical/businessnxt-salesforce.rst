==================================
BusinessNxt to Salesforce Dataflow
==================================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Address to Salesforce Division
------------------------------------
Every Visma Address will be synchronized with a Salesforce Division.

Once a link between a Visma Address and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Visma Company to Salesforce Division
------------------------------------
Every Visma Company will be synchronized with a Salesforce Division.

Once a link between a Visma Company and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Visma Country to Salesforce Currencytype
----------------------------------------
Every Visma Country will be synchronized with a Salesforce Currencytype.

Once a link between a Visma Country and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Country and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Visma Country Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Visma Order to Salesforce Invoice
---------------------------------
Every Visma Order will be synchronized with a Salesforce Invoice.

Once a link between a Visma Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - dueDate
     - FullSettlementDate
     - "string"
   * - invoiceDate
     - InvoiceDate
     - "string"
   * - invoiceDate
     - PostedDate
     - "string"


Visma Orderline to Salesforce Invoice
-------------------------------------
Every Visma Orderline will be synchronized with a Salesforce Invoice.

Once a link between a Visma Orderline and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Salesforce Invoice Property
     - Salesforce Data Type


Visma Productcategory to Salesforce Currencytype
------------------------------------------------
Every Visma Productcategory will be synchronized with a Salesforce Currencytype.

Once a link between a Visma Productcategory and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Productcategory and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Visma Productcategory Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Visma Vat to Salesforce Currencytype
------------------------------------
Every Visma Vat will be synchronized with a Salesforce Currencytype.

Once a link between a Visma Vat and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Vat and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Visma Vat Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Visma Address to Salesforce Organization
----------------------------------------
Every Visma Address will be synchronized with a Salesforce Organization.

Once a link between a Visma Address and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - addressLine1
     - Street
     - "string"
   * - addressNo
     - ID
     - "string"
   * - countryNo
     - Country
     - "string"
   * - fax
     - Fax
     - "string"
   * - fax
     - Fax	
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - Name	
     - "string"
   * - phone
     - Phone
     - "string"
   * - phone
     - Phone	
     - "string"
   * - postCode
     - PostalCode
     - "string"
   * - postCode
     - PostalCode	
     - "string"
   * - postalArea
     - City
     - "string"


Visma Company to Salesforce Organization
----------------------------------------
Every Visma Company will be synchronized with a Salesforce Organization.

Once a link between a Visma Company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - companyNo
     - ID
     - "string"
   * - name
     - Name
     - "string"
   * - name
     - Name	
     - "string"


Visma Currency to Salesforce Currencytype
-----------------------------------------
Every Visma Currency will be synchronized with a Salesforce Currencytype.

Once a link between a Visma Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Visma Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Visma Order to Salesforce Order
-------------------------------
Every Visma Order will be synchronized with a Salesforce Order.

Once a link between a Visma Order and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Order and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Visma Order Property
     - Salesforce Order Property
     - Salesforce Data Type
   * - dueDate
     - EffectiveDate
     - "string"
   * - dueDate
     - EndDate
     - "string"
   * - name
     - Name
     - "string"
   * - orderDate
     - EffectiveDate
     - "string"
   * - orderDate
     - OrderedDate
     - "string"
   * - settlementDate
     - EndDate
     - "string"


Visma Orderline to Salesforce Invoiceline
-----------------------------------------
Every Visma Orderline will be synchronized with a Salesforce Invoiceline.

Once a link between a Visma Orderline and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type


Visma Orderline to Salesforce Orderitem
---------------------------------------
Every Visma Orderline will be synchronized with a Salesforce Orderitem.

Once a link between a Visma Orderline and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - orderNo
     - OrderId
     - "string"


Visma Orderline to Salesforce Quotelineitem
-------------------------------------------
Every Visma Orderline will be synchronized with a Salesforce Quotelineitem.

Once a link between a Visma Orderline and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Orderline and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Visma Orderline Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type


Visma Product to Salesforce Product2
------------------------------------
Every Visma Product will be synchronized with a Salesforce Product2.

Once a link between a Visma Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Visma Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - description
     - Description
     - "string"
   * - description
     - Description	
     - "string"
   * - webPage
     - DisplayUrl
     - "string"
   * - webPage
     - DisplayUrl	
     - "string"

