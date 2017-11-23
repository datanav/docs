(This page describes how to configure a new installation of the
databrowser. It is intended for developers, not end-users.)

Databrowser configuration
=========================

Getting started
---------------

The rest of this document assumes that the databrowser is running on
http://localhost:6543 and is displaying the data from sesam.bouvet.no.

At this point the databrowser is using its default configuration, except
for the settings in the customized "databrowser.ini"-file that specify
which redis- and solr- servers to use. If you need to remove any old
(and/or wrong) configuration-settings, you can stop the redis-server,
delete the redis database and restart the redis-server and the
databrowser.

You should now be able to open a webbrowser on http://0.0.0.0:6543 and
see the databrowser startpage.

Specifying which itemtypes that appear in which section
-------------------------------------------------------

The unconfigured databrowser will display lots of different types of
items in the "Hvem", "Hvor" and "Hvordan" sections. This is because we
haven't yet specified which itemtypes should be displayed in these
sections (The "Hva"-section is configured in the default
"databrowser.ini"-file to only display topology information).

There are several ways of specifying what types of items should be
displayed in each section:

-  :ref:`Via the itemdetail view <section_types_via_itemdetail_view>`.
-  :ref:`Via the databrowser.ini file <section_types_via_databrowser_ini>`.
-  :ref:`Via the "Data types" adminpage <section_types_via_datatypes_adminpage>`.


.. _section_types_via_itemdetail_view:

