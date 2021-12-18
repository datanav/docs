========
Patterns
========


.. contents:: Table of Contents
   :depth: 2
   :local:

We've identified a set of patterns when working with problems related to data flows in Sesam. We find it very useful
to name these patterns as it makes it easier to refer to it when discussing problems.

Here we present a list of them grouped by which step the problem manifests itself.

Collect patterns
================

Source with since but no deletions
----------------------------------
Provides data with changes but nothing about deletions. Requires periodic rescans. Called update-in-place
systems.

Source that only provides delta streams
---------------------------------------
If you restart the pipe you lose a lot of data, make two pipes (?), disable reset and use durable pipe,
disable deletion tracking.

Source with parameterized input
-------------------------------
Fetch more data based on some input source, requires rescan all the time, perhaps partial rescan could work?

Recreate best effort history from a source
------------------------------------------
We become master, pipe should be durable.

Make periodic entities from a versioned history
-----------------------------------------------
We do that in Sesam Sesam from the datasets we read Sesam Portal that only has a current view of the world in
latest.

Enrich patterns
===============

Extract foreign references as separate datatypes
------------------------------------------------
Don't make NIs to stuff that is outside your control, keep the namespace local to the system. Extract the
properties to new separate datatypes. If you don't have them as objects you can't merge them with the same concept from
other sources. Time is not a good candidate for NI. Postnummer is an example. If you make a ni make it reference your
own namespace. Use create.

Adding type information
-----------------------
Useful to pick out relevant subsets from the globals later. Add data type property (rdf:type or $type).

Flattening complex objects
--------------------------
Gives you flat structures. Can be easier to work with.

Splitting out lists of sub objects
----------------------------------
Aggregate objects, are the sub objects part of the parent or can they live on their own? Use create-child and
emit_children.

Connect patterns
================

Washing data
------------
Should be added as new properties, you might need the dirty data.

Manual merge
------------
Hardhoded dataset with manually connected ids, could also be an external source with manual input. Linking table.

External merge
--------------
AI connected objects, same pattern as manual merge. Duke is an example. Produces link objects.

Golden property based on priority
---------------------------------
Use coalesce.

Golden property based on last updated
-------------------------------------
Make sure you have a reliable timestamp from the source that you propagate. Think about feedback loops if data is
synced back.

Transform patterns
==================

Share patterns
==============
