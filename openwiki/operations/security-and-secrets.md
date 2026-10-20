---
type: security-concept
title: Authorization, secret lifecycle, and network security
description: Explains subscription roles, node ACL enforcement, runtime pipe identity, write-only secrets, and outbound authentication. Covers configuration replacement risks, TLS verification, hosted network controls, VPN, encryption-at-rest limits, and security-focused validation.
tags: [security, authorization, secrets, authentication, networking, operations]
verified:
  - by: openwiki/0.7.2
    at: 2026-10-20T13:49:14.868Z
sources:
  - id: openwiki-source-e389b2c6e31446ccc4126746
    resource: repo://hub/api.rst
  - id: openwiki-source-8b35a0ce0ffe588f380e6470
    resource: repo://hub/documentation/building-blocks/environment-variables.rst
  - id: openwiki-source-5fd606e14966f8a238296bce
    resource: repo://hub/documentation/building-blocks/secrets.rst
  - id: openwiki-source-80eedbbd35c9d596a2d38fe2
    resource: repo://hub/documentation/operations/behind-the-scenes.rst
  - id: openwiki-source-5836a7a1bfae906d1c6a7cca
    resource: repo://hub/documentation/operations/continuous-integration.rst
  - id: openwiki-source-caeff9d3196d7b81403130e3
    resource: repo://hub/documentation/operations/security.rst
  - id: openwiki-source-36d87051e96fd518941e710f
    resource: repo://hub/documentation/operations/testing-locally.rst
  - id: openwiki-source-6a5de2a911806771b5cfd05a
    resource: repo://hub/documentation/service-configuration/configuration-metadata.rst
  - id: openwiki-source-9b06b9e105f615155cf1f604
    resource: repo://hub/documentation/service-configuration/environment-variables/environment-variables.rst
  - id: openwiki-source-b88ab8bcd7069b9437346a72
    resource: repo://hub/documentation/service-configuration/pipes/configuration-pipes.rst
  - id: openwiki-source-daba448c9f0497c50826d185
    resource: repo://hub/documentation/service-configuration/pipes/configuration-sinks-rest.rst
  - id: openwiki-source-709dcd56cf1f6f81f6584be7
    resource: repo://hub/documentation/service-configuration/pipes/configuration-sources-http.rst
  - id: openwiki-source-e3ab6d41e79b5df3ed8f521c
    resource: repo://hub/documentation/service-configuration/systems/configuration-systems-rest.rst
  - id: openwiki-source-4b9a915a059dfbaf16712b15
    resource: repo://hub/documentation/service-configuration/systems/configuration-systems-url.rst
  - id: openwiki-source-b15f1f3b073de71b578bbbbc
    resource: repo://hub/documentation/service-configuration/systems/configuration-systems.rst
  - id: openwiki-source-5156b81b00358c1c04a7aff2
    resource: repo://hub/features/api-config-groups.rst
  - id: openwiki-source-0ad01ca73409795763a8fc50
    resource: repo://hub/features/bring-your-own-key.rst
  - id: openwiki-source-3b18059c0de46330cdb99d29
    resource: repo://hub/features/network-policy.rst
  - id: openwiki-source-cba998551ab4133c8eef25c8
    resource: repo://hub/features/vpn.rst
  - id: openwiki-source-839eae38482865fc4eda4486
    resource: repo://hub/sesam-client.rst
  - id: openwiki-source-d0a16f79e90cff0f5bcc9290
    resource: repo://hub/swagger_portal.yaml
  - id: openwiki-source-c92a884f90ca8ac7f160c79a
    resource: repo://hub/swagger_public.yaml
generated: { by: "openwiki/0.7.2", at: "2026-10-20T13:49:14.868Z" }
---

# Authorization, secret lifecycle, and network security

