==================================
SuperOffice to MemberCare Dataflow
==================================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to MemberCare Companies
-------------------------------------------
Every SuperOffice Contact will be synchronized with a MemberCare Companies.

Once a link between a SuperOffice Contact and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Name
     - companyName
     - "string"
   * - Urls.Value
     - url
     - "string"


SuperOffice Person to MemberCare Persons
----------------------------------------
Every SuperOffice Person will be synchronized with a MemberCare Persons.

Once a link between a SuperOffice Person and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - Address.Street.City
     - addresses.postalCode.city
     - "string"
   * - Address.Street.Zipcode
     - addresses.postalCode.zipCode
     - "string"
   * - BirthDate
     - birthDate
     - "string"
   * - Country.CountryId
     - addresses.country.id
     - "string"
   * - Emails.Value
     - socialSecurityNumber.number (Dependant on having wd:Q1273217 in socialSecurityNumber.iso2Letter)
     - "string"
   * - Firstname
     - firstname
     - "string"
   * - Lastname
     - lastname
     - "string"
   * - PersonId
     - addresses.id
     - "string"


SuperOffice Product to MemberCare Products
------------------------------------------
Every SuperOffice Product will be synchronized with a MemberCare Products.

Once a link between a SuperOffice Product and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - Name
     - name
     - "string"


SuperOffice Quotealternative to MemberCare Invoices
---------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a MemberCare Invoices.

Once a link between a SuperOffice Quotealternative and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - MemberCare Invoices Property
     - MemberCare Data Type
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
     - deliverProductsTo.addresses.addressDescription
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.addressLineOne
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.addressType
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.attention
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.careOf
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.country
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.end
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.floor
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.formattedAddress
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.id
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.lastChange
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.letter
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.location
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.municipality
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.number
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.postOfficeBox
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.postalCode
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.start
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.street
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.streetAndZipOneLine
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.suite
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.url
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.addresses.zipCityCountry
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.anonymizedOn
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.businessNumbers.debtorLink
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.businessNumbers.productionNumber
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.businessNumbers.registrationNumberCVR
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.businessNumbers.registrationNumberVAT
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.businessNumbers.registrationNumbersRUT
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.businessNumbers.registrationNumbersSE
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.businessNumbers.url
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.closeDate
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.closeReason.description
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.closeReason.id
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.closeReason.url
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.closeReason.valid
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.contacts.end
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.contacts.id
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.contacts.lastChange
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.contacts.start
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.contacts.type
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.contacts.url
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.contacts.value
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.customFieldValues
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.dafualtPayerRule
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.debtorAccountNumber
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.defaultAddressType
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.defaultPayerLink
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.ean
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.einvoiceEan
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.einvoiceEmail
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.emailForInvoices
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.externalId
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.financeType
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.honorific
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.invoiceDistributionPreference
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.invoicesLink
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.lastChange
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberType
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.affiliateDate
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.affiliationReason 
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.affiliationSource 
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.applicationDate
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.applicationProcessDate
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.applicationStatus
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.applicationStatusComment
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.closeDate
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.description
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.disaffiliateDate
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.disaffiliateReason 
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.enableGeographic
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.feeExempt
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.id
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.member 
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.membershipCategory 
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.membershipWeights 
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.memberships.url
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.name
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.name1
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.name2
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.sendInvoicesTo
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.sendMailTo
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.socialSecurityNumber.iso2Letter
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.socialSecurityNumber.number
     - "string"
   * - sesam_Accepted
     - deliverProductsTo.url
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
     - sendInvoiceTo.addresses.addressDescription
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.addressLineOne
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.addressType
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.attention
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.careOf
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.country
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.end
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.floor
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.formattedAddress
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.id
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.lastChange
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.letter
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.location
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.municipality
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.number
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.postOfficeBox
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.postalCode
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.start
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.street
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.streetAndZipOneLine
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.suite
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.url
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.addresses.zipCityCountry
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.anonymizedOn
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.businessNumbers.debtorLink
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.businessNumbers.productionNumber
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.businessNumbers.registrationNumberCVR
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.businessNumbers.registrationNumberNorwegianCompanyNumber
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.businessNumbers.registrationNumberSwedishCompanyNumber
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.businessNumbers.registrationNumberVAT
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.businessNumbers.registrationNumbersRUT
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.businessNumbers.registrationNumbersSE
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.businessNumbers.url
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.closeDate
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.closeReason.description
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.closeReason.id
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.closeReason.url
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.closeReason.valid
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.contacts.end
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.contacts.id
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.contacts.lastChange
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.contacts.start
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.contacts.type
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.contacts.url
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.contacts.value
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.customFieldValues
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.dafualtPayerRule
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.debtorAccountNumber
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.defaultAddressType
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.defaultPayerLink
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.ean
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.einvoiceEan
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.einvoiceEmail
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.emailForInvoices
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.externalId
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.financeType
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.honorific
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.invoiceDistributionPreference
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.invoicesLink
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.lastChange
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberType
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.affiliateDate
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.affiliationReason 
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.affiliationSource 
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.applicationDate
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.applicationProcessDate
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.applicationStatus
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.applicationStatusComment
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.closeDate
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.description
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.disaffiliateDate
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.disaffiliateReason 
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.enableGeographic
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.feeExempt
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.id
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.member 
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.membershipCategory 
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.membershipWeights 
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.memberships.url
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.name
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.name1
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.name2
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.sendInvoicesTo
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.sendMailTo
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.socialSecurityNumber.iso2Letter
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.socialSecurityNumber.number
     - "string"
   * - sesam_Accepted
     - sendInvoiceTo.url
     - "string"
   * - sesam_Accepted
     - source
     - "string"
   * - sesam_Accepted
     - url
     - "string"


SuperOffice Quoteline to MemberCare Invoices
--------------------------------------------
Every SuperOffice Quoteline will be synchronized with a MemberCare Invoices.

Once a link between a SuperOffice Quoteline and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - Description
     - invoiceItems.description
     - "string"
   * - Quantity
     - invoiceItems.quantity
     - "string"
   * - UnitListPrice
     - invoiceItems.unitPrice
     - "string"


SuperOffice Sale to MemberCare Invoices
---------------------------------------
Every SuperOffice Sale will be synchronized with a MemberCare Invoices.

Once a link between a SuperOffice Sale and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - MemberCare Invoices Property
     - MemberCare Data Type


SuperOffice Listcountryitems to MemberCare Countries
----------------------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a MemberCare Countries.

Once a link between a SuperOffice Listcountryitems and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - Name
     - name
     - "string"
   * - ThreeLetterISOCountry
     - iso3Letter
     - "string"
   * - TwoLetterISOCountry
     - iso2Letter
     - "string"

