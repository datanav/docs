.. _DTL:

=============================
 Data Transformation Language
=============================

|
|
|


.. panels::
    :body: text-left
    :container: container-lg pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2 custom-card

    **Reference Guide**

    DTL is a declarative language that allows developers to model data and clearly describe transformations that should be performed on streams of data in order to create new datasets.

    .. link-button:: dtl/introduction
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Quick reference: transforms**

    Transforms are functions that apply transformations to entities. These functions have side-effects.

    .. link-button:: quickref_dtl_transform_functions
            :type: ref
            :text: Read more
            :classes: read-more
    ---
    **Quick reference: expressions**

    Expressions are functions that return values. These functions do not have side-effects.

    .. link-button:: quickref_dtl_expression_functions
            :type: ref
            :text: Read more
            :classes: read-more

|


.. toctree::
   :maxdepth: 2
   :hidden:

   Introduction <dtl/introduction.rst>
   Annotated Example <dtl/annotated-example.rst>
   Built-in Variables <dtl/variables.rst>
   Path Expressions and Hops <dtl/paths.rst>
   How joins work <dtl/joins.rst>
   Namespace aware functions <dtl/namespaces.rst>
   DTL: Transforms <dtl/dtl-functions-transforms.rst>
   DTL: Boolean logic <dtl/dtl-functions-boolean-logic.rst>
   DTL: Booleans <dtl/dtl-functions-booleans.rst>
   DTL: Bytes <dtl/dtl-functions-bytes.rst>
   DTL: Comparisons <dtl/dtl-functions-comparisons.rst>
   DTL: Conditionals <dtl/dtl-functions-conditionals.rst>
   DTL: Date and time <dtl/dtl-functions-date-and-time.rst>
   DTL: Dictionaries <dtl/dtl-functions-dictionaries.rst>
   DTL: Encryption <dtl/dtl-functions-encryption.rst>
   DTL: Hops <dtl/dtl-functions-hops.rst>
   DTL: JSON <dtl/dtl-functions-json.rst>
   DTL: Lists <dtl/dtl-functions-lists.rst>
   DTL: Math <dtl/dtl-functions-math.rst>
   DTL: Misc <dtl/dtl-functions-misc.rst>
   DTL: Namespaced identifiers <dtl/dtl-functions-namespaced-identifiers.rst>
   DTL: Nested transformations <dtl/dtl-functions-nested-transformations.rst>
   DTL: Nulls <dtl/dtl-functions-nulls.rst>
   DTL: Numbers <dtl/dtl-functions-numbers.rst>
   DTL: Paths <dtl/dtl-functions-paths.rst>
   DTL: Sets <dtl/dtl-functions-sets.rst>
   DTL: Strings <dtl/dtl-functions-strings.rst>
   DTL: URIs <dtl/dtl-functions-uris.rst>
   DTL: UUIDs <dtl/dtl-functions-uuids.rst>
   Argument types <dtl/argument-types.rst>
   Supported Timezones <dtl/timezones.rst>
