==============================
ZohoCRM to Membercare Dataflow
==============================

Generated: 2024-09-03 13:10:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Membercare Companies
---------------------------------------
Every ZohoCRM Account will be synchronized with a Membercare Companies.

Once a link between a ZohoCRM Account and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Account_Name
     - companyName
     - "string"
   * - Website
     - url
     - "string"


ZohoCRM Deal to Membercare Invoices
-----------------------------------
Every ZohoCRM Deal will be synchronized with a Membercare Invoices.

Once a link between a ZohoCRM Deal and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - Probability
     - creationInfo
     - "string"
   * - Probability
     - creditedInvoiceId
     - "string"
   * - Probability
     - creditedInvoiceLink
     - "string"
   * - Probability
     - deliverProductsTo
     - "string"
   * - Probability
     - eInvoiceInfo.accountingNo
     - "string"
   * - Probability
     - eInvoiceInfo.ean
     - "string"
   * - Probability
     - eInvoiceInfo.email
     - "string"
   * - Probability
     - eInvoiceInfo.reference
     - "string"
   * - Probability
     - eInvoiceInfo.requisitionNo
     - "string"
   * - Probability
     - eInvoiceInfo.url
     - "string"
   * - Probability
     - financeDate
     - "string"
   * - Probability
     - financeStatus
     - "string"
   * - Probability
     - incomeDate
     - "string"
   * - Probability
     - invoiceItems.buyer
     - "string"
   * - Probability
     - invoiceItems.buyer.addresses
     - "string"
   * - Probability
     - invoiceItems.buyer.anonymizedOn
     - "string"
   * - Probability
     - invoiceItems.buyer.businessNumbers
     - "string"
   * - Probability
     - invoiceItems.buyer.closeDate
     - "string"
   * - Probability
     - invoiceItems.buyer.closeReason
     - "string"
   * - Probability
     - invoiceItems.buyer.contacts
     - "string"
   * - Probability
     - invoiceItems.buyer.customFieldValues
     - "string"
   * - Probability
     - invoiceItems.buyer.dafualtPayerRule
     - "string"
   * - Probability
     - invoiceItems.buyer.debtorAccountNumber
     - "string"
   * - Probability
     - invoiceItems.buyer.defaultAddressType
     - "string"
   * - Probability
     - invoiceItems.buyer.defaultPayerLink
     - "string"
   * - Probability
     - invoiceItems.buyer.ean
     - "string"
   * - Probability
     - invoiceItems.buyer.einvoiceEan
     - "string"
   * - Probability
     - invoiceItems.buyer.einvoiceEmail
     - "string"
   * - Probability
     - invoiceItems.buyer.emailForInvoices
     - "string"
   * - Probability
     - invoiceItems.buyer.externalId
     - "string"
   * - Probability
     - invoiceItems.buyer.financeType
     - "string"
   * - Probability
     - invoiceItems.buyer.honorific
     - "string"
   * - Probability
     - invoiceItems.buyer.invoiceDistributionPreference
     - "string"
   * - Probability
     - invoiceItems.buyer.invoicesLink
     - "string"
   * - Probability
     - invoiceItems.buyer.lastChange
     - "string"
   * - Probability
     - invoiceItems.buyer.memberType
     - "string"
   * - Probability
     - invoiceItems.buyer.memberships
     - "string"
   * - Probability
     - invoiceItems.buyer.name
     - "string"
   * - Probability
     - invoiceItems.buyer.name1
     - "string"
   * - Probability
     - invoiceItems.buyer.name2
     - "string"
   * - Probability
     - invoiceItems.buyer.sendInvoicesTo
     - "string"
   * - Probability
     - invoiceItems.buyer.sendMailTo
     - "string"
   * - Probability
     - invoiceItems.buyer.socialSecurityNumber
     - "string"
   * - Probability
     - invoiceItems.buyer.url
     - "string"
   * - Probability
     - invoiceItems.creditedInvoiceItemId
     - "string"
   * - Probability
     - invoiceItems.creditedInvoiceLink
     - "string"
   * - Probability
     - invoiceItems.description
     - "string"
   * - Probability
     - invoiceItems.feeInfo.baseAmount
     - "string"
   * - Probability
     - invoiceItems.feeInfo.feeAmountInfo
     - "string"
   * - Probability
     - invoiceItems.feeInfo.period
     - "string"
   * - Probability
     - invoiceItems.feeInfo.rate
     - "string"
   * - Probability
     - invoiceItems.feeInfo.url
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.department
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.dimension3
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.dimension4
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.dimension5
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.productIdentification
     - "string"
   * - Probability
     - invoiceItems.financeDimensions.url
     - "string"
   * - Probability
     - invoiceItems.id
     - "string"
   * - Probability
     - invoiceItems.invoiceLink
     - "string"
   * - Probability
     - invoiceItems.isCredited
     - "string"
   * - Probability
     - invoiceItems.quantity
     - "string"
   * - Probability
     - invoiceItems.sequence
     - "string"
   * - Probability
     - invoiceItems.subscriptionInfo.transactionEnd
     - "string"
   * - Probability
     - invoiceItems.subscriptionInfo.transactionStart
     - "string"
   * - Probability
     - invoiceItems.subscriptionInfo.url
     - "string"
   * - Probability
     - invoiceItems.totalPrice
     - "string"
   * - Probability
     - invoiceItems.totalVat
     - "string"
   * - Probability
     - invoiceItems.unitPrice
     - "string"
   * - Probability
     - invoiceItems.url
     - "string"
   * - Probability
     - invoiceTexts.invoiceLink
     - "string"
   * - Probability
     - invoiceTexts.label
     - "string"
   * - Probability
     - invoiceTexts.labelId
     - "string"
   * - Probability
     - invoiceTexts.url
     - "string"
   * - Probability
     - invoiceTexts.value
     - "string"
   * - Probability
     - payer.addresses.addressDescription
     - "string"
   * - Probability
     - payer.addresses.addressLineOne
     - "string"
   * - Probability
     - payer.addresses.addressType
     - "string"
   * - Probability
     - payer.addresses.attention
     - "string"
   * - Probability
     - payer.addresses.careOf
     - "string"
   * - Probability
     - payer.addresses.country
     - "string"
   * - Probability
     - payer.addresses.end
     - "string"
   * - Probability
     - payer.addresses.floor
     - "string"
   * - Probability
     - payer.addresses.formattedAddress
     - "string"
   * - Probability
     - payer.addresses.id
     - "string"
   * - Probability
     - payer.addresses.lastChange
     - "string"
   * - Probability
     - payer.addresses.letter
     - "string"
   * - Probability
     - payer.addresses.location
     - "string"
   * - Probability
     - payer.addresses.municipality
     - "string"
   * - Probability
     - payer.addresses.number
     - "string"
   * - Probability
     - payer.addresses.postOfficeBox
     - "string"
   * - Probability
     - payer.addresses.postalCode
     - "string"
   * - Probability
     - payer.addresses.start
     - "string"
   * - Probability
     - payer.addresses.street
     - "string"
   * - Probability
     - payer.addresses.streetAndZipOneLine
     - "string"
   * - Probability
     - payer.addresses.suite
     - "string"
   * - Probability
     - payer.addresses.url
     - "string"
   * - Probability
     - payer.addresses.zipCityCountry
     - "string"
   * - Probability
     - payer.anonymizedOn
     - "string"
   * - Probability
     - payer.businessNumbers.debtorLink
     - "string"
   * - Probability
     - payer.businessNumbers.productionNumber
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumberCVR
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumberVAT
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumbersRUT
     - "string"
   * - Probability
     - payer.businessNumbers.registrationNumbersSE
     - "string"
   * - Probability
     - payer.businessNumbers.url
     - "string"
   * - Probability
     - payer.closeDate
     - "string"
   * - Probability
     - payer.closeReason.description
     - "string"
   * - Probability
     - payer.closeReason.id
     - "string"
   * - Probability
     - payer.closeReason.url
     - "string"
   * - Probability
     - payer.closeReason.valid
     - "string"
   * - Probability
     - payer.contacts.end
     - "string"
   * - Probability
     - payer.contacts.id
     - "string"
   * - Probability
     - payer.contacts.lastChange
     - "string"
   * - Probability
     - payer.contacts.start
     - "string"
   * - Probability
     - payer.contacts.type
     - "string"
   * - Probability
     - payer.contacts.url
     - "string"
   * - Probability
     - payer.contacts.value
     - "string"
   * - Probability
     - payer.customFieldValues
     - "string"
   * - Probability
     - payer.dafualtPayerRule
     - "string"
   * - Probability
     - payer.debtorAccountNumber
     - "string"
   * - Probability
     - payer.defaultAddressType
     - "string"
   * - Probability
     - payer.defaultPayerLink
     - "string"
   * - Probability
     - payer.ean
     - "string"
   * - Probability
     - payer.einvoiceEan
     - "string"
   * - Probability
     - payer.einvoiceEmail
     - "string"
   * - Probability
     - payer.emailForInvoices
     - "string"
   * - Probability
     - payer.externalId
     - "string"
   * - Probability
     - payer.financeType
     - "string"
   * - Probability
     - payer.honorific
     - "string"
   * - Probability
     - payer.invoiceDistributionPreference
     - "string"
   * - Probability
     - payer.invoicesLink
     - "string"
   * - Probability
     - payer.lastChange
     - "string"
   * - Probability
     - payer.memberType
     - "string"
   * - Probability
     - payer.memberships.affiliateDate
     - "string"
   * - Probability
     - payer.memberships.affiliationReason 
     - "string"
   * - Probability
     - payer.memberships.affiliationSource 
     - "string"
   * - Probability
     - payer.memberships.applicationDate
     - "string"
   * - Probability
     - payer.memberships.applicationProcessDate
     - "string"
   * - Probability
     - payer.memberships.applicationStatus
     - "string"
   * - Probability
     - payer.memberships.applicationStatusComment
     - "string"
   * - Probability
     - payer.memberships.closeDate
     - "string"
   * - Probability
     - payer.memberships.description
     - "string"
   * - Probability
     - payer.memberships.disaffiliateDate
     - "string"
   * - Probability
     - payer.memberships.disaffiliateReason 
     - "string"
   * - Probability
     - payer.memberships.enableGeographic
     - "string"
   * - Probability
     - payer.memberships.feeExempt
     - "string"
   * - Probability
     - payer.memberships.id
     - "string"
   * - Probability
     - payer.memberships.member 
     - "string"
   * - Probability
     - payer.memberships.membershipCategory 
     - "string"
   * - Probability
     - payer.memberships.membershipWeights 
     - "string"
   * - Probability
     - payer.memberships.url
     - "string"
   * - Probability
     - payer.name
     - "string"
   * - Probability
     - payer.name1
     - "string"
   * - Probability
     - payer.name2
     - "string"
   * - Probability
     - payer.sendInvoicesTo
     - "string"
   * - Probability
     - payer.sendMailTo
     - "string"
   * - Probability
     - payer.socialSecurityNumber.iso2Letter
     - "string"
   * - Probability
     - payer.socialSecurityNumber.number
     - "string"
   * - Probability
     - payer.url
     - "string"
   * - Probability
     - payments.amount
     - "string"
   * - Probability
     - payments.financeDimensions.department
     - "string"
   * - Probability
     - payments.financeDimensions.dimension3
     - "string"
   * - Probability
     - payments.financeDimensions.dimension4
     - "string"
   * - Probability
     - payments.financeDimensions.dimension5
     - "string"
   * - Probability
     - payments.financeDimensions.productIdentification
     - "string"
   * - Probability
     - payments.financeDimensions.url
     - "string"
   * - Probability
     - payments.financeStatus
     - "string"
   * - Probability
     - payments.id
     - "string"
   * - Probability
     - payments.invoiceId
     - "string"
   * - Probability
     - payments.invoiceLink
     - "string"
   * - Probability
     - payments.paymentDate
     - "string"
   * - Probability
     - payments.paymentIdentification
     - "string"
   * - Probability
     - payments.paymentSystemCardType
     - "string"
   * - Probability
     - payments.paymentType
     - "string"
   * - Probability
     - payments.shopOrderId
     - "string"
   * - Probability
     - payments.url
     - "string"
   * - Probability
     - payments.voucherNo
     - "string"
   * - Probability
     - recurringPaymentIdentification
     - "string"
   * - Probability
     - sendInvoiceTo
     - "string"
   * - Probability
     - source
     - "string"
   * - Probability
     - url
     - "string"


ZohoCRM Account to Membercare Countries
---------------------------------------
Every ZohoCRM Account will be synchronized with a Membercare Countries.

Once a link between a ZohoCRM Account and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Membercare Countries Property
     - Membercare Data Type
   * - Billing_Country
     - name
     - "string"
   * - Industry
     - name
     - "string"
   * - Shipping_Country
     - name
     - "string"


ZohoCRM Contact to Membercare Countries
---------------------------------------
Every ZohoCRM Contact will be synchronized with a Membercare Countries.

Once a link between a ZohoCRM Contact and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Membercare Countries Property
     - Membercare Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"

