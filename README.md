# Zenodo Auto-Publish Script

A Python utility for automatically publishing research documents and supplementary materials to Zenodo with full metadata support, including ORCID author identification.

## Features

- **Automated Deposit Creation**: Create new Zenodo deposits programmatically
- **File Upload**: Upload main documents and supplementary materials
- **Metadata Management**: Set comprehensive metadata including authors, ORCID, keywords, and descriptions
- **ORCID Support**: Automatically include ORCID identifiers for proper researcher attribution
- **Flexible Publishing**: Support for multiple document types (publications, posters, datasets, etc.)
- **Sandbox Testing**: Test integration against Zenodo's sandbox environment before publishing to production
- **Interactive Confirmation**: Prompt before publishing to prevent accidental submissions

## Installation

```bash
pip install requests
```

## Usage

### Basic Example

```bash
python zenodo_auto_publish.py \
  --token YOUR_ZENODO_API_TOKEN \
  --file path/to/main_document.pdf \
  --title "Your Research Title" \
  --description "Your research abstract or description" \
  --author "Walter-Evans, Audrey" \
  --orcid "0009-0005-0663-7832" \
  --keywords "keyword1" "keyword2" "keyword3" \
  --type publication \
  --subtype preprint
```

### With Supplementary Materials

```bash
python zenodo_auto_publish.py \
  --token YOUR_ZENODO_API_TOKEN \
  --file main_paper.pdf \
  --supp infographic1.jpg infographic2.jpg data.csv \
  --title "Ocean-2 V2: Wave Energy Converter" \
  --description "Advanced wave energy converter with green hydrogen integration" \
  --author "Walter-Evans, Audrey" \
  --orcid "0009-0005-0663-7832" \
  --keywords "wave energy" "green hydrogen" "ocean energy" \
  --type publication \
  --subtype preprint
```

### Testing with Sandbox

```bash
python zenodo_auto_publish.py \
  --token YOUR_SANDBOX_TOKEN \
  --file test_document.pdf \
  --title "Test Publication" \
  --description "Testing the auto-publish workflow" \
  --author "Test, Author" \
  --orcid "0009-0005-0663-7832"
  # Note: --live flag is NOT used, defaults to sandbox
```

### Publishing to Production

```bash
python zenodo_auto_publish.py \
  --token YOUR_PRODUCTION_TOKEN \
  --file document.pdf \
  --title "Your Publication" \
  --description "Your description" \
  --author "Your, Name" \
  --orcid "YOUR-ORCID-ID" \
  --live  # Enable production Zenodo
```

## Command-Line Arguments

| Argument | Required | Description |
| :--- | :--- | :--- |
| `--token` | Yes | Zenodo API access token (obtain from https://zenodo.org/account/settings/applications/tokens/new/) |
| `--file` | Yes | Path to the main document to upload |
| `--supp` | No | Space-separated list of supplementary files |
| `--title` | Yes | Title of the publication |
| `--description` | Yes | Abstract or description of the publication |
| `--author` | No | Author name in format "Family, Given" (default: Audrey Walter-Evans) |
| `--orcid` | No | Author ORCID identifier (default: 0009-0005-0663-7832) |
| `--keywords` | No | Space-separated keywords for indexing |
| `--type` | No | Upload type: publication, poster, image, dataset, etc. (default: publication) |
| `--subtype` | No | Publication subtype: preprint, article, report, etc. (default: preprint) |
| `--live` | No | Use production Zenodo (default: sandbox for testing) |

## Obtaining a Zenodo API Token

1. Create a Zenodo account at https://zenodo.org/signup/
2. Go to https://zenodo.org/account/settings/applications/tokens/new/
3. Create a new personal access token with scopes: `deposit:write` and `deposit:actions`
4. Copy the token and use it with the `--token` argument

For sandbox testing, use https://sandbox.zenodo.org/ instead.

## Metadata Fields

The script automatically sets the following metadata:

- **Title**: Your publication title
- **Description**: Abstract or summary
- **Creators**: Author name and ORCID
- **Access Right**: Open Access (default)
- **License**: CC-BY 4.0 (default, can be customized)
- **Keywords**: Searchable terms for discovery
- **Publication Type**: Preprint, article, report, etc.

## Workflow

1. Prepare your document and supplementary files
2. Generate or obtain your Zenodo API token
3. Run the script with your parameters
4. Review the output and confirm publication
5. Access your published record at the provided DOI URL

## Example: Ocean-2 V2 Research Publication

```bash
python zenodo_auto_publish.py \
  --token $ZENODO_TOKEN \
  --file Walter-Evans-Ocean2-V2-SSRN-Paper.pdf \
  --supp ocean2_infographic.jpg ocean2_roadmap.jpg \
  --title "Ocean-2 V2: Scaling Deep-Ocean Wave Energy through Integrated Overtopping and Green Hydrogen Conversion" \
  --description "Technical analysis of Ocean-2 V2 improvements, comparison to V1, and innovation claims for wave energy conversion with integrated hydrogen production." \
  --author "Walter-Evans, Audrey" \
  --orcid "0009-0005-0663-7832" \
  --keywords "wave energy converter" "green hydrogen" "blue economy" "renewable energy" "ocean-2 v2" \
  --type publication \
  --subtype preprint \
  --live
```

## Error Handling

The script provides detailed error messages for:

- Invalid API tokens (401 Unauthorized)
- Missing files (404 Not Found)
- Invalid metadata (400 Bad Request)
- Network issues (connection errors)

If a deposit fails, the script will display the error response and exit gracefully without publishing.

## References

- [Zenodo REST API Documentation](https://developers.zenodo.org/)
- [ORCID Integration](https://orcid.org/)
- [Creative Commons Licenses](https://creativecommons.org/)

## License

This script is provided as-is for research and publication purposes.

## Author

Audrey Walter-Evans  
ORCID: 0009-0005-0663-7832  
GitHub: MIDNGHTSAPPHIRE
