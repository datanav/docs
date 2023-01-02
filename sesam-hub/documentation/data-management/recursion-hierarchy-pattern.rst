Defining hierarchies for recursion
----------------------------------
:ref:`Recursive hops <hops>` should be used when your data exhibits inverse relationships. Typically used when filtering on reference/classification properties.

An inverse relationship allows for you to `broaden or narrow <https://www.w3.org/TR/2005/WD-swbp-skos-core-guide-20051102/#sechierarchy>`_ the scope of your data.

When doing recursive hops, you should define the property ``max_depth`` to safeguard against never ending recursions.