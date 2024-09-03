==================================
SuperOffice to Membercare Dataflow
==================================

Generated: 2024-09-03 13:10:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Membercare Companies
-------------------------------------------
Every SuperOffice Contact will be synchronized with a Membercare Companies.

Once a link between a SuperOffice Contact and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Name
     - companyName
     - "string"
   * - Urls.Value
     - url
     - "string"


SuperOffice Quotealternative to Membercare Invoices
---------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Membercare Invoices.

Once a link between a SuperOffice Quotealternative and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - sesam_Accepted
     - creationInfo
     - "string"
   * - sesam_Accepted
     - creditedInvoiceId
     - "string"
   * - sesam_Accepted
     - creditedInvoiceLink
     - "string"
   * - sesam_Accepted
     - deliverProductsTo
     - "string"
   * - sesam_Accepted
     - eInvoiceInfo.accountingNo
     - "string"
   * - sesam_Accepted
     - eInvoiceInfo.ean
     - "string"
   * - sesam_Accepted
     - eInvoiceInfo.email
     - "string"
   * - sesam_Accepted
     - eInvoiceInfo.reference
     - "string"
   * - sesam_Accepted
     - eInvoiceInfo.requisitionNo
     - "string"
   * - sesam_Accepted
     - eInvoiceInfo.url
     - "string"
   * - sesam_Accepted
     - financeDate
     - "string"
   * - sesam_Accepted
     - financeStatus
     - "string"
   * - sesam_Accepted
     - incomeDate
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.addresses
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.anonymizedOn
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.businessNumbers
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.closeDate
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.closeReason
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.contacts
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.customFieldValues
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.dafualtPayerRule
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.debtorAccountNumber
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.defaultAddressType
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.defaultPayerLink
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.ean
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.einvoiceEan
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.einvoiceEmail
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.emailForInvoices
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.externalId
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.financeType
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.honorific
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.invoiceDistributionPreference
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.invoicesLink
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.lastChange
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.memberType
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.memberships
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.name
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.name1
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.name2
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.sendInvoicesTo
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.sendMailTo
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.socialSecurityNumber
     - "string"
   * - sesam_Accepted
     - invoiceItems.buyer.url
     - "string"
   * - sesam_Accepted
     - invoiceItems.creditedInvoiceItemId
     - "string"
   * - sesam_Accepted
     - invoiceItems.creditedInvoiceLink
     - "string"
   * - sesam_Accepted
     - invoiceItems.description
     - "string"
   * - sesam_Accepted
     - invoiceItems.feeInfo.baseAmount
     - "string"
   * - sesam_Accepted
     - invoiceItems.feeInfo.feeAmountInfo
     - "string"
   * - sesam_Accepted
     - invoiceItems.feeInfo.period
     - "string"
   * - sesam_Accepted
     - invoiceItems.feeInfo.rate
     - "string"
   * - sesam_Accepted
     - invoiceItems.feeInfo.url
     - "string"
   * - sesam_Accepted
     - invoiceItems.financeDimensions.department
     - "string"
   * - sesam_Accepted
     - invoiceItems.financeDimensions.dimension3
     - "string"
   * - sesam_Accepted
     - invoiceItems.financeDimensions.dimension4
     - "string"
   * - sesam_Accepted
     - invoiceItems.financeDimensions.dimension5
     - "string"
   * - sesam_Accepted
     - invoiceItems.financeDimensions.productIdentification
     - "string"
   * - sesam_Accepted
     - invoiceItems.financeDimensions.url
     - "string"
   * - sesam_Accepted
     - invoiceItems.id
     - "string"
   * - sesam_Accepted
     - invoiceItems.invoiceLink
     - "string"
   * - sesam_Accepted
     - invoiceItems.isCredited
     - "string"
   * - sesam_Accepted
     - invoiceItems.quantity
     - "string"
   * - sesam_Accepted
     - invoiceItems.sequence
     - "string"
   * - sesam_Accepted
     - invoiceItems.subscriptionInfo.transactionEnd
     - "string"
   * - sesam_Accepted
     - invoiceItems.subscriptionInfo.transactionStart
     - "string"
   * - sesam_Accepted
     - invoiceItems.subscriptionInfo.url
     - "string"
   * - sesam_Accepted
     - invoiceItems.totalPrice
     - "string"
   * - sesam_Accepted
     - invoiceItems.totalVat
     - "string"
   * - sesam_Accepted
     - invoiceItems.unitPrice
     - "string"
   * - sesam_Accepted
     - invoiceItems.url
     - "string"
   * - sesam_Accepted
     - invoiceTexts.invoiceLink
     - "string"
   * - sesam_Accepted
     - invoiceTexts.label
     - "string"
   * - sesam_Accepted
     - invoiceTexts.labelId
     - "string"
   * - sesam_Accepted
     - invoiceTexts.url
     - "string"
   * - sesam_Accepted
     - invoiceTexts.value
     - "string"
   * - sesam_Accepted
     - payer.addresses.addressDescription
     - "string"
   * - sesam_Accepted
     - payer.addresses.addressLineOne
     - "string"
   * - sesam_Accepted
     - payer.addresses.addressType
     - "string"
   * - sesam_Accepted
     - payer.addresses.attention
     - "string"
   * - sesam_Accepted
     - payer.addresses.careOf
     - "string"
   * - sesam_Accepted
     - payer.addresses.country
     - "string"
   * - sesam_Accepted
     - payer.addresses.end
     - "string"
   * - sesam_Accepted
     - payer.addresses.floor
     - "string"
   * - sesam_Accepted
     - payer.addresses.formattedAddress
     - "string"
   * - sesam_Accepted
     - payer.addresses.id
     - "string"
   * - sesam_Accepted
     - payer.addresses.lastChange
     - "string"
   * - sesam_Accepted
     - payer.addresses.letter
     - "string"
   * - sesam_Accepted
     - payer.addresses.location
     - "string"
   * - sesam_Accepted
     - payer.addresses.municipality
     - "string"
   * - sesam_Accepted
     - payer.addresses.number
     - "string"
   * - sesam_Accepted
     - payer.addresses.postOfficeBox
     - "string"
   * - sesam_Accepted
     - payer.addresses.postalCode
     - "string"
   * - sesam_Accepted
     - payer.addresses.start
     - "string"
   * - sesam_Accepted
     - payer.addresses.street
     - "string"
   * - sesam_Accepted
     - payer.addresses.streetAndZipOneLine
     - "string"
   * - sesam_Accepted
     - payer.addresses.suite
     - "string"
   * - sesam_Accepted
     - payer.addresses.url
     - "string"
   * - sesam_Accepted
     - payer.addresses.zipCityCountry
     - "string"
   * - sesam_Accepted
     - payer.anonymizedOn
     - "string"
   * - sesam_Accepted
     - payer.businessNumbers.debtorLink
     - "string"
   * - sesam_Accepted
     - payer.businessNumbers.productionNumber
     - "string"
   * - sesam_Accepted
     - payer.businessNumbers.registrationNumberCVR
     - "string"
   * - sesam_Accepted
     - payer.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - sesam_Accepted
     - payer.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - sesam_Accepted
     - payer.businessNumbers.registrationNumberVAT
     - "string"
   * - sesam_Accepted
     - payer.businessNumbers.registrationNumbersRUT
     - "string"
   * - sesam_Accepted
     - payer.businessNumbers.registrationNumbersSE
     - "string"
   * - sesam_Accepted
     - payer.businessNumbers.url
     - "string"
   * - sesam_Accepted
     - payer.closeDate
     - "string"
   * - sesam_Accepted
     - payer.closeReason.description
     - "string"
   * - sesam_Accepted
     - payer.closeReason.id
     - "string"
   * - sesam_Accepted
     - payer.closeReason.url
     - "string"
   * - sesam_Accepted
     - payer.closeReason.valid
     - "string"
   * - sesam_Accepted
     - payer.contacts.end
     - "string"
   * - sesam_Accepted
     - payer.contacts.id
     - "string"
   * - sesam_Accepted
     - payer.contacts.lastChange
     - "string"
   * - sesam_Accepted
     - payer.contacts.start
     - "string"
   * - sesam_Accepted
     - payer.contacts.type
     - "string"
   * - sesam_Accepted
     - payer.contacts.url
     - "string"
   * - sesam_Accepted
     - payer.contacts.value
     - "string"
   * - sesam_Accepted
     - payer.customFieldValues
     - "string"
   * - sesam_Accepted
     - payer.dafualtPayerRule
     - "string"
   * - sesam_Accepted
     - payer.debtorAccountNumber
     - "string"
   * - sesam_Accepted
     - payer.defaultAddressType
     - "string"
   * - sesam_Accepted
     - payer.defaultPayerLink
     - "string"
   * - sesam_Accepted
     - payer.ean
     - "string"
   * - sesam_Accepted
     - payer.einvoiceEan
     - "string"
   * - sesam_Accepted
     - payer.einvoiceEmail
     - "string"
   * - sesam_Accepted
     - payer.emailForInvoices
     - "string"
   * - sesam_Accepted
     - payer.externalId
     - "string"
   * - sesam_Accepted
     - payer.financeType
     - "string"
   * - sesam_Accepted
     - payer.honorific
     - "string"
   * - sesam_Accepted
     - payer.invoiceDistributionPreference
     - "string"
   * - sesam_Accepted
     - payer.invoicesLink
     - "string"
   * - sesam_Accepted
     - payer.lastChange
     - "string"
   * - sesam_Accepted
     - payer.memberType
     - "string"
   * - sesam_Accepted
     - payer.memberships.affiliateDate
     - "string"
   * - sesam_Accepted
     - payer.memberships.affiliationReason 
     - "string"
   * - sesam_Accepted
     - payer.memberships.affiliationSource 
     - "string"
   * - sesam_Accepted
     - payer.memberships.applicationDate
     - "string"
   * - sesam_Accepted
     - payer.memberships.applicationProcessDate
     - "string"
   * - sesam_Accepted
     - payer.memberships.applicationStatus
     - "string"
   * - sesam_Accepted
     - payer.memberships.applicationStatusComment
     - "string"
   * - sesam_Accepted
     - payer.memberships.closeDate
     - "string"
   * - sesam_Accepted
     - payer.memberships.description
     - "string"
   * - sesam_Accepted
     - payer.memberships.disaffiliateDate
     - "string"
   * - sesam_Accepted
     - payer.memberships.disaffiliateReason 
     - "string"
   * - sesam_Accepted
     - payer.memberships.enableGeographic
     - "string"
   * - sesam_Accepted
     - payer.memberships.feeExempt
     - "string"
   * - sesam_Accepted
     - payer.memberships.id
     - "string"
   * - sesam_Accepted
     - payer.memberships.member 
     - "string"
   * - sesam_Accepted
     - payer.memberships.membershipCategory 
     - "string"
   * - sesam_Accepted
     - payer.memberships.membershipWeights 
     - "string"
   * - sesam_Accepted
     - payer.memberships.url
     - "string"
   * - sesam_Accepted
     - payer.name
     - "string"
   * - sesam_Accepted
     - payer.name1
     - "string"
   * - sesam_Accepted
     - payer.name2
     - "string"
   * - sesam_Accepted
     - payer.sendInvoicesTo
     - "string"
   * - sesam_Accepted
     - payer.sendMailTo
     - "string"
   * - sesam_Accepted
     - payer.socialSecurityNumber.iso2Letter
     - "string"
   * - sesam_Accepted
     - payer.socialSecurityNumber.number
     - "string"
   * - sesam_Accepted
     - payer.url
     - "string"
   * - sesam_Accepted
     - payments.amount
     - "string"
   * - sesam_Accepted
     - payments.financeDimensions.department
     - "string"
   * - sesam_Accepted
     - payments.financeDimensions.dimension3
     - "string"
   * - sesam_Accepted
     - payments.financeDimensions.dimension4
     - "string"
   * - sesam_Accepted
     - payments.financeDimensions.dimension5
     - "string"
   * - sesam_Accepted
     - payments.financeDimensions.productIdentification
     - "string"
   * - sesam_Accepted
     - payments.financeDimensions.url
     - "string"
   * - sesam_Accepted
     - payments.financeStatus
     - "string"
   * - sesam_Accepted
     - payments.id
     - "string"
   * - sesam_Accepted
     - payments.invoiceId
     - "string"
   * - sesam_Accepted
     - payments.invoiceLink
     - "string"
   * - sesam_Accepted
     - payments.paymentDate
     - "string"
   * - sesam_Accepted
     - payments.paymentIdentification
     - "string"
   * - sesam_Accepted
     - payments.paymentSystemCardType
     - "string"
   * - sesam_Accepted
     - payments.paymentType
     - "string"
   * - sesam_Accepted
     - payments.shopOrderId
     - "string"
   * - sesam_Accepted
     - payments.url
     - "string"
   * - sesam_Accepted
     - payments.voucherNo
     - "string"
   * - sesam_Accepted
     - recurringPaymentIdentification
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo
     - "string"
   * - sesam_Accepted
     - source
     - "string"
   * - sesam_Accepted
     - url
     - "string"


SuperOffice Quoteline to Membercare Invoices
--------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Membercare Invoices.

Once a link between a SuperOffice Quoteline and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Membercare Invoices Property
     - Membercare Data Type


SuperOffice Sale to Membercare Invoices
---------------------------------------
Every SuperOffice Sale will be synchronized with a Membercare Invoices.

Once a link between a SuperOffice Sale and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Membercare Invoices Property
     - Membercare Data Type


SuperOffice Listcountryitems to Membercare Countries
----------------------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a Membercare Countries.

Once a link between a SuperOffice Listcountryitems and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - Membercare Countries Property
     - Membercare Data Type
   * - Name
     - name
     - "string"
   * - ThreeLetterISOCountry
     - iso3Letter
     - "string"
   * - TwoLetterISOCountry
     - iso2Letter
     - "string"

