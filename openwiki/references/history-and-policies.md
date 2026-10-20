---
type: reference-guide
title: Changelogs, deprecations, discontinued services, and policies
description: Navigate Sesam's historical and legal references without mistaking old capabilities, roadmap plans, or commercial terms for current runtime guarantees. Includes end-of-life evidence and a method for qualifying availability, experimental features, and pricing.
tags: [references, history, deprecations, availability, pricing, policies]
verified:
  - by: openwiki/0.7.2
    at: 2026-10-20T13:49:14.868Z
sources:
  - id: openwiki-source-b5aec4802496a78d4d532ddd
    resource: repo://community.rst
  - id: openwiki-source-4bbe4e83d74f3fe902420d24
    resource: repo://hub/changelog.rst
  - id: openwiki-source-bd024a2a6f605b5e87c13edc
    resource: repo://hub/databrowser.rst
  - id: openwiki-source-94c0ec50b6458d32bee9aa4b
    resource: repo://hub/deprecations.rst
  - id: openwiki-source-c5c1512bb5c6ab896e1c0669
    resource: repo://hub/discontinued-services.rst
  - id: openwiki-source-b16009034f286ce228a41a35
    resource: repo://hub/features/compaction-feature.rst
  - id: openwiki-source-d496de71635dcd7d5827ad5d
    resource: repo://hub/features/durable-data.rst
  - id: openwiki-source-b7fe0a062d08b595ab024630
    resource: repo://hub/features/integrated-search.rst
  - id: openwiki-source-6903130fd4e1c31a5b69b78a
    resource: repo://hub/features/metrics-api.rst
  - id: openwiki-source-b8c1aa2cd0b984f516a8bc50
    resource: repo://hub/features/software-channels.rst
  - id: openwiki-source-293c6065c127d8687c065bd0
    resource: repo://hub/gdpr-platform.rst
  - id: openwiki-source-9539e9c49e7b9e9a0bf96c74
    resource: repo://hub/index-developer.rst
  - id: openwiki-source-bcbee3728e5f87e8d24258b4
    resource: repo://hub/index-management-console.rst
  - id: openwiki-source-a8d5beddbb38f9b4d3ccda2f
    resource: repo://hub/legal-sla.rst
  - id: openwiki-source-c14aa78199fe4f034432e902
    resource: repo://hub/open-sesam.rst
  - id: openwiki-source-5061e0804c08ee434d45bc56
    resource: repo://hub/roadmap.rst
  - id: openwiki-source-0cf45857f139d7ef03466d34
    resource: repo://legal-dap.rst
  - id: openwiki-source-4b9fcd10d06cb399994cfd34
    resource: repo://legal-service.rst
  - id: openwiki-source-832f2a6f7b0fb248ce435fa5
    resource: repo://partner-agreement-part-1.rst
  - id: openwiki-source-e2f40343addf63e273b32b32
    resource: repo://partner-agreement-part-2.rst
  - id: openwiki-source-5a3af5ced3903ed7fb8ccca4
    resource: repo://partner-agreement.rst
  - id: openwiki-source-c7a64279defb397411144f15
    resource: repo://pricing.rst
  - id: openwiki-source-b9d1102152dd5273d335e6c1
    resource: repo://privacy-policy.rst
  - id: openwiki-source-d7754cc8baaccb199775b869
    resource: repo://talk/index.rst
  - id: openwiki-source-612ac4323087d90e2cd678da
    resource: repo://terms.rst
generated: { by: "openwiki/0.7.2", at: "2026-10-20T13:49:14.868Z" }
---

# Changelogs, deprecations, discontinued services, and policies

Use these sources to **qualify** a technical reference, not replace it. A changelog records a dated change; a retained guide may describe a retired service; a roadmap mixes intentions with availability notes; a contract describes terms rather than proving runtime behavior. Start with the focused feature/API/configuration documentation, then add the history, deployment scope, and commercial or legal qualifications relevant to the question.

