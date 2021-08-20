
.. _tc_sesam_pro:

================
Get pro at Sesam
================

.. toctree::
   :maxdepth: 2

.. _tc_dev-ci-test-prod-nodes-4-3:

Multiple Sesam node environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

dev = personlig node der utvikling foregår

test = node som kjører samme config som prod med testdata for å finne
bugs

CI = do tests for pull requests /deployments before deploying.

prod = live node som kjører live integrasjoner

Tagging av brancher for deployment

.. _tc_using-a-microservice-as-output-in-sesam-5-3:

Using a Microservice as Output in Sesam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Ukjent: Business logikk

Eventual Consistency 1.4.30

NB!! \_properties blir med ut!! NB!!

Filter

\_filtered - blir ikke sendt videre

\_deleted - blir sendt videre

Endpoints fjerner namespaces

Batching/streaming

NB! siste batch sendt fra sesam er alltid en tom liste

.. _tc_chaining-5-4:

Chaining
~~~~~~~~

Ref advanced system 2.4.13.

.. _tc_create-child:

"Create-child"
~~~~~~~~~~~~~~

1-N

dep. Tracking, $children, emit_child transform type (2 pipes necessary
for all updates to propagate)

