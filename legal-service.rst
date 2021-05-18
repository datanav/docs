===========================
Description of the Services
===========================

1. Specification of the Services
================================

SESAM shall deliver the Services and complete the tasks related to the
Services as set out in section 1 and that is set out in the service
catalogue in the table below.

.. list-table:: Service specification
   :widths: 20 80
   :header-rows: 1

   * - SaaS-Service
     - Specification of tasks and contents of Sesam SaaS-Service
   * - 1. Description of the SaaS-Service
     - SESAM is a data-oriented integration platform delivered as a Service.
       Sesam consists of service instances that exposes an API (see
       http://docs.sesam.io for documentation). The Service instance can be
       configured through this API. The Service may be configured to fetch data
       from various systems and databases, and the data that is so collected and
       stored in SESAM. Such configuration may be performed by the Customer or
       by a separate consulting agreement between SESAM and Customer. API's
       are also used to transform and expose the stored data.

       The SaaS-Service consists of two applications:

       1. SESAM Integration Service that collects, connects and transforms data
       before it is routed to a receiving system or search engine.
       2. SESAM Data Browser, which is a search interface against structured
       data that links with data in a search index populated from the SESAM
       Integration Service.

       The SaaS-Service is secured with SSL-certificates that are unique for each
       Customer and through access controls that may be set for the stored data.
       Access to the SaaS-Service is through the currently supported interface
       published at sesam.io.

       The Service Instance reports operations-oriented metadata back to
       SESAM. These metadata are used to monitor the system's conditions and
       provides the Customer with the opportunity to receive notifications on the
       data flow in the service.
   * - 2. Requirements for scaleability
     - The SaaS-Service can be scaled both in terms of the number of Users,
       amounts of data and requirements for computing capacity.

       Storage scales automatically, while increased computing power, monitoring
       or SLA-changes can be selected via the My Page in the SESAM-portal.
   * - 3. Backup and securing data
     - SESAM shall keep the Customer's data logically separated from any third
       parties' data to limit the risk of data loss or unauthorized disclosure. By
       «logically separated» is meant that necessary technical measures securing
       the data against unwanted alteration and access are implemented.

       Backup of data may be selected as an optional service on My Page in the
       SESAM-portal. The cloud service, as a basis, only contains copies of data
       from other sources that the Customer has chosen to integrate with, and
       transformations of such data. Therefore, all data may be re-imported and
       recreated when needed for such sources. Re-creating from back-up may,
       however, be faster for large quantities of data.
   * - 4. Reconstruction of data
     - If data is lost or corrupted due to causes which SESAM is responsible for,
       SESAM shall re-establish the data from the latest backup within reasonable
       time and at SESAM's own cost, if not otherwise agreed below.

       SESAM's responsibility for costs is limited to the costs for re-establishment
       of the data from the latest backup, and additional costs that may arise due
       to SESAM not having performed backups as set forth in the Agreement.
       Costs attributable to reconstruction of data after the latest backup may only
       be attributed to SESAM if the data loss is due to gross negligence by
       SESAM. If the cause of the data loss is such that the Customer shall carry
       the costs, the Customer shall approve the scope of the work before it
       commences.
   * - 5. Notification of updates of the Services
     - Major updates and planned maintenance / downtime is notified through the
       SESAM Service Desk.
   * - 6. System documentation for the Services
     - SESAM is documented here: https://docs.sesam.io/overview.html
   * - 7. Third party cloud services included in the Services

          or

          Third party
          cloud services are included in the Services, but it is set forth in
          this agreement that the Customer will provide the operating
          environment
     - SESAM is delivered as a SaaS from virtual servers in Microsoft Azure
       Cloud. For Azure, separate terms of service apply from Microsoft: `Online Subscription Agreement <https://azure.microsoft.com/en-us/support/legal/subscription-agreement/?country=no&language=en>`_
       and `Online Services Terms <http://www.microsoftvolumelicensing.com/DocumentSearch.aspx?Mode=3&DocumentTypeId=46>`_.
       These terms are
       binding on the Customer as they are amended and updated by Microsoft at
       any given time.

       or

       It is agreed between the parties that the Customer will acquire and use
       another operating environment with their own terms of service, when using
       SESAM's Services. The Customer is responsible for entering into contract
       with the supplier of the operating environment.
   * - 8. The Customer's responsibility in connection with the Services
     - Configuring routers and firewalls for expanding the Customer's network to
       include the Services, included securing the network communication.
       Configuring access to applications to be integrated with the Service.
       SESAM will assist with specifications for network configuration.

2. Service level agreement and standardized refunds
===================================================

Since SESAM is delivered as SaaS, the Customer may consecutively select
capacity and service levels as required. The applicable selected
capacity and SLA-level will be defined at the Customer's My Page on the
SESAM-portal.

The Customer shall report errors to SESAM according to the following
procedure: Through SESAM Service Desk.

2.1. Availability for the Services
----------------------------------

**Availability target** SESAM, as a SaaS, is provided with the target of
99.5% uptime per installation (cf. production environment, test or
development, which corresponds to approximately 1 hour maximum unplanned
downtime per month for the individual installation.

**Planned downtime** SESAM, as a SaaS, is maintained and updated almost
continually. Planned maintenance is therefore nightly from 00:00 to
03:00 hours Central European Time.

Other planned maintenance shall be notified at least 48 hours in
advance.

**Definition of downtime** If a service's API or User interface is not
responding within a time period of ten minutes, this shall be considered
downtime. This is monitored and logged by the SESAM-service. It is not
considered downtime if the error is in the Customer's applications,
databases or other systems, or is due to downtime on the operating
environment.

Points accumulated on unplanned downtime (to be calculated per
installation):

On unplanned downtime, points are accumulated as set out below:

.. list-table:: Hours of downtime per month to points
   :widths: 30 30 40
   :header-rows: 1

   * - Hours from
     - Hours to
     - Number of points
   * - 1
     - 2
     - 4
   * - 2
     - 4
     - 8
   * - 4
     - 6
     - 12
   * - 6
     - 10
     - 15
   * - 10
     -
     - 25

Upon non-conformity with these requirements, any standardized penalties
set out under section 2.4 is to be calculated.

SESAM shall maintain a log of all events concerning downtime, with the
date and time of when downtime was reported, cause/symptom, solution and
duration of the downtime.

2.2. Capacity requirements
--------------------------

SESAM shall deliver on the following capacity requirements for the
Services:

For SESAM Search the capacity levels Basic, Standard and Enterprise can
be selected, which respectively guarantees 1, 5 and 10 RPS (Requests per
second).

The selected level upon start of the Service period is set out in the
price matrix in Appendix 2. If the Customer desires to change the level,
this can be done on the Customer's My Page on the SESAM-portal.

For other SESAM SaaS-Services, no quantified capacity requirements
apply.

2.3. Requirements for processing and reaction times
---------------------------------------------------

Upon errors in the Services, SESAM shall fulfil the following
requirements for processing and reaction:

.. list-table:: Reaction time target and correction time
   :widths: 5 35 10 10 10 30
   :header-rows: 1

   * - Level
     - Category
     - Enterprise
     - Standard
     - Basic
     - Correction target
   * - A
     - Critical error that is so serious
       that the entirety or significant
       parts of the Services are not
       available or not functioning
     - 1 hour
     - 8 hour
     - n/a
     - A workaround of the error
       shall be delivered without
       undue delay, and at the
       latest within

       * Next business day for Enterprise
       * 3 days for Standard
       * n/a for Basic

       If this is not possible, a fix
       will be delivered within 10
       days.
   * - B
     - Serious error that may be
       fixed with a work around, but
       which delay the usage of the
       Services
     - 4 hours
     - 2 days
     - n/a
     - A workaround of the error
       shall be delivered within 10
       business days.

       If this is not possible, a fix
       will be delivered in the next
       release.
   * - C
     - Less serious error, which
       does not entail delays in the
       usage of the Services
     - None
     - None
     - None
     - The error is evaluated with
       the goal of a fix in the next
       release in line with the
       normal release schedule.

All requirements in the table shall be calculated within SESAM's
standard business hours, 0800 -  1600 hours Central European time, excluding public holidays and other
holidays in Norway, and excluding Christmas Eve and New Year's Eve.
The vendor assigns the priority for reported errors.

With “reaction time” is meant the time from the Customer has reported
the error until SESAM has started the work on identifying the cause for
an error. The “correction time” is the time from the error has been
reported to SESAM until a temporary or permanent fix is implemented and
a normal situation for the Service has been re-established. The
correction time therefore includes the reaction time.

The above mentioned requirements do not apply for errors that are caused
by errors in the Customer's applications, databases or other systems.
Neither do the requirements apply for errors in the operating
environment, but SESAM shall in such cases report relevant errors to
supplier of the operating environment without undue delay.

The selected SLA-level upon start of the service period is set out in
the price matrix in Appendix 2. If the Customer desires to change the level, this can be done on the
Customer's My Page on the SESAM-portal.

To ensure the compliance with these requirements, SESAM shall be able to
demonstrate that continuous monitoring of the Services is implemented,
and that measures are taken to optimize the performance.

For each case of a non-adherence to the processing and reaction times
set out above, points are accumulated within a month as set out below:

.. list-table:: Point accumulation
   :widths: 30 15 15 15 15
   :header-rows: 1

   * - Description
     - Twice as long time
     - 4 times as long time
     - 8 times as long time
     - More than 8 times as long time
   * - Reaction time, Critical error (A)
     - 4 points
     - 6 points
     - 8 points
     - 10 points
   * - Reaction time, Serious error (B)
     - 2 points
     - 4 points
     - 6 points
     - 8 points
   * - Correction time, Critical error (A)
     - 4 points
     - 6 points
     - 8 points
     - 10 points
   * - Correction time, Serious error (B)
     - 2 points
     - 4 points
     - 6 points
     - 8 points

On this basis, standardized penalties are calculated as set out in
section 2.4 below.

2.4. Standardized penalties
---------------------------

Standardized penalties are calculated per installation (cf. production
environment, test or development) when actual measured availability (see
section 2.1.) or processing and reaction times (see section 2.3) in a
SLA measurement period deviates from the agreed level, with the
exception of errors due to the Customer or the Customer's other vendors.
If the deviation within an installation impacts on several
SLA-requirements, points are calculated only for the part of the service
(see either section 2.1 or 2.3) that results in the highest number of
points.

The invoicing period for services delivered and any standardized
penalties is in arrears every month.

The calculation basis for standardized penalties is the last monthly
subscription fee for the application installation in question. The
penalty is calculated as the given percentage of the calculation basis.
The maximum total standardized penalty is 40% of the subscription fee
for the Service for the installation in question in the same billing
period.

The deviation from the agreed service quality (SLA) is measured in the
number of points incurred by SESAM during a one-month period. Points are
calculated for reaction time, correction time and non-planned downtime
within the installation in question.

.. list-table:: Accumulated points to reduction of fee
   :widths: 20 20 60
   :header-rows: 1

   * - Points from
     - Points to
     - Reduction of monthly subscription fee for the relevant installation
   * - 1
     - 10
     - 0%
   * - 11
     - 20
     - -5%
   * - 21
     - 30
     - -10%
   * - 31
     - 40
     - -15%
   * - 41
     - 50
     - -20%
   * - 51
     - 60
     - -25%
   * - 61
     -
     - -40%
