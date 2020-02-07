# WORKLIST improve-docs-gdpr branch
A list of what need to be done/looked into and open questions.
The feature branch improve-docs-gdpr is focused on improving the documentation of the Sesam GDPR Platform.
First focus is the "Getting started" section.

## TODO
    [x] Ask for GDPR dev node
    [] Harmonize with general "Getting started with Sesam" and sesam.io
        [x] Mirror structure: Overview, Getting started, detailed thematic sections
        [x] https://sesam.io/privacy https://sesam.io/privacy/howitworks/technical-features.html info@sesam.io https://support.sesam.io
        [x] sureway.no and other partner solutions? https://sesam.io/privacy/partners/
    [x] salesforce-lead.json correct error in json formating
    [x] report bugs in frontend (is now fixed in beta.portal but not regular)
    [x] report dead link https://sesam.io/gdpr/price-calculator/index.html (is now fixed)
    [ ] all required fields in webforms and excel templates should be documented. Effects. (But in getting-started?)
    [ ] modify examples to be easier to relate to common GDPR tasks and better "flow" in names. Describe example case/objectives first?
    [ ] images/gdpr-getting-started/purpose-creation.png update to show ALL required fields.
    [ ] images/gdpr-getting-started/data-type-creation.png update to show ALL required fields.
    [ ] images/excel-data-type-example.png show sheet in template for data types too
    [ ] image that map side effects of adding Purposes and Data types.
    [ ] Short about default GDPR rolls
    [ ] Explanations GDPR-pipes (admin). Filterd out as default. In graph.
    [ ] Distinctions excel-setup/webform-setup
    [ ] show and explain general elements in Data Access Platform. E.g. "Purpose", "Your data", filterboxes and how this is related to your setup
    [ ] explain/introduce Policies tab related to Purpose
    [ ] explain/introduce Translations 
    [ ] explain/introduce 
    [ ] Advanced example: Sesam GDPR node to support export anatomized data sets for analysis. 
    [ ] "Handle data request as system owner" - specify where sheet names come from
    [x] rapport problems with webforms. Filled out fields get blanked out in overview lists and i fields if you try to edit with webform.
    [ ] info about the Data browser? How to make data editable to user (change request)

## CHECK
    [x] Prizing or possibility for a "Click on Request private trial - GDPR Platform"
    [x] emailing to contact person is not working in my test node. (working when setup with excel). 
        [ ] webform setup missing something?
    [ ] rolls. Add one of the other consultants and check different rolls.
    [ ] excel templates latest version? 
    [ ] should privacy in grate extent be used instead of GDPR term throughout documentation?
    [ ] not receiving access request emails as system owner
    [ ] gdpr-template-excel-setup-data "gdpr-template-excel-setup-data:sesam_excel_setup_type": "sesam-gdpr:datatype"/"sesam-gdpr:purpose" switched? logic upstream seem to be swished too and counteract this.
    [ ] data-source and data-target is NOT? systems? but more general descriptive text?
    [ ] name on tabs on Request template for system owners. Where does the names come from? Data types? If so, Data types from webform is not showing up.

## Open questions
    Distinction of products?
        - Sesam - core node?
        - Open Sesam?
        - Sesam GDPR platform?
            - Workflow?
            - Automatic?
    What to do about the detailed thematic sections? Getting started is more up to date.
        E.g. the "Data types and purposes configuration" section is only about excel setup. 
    Data browser documentation is not so recognizable in GDPR portal context https://docs.sesam.io/databrowser-guide.html is it up to date?
    How do you clean up node after testing examples and you want to set up your own node from scratch?