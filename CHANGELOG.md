# Changelog

All notable changes to **zenodo-auto-publish** are documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)  
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

---

## [Unreleased]

### Added
- `.github/labels.yml` — canonical revvel-standards label set (status, type, priority, product, release)
- `.github/workflows/sync-labels.yml` — auto-syncs labels to GitHub on push to main
- `.github/PULL_REQUEST_TEMPLATE.md` — PR template with required label checklist
- `.github/ISSUE_TEMPLATE/feature.yml` — structured feature request with auto-labels
- `.github/ISSUE_TEMPLATE/bug.yml` — structured bug report with auto-labels
- `.github/ISSUE_TEMPLATE/work-request.yml` — structured WR template for chores/tasks
- `CHANGELOG.md` — this file, per revvel-standards
- `DEPLOYMENT_GUIDE.md` — step-by-step production deployment guide
- `GO_TO_MARKET.md` — market research, competitive analysis, launch strategy
- `validate.py` — deployment readiness validation script

---

## [1.0.0] — 2026-05-02

### Added
- `zenodo_auto_publish.py` — core script for automated Zenodo deposition
- Sandbox / production mode toggle via `--live` flag
- Multi-file upload: main document + supplementary materials
- Full Zenodo metadata: title, description, creators, ORCID, license, keywords, upload type
- Interactive confirmation before publish to prevent accidental submissions
- Detailed error output for 400/401/404 responses

[Unreleased]: https://github.com/midnghtsapphire/zenodo-auto-publish/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/midnghtsapphire/zenodo-auto-publish/releases/tag/v1.0.0
