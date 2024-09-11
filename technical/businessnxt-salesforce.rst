==================================
BusinessNxt to Salesforce Dataflow
==================================

Generated: 2024-09-11 08:37:15

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


BusinessNxt Address to Salesforce Organization
----------------------------------------------
Every BusinessNxt Address will be synchronized with a Salesforce Organization.

Once a link between a BusinessNxt Address and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Address and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Address Property
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


BusinessNxt Company to Salesforce Organization
----------------------------------------------
Every BusinessNxt Company will be synchronized with a Salesforce Organization.

Once a link between a BusinessNxt Company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Company Property
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


BusinessNxt Currency to Salesforce Currencytype
-----------------------------------------------
Every BusinessNxt Currency will be synchronized with a Salesforce Currencytype.

Once a link between a BusinessNxt Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


BusinessNxt Order to Salesforce Order
-------------------------------------
Every BusinessNxt Order will be synchronized with a Salesforce Order.

Once a link between a BusinessNxt Order and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Order and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Order Property
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


BusinessNxt Orderline to Salesforce Invoiceline
-----------------------------------------------
Every BusinessNxt Orderline will be synchronized with a Salesforce Invoiceline.

Once a link between a BusinessNxt Orderline and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type


BusinessNxt Orderline to Salesforce Orderitem
---------------------------------------------
Every BusinessNxt Orderline will be synchronized with a Salesforce Orderitem.

Once a link between a BusinessNxt Orderline and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - orderNo
     - OrderId
     - "string"


BusinessNxt Orderline to Salesforce Quotelineitem
-------------------------------------------------
Every BusinessNxt Orderline will be synchronized with a Salesforce Quotelineitem.

Once a link between a BusinessNxt Orderline and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Orderline and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Orderline Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type


BusinessNxt Product to Salesforce Product2
------------------------------------------
Every BusinessNxt Product will be synchronized with a Salesforce Product2.

Once a link between a BusinessNxt Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a BusinessNxt Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - BusinessNxt Product Property
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

