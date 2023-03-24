Service level agreement and standardized refunds
================================================


Availability for the Services
-----------------------------

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

Capacity requirements
---------------------

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

Requirements for processing and reaction times
----------------------------------------------

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

Standardized penalties
----------------------

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
