# Go-to-Market — zenodo-auto-publish

Market research, competitive analysis, and launch strategy for the `zenodo-auto-publish` tool.

---

## Product Overview

**zenodo-auto-publish** is a Python CLI utility that automates the submission of research documents and supplementary materials to [Zenodo](https://zenodo.org), the open-access scientific repository operated by CERN. It handles deposit creation, file upload, metadata configuration (including ORCID), and publication through a single command.

**Primary use case:** Independent researchers, small labs, and solo scientists who publish preprints, datasets, and supplementary materials to Zenodo and want to automate the manual web UI workflow.

---

## Target Audience

| Segment | Description | Size |
|---------|-------------|------|
| **Independent researchers** | Solo scientists, citizen scientists, PhD students | Large — growing segment as open-access mandates expand |
| **Small research labs** | 2–10 person teams publishing frequently | Medium — underserved by heavyweight institutional tools |
| **Technical writers / open science advocates** | Publish white papers, policy documents, technical reports | Medium |
| **Developers automating CI/CD for research outputs** | Want Zenodo as a publish target in automated pipelines | Niche but high-value |

**Primary persona:** Audrey Walter-Evans — independent ocean energy researcher, publishes preprints and supplementary data, needs repeatable automation without institutional IT support.

---

## Problem Statement

Publishing to Zenodo manually requires:

1. Log in to zenodo.org
2. Navigate to "New Upload"
3. Fill in 12+ metadata fields
4. Upload each file individually
5. Set access rights, license, keywords
6. Confirm and publish
7. Repeat for every version or supplementary update

This is **slow, error-prone, and not repeatable**. Researchers who publish frequently or maintain multiple versions waste hours on this process.

---

## Competitive Analysis

| Tool | Strengths | Weaknesses vs. zenodo-auto-publish |
|------|-----------|-------------------------------------|
| **Zenodo Web UI** | Official, no setup | Manual, slow, not scriptable |
| **Invenio RDM CLI** | Full-featured, extensible | Heavy dependency, complex setup, institutional focus |
| **cff-converter-python** | Citation file format conversion | Not a publisher — no upload capability |
| **Figshare / OSF API clients** | Multi-repo support | Different platforms, not Zenodo-specific |
| **GitHub → Zenodo integration** | Zero config for GitHub repos | Requires GitHub repo; not for standalone docs/PDFs |
| **zenodo-auto-publish** | Minimal deps (requests only), single-file script, ORCID support, sandbox/live toggle | Single-platform (Zenodo only) |

**Differentiators:**
- **Zero friction setup** — `pip install requests` and go
- **ORCID-first** — author attribution is a first-class citizen
- **Sandbox/production parity** — identical commands, single flag difference
- **Single-file** — easy to audit, fork, embed in other workflows
- **Open source, no lock-in**

---

## Distribution Channels

| Channel | Status | Priority |
|---------|--------|----------|
| GitHub (this repo) | ✅ Live | Primary |
| PyPI package (`zenodo-auto-publish`) | ❌ Not yet | High — enables `pip install zenodo-auto-publish` |
| Zenodo community listing | ❌ Not yet | Medium — meta: publish the tool to Zenodo itself |
| Dev.to / Hashnode article | ❌ Not yet | Medium — "Automate your Zenodo submissions in 5 minutes" |
| Twitter/X thread | ❌ Not yet | Medium — open science community |
| r/MachineLearning, r/Physics, r/OpenScience | ❌ Not yet | Low-medium |
| ORCID community forums | ❌ Not yet | Low |

---

## Launch Plan

### Phase 1 — v1.0 Hardening (Current sprint)
- [x] Core script functional
- [x] Sandbox + production modes
- [x] ORCID support
- [ ] Tests (`test_zenodo_auto_publish.py`)
- [ ] PyPI packaging (`pyproject.toml`)
- [ ] Validate production end-to-end

### Phase 2 — Distribution
- [ ] Publish to PyPI as `zenodo-auto-publish`
- [ ] Publish a Zenodo record of the tool itself (dogfood)
- [ ] Write a Dev.to launch article
- [ ] Share in open science communities

### Phase 3 — Whitepaper Integration
- [ ] Bundle with whitepaper generation module (if/when built)
- [ ] One-command: generate whitepaper → auto-publish to Zenodo
- [ ] GitHub Action: on tagged release, publish paper to Zenodo automatically

---

## Success Metrics

| Metric | Target (90 days post-launch) |
|--------|------------------------------|
| GitHub stars | 50+ |
| PyPI downloads/month | 100+ |
| Issues/PRs from outside contributors | 3+ |
| Zenodo records created using this tool | 5+ |

---

## Pricing

Free and open source. MIT-adjacent (see LICENSE).  
No paid tier, no SaaS, no vendor lock-in.

---

## Risks

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Zenodo API changes | Low | Pin to stable API version; monitor changelog |
| Token management complexity for new users | Medium | DEPLOYMENT_GUIDE.md, clear error messages |
| Scope creep (multi-platform support) | Medium | Stay Zenodo-only until v1.0 is solid |
| Competition from official Zenodo CLI | Low | Unlikely near-term; differentiate on simplicity |