The developer documentation explicitly warns that features marked **Experimental** can change or disappear without warning and must not be used in production. It also routes readers separately to deprecated features and discontinued services. Both retirement indexes say not to use their contents. See [developer entrypoint, lines 5–25](../../hub/index-developer.rst#L5-L25), [`deprecations`, lines 1–16](../../hub/deprecations.rst#L1-L16), and [discontinued services, lines 5–13](../../hub/discontinued-services.rst#L5-L13).

## Task-to-source map

Labels below are exact RST labels where present. Otherwise, use the named heading; do not invent a label or infer a software version from a heading date.

| Task | Source and section/label | What it establishes |
|---|---|---|
| Check when wording, a default, or support changed | [`hub/changelog.rst`](../../hub/changelog.rst); the relevant `changelog_…` label, with its exact spelling | Dated additions, fixes, breaking changes, warnings, and removals. Read the linked technical section too. |
| Identify unsafe legacy operators or configuration | [`hub/deprecations.rst`](../../hub/deprecations.rst#L1-L18), label `deprecations`; operator/feature labels within it | Deprecated documentation remains available for interpretation of old configurations, not recommendation for new ones. |
| Check a retired service | [`hub/discontinued-services.rst`](../../hub/discontinued-services.rst#L15-L27), labels `sesam_talk_discontinue`, `open_sesam_discontinue`; see the end-of-life table below | Service retirement, separate from individual operator deprecation. |
| Separate plans from delivered features | [`hub/roadmap.rst`](../../hub/roadmap.rst#L1-L48), label `roadmap`; headings **Planned**, **Public Preview**, **Generally Available**, **Discontinued** | Subject-to-change plans and explicitly qualified availability notes. |
| Qualify rollout timing for an installation | [`hub/features/software-channels.rst`](../../hub/features/software-channels.rst#L1-L22), labels `software-channels`, `software_channels` | Phased release channels and promotion caveats, not a guarantee that every subscription received a dated change immediately. |
| Check subscription charges and environment eligibility | [`pricing.rst`](../../pricing.rst#L1-L105), labels `pricing`, `pricing-developer`, `pricing-production`; headings **Invoicing**, **Due date**, **Price adjustment** | Subscription compute/data/SLA pricing, footnotes, payment terms, and adjustments. Feature-specific consumption notes belong in the feature reference. |
| Locate service-level targets and remedies | [`hub/legal-sla.rst`](../../hub/legal-sla.rst): **Availability for the Services**, **Capacity requirements**, **Requirements for processing and reaction times**, **Standardized penalties** | SLA definitions, scopes, exclusions, and targets; not pipe execution or durability semantics. |
| Locate access/use terms and service specification | [`terms.rst`](../../terms.rst#L12-L56): **1.1. Purpose**, **1.2. Description of the Services**; [`legal-service.rst`](../../legal-service.rst#L7-L93): **1. Specification of the Services**, **2. Service level agreement and standardized refunds** | Customer/service relationship and contractual service description. |
| Review processing of customer personal data | [`legal-dap.rst`](../../legal-dap.rst#L7-L85): **1. Definitions**, **2. Processing of Personal Data on the Controller's behalf**, **4. Security**, **5. Subprocessing**, **6. Data Subject Rights**, **7. Personal Data Breach**, **9. Deletion or return of the Personal Data**, **10. Audit rights** | Data processing agreement (DPA); the filename is `legal-dap.rst`, not `legal-dpa.rst`. Sections 5–10 are at [lines 268–415](../../legal-dap.rst#L268-L415). |
| Select the appropriate privacy notice | [`privacy-policy.rst`](../../privacy-policy.rst): **[SESAM Privacy Notice](../../privacy-policy.rst#L18-L35)**, **[SESAM Privacy Policy](../../privacy-policy.rst#L126-L145)**, **[Service Privacy Policy](../../privacy-policy.rst#L308-L353)**, **[Recruiting Privacy Notice](../../privacy-policy.rst#L523-L529)** | Notices for different collection purposes; do not apply a notice's retention wording to all dataset history. |
| Find partner/legal inputs or community guidance | [`legal.rst`](../../legal.rst#L7-L22): legal index and **Downloads**; [`partner-agreement.rst`](../../partner-agreement.rst#L1-L5): assembled agreement; [`community.rst`](../../community.rst#L9-L42), label `community` | Contract navigation, partner collaboration terms, and separate unofficial community resources. Partner parts are explained below. |

## How to qualify current reference wording

1. **Identify the precise object and scope.** Distinguish an operator from a service, Management Console from Management Studio, a cloud subscription from self-hosting, and an available feature from an enabled one. Cite the technical section that owns the behavior.
2. **Read focused history in both directions.** An “added” entry is insufficient if a later entry changes defaults, marks it experimental, deprecates it, or removes support. Preserve “added documentation” versus “added support”: for example, [`changelog_2026-03-30`](../../hub/changelog.rst#L24-L29) says documentation was added for the replicated dataset sink, not that the sink necessarily first existed on that date.
3. **Preserve the status words and migration caveats.** Use “documented as experimental,” “deprecated,” “announced end-of-life,” or “removed support” as appropriate. Do not turn deprecated into proven removal, or a future-dated warning into proof of an actual shutdown on that date.
4. **Resolve material conflicts with the narrower reference and explicit later history.** Record what each source says rather than silently modernizing an old guide. Use focused history only as needed, and keep exact labels: this changelog uses both underscore and hyphen date-label forms.
5. **Separate documented change dates from installation state.** Do not use file dates or Sphinx release metadata as product versions. The [software-channel reference, lines 9–22](../../hub/features/software-channels.rst#L9-L22) documents a phased rollout: `weekly-prod` for production, `weekly` for staging, `nightly` for development, and `latest` for development with additional caution. Promotion can be withheld; build dates indicate minimum, not maximum, age. Downgrades are not supported. Verify the installation and channel before attributing an observed behavior to a note.

Useful examples of qualification, not a release-note inventory:

- **Deprecation does not erase the old explanation.** [`changelog_2025-12-22`](../../hub/changelog.rst#L58-L62) deprecates `ni-collapse` and `ni-expand`. Their retained sections, labels `ni_collapse_dtl_function` and `ni_expand_dtl_function`, still describe them as experimental and intended for `global_defaults.symmetric_namespace_collapse=true` ([lines 199–220](../../hub/deprecations.rst#L199-L220), [260–279](../../hub/deprecations.rst#L260-L279)). That is historical context, not an endorsed production option.
- **Migration advice is scoped.** [`changelog_2022_01_25`](../../hub/changelog.rst#L966-L971) deprecates the lower keys, upper keys, and undirected graph transforms, but names DTL transforms as replacements for the lower/upper keys functionality, not for undirected graph. Do not extend that replacement claim to undirected graph. [`changelog_2021_12_20`](../../hub/changelog.rst#L1006-L1013) says new pipes should use `hops` `subsets` rather than deprecated `prefilters`, and changing an existing pipe may require a reset.
- **A roadmap plan can be overtaken without granting broader semantics.** The roadmap retains **Permanent deletion of history for selected entities (Q4 2025)** as a plan ([lines 27–34](../../hub/roadmap.rst#L27-L34)). Later, [`changelog_2026-04-07`](../../hub/changelog.rst#L17-L21) records `compaction.retract`. The focused [`compaction_retract_detail` reference, lines 120–137](../../hub/features/compaction-feature.rst#L120-L137) says it removes earlier versions only in the pipe's sink dataset, retaining the current version and leaving deletion state unchanged. Upstream datasets and external consumers are unchanged. Do not summarize this as universal erasure of an entity.

## Material end-of-life references

Retained instructions, schemas, and API descriptions in these areas are historical navigation, not evidence that the service remains available.

| Capability | Exact documented status/date caveat | Evidence and destination |
|---|---|---|
| **Databrowser** | End-of-life was announced for **December 31st 2023**; it is superseded by **Integrated Search**. | [`databrowser` warning, lines 1–15](../../hub/databrowser.rst#L1-L15); [`changelog_2022_03_21`, lines 921–927](../../hub/changelog.rst#L921-L927). For retained access/auth/API material, use [Legacy data access](legacy-data-access.md). |
| **GDPR Platform** | The warning and **2025-04-02** entry scheduled end-of-life for **June 30th 2025**. The **2025-04-11** entry then records **early retirement**. Do not present the original schedule as the final retirement timing. | [Platform warning and legacy navigation, lines 1–18](../../hub/gdpr-platform.rst#L1-L18); [`changelog_2025-04-02` and `changelog_2025-04-11`, lines 151–165](../../hub/changelog.rst#L151-L165). No replacement is named in those entries. |
| **Notifications feature** | The **2025-04-02** entry announces end-of-life **June 30th 2025**, superseded by **Metrics**. This is the announcement, not a separate confirmation of execution on that date. | [`changelog_2025-04-02`, lines 159–165](../../hub/changelog.rst#L159-L165); successor label `metrics-api` in [Metrics](../../hub/features/metrics-api.rst#L1-L42). Do not infer that the successor lacks custom notifications: its documented bundle includes them. |
| **Management Console / multitenancy** | **2025-04-11** records removal of support for both. The Console warning identifies it as part of multitenancy; the roadmap marks multitenancy discontinued. | [`changelog_2025-04-11`, lines 151–157](../../hub/changelog.rst#L151-L157); [`management_console`, lines 1–17](../../hub/index-management-console.rst#L1-L17); [roadmap, lines 178–191](../../hub/roadmap.rst#L178-L191). This is not a claim that all Management Studio/UI functionality was removed. |
| **Sesam Talk** | The Universal Semantic Data Synchronization service was discontinued in **November 2024**. Its landing page says it should not be used. | [`sesam_talk_discontinue`, lines 15–20](../../hub/discontinued-services.rst#L15-L20); [Talk landing page, lines 1–9](../../talk/index.rst#L1-L9). Do not import its managed-service promises into Data Hub runtime guarantees. |
| **Open Sesam** | Discontinued and should not be used. The cited notices give **no retirement date**. Its historical purpose was free hosting, enrichment, and publication of data. | [`open_sesam_discontinue`, lines 22–27](../../hub/discontinued-services.rst#L22-L27); [Open Sesam notice, lines 9–16](../../hub/open-sesam.rst#L9-L16). Old sign-up/publication instructions are not a current free-service offer. |

## Roadmap availability is not a promise to ship

The roadmap explicitly says it may change. **Planned** includes self-hosted clustered architecture **(Q2 2025)**, resource optimization on multi compute **(Q3 2025)**, selected-entity history deletion **(Q4 2025)**, and high-level configuration **(2026)**. Preserve these as the document's planning horizons, not release deadlines or proof of delivery ([lines 7–43](../../hub/roadmap.rst#L7-L43)).

**Public Preview** is described as available for experimental use. It retains exploratory prose alongside notes that TTL on deletes, webhooks, and connectors are now available; property lineage is now offered within Integrated Search ([lines 45–94](../../hub/roadmap.rst#L45-L94)). For TTL semantics, follow `changelog_2024_11_27` and the compaction reference rather than treating preview prose as a complete retention specification.

Even **Generally Available** needs its explicit scope. The roadmap's availability notes qualify Metrics, Integrated Search, and self-service VPN by **Clustered Architecture**; say **all cloud subscriptions** now run clustered architecture; and say Durable Data is available on **all cloud subscriptions** ([lines 96–176](../../hub/roadmap.rst#L96-L176)). None of that alone establishes that the planned self-hosted clustered variant shipped. Use [Deployment and durability](../operations/deployment-and-durability.md) and [Monitoring and troubleshooting](../operations/monitoring-and-troubleshooting.md) for operational details.

## Keep commercial and legal evidence in its lane

### Pricing and paid-feature notes

The subscription reference distinguishes developer environments from production/test environments. Developer environments serve a single developer or CI, are cloud-only and restricted, lack backup/VPN/SLA support, and cannot host test, staging, or production. Production/test environments document automated backup and support for SLA and VPN; the backup footnote says geo-replicated backup is included in cloud environments ([`pricing-developer` and `pricing-production`, lines 10–79](../../pricing.rst#L10-L79)). **Support for SLA** does not by itself establish the selected agreement or entitlement.

Do not copy an old estimate or fee into timeless technical prose. For example, the [Developer Pro roadmap text, lines 156–166](../../hub/roadmap.rst#L156-L166) retains an estimated monthly price alongside an availability note, whereas `pricing.rst` has a separate subscription table. Read the applicable pricing table, currency, footnotes, payment terms, and **Price adjustment** section; subscription fees can be adjusted under that section ([lines 97–105](../../pricing.rst#L97-L105)). Confirm applicable commercial terms rather than reconciling them by inference here.

Feature badges are not complete cost models:

- [Durable Data](../../hub/features/durable-data.rst#L68-L89), labels `durable_data` / `durable-data`, is paid; `metadata.durable` defaults to `false`, and activation increases the data consumption of durable pipes by **3x**. Its [use-case description, lines 9–24](../../hub/features/durable-data.rst#L9-L24) describes reduced data-loss risk. Do not infer zero loss or exactly-once delivery from it.
- [Integrated Search, lines 1–16](../../hub/features/integrated-search.rst#L1-L16), label `integrated_search`, is marked free but documents **2x** data size for global pipes when enabled, and clustered-architecture availability.
- [Metrics, lines 1–42](../../hub/features/metrics-api.rst#L1-L42), labels `metrics-api` / `metrics_api`, is marked free but also directs readers to the enablement steps to check the monthly-price effect. Preserve both statements rather than asserting universal zero cost.

### SLA, service terms, DPA, privacy, and partners

Keep these as separate review inputs, not a paraphrased contract:

- **SLA:** `hub/legal-sla.rst` states a **99.5% uptime target per installation**, defines downtime and exclusions, and specifies planned maintenance ([lines 5–25](../../hub/legal-sla.rst#L5-L25)). Its reaction/correction-time section distinguishes starting investigation from restoring normal service, uses stated business-hour/holiday qualifications, and assigns priority through the vendor ([lines 142–162](../../hub/legal-sla.rst#L142-L162)). Read the actual selected SLA and remedies; neither this target nor the pricing response-time row proves per-request latency, recovery-point objectives, or pipe success.
- **Service terms and specification:** `terms.rst` **1.2** describes access to evolving service functionality rather than a right tied to a specific software version ([lines 46–56](../../terms.rst#L46-L56)). Use `legal-service.rst` for the contractual service catalogue, reconstruction, customer/network responsibilities, and error-reporting procedure, not as an independent implementation specification ([lines 30–93](../../legal-service.rst#L30-L93)).
- **DPA:** The document applies if/when the service processes customer personal data and defines the Customer as Controller and Vendor (or Subprocessor) as Processor ([lines 7–42](../../legal-dap.rst#L7-L42)). Its security, subprocessing, breach, audit, and cessation deletion/return sections are legal review destinations. Do not translate cessation obligations into a dataset compaction timer or assume the retired GDPR Platform is required for DPA applicability.
- **Privacy:** The overview distinguishes collection purposes and explicitly says the policies were last updated **September 2020** ([lines 5–16](../../privacy-policy.rst#L5-L16)); that is a notice caveat, not a product version. **Service Privacy Policy** distinguishes service personal data from general customer/contact data and states that relevant privacy provisions of the Terms of Service, including the DPA, take precedence in inconsistencies ([lines 308–353](../../privacy-policy.rst#L308-L353)). Follow the appropriate notice without exporting its retention periods to unrelated data.
- **Partner/legal inputs:** The assembled partner agreement includes both source parts. [Part 1](../../partner-agreement-part-1.rst#L36-L64) covers **Purpose** and the collaboration framework, with **Collaborative Results and Discount** at [lines 108–146](../../partner-agreement-part-1.rst#L108-L146). [Part 2](../../partner-agreement-part-2.rst#L19-L102) continues with **Partner Obligations**, **Sesam's Obligations**, and **Financing and Fees**, then [intellectual-property and confidentiality provisions, lines 104–180](../../partner-agreement-part-2.rst#L104-L180). These govern commercial collaboration; they are not connector runtime contracts. [Community guidance](../../community.rst#L15-L42) instead points to sharing guidelines, connector repositories, informal Q&A, feature requests, and unofficial Slack discussions—not contractual support commitments.

## Applying this in documentation maintenance

Before publishing a historical or availability statement, check:

- Does the citation include the local source, exact label or heading, and relevant lines?
- Is the statement about shipped behavior, documentation added, a rollout, a plan, or an announcement?
- Are experimental, deprecation, end-of-life, architecture, enablement, and migration caveats preserved?
- Are prices/consumption effects separate from guarantees, and legal terms left for review rather than reinterpreted?
- Is a retained legacy example clearly historical, with a named successor only where the source supplies one?

Carry those qualifications into [Documentation maintenance](../workflows/documentation-maintenance.md), [DTL evaluation and operators](../concepts/dtl-evaluation-and-operators.md), [Connectors and contracts](../integrations/connectors-and-contracts.md), and [Security and secrets](../operations/security-and-secrets.md). Use the [Quickstart](../quickstart.md) for active setup guidance rather than retired-service onboarding instructions.