Specifying what appears in the "Hvem"-section via the itemdetail view.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the "Hvem"-heading to to focus on the "Hvem"-section. The
section will expand to take up the full width of the screen, and will
display a "Hva" facetsection. The "Hva" facetsection will by default
display facetvalues from the "type"
(http://www.w3.org/1999/02/22-rdf-syntax-ns#type) attribute. The "Hva"
facetsection looks something like this:

::

    Hva
    297 hits
    #jiraaction (~200000)
    #worklog (~200000)
    #SBK (~100000)
    #jiraissue (~100000)
    #nodeassociation (~100000)
    #issuelink (~60000)
    #fileattachment (~50000)
    #LOG (~40000)
    #Underoppgave (~40000)
    #BKG_LOG (~40000)
                      ...

This tells us that the "Hvem" section is displaying all kinds of
non-person items. Lets fix that.

-  Click on the more-link of the "Hva" facetsection (the "..." in the
   bottom right corner). This will display more facetvalues.
-  Scroll down until you find the "#person" value (you may have to click
   the "more"-link more than once). Click the "#person"-value.
   This will make the "Hvem"-section only display items that has the
   type "person".
-  Click on the first search-result. This opens the itemdetail view.
-  Click on the "expand"-link if neccessary, to make the itemdetail view
   take up the whole browserwindow.
-  Click on the "edit"-button (The little pencil in the top right corner
   of the browserwindow)
-  At the top of the itemdetail view there will now be displayed all the
   types of the selected item. After each type name is listed the
   section that items of that type will appear in. Initially, all
   sections are "Unknown".
-  Click on the first "Unknown"-text after the "person"-type. This will
   open a dialogbox where you can select one of the "Hvem", "Hva",
   "Hvor", "Hvordan" sections. Select "Hvem".
-  Click on the sesam-logo in the top left corner. This will return you
   to the front page.

The "Hvem"-section will now only display persons.

.. _section_types_via_databrowser_ini:

Specifying what appears in the "Hvor"-section via the "databrowser.ini" file.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The "Hvor"-section still display all types of items. Lets fix that. We
could do it in the same way as for the "Hvem"-section, but instead we
will do it via the "databrowser.ini"-file. Lets assume that we want the
"Hvor"-section to display projects from jira and currenttime, and that
we know the ids of those types.

Use your favorite texteditor to open the "databrowser.ini"-file that you
created when you set up the databrowser to run locally. Add the
following lines to the "databrowser.ini"-file:

::

    [where]
    types=
        http://data.bouvet.no/sesam/jira/project
        http://data.bouvet.no/sesam/currenttime/project
        

Save the databrowser.ini file, restart the databrowser and go to the
front page. The "Hvor"-section will now only display projects and tasks.

.. _section_types_via_datatypes_adminpage:

Specifying what appears in the "Hva"-section via the "Data types" adminpage.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The "Hvordan"-section still display all types of items. Lets fix that,
too. This time we will use the third and final way: the "Data types"
adminpage. This is a special page that displays all the datatypes and
lets you specify (among other things) the sections that items a certain
datatype should appear in.

Lets assume that we want to display jira-issues in the
"Hvordan"-section.

::

    * Click on the "Admin pages"-link at the bottom of the screen. This opens a new page with a couple of links. 
    * Click the "Data types"-link. This opens the "Data types" adminpage.
    * Under the "Item types" heading:  
      Find the row for the "http://data.bouvet.no/sesam/jira/jiraissue" itemtype and click the "Unknown"-text 
    to bring up the dialogbox that lets you select the section
    * Select "Hvordan" and click the submitbutton
    * Click the sesam-logo in the top left corner to go back to the front page

The "Hvordan"-section will now only contain jiraissues.


.. _facetsection_assignment:

Specifying what appears in which facetsection
---------------------------------------------

The unconfigured databrowser will only display the "Hva" facetsection.
The "Hva" facetsection has been configured in the default
"databrowser.ini"-file to display facetvalues from the "type"
(http://www.w3.org/1999/02/22-rdf-syntax-ns#type) attribute.

We can add additional attributes to the facetsections in three different
ways: There are several ways of specifying what attributetypes should be
displayed in each facetsection:


-  :ref:`Via the itemdetail view <facetsection_via_itemdetail_view>`.
-  :ref:`Via the databrowser.ini file <facetsection_via_databrowser_ini>`.
-  :ref:`Via the "Data types" adminpage <facetsection_via_datatypes_adminpage>`.


.. _facetsection_via_itemdetail_view:

Specifying what appears in the "Hvor"-facetsection via the itemdetail view.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the "Hvem"-heading to to focus on the "Hvem"-section. The
section will expand to take up the full width of the screen, and will
display a "Hva" facetsection. Only the "Hva" facetsection will be
visible at this point.

Lets assume that we want to have a "Hvor" facetsection that displays the
values of the "departmentid" attribute.

-  Go to the front page and click on the first searchresult in the
   "Hvem"-section
-  Click on the "expand"-link if neccessary, to make the itemdetail view
   take up the whole browserwindow.
-  Click on the "edit"-button (The little pencil in the top right corner
   of the browserwindow)
-  Find the "departmentid" label and click on it. This opens a dialog
   where you can configure the attribute.
-  Select "Hvor" in the "Facet section" dropdown and click the
   submit-button.
-  Click on the sesam-logo in the top left corner to go back to the
   front page
-  Click on the "more"-link in the bottom right corner of the
   "Hvem"-section

The "Hvem"-section will now display a "Hvor"-facetsection (in addition
to the old "Hva"-facetsection).

.. _facetsection_via_databrowser_ini:

Specifying what appears in the "Hvordan"-facetsection via the "databrowser.ini" file.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lets assume that we want to have a "Hvordan"-facetsection that displays
the values of the "employee\_\_updateby"-attribute.

We could do it in the same way as for the "Hvor"-facetsection, but
instead we will do it via the "databrowser.ini"-file.

Use your favorite texteditor to open the "databrowser.ini"-file that you
created when you set up the databrowser to run locally. Add the
following lines:

::

    [how]
    facets=
        http://data.bouvet.no/sesam/currenttime/employee__updateby
        

-  Save the databrowser.ini file, restart the databrowser and go to the
   front page.
-  Click on the "more"-link in the bottom right corner of the
   "Hvem"-section

The "Hvem"-section will now display a "Hvordan"-facetsection.

.. _facetsection_via_datatypes_adminpage:

Specifying what appears in the "Hvem"-facetsection via the "Data types" adminpage.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lets assume that we want to have a "Hvem"-facetsection that displays the
values of the "RES\_\_RES\_TEXT1"-attribute (whatever that is, I (knutj)
just picked a random attribute that referred to another person).

We could do this either via the :ref:`itemdetail view <facetsection_via_itemdetail_view>`
or via the :ref:`the databrowser.ini file <facetsection_via_databrowser_ini>`, but instead
we will do it in a third way: via the "Data types" adminpage.

-  Click on the "Admin pages"-link at the bottom of the screen. This
   opens a new page with a couple of links.
-  Click the "Data types"-link. This opens the "Data types" adminpage.
-  Under the "Attribute types" heading:
-  Find the row for the
   "http://data.bouvet.no/sesam/retain/RES\_\_RES\_TEXT1" attributetype
   and click the label. to bring up the dialogbox that lets you
   configure the attributetype. This is the same dialogbox that would
   appear if you configured the attribute via the itemdetail view.
-  In the "Facetsection"-dropdown: Select "Hvem"
-  Click the submitbutton
-  Click the sesam-logo in the top left corner to go back to the front
   page
-  Click on the "more"-link in the bottom right corner of the
   "Hvem"-section

The "Hvem"-section will now display a "Hvem"-facetsection (in addition
to the other facetsections that were already present).

.. _display_fields_assignment:

Display fields
--------------

Display fields are sets of fields that are displayed in a special way.
There are four sets of display fields:

-  | type:
   | Specifies the field(s) that will be used when displaying the
     type(s) of an item.

-  | title:
   | Specifies the field(s) that will be used when displaying the
     title(s) of an item.

-  | description:
   | Specifies the field(s) that will be used when displaying the
     description(s) of an item (i.e. in ItemContainer).

-  | date:
   | Specifies the field(s) that will be used when displaying the dates
     of an item (i.e. in ItemContainer).

As with the :ref:`facetsection <facetsection_assignment>` assignments, the
display fields can be configured in several different ways: via the
itemdetail view, via the "databrowser.ini"-file and via the "Data types"
adminpage.

For brevity's sake, we will only look at the itemdetail view way here.
Lets assume that we want to add the field "description" to the
"description" display fields set.

-  Go to the front page and click on the first searchresult in the
   "Hvem"-section
-  Click on the "expand"-link if neccessary, to make the itemdetail view
   take up the whole browserwindow.
-  Click on the "edit"-button (The little pencil in the top right corner
   of the browserwindow)
-  Find the "description" label and click on it. This opens a dialog
   where you can configure the attribute.
   NOTE: not all person-items have the "description"-field. If you
   cannot find it, try again with another person.
-  Select "Beskrivelse" in the "Display field" dropdown and click the
   submit-button.
-  Click on the "edit"-button again to leave edit-mode and make the
   itemdetail view re-render.

The text in the "description"-field will now appear beneath the
item-titles.

Search fields
-------------

Search fields are sets of fields that are used for searching in various
way. There are several sets of display fields:

.. _databrowser_ini_ID_FIELDS:

-  | id:
   | These fields are used when trying to locate an item based on one of
     the items ids.

-  | type:
   | The "type" and "indirecttype" specifies the field(s) that will be
     used when searching for items of a specific type.

-  title: Used when searching for an item based on its name; i.e when a
   #Facetvalue has been selected.

-  | email:
   | used to look up information related to a used based on the users
     email address

-  | related:
   | Used when lookup up items that are related. The default value
     "entities" is a special field into which solr is configured to copy
     the values of all the "psi\* fields (i.e. everything that the item
     points to).

-  | date:
   | Used when narrowing the searchresults based on a date-range (by
     using the data-range slider next to the searchtext-box)

As with the :ref:`display fields <display_fields_assignment>` assignments,
the display fields can be configured in several different ways: via the
itemdetail view, via the "databrowser.ini"-file and via the "Data types"
adminpage.

Item attributes
---------------

By default, the itemdetail view displays all the attributes of the item
in a random order. It is usually neccessary to hide some of the
attributes, and to organize them into logical groups. This is done via
the edit-mode on the itemdetail view:

-  Go to the front page and click on the first searchresult in the
   "Hvem"-section
-  Click on the "expand"-link if neccessary, to make the itemdetail view
   take up the whole browserwindow.
-  Click on the "edit"-button (The little pencil in the top right corner
   of the browserwindow)
-  Click on some attribute; this opens a dialogbox that lets you change
   how the attribute is rendered.
-  Change the attributes label and group to for instance "Test label"
   and "Test group" and click on the submit-button
-  Click on the "edit"-button again to re-render the itemdetail view
   with the new settings

The attribute will now appear in the new group "Test group", and be
labeled "Test label".

Specifying how the itemdetail view is rendered
----------------------------------------------

It is possible to change how the itemdetail view is rendered by adding
an installation-specific "itemdetailrenderers.yaml"-file (put it in the
same folder as the installation-specific "databrowser.ini" file). The
rendering can be configure for all itemtypes, or for one specific type.

The default 'itemdetailrenderers.yaml'
file contains examples and documentation on how this is done.

Specifying how the searchresults are rendered
---------------------------------------------

It is possible to change how each searchresults item are rendered by
adding an installation-specific "resultitemrenderers.yaml"-file (put it
in the same folder as the installation-specific "databrowser.ini" file).
The rendering can be configure for all itemtypes, or for one specific
type.

The default 'itemdetailrenderers.yaml' file contains examples and documentation on how this is done.

Specifying how the searchresults are rendered
---------------------------------------------

It is possible to change how each section is rendered by adding an
installation-specific "sectionrenderers.yaml"-file (put it in the same
folder as the installation-specific "databrowser.ini" file). The default
configuration adds a map to the "where"-section if any of the display
searchresult items in the where section contains geo-location
information.

The default 'sectionrenderers.yaml' file contains examples and documentation
on how this is done.
