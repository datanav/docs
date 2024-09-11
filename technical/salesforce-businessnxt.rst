==================================
Salesforce to BusinessNxt Dataflow
==================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Currencytype to Visma Country
----------------------------------------
Every Salesforce Currencytype will be synchronized with a Visma Country.

Once a link between a Salesforce Currencytype and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Visma Country Property
     - Visma Data Type


Salesforce Division to Visma Address
------------------------------------
Every Salesforce Division will be synchronized with a Visma Address.

Once a link between a Salesforce Division and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Visma Address Property
     - Visma Data Type
   * - Name
     - name
     - "string"


Salesforce Invoice to Visma Order
---------------------------------
Every Salesforce Invoice will be synchronized with a Visma Order.

Once a link between a Salesforce Invoice and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Visma Order Property
     - Visma Data Type
   * - FullSettlementDate
     - dueDate
     - "string"
   * - InvoiceDate
     - invoiceDate
     - "string"
   * - PostedDate
     - invoiceDate
     - "string"


Salesforce Invoiceline to Visma Order
-------------------------------------
Every Salesforce Invoiceline will be synchronized with a Visma Order.

Once a link between a Salesforce Invoiceline and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Visma Order Property
     - Visma Data Type


Salesforce Orderitem to Visma Order
-----------------------------------
Every Salesforce Orderitem will be synchronized with a Visma Order.

Once a link between a Salesforce Orderitem and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Visma Order Property
     - Visma Data Type


Salesforce Quote to Visma Order
-------------------------------
Every Salesforce Quote will be synchronized with a Visma Order.

Once a link between a Salesforce Quote and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Visma Order Property
     - Visma Data Type
   * - Discount
     - totalDiscountAmountInCurrency
     - "string"
   * - Name
     - name
     - "string"
   * - Tax
     - taxCode
     - "string"


Salesforce Quotelineitem to Visma Order
---------------------------------------
Every Salesforce Quotelineitem will be synchronized with a Visma Order.

Once a link between a Salesforce Quotelineitem and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - Visma Order Property
     - Visma Data Type


Salesforce Contact to BusinessNxt Country
-----------------------------------------
Every Salesforce Contact will be synchronized with a BusinessNxt Country.

Once a link between a Salesforce Contact and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Currencytype to BusinessNxt Currency
-----------------------------------------------
Every Salesforce Currencytype will be synchronized with a BusinessNxt Currency.

Once a link between a Salesforce Currencytype and a BusinessNxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a BusinessNxt Currency:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - BusinessNxt Currency Property
     - BusinessNxt Data Type


Salesforce Invoiceline to BusinessNxt Orderline
-----------------------------------------------
Every Salesforce Invoiceline will be synchronized with a BusinessNxt Orderline.

Once a link between a Salesforce Invoiceline and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type


Salesforce Order to BusinessNxt Country
---------------------------------------
Every Salesforce Order will be synchronized with a BusinessNxt Country.

Once a link between a Salesforce Order and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
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


Salesforce Order to BusinessNxt Order
-------------------------------------
Every Salesforce Order will be synchronized with a BusinessNxt Order.

Once a link between a Salesforce Order and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
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


Salesforce Orderitem to BusinessNxt Orderline
---------------------------------------------
Every Salesforce Orderitem will be synchronized with a BusinessNxt Orderline.

Once a link between a Salesforce Orderitem and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type
   * - OrderId
     - orderNo
     - "string"


Salesforce Organization to BusinessNxt Address
----------------------------------------------
Every Salesforce Organization will be synchronized with a BusinessNxt Address.

Once a link between a Salesforce Organization and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
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


Salesforce Organization to BusinessNxt Company
----------------------------------------------
Every Salesforce Organization will be synchronized with a BusinessNxt Company.

Once a link between a Salesforce Organization and a BusinessNxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a BusinessNxt Company:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - BusinessNxt Company Property
     - BusinessNxt Data Type
   * - ID
     - companyNo
     - "string"
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"


Salesforce Product2 to BusinessNxt Product
------------------------------------------
Every Salesforce Product2 will be synchronized with a BusinessNxt Product.

Once a link between a Salesforce Product2 and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
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


Salesforce Quote to BusinessNxt Country
---------------------------------------
Every Salesforce Quote will be synchronized with a BusinessNxt Country.

Once a link between a Salesforce Quote and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
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


Salesforce Quotelineitem to BusinessNxt Orderline
-------------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a BusinessNxt Orderline.

Once a link between a Salesforce Quotelineitem and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type


Salesforce User to BusinessNxt Country
--------------------------------------
Every Salesforce User will be synchronized with a BusinessNxt Country.

Once a link between a Salesforce User and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - Country
     - name
     - "string"
   * - CountryCode
     - isoCode
     - "string"

