==================================
Businessnxt to Salesforce Dataflow
==================================

Generated: 2024-09-09 10:37:50

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businessnxt to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businessnxt Address to Salesforce Division
------------------------------------------
Every Businessnxt Address will be synchronized with a Salesforce Division.

Once a link between a Businessnxt Address and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Businessnxt Company to Salesforce Division
------------------------------------------
Every Businessnxt Company will be synchronized with a Salesforce Division.

Once a link between a Businessnxt Company and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Businessnxt Country to Salesforce Currencytype
----------------------------------------------
Every Businessnxt Country will be synchronized with a Salesforce Currencytype.

Once a link between a Businessnxt Country and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Country and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Businessnxt Country Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Businessnxt Order to Salesforce Invoice
---------------------------------------
Every Businessnxt Order will be synchronized with a Salesforce Invoice.

Once a link between a Businessnxt Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
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


Businessnxt Orderline to Salesforce Invoice
-------------------------------------------
Every Businessnxt Orderline will be synchronized with a Salesforce Invoice.

Once a link between a Businessnxt Orderline and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Salesforce Invoice Property
     - Salesforce Data Type


Businessnxt Productcategory to Salesforce Currencytype
------------------------------------------------------
Every Businessnxt Productcategory will be synchronized with a Salesforce Currencytype.

Once a link between a Businessnxt Productcategory and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Productcategory and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Businessnxt Productcategory Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Businessnxt Vat to Salesforce Currencytype
------------------------------------------
Every Businessnxt Vat will be synchronized with a Salesforce Currencytype.

Once a link between a Businessnxt Vat and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Vat and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Businessnxt Vat Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Businessnxt Address to Salesforce Organization
----------------------------------------------
Every Businessnxt Address will be synchronized with a Salesforce Organization.

Once a link between a Businessnxt Address and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Address and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Businessnxt Address Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - countryNo
     - Country
     - "string"
   * - fax
     - Fax	
     - "string"
   * - name
     - Name	
     - "string"
   * - phone
     - Phone	
     - "string"
   * - postCode
     - PostalCode	
     - "string"
   * - postalArea
     - City
     - "string"


Businessnxt Company to Salesforce Organization
----------------------------------------------
Every Businessnxt Company will be synchronized with a Salesforce Organization.

Once a link between a Businessnxt Company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Businessnxt Company Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"


Businessnxt Currency to Salesforce Currencytype
-----------------------------------------------
Every Businessnxt Currency will be synchronized with a Salesforce Currencytype.

Once a link between a Businessnxt Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Businessnxt Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Businessnxt Order to Salesforce Order
-------------------------------------
Every Businessnxt Order will be synchronized with a Salesforce Order.

Once a link between a Businessnxt Order and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Order and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Businessnxt Order Property
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


Businessnxt Orderline to Salesforce Invoiceline
-----------------------------------------------
Every Businessnxt Orderline will be synchronized with a Salesforce Invoiceline.

Once a link between a Businessnxt Orderline and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type


Businessnxt Orderline to Salesforce Orderitem
---------------------------------------------
Every Businessnxt Orderline will be synchronized with a Salesforce Orderitem.

Once a link between a Businessnxt Orderline and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - orderNo
     - OrderId
     - "string"


Businessnxt Orderline to Salesforce Quotelineitem
-------------------------------------------------
Every Businessnxt Orderline will be synchronized with a Salesforce Quotelineitem.

Once a link between a Businessnxt Orderline and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Orderline and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Businessnxt Orderline Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type


Businessnxt Product to Salesforce Product2
------------------------------------------
Every Businessnxt Product will be synchronized with a Salesforce Product2.

Once a link between a Businessnxt Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businessnxt Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Businessnxt Product Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - description
     - Description	
     - "string"
   * - webPage
     - DisplayUrl	
     - "string"