Sesam documents two security domains: **user authorization** controls who may perform actions, while **secrets** hold credentials used by integrations. Keep both separate from network reachability and from authentication to an external service. A valid user JWT is not an external-system credential, and possessing a database password does not grant permission to administer a node. [Security domains](../../hub/documentation/operations/security.rst#L8-L39)

This page describes the published contracts in this documentation repository, not the implementation of the portal or node. For implementation work, use [APIs and repository handoffs](../integrations/apis-and-repository-handoffs.md). Deprecated databrowser authentication belongs in [Legacy data access](../references/legacy-data-access.md), not in a new node-authentication design. Security-policy history and legal material belong in [History and policies](../references/history-and-policies.md); this page does not derive compliance guarantees or legal obligations from certification statements.

## Responsibility boundaries

| Layer | What it controls | What to configure or inspect |
| --- | --- | --- |
| Portal subscription roles | A user's actions in the portal, scoped to a subscription | Subscription membership and roles |
| Node resource permissions | Authorized actions on pipes, systems, and datasets | Resource ACLs and the role principals in the JWT |
| Runtime pipe permissions | Whether a running pipe may use its source and target systems | The roles inherited when the pipe was created, plus system permissions |
| Configuration groups | Which collection of pipe/system configuration is retrieved or replaced | `metadata["$config-group"]` or the group in the configuration URL |
| External-system authentication | Credentials sent by URL/REST systems to remote servers | `authentication`, `jwt_token`, `oauth2`, or REST `custom_auth` |
| Network and storage controls | Reachability, transport security, and hosted encryption at rest | Network policy, VPN, certificate verification, and subscription-specific BYOK eligibility |

Roles, node permissions, and runtime checks are defined in the [security reference](../../hub/documentation/operations/security.rst#L23-L123). Configuration grouping is defined separately in [Config groups](../../hub/features/api-config-groups.rst), and outbound authentication in the [URL](../../hub/documentation/service-configuration/systems/configuration-systems-url.rst) and [REST](../../hub/documentation/service-configuration/systems/configuration-systems-rest.rst) system contracts.

## User-to-node authorization

### Login, subscription selection, signature validation, and ACL checks

Roles are assigned to users **within a subscription**: the same person can have different roles in different subscriptions. Node permissions are assigned to roles through the GUI's Permissions pages. The node evaluates the user's roles against permissions on the requested resource; portal membership alone is not the resource permission check.

The documented dataset-read example follows this sequence:

```mermaid
sequenceDiagram
    actor Person as User
    participant GUI as Management Studio GUI
    participant Portal as Sesam Portal backend
    participant Node as Subscription node
    Person->>GUI: Log in with email and password
    GUI->>Portal: Submit login
    Portal->>Portal: Check existing user and assigned roles
    Portal-->>GUI: Subscriptions where user has a role
    Person->>GUI: Select subscription subA
    GUI->>Portal: GET /api/subscriptions/subA/jwt
    Portal->>Portal: Include roles in subA and sign JWT with private key
    Portal-->>GUI: Signed JWT
    Person->>GUI: Select dataset1
    GUI->>Node: Request dataset with Authorization Bearer JWT
    Node->>Node: Validate signature using portal public key
    Note over Node: For a valid JWT, evaluate resource permissions
    Node->>Node: Load dataset ACL and check Read data against user roles
    alt Required permission granted
        Node-->>GUI: Dataset contents
        GUI-->>Person: Display data
    else Required permission not granted
        Node-->>GUI: 403 Forbidden
        GUI-->>Person: Access denied
    end
```
*The portal establishes subscription-scoped roles in a signed JWT; the node validates the signature and makes the resource-specific allow/deny decision.*

The portal exposes `GET /api/jwt` for the logged-in user, `POST /api/jwt` for form-encoded `email` and `password` with optional `subscription_id`, and `GET /api/subscriptions/{subscription_id}/jwt` for a particular subscription. If the POST omits `subscription_id`, the contract says it returns a JWT for all the user's subscriptions. `GET /api/jwt/publickey` returns the RSA public key used to verify signatures. [Portal JWT API](../../hub/swagger_portal.yaml#L256-L326)

Most node API calls require a JWT, sent on **each request** as `Authorization: Bearer ` followed by the token. Use the connection URL shown for the actual subscription; a typical hosted API base is `https://instance-guid.sesam.cloud/api`. This illustrative token is intentionally invalid:

```http
Authorization: Bearer synthetic-jwt-not-valid
```

The documented `403 Forbidden` above is an **ACL denial after authentication**. The login example does not specify an HTTP status for an invalid signature; do not treat every authorization failure as the same failure mode. [Header contract](../../hub/api.rst#L10-L58), [authorization sequence](../../hub/documentation/operations/security.rst#L45-L63)

### Roles are not permission names

The published role overview gives these broad capabilities; consult the actual resource ACL when diagnosing a node request:

| Role | Documented overview |
| --- | --- |
| Admin | Manages subscription, resources, roles, permissions, other users, admin, ACLs, configuration uploads, and licenses |
| Developer | Manages subscription, pipes, systems, datasets, roles, permissions, and configuration uploads, but not admin, other users, ACL management, or license uploads |
| User | Manages own pipes and systems, and manages datasets; not subscription, roles, permissions, or configuration uploads |
| Guest | Views pipes and systems only in this overview; no dataset management |

[Role-based access overview](../../hub/documentation/operations/security.rst#L65-L92)

Pipe and system configurations accept a `permissions` list. Each ACL entry is a three-element list: action, list of groups/roles, and list of permission names. The prose describes actions as `"ALLOW"|"DENY"`; the published JSON examples use lowercase `"allow"` and `"deny"`. Preserve the example syntax rather than inventing a different ACL format. For example, the documented Developer grants are:

**Pipe configuration fragment:**

```json
{
  "permissions": [
    ["allow", ["group:Developer"], ["read_config", "write_config", "run_pump_operation", "read_data", "write_data"]]
  ]
}
```

**System configuration fragment:**

```json
{
  "permissions": [
    ["allow", ["group:Developer"], ["read_data", "write_data", "read_config", "write_config", "read_proxy", "write_proxy"]]
  ]
}
```

These grants illustrate different operations: configuration access, data access, pump operations, and system proxy access are distinct permission names. Do not broaden the list just to make one failed operation succeed. The inspected documentation does not establish conflict ordering between allow and deny entries or a universal default ACL. Resolve such implementation questions through the repository handoff rather than assuming filesystem-like precedence. [ACL structure](../../hub/documentation/service-configuration/systems/configuration-systems.rst#L19-L35), [pipe ACL property](../../hub/documentation/service-configuration/pipes/configuration-pipes.rst#L109-L114), [permission examples](../../hub/documentation/operations/security.rst#L94-L113)

### Runtime pipe identity is another check

When a user creates a pipe, it inherits that user's roles, stored in the pipe configuration. At runtime, the node checks whether the pipe may read from its source system and write to its target system. Failure makes the **pipe run fail**, with an error on the pipe's GUI page. Being able to upload configuration or start a pump is therefore not a substitute for checking the running pipe's system access. [Runtime checks](../../hub/documentation/operations/security.rst#L115-L123)

For pipe/system configuration structure, see [Pipes and systems](../configuration/pipes-and-systems.md).

### Automation tokens and revocation

The portal's `/api/subscriptions/{subscription_id}/api_json_web_tokens` collection supports listing, creating, and updating API JWTs for scripts and cron jobs. Creation requires `exp` and `principals`, such as `group:Developer`. Without refresh configuration, `exp` is the expiration date in epoch seconds. With `refresh_interval`, the configured `exp` is the last time the token can be refreshed, while the signed token's expiry is `current_time + refresh_interval`.

The actual `jwt_string` is returned **only on creation**. A refresh-enabled token also has a `client_id` and a `client_secret`, with the secret likewise returned only on creation. Securely capture these at issuance; a later listing is not a credential-recovery mechanism. The portal also documents `POST /api/openid_connect/token` with `grant_type` values `client_credentials` and `refresh_token`, plus `client_id` and `client_secret`. This portal token endpoint is not the remote provider's token endpoint in a system's `oauth2` configuration. [API JWT operations](../../hub/swagger_portal.yaml#L521-L692), [JWT fields](../../hub/swagger_portal.yaml#L4702-L4788), [portal token endpoint](../../hub/swagger_portal.yaml#L2794-L2821)

The portal exposes `/api/subscriptions/{subscription_id}/revoked_json_web_tokens` for subscription nodes to learn about changed user permissions and revoked API JWTs. It covers both transient GUI JWTs and long-lived API JWTs, and supports continuation using the last entity's `_updated` value as `since`. Revocation records identify either a `user_principal` or an `api_token_id`, never both; the latter invalidates one API token. The contract does not specify a node polling interval or an instantaneous revocation guarantee. [Revocation feed](../../hub/swagger_portal.yaml#L2627-L2659), [revocation identities](../../hub/swagger_portal.yaml#L5487-L5503)

## Configuration groups: replacement scope, not role groups

Every pipe/system belongs to a config group. For individual configuration endpoints, set it in metadata:

```json
{
  "metadata": {
    "$config-group": "synthetic-integration-group"
  }
}
```

For bulk `/api/config/{config-group}` operations, the group is selected by the URL. Omission selects the `default` group, including `PUT /api/config`. **Bulk PUT replaces all configuration in the selected group**, not just the items being changed. `PUT /api/config-all` overwrites all groups. These are deployment boundaries, not substitutes for `group:Developer` or resource ACLs. Review the complete intended group before replacing it, especially where system deletion/recreation could destroy system-local secrets. The default-group and all-group PUT contracts also warn that `force=true` accepts configuration errors and applies configuration on a best-effort basis; do not use it as a security fix. [Config group assignment and replacement](../../hub/features/api-config-groups.rst#L29-L46), [bulk API contracts](../../hub/swagger_public.yaml#L1226-L1348)

See [Deployment and durability](deployment-and-durability.md) for deployment and recovery procedures.

## Write-only secrets and environment substitution

### Choose the right scope and retain the originals

Use `$SECRET(name)` for passwords, tokens, and other sensitive values. Secrets are write-only: their **names** can be listed, but their original values cannot be extracted after upload. The secrets manager stores values encrypted with an instance-unique key. Keep a secure **off-site** copy of the originals, including the material needed to re-upload them; downloading configuration or listing secret keys does not replace this responsibility.

Prefer **system-local secrets**. They are visible to one specified system. Global secrets are available to all systems and are supported but not recommended. Global secrets survive until explicitly deleted. System-local secrets survive until explicitly deleted **or the system is removed**. Deleting and re-adding a system, even with the same intended identity, requires uploading its local secrets again. [Secret scope, encryption, and retention](../../hub/documentation/operations/security.rst#L131-L187), [local-scope recommendation](../../hub/documentation/building-blocks/secrets.rst)

```mermaid
flowchart TD
    Original["Original values retained securely off-site"] --> Upload["Upload to secrets manager"]
    Upload --> Local["System-local encrypted secrets"]
    Upload --> Global["Global encrypted secrets"]
    Local --> UseLocal["Resolve SECRET references at runtime for that system"]
    Global --> UseGlobal["Resolve SECRET references at runtime for systems"]
    Local --> RemoveLocal["Explicit secret deletion or system removal"]
    Global --> RemoveGlobal["Explicit secret deletion"]
    RemoveLocal --> Recreate["Recreate system if needed"]
    Recreate --> Reupload["Re-upload local secrets from retained originals"]
    Original --> Reupload
    Reupload --> Local
```
*System removal ends the lifetime of system-local secrets; recreating the configuration does not restore the values.*

### Management entrypoints and update semantics

Node paths below include the `/api` prefix. Upload a JSON mapping of secret names to string values. The narrative security guide mentions a single object or a list of objects, but the API contracts specify an object; use the mapping form for API integrations.

| Operation | Global secrets | System-local secrets |
| --- | --- | --- |
| List names only | `GET /api/secrets` | `GET /api/systems/{system_id}/secrets` |
| Upload with PUT | Adds named values and overwrites matching names | **Overwrites the secrets for the specified system** |
| Add/update with POST | Adds values, overwrites matching names, does not delete existing secrets | Adds values, overwrites matching names, does not delete existing secrets |
| Delete one value | `DELETE /api/secrets/{secret_key}` | `DELETE /api/systems/{system_id}/secrets/{secret_key}` |

Do not assume global and system PUT have identical replacement semantics. For a targeted rotation that must retain unrelated local keys, the POST contract explicitly supplies additive behavior. [Global secret API](../../hub/swagger_public.yaml#L1504-L1551), [system secret API](../../hub/swagger_public.yaml#L2556-L2640), [mapping schema](../../hub/swagger_public.yaml#L2918-L2930)

A synthetic upload document, retained securely outside the node, might be:

```json
{
  "service-password": "synthetic-password-not-valid",
  "api-key": "synthetic-api-key-not-valid"
}
```

The security guide's CLI entrypoints are:

```sh
sesam put-secrets my_system_id my-system-secrets.json
sesam get-secrets my_system_id
sesam put-secrets my-secrets.json
sesam get-secrets
```

The first pair addresses system-local secrets; the second addresses globals. `get-secrets` lists names, not values. These are reference commands, not an endorsement of running the testing-oriented Sesam client against production: the client guide explicitly warns against production use. Use an approved administration process for production, with the documented HTTP API as the integration contract. [CLI examples](../../hub/documentation/operations/security.rst#L147-L178), [client safety warnings](../../hub/sesam-client.rst#L21-L36)

### Substitution constraints

| Mechanism | Intended use | Configuration scope |
| --- | --- | --- |
| `$SECRET(mysecret)` | Sensitive, write-only values | Supported locations in **System configuration entities only** |
| `$ENV(myvariable)` | Nonsensitive configuration parameters | System, Pipe, and service metadata; variables are **global only** |

A system can compose several references in a string, including secrets and environment variables, but **references cannot be nested**. A property composed from multiple references is always a string. Do not put secrets in pipe transforms or assume every configuration location supports them. The security guide says resolved secret values are used as needed at runtime and are not exposed through the API or ordinary logs; tracing has a separate best-effort warning below. [Secret substitution](../../hub/documentation/operations/security.rst#L193-L253), [environment scope and composition](../../hub/documentation/service-configuration/environment-variables/environment-variables.rst#L6-L46), [no sensitive environment variables](../../hub/documentation/building-blocks/environment-variables.rst)

For example, an outbound URL system with synthetic endpoints and secret references:

```json
{
  "_id": "synthetic-http-service",
  "type": "system:url",
  "url_pattern": "https://$ENV(api-host)/%s",
  "verify_ssl": true,
  "authentication": "basic",
  "username": "$SECRET(service-user)",
  "password": "$SECRET(service-password)",
  "headers": {
    "X-Api-Key": "$SECRET(api-key)"
  }
}
```

## Authentication to external URL and REST systems

URL systems supply HTTP/HTTPS session handling, connection pooling, and authentication to sources and sinks. REST systems extend URL systems, inheriting their configuration properties. These credentials authenticate **Sesam to the remote system**, not a human to the node. [URL responsibilities](../../hub/documentation/service-configuration/systems/configuration-systems-url.rst#L6-L9), [REST inheritance](../../hub/documentation/service-configuration/systems/configuration-systems-rest.rst#L6-L16)

### Built-in authentication and OAuth2

- Authentication is **opt-in**, with no authentication by default. The documented `authentication` values are `basic`, `digest`, `ntlm`, `tripletex`, and `jwt`. For username/password modes, the username only has an effect when both the authentication protocol and password are supplied; password is mandatory when username is provided.
- `authentication: "jwt"` requires `jwt_token` for the remote server. Using `jwt_token` automatically overwrites an `Authorization` header supplied in `headers`. For REST systems, operation-level headers can override system header keys but cannot discard them.
- `oauth2` supports client-credentials and refresh-token grants. Supply `client_id`, `client_secret`, and `token_url`; refresh-token mode additionally requires `access_token` and `refresh_token`. Optional settings include `scope`, `extra` token-request parameters, and `refresh_window` (default 30 seconds before expiry).
- **Do not combine `oauth2` with JWT authentication or `jwt_token`.** The URL contract states that OAuth2 requires TLS-secured transport both for `token_url` and the target `url_pattern`.
- Tripletex configuration requires `consumer_token`, `employee_token`, and `token_url`; `ttl` defaults to 48 hours and expired tokens are automatically refreshed. Store the token inputs as secrets.
- HTTP(S) and SOCKS5 proxy configurations can embed authentication. If used, keep embedded username/password values in system secrets, for example `socks5://$SECRET(proxy-user):$SECRET(proxy-password)@proxy.example.invalid:1080`.

[URL authentication constraints](../../hub/documentation/service-configuration/systems/configuration-systems-url.rst#L101-L174), [REST header rules](../../hub/documentation/service-configuration/systems/configuration-systems-rest.rst#L105-L110)

### REST custom authentication is an extension point

`custom_auth` is documented as **experimental**. It names REST operations for acquiring tokens and makes their response properties available in Jinja's `token` object. `get_token_operation` is required. An optional `get_refresh_token_operation` runs first; initial refresh-token properties can be supplied through `initial_refresh_token` and are later replaced by fetched values.

```mermaid
sequenceDiagram
    participant REST as REST system
    participant Remote as External token service
    opt Refresh-token operation configured
        REST->>Remote: Execute get_refresh_token_operation
        Remote-->>REST: Refresh-token response
        REST->>REST: Make response properties available in token object
    end
    REST->>Remote: Execute get_token_operation
    Remote-->>REST: Access-token response
    REST->>REST: Evaluate expiry expressions and token properties
    REST->>Remote: Execute business operation with templated credentials
```
*Custom authentication obtains remote tokens through configured REST operations before using their properties in business requests.*

Provide `expires_at_expression` or `expires_in_expression`; the former must produce a date, the latter seconds, and a valid absolute expiry takes precedence if both are configured. `refresh_window` defaults to 30 seconds. If a refresh-token operation is configured, provide its corresponding refresh-token expiry expression. Prefer `{{ token.access_token }}`-style references over the deprecated `access_token_property` and `refresh_token_property` helpers. The resulting template can construct an outbound header such as `"Authorization": "Bearer {{ token.access_token }}"`.

A documented limitation matters for recovery: **on-premise single subscriptions keep newly fetched custom-auth refresh tokens only in memory**. After reboot, pipes can fail if a new token had been fetched; `initial_refresh_token` must be manually updated to that new refresh token. Plan retention and restart validation rather than assuming automatic durable token storage. [Custom-auth flow and settings](../../hub/documentation/service-configuration/systems/configuration-systems-rest.rst#L488-L639), [token templates](../../hub/documentation/service-configuration/systems/configuration-systems-rest.rst#L715-L730)

For operation configuration and provider-specific integration work, see [Connectors and contracts](../integrations/connectors-and-contracts.md) and [Extensions and JSON protocols](../integrations/extensions-and-json-protocols.md).

## Transport, reachability, and hosted encryption

### Outbound TLS verification must be explicit

URL systems document `verify_ssl` as **false by default**. Service metadata's `global_defaults.verify_ssl` is also documented with default `false`. For safe HTTPS integrations, set verification to `true` explicitly or establish the global default and inspect overrides. `custom_ca_pem_chain` supplies a PEM certificate chain only when `verify_ssl` is true. HTTPS transport and certificate verification are separate settings: do not copy the unverified prototypes into production or disable verification to work around a certificate issue. REST inherits these URL properties. [URL TLS settings](../../hub/documentation/service-configuration/systems/configuration-systems-url.rst#L86-L97), [global verification default](../../hub/documentation/service-configuration/configuration-metadata.rst#L354-L360)

### Hosted ingress and network policy

The hosted architecture reference describes an Azure Network Security Group in front of each cloud service, with only port **443** openable for the service API. Its reverse proxy terminates TLS and routes API traffic. Certificates are managed through Let's Encrypt; the single-machine description also supports bringing your own certificates. Do not confuse these inbound certificates with a URL system's outbound CA configuration.

The network-policy feature can block public access completely or allow only listed IP addresses/ranges. In the described new architecture, IP allowlisting can move down to the reverse proxy, with custom pipe rules for public and restricted access. The feature reference explicitly states that **outgoing traffic is currently unrestricted**; it is not an egress allowlist guarantee. The portal schema exposes `public-access` and `network-acl`; a network ACL entry requires `address` and may specify `access` as `Allow` or `Deny`, plus an optional `description`. This object format differs from a resource's three-element permission ACL.

Subscriptions are described as isolated on separate hardware, but subscriptions within the same **subscription group share a network**. Evaluate that grouping when planning private connectivity rather than assuming every subscription has an independent network. [Hosted proxy and NSG](../../hub/documentation/operations/behind-the-scenes.rst#L27-L39), [clustered proxy](../../hub/documentation/operations/behind-the-scenes.rst#L58-L74), [isolation and firewall](../../hub/documentation/operations/behind-the-scenes.rst#L108-L116), [network policy](../../hub/features/network-policy.rst), [network settings schema](../../hub/swagger_portal.yaml#L4507-L4519), [network ACL entry](../../hub/swagger_portal.yaml#L3832-L3846)

### VPN setup and limitations

VPN extends Sesam into an on-premises network through **IPSec**. In Management Studio, select Subscription → Products → Enable VPN, then configure the VPN tab. Use the displayed Sesam Peer VPN Gateway and Sesam address spaces to configure the on-premises device. Supply:

- **Gateway Address:** the on-premises device's IP address or FQDN.
- **Address Spaces:** address ranges Sesam should route to that device.
- **Pre-shared Key:** the authentication key between the two VPN devices.

VPN has an additional surcharge. Developer subscriptions are documented without VPN support. Multi and flexi subscriptions support advanced highly available VPN configurations with redundant BGP-enabled connections and custom IPSec rules, arranged through support. VPN reachability does not replace JWT, ACL, or remote-server authentication checks. [VPN procedure and advanced support](../../hub/features/vpn.rst), [Developer limitation](../../hub/documentation/operations/behind-the-scenes.rst#L8-L11)

### Encryption at rest and BYOK: use the feature's scope

The dedicated BYOK reference says hosted disks and remote geo-replicated backup storage use platform-managed encryption keys by default. Its BYOK support means **Sesam manages the encryption key for you**, with the option to revoke it. Revocation generally requires the data to be reloadable afterwards. BYOK is opt-in for **new single subscriptions**, not yet supported for multi subscriptions, and must be enabled through support.

There is a source discrepancy: the general hosted-architecture page still says bringing your own key is not supported. Do not turn that sentence into a blanket limitation, or the dedicated feature into a promise for all deployments. Confirm eligibility with support for the specific subscription. These storage keys are also a different mechanism from the secrets manager's instance-unique encryption key. [BYOK feature](../../hub/features/bring-your-own-key.rst#L6-L9), [general architecture statement](../../hub/documentation/operations/behind-the-scenes.rst#L15-L19), [secret encryption](../../hub/documentation/operations/security.rst#L176-L178)

## Telemetry, tracing, and deletion boundaries

The hosted monitoring reference says shipped logs include service errors, health/status, configuration without embedded data or secrets, kernel logs, and the pipe execution dataset **only when pipe monitoring is enabled**. Failing execution logs can contain the entity objects that caused failure locally, but the reference says those objects are not shipped to Sesam. Prometheus-compatible resource telemetry is pushed from local virtual machines for monitoring and operations. Scope these statements to the described hosted monitoring path, not every custom logger or external integration. [Monitoring data](../../hub/documentation/operations/behind-the-scenes.rst#L88-L106)

**Tracing is a separate exposure risk.** REST and HTTP-endpoint tracing can log headers and body prefixes into pipe execution events. Tracing defaults to off. REST `trace.log_secret_redacted_bytes` defaults to 600; `-1` requests redaction of all secret bytes. The metadata and REST references explicitly describe redaction as **best effort**, with possible leakage. HTTP endpoint tracing describes the same setting in terms of redacting the `Authorization` request header. Do not interpret the ordinary secret-substitution promise as a universal guarantee about trace logs. Keep tracing off unless needed, minimize what is logged, and inspect logs securely before sharing them; never copy credentials or failing entity payloads into tickets or wiki examples. [Global trace behavior and warning](../../hub/documentation/service-configuration/configuration-metadata.rst#L299-L352), [REST trace warning](../../hub/documentation/service-configuration/pipes/configuration-sinks-rest.rst#L79-L128), [HTTP endpoint trace](../../hub/documentation/service-configuration/pipes/configuration-sources-http.rst#L105-L150)

Subscription termination is documented to delete its data and backups, but the **single-machine Azure backup path retains backups for 30 days after deletion**. Self-hosted owners are responsible for off-site backups. This backup-retention exception is distinct from explicitly deleting a secret or retaining your own off-site originals; do not promise instant erasure of every copy. See [Deployment and durability](deployment-and-durability.md) for the backup paths and [Monitoring and troubleshooting](monitoring-and-troubleshooting.md) for operational diagnostics. [Backup responsibility and retention](../../hub/documentation/operations/behind-the-scenes.rst#L45-L51), [termination](../../hub/documentation/operations/behind-the-scenes.rst#L118-L121)

## Security-focused validation before a change

The following are **recommended checks of the documented contracts**, not a claim that this repository contains or has run a node security test suite. Use synthetic credentials, a personal/test subscription, and remote test services:

1. **Role scope and resource denial:** obtain a JWT for the intended subscription. Verify a permitted dataset read and a valid-JWT read without `Read data` permission returning `403 Forbidden`. Check that editing configuration, reading data, and triggering pump operations are tested separately.
2. **Runtime access:** test a pipe whose inherited roles have the required source/target access, then remove one required system grant in the test setup and verify the documented failed run and GUI error.
3. **Secret lifecycle:** list keys without attempting value recovery. POST a targeted rotation and confirm unrelated local key names remain. Delete/recreate a disposable system and verify that local secrets require re-upload from retained originals. Keep this destructive test away from production.
4. **Configuration replacement:** review the complete selected config group before bulk PUT, including permissions and system identity. Do not test a partial group replacement against production or use `force=true` to bypass a failing security configuration.
5. **External authentication:** test the intended provider grant, token expiry/refresh, and outbound header construction. For on-premise single custom auth, include a reboot/recovery test with synthetic refresh tokens.
6. **Network and TLS:** test both allowed and blocked client networks, confirm the configured VPN route reaches the test system, and ensure certificate verification succeeds with the intended trust chain rather than disabling verification.
7. **Telemetry:** if trace is required, inspect its headers/body limits and redaction with synthetic values before enabling it for sensitive traffic.

The CI guide requires a designated CI node, serialized tests, and a node unable to write to external systems; at minimum it should lack the variables and secrets needed for those output connections. The client guide warns against production use and concurrent client commands, while local-testing guidance requires output pipes to be disabled or unable to send externally. These are essential isolation constraints for security experiments as well as functional tests. [CI safety](../../hub/documentation/operations/continuous-integration.rst#L7-L24), [client constraints](../../hub/sesam-client.rst#L21-L42), [local test isolation](../../hub/documentation/operations/testing-locally.rst#L7-L9)
