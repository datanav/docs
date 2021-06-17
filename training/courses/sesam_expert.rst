
.. _sesam_intro:

=====================
Introduction to Sesam
=====================

Beginner Topics
---------------

   ###.. _different-types-of-architectures-1-1:###
   ###.. _datahub-1-1:###
   ###.. _the_parts_of_sesam-1-1:###
   ###.. _the_sesam_portal-1-1:###
   ###.. _naming-conventions-1-1:###
   ###.. _systems-1-1:###
   ###.. _pipes-1-1:###
   ###.. _datasets-1-1:###
   ###.. _entities-json-keyvalpairs-1-1:###
   ###.. _special-sesam-attributes-1-1:###
   ###.. _pipes-where-dtl-executes-3-1:###
   ###.. _entities-pipes-and-id-3-1:###
   ###.. _dtl-in-practice-3-1:###
   ###.. _pipe-interaction-with-systems.-2-1:###
   ###.. _systems-as-a-pipe-source-2-2:###
   ###.. _how-to-create-a-system-with-templates-2-1:###


Introduction to some case.
--------------------------

Represent a case which the reader/participants need to work through.
The case can include multiple dataflows and in total needs to entail the following:

* Multiple input pipes for the same type entity/concept. These must be merged into a global.
* One or more input pipes for different entities/concepts which connect to the main entity/concept. This/these pipe(s) must go into a global which will be hopped to.
* An endpoint system which is interested in the data we retrieve, connect and enhance.
* Possibility to design a dataflow (AC)
* Possibility to code a dataflow  (Dev)
* Possibility to design a integration (AC)
* Planning for eventual consistency (AC)
* Possibility of defining golden-properties. (AC & Dev)
* Microservice usage (AC)
* Microservice creation (Dev)
* Incremental queries/api usage (AC & Dev)
* Creating CLI tests. (Dev)
* Creating mapping files. (AC & Dev)
* Emit children (AC & Dev)
*

Creating a system
-----------------

Some task to make a system.

Creating an input pipe
----------------------

Some task to make an input pipe reading from system created previously.

THIS IS WHERE THE PATHS DIVERGE
-------------------------------

From here on out we will give different tasks and go into different depth
for the topics we bring up based on who is taking the course.

Most topics will be covered for both participant groups, but the perspective
shown and tasks given will be different.

For the context of this document I will annotate where AC(architect) and devs
differ for each topic.

DEV & AC
--------

   ###.. _globals-as-a-concept-1-1:###
   ###.. _joining-data-1-2:###
   ###.. _full-outer-join-merge-1-2:###

DEV
---

   ###.. _merge-as-a-source-3-2:###

DEV & AC
--------

   ###.. _global-1-2:###

Creating a global pipe
----------------------

Task to make a global pipe.
Devs will get the design (pipes to include and eq) and create the config.
Architects pick attributes to join on and get the config.

Important that only 1 answer for the eq produces the output we want - ikke no slingringsrom.

DEV & AC
--------

   ###.. _guidelines-inbound-and-outbound-pipes-1-2:###
   ###.. _change-tracking-data-delta-1-2:###

Creating a preparation pipe
---------------------------

DEV & AC
--------

Dev får info om funksjonaliteten, men fokuserer mer på configen
AC fokuserer mer på funksjonaliteten, men blir vist konfig & output.

   ###.. _left-join-hops-1-2:###
   ###.. _hops-3-2:###

Hopping with a preparation pipe
-------------------------------

A new preparation pipe which hops, reads from same global.
Uses some of the same values as the opther prep pipe but not 100% match.

Architects create the mapping and get almost the whole pipe config.
For example let them add all the "_S.someattribute" but have everything else ready

Devs create the pipe config and get the mapping.

The value of golden properties can now be understood as we have re-done mapping
twice.


Prioritization of data sources
------------------------------

FUN IDEA FOR A COURSE ONLY THING.
Course teachers act as DBA's / People responsible for two different systems.
We don't know anything about eachothers systems but know everything about our own.
The course participants must ask questions to us one at a time regarding what data
we care about, what data gets updated by our system and where the data we hold come from.

Then the participants must make real decisions when it comes to prioritizing
the origin of golden attributes based on the information we have provided.

No wrong answers as long as justification is good - possibility of showing how
easy it can be to interpret things differently.

Maybe let the DBA's talk to eachother after the participants have answered (?)

   ###.. _coalesce-3-2:###

Defining golden properties
--------------------------

Devs use the information above to code the coalesce's.
Architects use the information above to define the mapping and prioritization.

Using a microservice in prep pipe
---------------------------------

Dev, koder microservice eller bare bruker den?
AC går i dybden på hvorfor en microservice er en god løsning og ikke innebygd
sesam funksjon.

HVOR FETT HADDE DET VÆRT OM VI KJØRTE AC & DEV KURS SAMTIDIG
------------------------------------------------------------

AC gjør all design også kommer dev etterpå og implementerer det.
2 instruktører og 2 rom, som møtes for å gjøre oppgaver.
Perfekt mulighet for naturlig overførsel av informasjon fra arkitektur siden
til dev siden.
?????????? :D
