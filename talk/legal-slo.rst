Service level objective
================================================


Availability for the Services
-----------------------------

**Availability target** SESAM, as a SaaS, is provided with the target of
99.5% uptime per tenant. 

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


SESAM shall maintain a log of all events concerning downtime, with the
date and time of when downtime was reported, cause/symptom, solution and
duration of the downtime.


Requirements for processing and reaction times
----------------------------------------------

Upon errors in the Services, SESAM shall fulfill the following
requirements for processing and reaction:

.. list-table:: Reaction time target and correction time
   :widths: 5 35 10 10 30
   :header-rows: 1

   * - Level
     - Category
     - Partner
     - User
     - Correction target

   * - A
     - Critical error that is so serious
       that the entirety or significant
       parts of the Services are not
       available or not functioning
     - 8 hour
     - n/a
     - A workaround of the error
       shall be delivered without
       undue delay, and at the
       latest within
       * 3 days for Standard
       * n/a for Basic
       If this is not possible, a fix
       will be delivered within 10
       days.

   * - B
     - Errors that do not result in opration stoppages for the service.
     - 2 days
     - n/a
     - A workaround of the error
       shall be delivered within 10
       business days.

       If this is not possible, a fix
       will be delivered in the next
       release.
   * - C
     - Problems or questions that do not cause negative side in the service.
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


To ensure the compliance with these requirements, SESAM shall be able to
demonstrate that continuous monitoring of the Services is implemented,
and that measures are taken to optimize the performance.


