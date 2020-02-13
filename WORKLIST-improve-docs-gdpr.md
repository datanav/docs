# WORKLIST improve-docs-gdpr branch
A list of what need to be done/looked into and open questions.
The feature branch improve-docs-gdpr is focused on improving the documentation of the Sesam GDPR Platform.
First focus is the "Getting started" section.

## TODO
    [x] Ask for GDPR dev node
    [ ] Mention Data Protection Official/Officer (personvernombud) (or should this be in https://sesam.io/privacy/ ?)
    [ ] Harmonize with general "Getting started with Sesam" and sesam.io
        [x] Mirror structure: Overview, Getting started, detailed thematic sections
        [x] https://sesam.io/privacy https://sesam.io/privacy/howitworks/technical-features.html info@sesam.io https://support.sesam.io
        [x] sureway.no and other partner solutions? https://sesam.io/privacy/partners/
    [x] salesforce-lead.json correct error in json formating
    [x] report bugs in frontend (is now fixed in beta.portal but not regular)
    [x] reported no horizontal scrolling tables Purposes/Data types/Policies. Risk of Edit column not showing.
    [x] report dead link https://sesam.io/gdpr/price-calculator/index.html (is now fixed)
    [ ] all required fields in webforms and excel templates should be documented. Effects. (But in getting-started?)
    [ ] modify examples to be easier to relate to common GDPR tasks and better "flow" in names. Describe example case/objectives first?
    [ ] images/gdpr-getting-started/purpose-creation.png update to show ALL required fields.
    [ ] images/gdpr-getting-started/data-type-creation.png update to show ALL required fields. (fields reqired for automation are missing)
    [ ] images/excel-data-type-example.png show sheet in template for data types too
    [ ] image that map side effects of adding Purposes and Data types.
    [ ] Short about default GDPR rolls
    [ ] Explanations central GDPR-pipes (admin). Filtered out as default. In graph. Monitoring. (But in getting-started?)
    [ ] Distinctions excel-setup/webform-setup
    [ ] show and explain general elements in Data Access Platform. E.g. "Purpose", "Your data", filter boxes and how this is related to your setup
    [ ] explain/introduce Policies tab related to Purpose (But in getting-started?)
    [ ] explain/introduce Translations (But in getting-started?)
    [ ] explain/introduce 
    [ ] Advanced example: Sesam GDPR node to support export anatomized data sets for analysis.(But in getting-started?)
    [ ] "Handle data request as system owner" - specify where sheet names come from
    [x] rapport problems with webforms. Filled out fields get blanked out in overview lists and i fields if you try to edit with webform.
    [ ] info about the Data browser? How to make data editable to user (change request)
    [ ] Write that "forced" naming of purpose, "<Type> for <System>", might lead to "strange" purpose title if <Type> not carefully selected.
    [ ] how to test portal as admin (challenges and tricks)
        [ ] delay
        [ ] cookies in browser
        [ ] SMS
        [ ] email
        [ ] The query is a point-in-time query and as such reflects the state of the document index at that point in time. To update the search result, a new GDPR access request must be submitted by the data subject.

## CHECK
    [ ] Documentation as marketing?
    [ ] General update of gdpr documentation and not only getting started? Getting started should be terse and reference general documentation for details.
    [ ] Is https://sesam.io/privacy/howitworks/technical-features.html over promising? Some features are at least not documented. E.g. "Communication of personal data breach".
    [x] Prizing or possibility for a "Click on Request private trial - GDPR Platform" (prizing see https://sesam.io/privacy/)
    [x] emailing to contact person is not working in my test node. (working when setup with excel). 
        [ ] webform setup missing something?
    [x] not receiving access request emails as system owner (working when setup with excel). 
        [ ] webform setup missing something?
    [ ] rolls. Add one of the other consultants and check different rolls.
    [ ] should privacy in grate extent be used instead of GDPR term throughout documentation?
    [ ] gdpr-template-excel-setup-data "gdpr-template-excel-setup-data:sesam_excel_setup_type": "sesam-gdpr:datatype"/"sesam-gdpr:purpose" switched? logic upstream seem to be swished too and counteract this.
    [ ] data-source and data-target is NOT? systems? but more general descriptive text?
    [x] name on tabs on Request template for system owners. Where does the names come from? Data types? If so, Data types from webform is not showing up. ("Data types" are name of tabs. Working with excel but not webforms)
    [x] Column named Purpose in purpose sheet in example excel template file need to be named PurposeDescription to show in Description column i GDPR menu Purposes tab (is transformed to gdpr-purpose:description in gdpr-purpose pipe).
    [ ] excel templates latest version? 
    [ ] Inconsistency in explanation of value of TypeID. rdf:type in getting started and data set id in excel template (hyphen or colon?) https://docs.sesam.io/gdpr-platform-developer-docs.html#the-additional-data-type-properties what is the Related "chain"? (from gdpr-template-subject-data-link it looks like rdf:type is correct)
    [x] TypeID value data set ID (excel template help note) or rdf:type (gdpr getting started) (from gdpr-template-subject-data-link it looks like rdf:type is correct)
    [ ] Identifiers and TypeID fields are missing from Create new data type dialog.
    [ ] Valid data type levels in excel templates are Personal and Related. The webform also have Sensitive.
    [ ] How do you clean up node after testing examples and you want to set up your own node from scratch? Ask support for a reset? Many pipes can not be edited or started/restarted without portal admin powers.
    [ ] mixing access requests with email and phone number as id
    [ ] MUST use explicit country code for request with phone number as ID?? Phone_number in entity MUST be with country code?? (that is how I made it work in portal, or was it delay "magic"?)

## Open questions
    [ ] Distinction of products?
        - Sesam - core node?
        - Open Sesam?
        - Sesam GDPR platform?
            - Workflow?
            - Automatic?
    [ ] What to do about the detailed thematic sections? Getting started is more up to date.
        E.g. the "Data types and purposes configuration" section is only about excel setup. 
    [ ] Data browser documentation is not so recognizable in GDPR portal context https://docs.sesam.io/databrowser-guide.html is it up to date?
    [ ] https://docs.sesam.io/gdpr-platform-developer-docs.html#the-additional-data-type-properties """The "level" of the data - it can be either "Personal" or "Related", i.e. directly about the data subject or indirectly (for example data about the customer such as address or orders for the customer, respectively)
    If the level property is Related it will be matched to the closest "parent" record with the top-most in such a chain being matched with subject record (a "Personal" level data type".""" What does this mean?
    [ ] The Sensitive level is not mentioned in Getting started - should it? It is a choice in webform.
    What is the anonymizedEmail in GDPR Access request?
    [ ] https://docs.sesam.io/gdpr-getting-started.html#gdpr-unstructured-data-handling what about