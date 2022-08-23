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

    DTL is a programming language that allows developers to model data and clearly describe transformations that should be performed on streams of data in order to create new datasets.

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
            :text: Ream more
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
   Argument types <dtl/argument-types.rst>
   DTL Transform Functions <dtl/transform-functions.rst>
   DTL Expression Functions <dtl/expression-functions.rst>
   Supported Timezones <dtl/timezones.rst>
