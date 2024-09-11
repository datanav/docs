=========================================
Salesforce to Visma Business Nxt Dataflow
=========================================

Generated: 2024-09-11 07:48:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Currencytype to Businessnxt Country
----------------------------------------------
Every Salesforce Currencytype will be synchronized with a Businessnxt Country.

Once a link between a Salesforce Currencytype and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Salesforce Division to Businessnxt Address
------------------------------------------
Every Salesforce Division will be synchronized with a Businessnxt Address.

Once a link between a Salesforce Division and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - Name
     - name
     - "string"


Salesforce Invoice to Businessnxt Order
---------------------------------------
Every Salesforce Invoice will be synchronized with a Businessnxt Order.

Once a link between a Salesforce Invoice and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - FullSettlementDate
     - dueDate
     - "string"
   * - InvoiceDate
     - invoiceDate
     - "string"
   * - PostedDate
     - invoiceDate
     - "string"


Salesforce Invoiceline to Businessnxt Order
-------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Businessnxt Order.

Once a link between a Salesforce Invoiceline and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Salesforce Orderitem to Businessnxt Order
-----------------------------------------
Every Salesforce Orderitem will be synchronized with a Businessnxt Order.

Once a link between a Salesforce Orderitem and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Salesforce Quote to Businessnxt Order
-------------------------------------
Every Salesforce Quote will be synchronized with a Businessnxt Order.

Once a link between a Salesforce Quote and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - Discount
     - totalDiscountAmountInCurrency
     - "string"
   * - Name
     - name
     - "string"
   * - Tax
     - taxCode
     - "string"


Salesforce Quotelineitem to Businessnxt Order
---------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Businessnxt Order.

Once a link between a Salesforce Quotelineitem and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Salesforce Contact to Visma Country
-----------------------------------
Every Salesforce Contact will be synchronized with a Visma Country.

Once a link between a Salesforce Contact and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Visma Country Property
     - Visma Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Currencytype to Visma Currency
-----------------------------------------
Every Salesforce Currencytype will be synchronized with a Visma Currency.

Once a link between a Salesforce Currencytype and a Visma Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Visma Currency:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Visma Currency Property
     - Visma Data Type


Salesforce Invoiceline to Visma Orderline
-----------------------------------------
Every Salesforce Invoiceline will be synchronized with a Visma Orderline.

Once a link between a Salesforce Invoiceline and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Visma Orderline Property
     - Visma Data Type


Salesforce Order to Visma Country
---------------------------------
Every Salesforce Order will be synchronized with a Visma Country.

Once a link between a Salesforce Order and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Visma Country Property
     - Visma Data Type
   * - BillingCountry
     - name
     - "string"
   * - BillingCountryCode
     - isoCode
     - "string"
   * - ShippingCountry
     - name
     - "string"
   * - ShippingCountryCode
     - isoCode
     - "string"


Salesforce Order to Visma Order
-------------------------------
Every Salesforce Order will be synchronized with a Visma Order.

Once a link between a Salesforce Order and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Visma Order Property
     - Visma Data Type
   * - EffectiveDate
     - dueDate
     - "string"
   * - EffectiveDate
     - orderDate
     - "string"
   * - EndDate
     - dueDate
     - "string"
   * - EndDate
     - settlementDate
     - "string"
   * - Name
     - name
     - "string"
   * - OrderedDate
     - orderDate
     - "string"


Salesforce Orderitem to Visma Orderline
---------------------------------------
Every Salesforce Orderitem will be synchronized with a Visma Orderline.

Once a link between a Salesforce Orderitem and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Visma Orderline Property
     - Visma Data Type
   * - OrderId
     - orderNo
     - "string"


Salesforce Organization to Visma Address
----------------------------------------
Every Salesforce Organization will be synchronized with a Visma Address.

Once a link between a Salesforce Organization and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Visma Address Property
     - Visma Data Type
   * - City
     - postalArea
     - "string"
   * - Country
     - countryNo
     - "string"
   * - Fax
     - fax
     - "string"
   * - Fax	
     - fax
     - "string"
   * - ID
     - addressNo
     - "string"
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"
   * - Phone
     - phone
     - "string"
   * - Phone	
     - phone
     - "string"
   * - PostalCode
     - postCode
     - "string"
   * - PostalCode	
     - postCode
     - "string"
   * - Street
     - addressLine1
     - "string"


Salesforce Organization to Visma Company
----------------------------------------
Every Salesforce Organization will be synchronized with a Visma Company.

Once a link between a Salesforce Organization and a Visma Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Visma Company:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Visma Company Property
     - Visma Data Type
   * - ID
     - companyNo
     - "string"
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"


Salesforce Product2 to Visma Product
------------------------------------
Every Salesforce Product2 will be synchronized with a Visma Product.

Once a link between a Salesforce Product2 and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Visma Product Property
     - Visma Data Type
   * - Description
     - description
     - "string"
   * - Description	
     - description
     - "string"
   * - DisplayUrl
     - webPage
     - "string"
   * - DisplayUrl	
     - webPage
     - "string"


Salesforce Quote to Visma Country
---------------------------------
Every Salesforce Quote will be synchronized with a Visma Country.

Once a link between a Salesforce Quote and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Visma Country Property
     - Visma Data Type
   * - BillingCountry
     - name
     - "string"
   * - BillingCountryCode
     - isoCode
     - "string"
   * - ShippingCountry
     - name
     - "string"
   * - ShippingCountryCode
     - isoCode
     - "string"


Salesforce Quotelineitem to Visma Orderline
-------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Visma Orderline.

Once a link between a Salesforce Quotelineitem and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Visma Orderline Property
     - Visma Data Type


Salesforce User to Visma Country
--------------------------------
Every Salesforce User will be synchronized with a Visma Country.

Once a link between a Salesforce User and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - Visma Country Property
     - Visma Data Type
   * - Country
     - name
     - "string"
   * - CountryCode
     - isoCode
     - "string"

