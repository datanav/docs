=======
Pricing
=======

.. contents:: Table of Contents
   :depth: 2
   :local:

Introduction
------------

Self-hosted same price as cloud. Pricing is pr month. Up front payment. Data storage use is based on last day of previous month.

Subscription elements
---------------------

All subscriptions require compute.

Compute
=======

Abstract, indicator of how many concurrent pipes you can run. Small (intended for development), 1 Engine, max 40GB data limit, 100 EUR. Medium, 4 engines, max 350GB data limit, 800 EUR. Large, 8 engines max 750GB data limit, 1500 EUR. X-large, 16 engines max 1TB data limit, 3000 EUR. If data storage is more than 1TB you will be billed with an additional X-large compute for every TB above 1TB. As an example, if you have 4,5TB of data you will be billed with 5 quantities of X-large computes. 

Automatically upgraded if data use exceeds specified limits, but you can upgrade without data storage in case you want higher performance.

Data storage
============

Compressed internal storage, includes indexes and execution logs, 10 EUR pr GB.

VPN
===

Billed by storage use, 2 EUR pr GB. Setup is billed by the hour.

Geo-reduntant backup
====================

Billed by storage use, 2 EUR pr GB.

Warning: Note that by default no backups are made. Data and service configuration will be lost. 

SLA
===

Billed by storage use, but capped at 300GB. Basic is default and no additional cost. Standard 4h response 15 EUR pr GB. Enterprise 1h response 30 EUR pr GB. Premium 30m 24/7 100 EUR pr GB. Premium require fixed price minimum 300GB storage use (TODO check this).

Pipe monitoring
===============

Billed by enabled pipe. Standard (Insight) provides you with trends and statistics, 5 EUR pr pipe. Enterprise (Notification rules) provides you with alerts, 20 EUR pr pipe.

Sesam Access Portal
===================

Billed by storage use. Basic max 1 request pr second, 50 EUR pr GB. Standard max 5 requests pr second, 100 EUR pr GB. Enterprise max 10 requests pr second, 200 EUR pr GB.

Fixed price
-----------

Commit to a fixed data storage use. Half price for all storage based elements as long as data storage is kept below the fixed data storage. If data storage exceeds limit, the storage based prices for the excessive storage are doubled.

Partner program
---------------

To be eligible for the 15% discount the Partner must be a Sesam Certified Solution Partner. To qualify for the 15% disocunt, the Partner must run and drive the process, as well as invoice the Customer/End User. TODO link to PDF.
