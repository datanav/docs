---
type: Repository guide
title: Sesam Hub Product Documentation Wiki Instructions
description: A navigable, source-grounded Sesam Hub product reference and documentation-maintenance guide for humans and coding agents.
tags: [sesam-hub, product-reference, sphinx, repository-guide]
---

# Purpose and Scope

Distill the authored documentation in this repository into the product-reference member of a five-repository Sesam Hub knowledge network. Serve integration developers learning and configuring Sesam, operators troubleshooting it, and coding agents finding precise product semantics and the original reference. This repository documents the product; it does not implement the lake runtime, portal backend, or Management Studio UI.

Prioritize durable concepts, exact configuration contracts, practical workflows, and navigation over marketing copy, screenshots, release-note inventories, or one wiki page per source file. Keep useful depth: split major domains into linked pages and avoid a single exhaustive page. Preserve the original reStructuredText sources unchanged.

# Source Map and Evidence

- Start with `index.rst`, `hub/index.rst`, `README.md`, `conf.py`, `Makefile`, and `requirements.txt`. Follow actual toctrees, includes, substitutions, explicit labels, and cross-references to their authored definitions; do not infer the site structure from filenames alone.
- Prioritize `hub/concepts.rst`, `hub/core-principles.rst`, `hub/data-architecture.rst`, `hub/documentation/`, `hub/features/`, `hub/data-transformation-language.rst`, `hub/api.rst`, and the Swagger YAML files under `hub/`. Follow the relevant tutorials, guides, synchronization, security, operations, and extension-point material they reference.
- Cite local source paths, section labels, and relevant line ranges; use OpenWiki's normal Grounded Claims/provenance support. Authored docs are evidence of documented behavior, not proof of implementation or a successful execution. Identify backend/UI implementation questions as handoffs.
- Preserve exact JSON/YAML property names, DTL operators, namespaces, datatype notation, endpoint paths, defaults, units, and examples. Do not simplify typed Sesam data into ordinary untyped JSON or silently repair source examples. Distinguish required/optional/deprecated properties and version-dependent semantics.
- Resolve conflicting or stale guidance explicitly. Use changelogs/deprecations to qualify availability and historical behavior, not to assume every old capability is current. Do not use file dates as product versions. Check focused history only when it explains a material documentation change.

# Required Coverage

- `quickstart.md`: what Sesam Hub is, a reader-oriented topic map, a small integration-learning path, and a separate contributor preview/build path. Verify documented commands and prerequisites against the current Makefile/configuration; identify platform requirements and distinguish source inspection from commands actually run.
- Concepts and glossary: entities, datasets, pipes, sources, sinks, systems, transforms/DTL, identifiers and typed values, namespaces, dependencies, synchronization, and data lineage. Include product synonyms and link each term to its primary reference. Explain relationships and invariants with a source-grounded diagram where useful.
- Configuration reference: common building blocks, configuration structure, entity/data formats, defaults, incremental/full synchronization, scheduling, dependencies/completeness, deletion/reset behavior, error handling, and practical configuration examples. Point to detailed source references instead of duplicating every option.
- DTL guide: evaluation model, data/property paths, operators grouped by task, typing and namespaces, transformation patterns, and common mistakes. Use small synthetic examples taken from inspected sources and preserve semantics. Link the full operator reference for long-tail lookup.
- API and extension points: node, portal, and databrowser API boundaries; authentication/authorization documentation; custom sources/sinks/transforms and microservice integration. Distinguish specification-backed contracts from narrative documentation, and identify the owning implementation repository.
- Operations and security: monitoring/metrics, logs and failure diagnosis, lineage/search, backup/restore or durability where documented, deployment variants, access control, secrets handling, GDPR/data access, and documented limitations. Keep dangerous administrative steps clearly labeled with prerequisites and impact.
- Documentation maintenance: Sphinx/reStructuredText structure, includes and labels, theme/templates/assets, local HTML and alternative build targets, Docker/publishing inputs, link/format checks actually available, and where to change each reference. Capture build-flavor differences such as SaaS exclusions only when verified.
- Historical and policy material: index changelogs, deprecations, discontinued services, pricing, terms, privacy, and partner/legal material as secondary references. Preserve scope/version caveats; do not reinterpret legal obligations or pricing as timeless runtime guarantees.

# Page Design for Humans and Agents

Use descriptive, searchable headings and concise summaries followed by exact contracts, constraints, examples, and source links. Separate product usage from contributing to this documentation repository. For a topic, give a primary source, related concepts, version/deprecation caveats, and the implementation owner when known. Add a task-to-reference/source map so agents can locate the relevant configuration or rule without rereading the whole wiki. Use Mermaid only for relationships actually described by the sources. Keep page navigation bidirectional and avoid repeating the same glossary or examples across pages.

# Sesam Hub Knowledge Network

Ownership: `docs` owns documented product semantics; `lake` owns the data-processing runtime and related services; `portal` owns account/subscription management; `webconsole` owns the Management Studio UI; `counting-semaphore` owns the semaphore service. Explain product-level boundaries without claiming to have inspected sibling implementations.

Research only this repository. Identify cross-repository questions and verified interfaces in an integration section. If a linked OpenWiki workspace is available, verify a target page before linking it; otherwise record the repository/topic as a not-yet-linked handoff. Never invent relative links to unbuilt pages or use machine-specific absolute paths. Keep each wiki standalone so the five generated wikis can later be aggregated with `openwiki link`.

# Boundaries

Honor `.openwikiignore` and prefer authored text/specifications over generated HTML, PDFs, archives, or presentation assets. Never reproduce embedded credentials, private keys, real customer data, or internal account details from otherwise allowed docs; use synthetic placeholders. Do not install tools, build the documentation site, start servers/containers, or contact live APIs while researching. Wiki generation must only modify OpenWiki documentation/metadata and its normal managed agent-navigation blocks; preserve original documentation and existing contributor instructions.
