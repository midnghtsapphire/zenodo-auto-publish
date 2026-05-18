# Deployment Guide — zenodo-auto-publish

Step-by-step instructions for deploying and running `zenodo_auto_publish.py` in production.

---

## Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | 3.10 or later |
| pip | Latest |
| Zenodo account | [zenodo.org](https://zenodo.org/signup/) |
| Zenodo API token | `deposit:write` + `deposit:actions` scopes |

---

## 1. Clone the Repository

```bash
git clone https://github.com/midnghtsapphire/zenodo-auto-publish.git
cd zenodo-auto-publish
```

## 2. Install Dependencies

```bash
pip install requests
```

There are no other dependencies. The script uses only the Python standard library plus `requests`.

## 3. Configure Your API Token

**Never hard-code the token.** Use an environment variable:

```bash
export ZENODO_TOKEN="your_token_here"
```

Or store it in a `.env` file (already in `.gitignore`):

```
ZENODO_TOKEN=your_token_here
```

Then load it:

```bash
export $(grep -v '^#' .env | xargs)
```

### Obtaining a Token

| Environment | URL |
|-------------|-----|
| **Sandbox** (testing) | https://sandbox.zenodo.org/account/settings/applications/tokens/new/ |
| **Production** (live) | https://zenodo.org/account/settings/applications/tokens/new/ |

Required scopes: `deposit:write`, `deposit:actions`

---

## 4. Validate Your Setup

Run the validation script before publishing:

```bash
python validate.py
```

All checks must pass before proceeding to production.

---

## 5. Test in Sandbox (Required Before Production)

Always run a sandbox test first. The sandbox is completely isolated from production — nothing published there becomes a real DOI.

```bash
python zenodo_auto_publish.py \
  --token $ZENODO_TOKEN \
  --file test_document.pdf \
  --title "Sandbox Test" \
  --description "Testing the auto-publish workflow" \
  --author "Walter-Evans, Audrey" \
  --orcid "0009-0005-0663-7832"
  # No --live flag = sandbox mode
```

Confirm the deposit appears at https://sandbox.zenodo.org/me/uploads

---

## 6. Publish to Production

Once sandbox testing passes, run with the `--live` flag using a **production token** (not the sandbox token):

```bash
python zenodo_auto_publish.py \
  --token $ZENODO_TOKEN \
  --file your_document.pdf \
  --title "Your Publication Title" \
  --description "Your abstract." \
  --author "Walter-Evans, Audrey" \
  --orcid "0009-0005-0663-7832" \
  --keywords "keyword1" "keyword2" \
  --type publication \
  --subtype preprint \
  --live
```

The script will prompt for confirmation before publishing. Type `y` to confirm.

---

## 7. Verify the Published Record

After publishing, the script will return a DOI URL. Verify:

1. Open the DOI URL in your browser
2. Confirm title, authors, ORCID, and files are correct
3. Download the uploaded file(s) and verify integrity
4. Check that the access right is `Open Access`

---

## CI/CD Integration (Optional)

To automate publication in a GitHub Actions workflow:

```yaml
- name: Publish to Zenodo
  run: |
    python zenodo_auto_publish.py \
      --token ${{ secrets.ZENODO_TOKEN }} \
      --file output/paper.pdf \
      --title "${{ env.PAPER_TITLE }}" \
      --description "${{ env.PAPER_ABSTRACT }}" \
      --author "Walter-Evans, Audrey" \
      --orcid "0009-0005-0663-7832" \
      --live
  env:
    ZENODO_TOKEN: ${{ secrets.ZENODO_TOKEN }}
```

**Important:** Set `ZENODO_TOKEN` in your repository secrets, not in workflow YAML.

---

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `401 Unauthorized` | Invalid or expired token | Generate a new token with correct scopes |
| `400 Bad Request` | Invalid metadata | Check `--type` and `--subtype` values against [Zenodo docs](https://developers.zenodo.org/) |
| `404 Not Found` | File path incorrect | Use absolute or correct relative paths |
| Connection error | Network issue | Check internet connectivity and Zenodo status |

---

## Environment Variables Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `ZENODO_TOKEN` | Yes | Zenodo API access token |

---

## Security Notes

- Never commit tokens to source control
- Rotate tokens regularly
- Use separate tokens for sandbox and production
- Store secrets in environment variables or a secrets manager, never in `.env` committed to git
