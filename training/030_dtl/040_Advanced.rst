.. _dtl-advanced:

Advanced
--------


.. _more-on-pipes-3-3:

More on pipes
~~~~~~~~~~~~~

How do you deploy changes to logic?
Maybe you don't want to resend old data
which will be changed?
f.ex disable endpoint,
reset upstream pipe
reset endpoint to end
enable endpoint

how to setup dead letter?
how does write-error:xxx : {resolved: true} work?
dead = false + retryable = false = resolved…
niche stuff.

• Pump

○ Dead-letter…

• Metadata

• Reset-to-end

• Stop

• Enable/disable

.. seealso::

  TODO

.. _if-3-3:

"if" as an expression and transform.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. seealso::

  TODO

.. _case-case-eq-3-3:

Case & case-eq
~~~~~~~~~~~~~~

also both and expression and transform

.. seealso::

  TODO

.. _multiple-transforms-3-3:

Multiple transforms
~~~~~~~~~~~~~~~~~~~

what can you do in the first transform?
what can't you do in the first transform?
lead into dependency tracking, next topic

.. seealso::

  TODO

.. _dependency-tracking-in-hops-3-3:

Dependency tracking in Hops
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When does dependency tracking work? How does it work? When doesn’t it
work (multiple transforms) Ref 1.3.25

.. seealso::

  TODO

.. _apply-hops-3-3:

"Apply-hops"
~~~~~~~~~~~~

Apply a function to the entities retrieved by your hop

.. seealso::

  TODO

.. _source-subset-3-3:

Source Subset
~~~~~~~~~~~~~

use subset to speed up processing & minimize
replica size.

.. seealso::

  TODO


.. _filter-as-an-expression:

Filter as an expression
~~~~~~~~~~~~~~~~~~~~~~~

VS as a transform (filter objects in list)

.. seealso::

  TODO

.. _underline-dot-syntax-and-functions:

\_. Syntax and Functions
~~~~~~~~~~~~~~~~~~~~~~~~

\_. : path, map, filter, what does it reference? How does it work?

.. seealso::

  TODO

.. _map:

Map
~~~

Map, map-values, map-dict

.. seealso::

  TODO

.. _underline-P-underline-R:

\_P & \_R – Parent & Root
~~~~~~~~~~~~~~~~~~~~~~~~~

How do I use \_P. notation? Where does it point?
Where do I use it?

.. seealso::

  TODO

.. _create-child:

"Create-child"
~~~~~~~~~~~~~~

1-N

dep. Tracking, $children, emit_child transform type (2 pipes necessary
for all updates to propagate), reference Archi Adv

.. seealso::

  TODO

.. _recursion-in-hops-apply:

Recursion in Hops & Apply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I have never written a recursive hop,
but they are a thing…

.. seealso::

  TODO

.. _key-values:

Key-values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

explicitly the key-values function,
split up an entities properties into
{key: value} dicts in a list, to run f.ex
map, filter out null values, etc.

can even do [add, _.key, _.value] in a map!

.. seealso::

  TODO

.. _escape-namespaced-identifiers-ni:

Escape Namespaced Identifiers [ni]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add ::hello to escape namespace, like
rdf:type, we manually set the namespace to rdf

useful for debugging - want something at the
top of preview? [add ::$test <expr>]

.. seealso::

  TODO

.. _tasks-for-dtl-advanced:

3.4 Tasks for DTL: Advanced
~~~~~~~~~~~~~~~~~~~~~~~~~~~

convert a hop to apply-hops
use _R.property and _P.property and get different results
combine map and filter
