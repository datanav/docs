===================================
Business Nxt to Salesforce Dataflow
===================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Address to Salesforce Division
-------------------------------------------
Every Business Nxt Address will be synchronized with a Salesforce Division.

Once a link between a Business Nxt Address and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Business Nxt Company to Salesforce Division
-------------------------------------------
Every Business Nxt Company will be synchronized with a Salesforce Division.

Once a link between a Business Nxt Company and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Business Nxt Country to Salesforce Currencytype
-----------------------------------------------
Every Business Nxt Country will be synchronized with a Salesforce Currencytype.

Once a link between a Business Nxt Country and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Country and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Business Nxt Country Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Business Nxt Order to Salesforce Invoice
----------------------------------------
Every Business Nxt Order will be synchronized with a Salesforce Invoice.

Once a link between a Business Nxt Order and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
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


Business Nxt Orderline to Salesforce Invoice
--------------------------------------------
Every Business Nxt Orderline will be synchronized with a Salesforce Invoice.

Once a link between a Business Nxt Orderline and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - Salesforce Invoice Property
     - Salesforce Data Type


Business Nxt Productcategory to Salesforce Currencytype
-------------------------------------------------------
Every Business Nxt Productcategory will be synchronized with a Salesforce Currencytype.

Once a link between a Business Nxt Productcategory and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Productcategory and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Business Nxt Productcategory Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Business Nxt Vat to Salesforce Currencytype
-------------------------------------------
Every Business Nxt Vat will be synchronized with a Salesforce Currencytype.

Once a link between a Business Nxt Vat and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Vat and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Business Nxt Vat Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Business Nxt Address to Salesforce Organization
-----------------------------------------------
Every Business Nxt Address will be synchronized with a Salesforce Organization.

Once a link between a Business Nxt Address and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
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


Business Nxt Company to Salesforce Organization
-----------------------------------------------
Every Business Nxt Company will be synchronized with a Salesforce Organization.

Once a link between a Business Nxt Company and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
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


Business Nxt Currency to Salesforce Currencytype
------------------------------------------------
Every Business Nxt Currency will be synchronized with a Salesforce Currencytype.

Once a link between a Business Nxt Currency and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Currency and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Business Nxt Currency Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Business Nxt Order to Salesforce Order
--------------------------------------
Every Business Nxt Order will be synchronized with a Salesforce Order.

Once a link between a Business Nxt Order and a Salesforce Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Order and a Salesforce Order:

.. list-table::
   :header-rows: 1

   * - Business Nxt Order Property
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


Business Nxt Orderline to Salesforce Invoiceline
------------------------------------------------
Every Business Nxt Orderline will be synchronized with a Salesforce Invoiceline.

Once a link between a Business Nxt Orderline and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type


Business Nxt Orderline to Salesforce Orderitem
----------------------------------------------
Every Business Nxt Orderline will be synchronized with a Salesforce Orderitem.

Once a link between a Business Nxt Orderline and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - orderNo
     - OrderId
     - "string"


Business Nxt Orderline to Salesforce Quotelineitem
--------------------------------------------------
Every Business Nxt Orderline will be synchronized with a Salesforce Quotelineitem.

Once a link between a Business Nxt Orderline and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Orderline and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Business Nxt Orderline Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type


Business Nxt Product to Salesforce Product2
-------------------------------------------
Every Business Nxt Product will be synchronized with a Salesforce Product2.

Once a link between a Business Nxt Product and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
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

