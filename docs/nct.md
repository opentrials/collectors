# NCT

https://clinicaltrials.gov/

ClinicalTrials.gov is a registry and results database of publicly and privately supported clinical studies of human participants conducted around the world.

## Source Data model

Analysis of NCT data model.

### Visual representation

- copy text from `https://www.clinicaltrials.gov/ct2/html/images/info/public.xsd`
- past text to `http://xmlgrid.net/` and click `Submit`
- now you can discover the whole data model, data types etc

> Only around 10% of studies have a `clinical_results` section - https://www.clinicaltrials.gov/ct2/help/how-find/find-study-results

---

![](https://cloud.githubusercontent.com/assets/557395/10075868/d77548fe-62e0-11e5-84e0-c81ec6badcfe.png)

### Textual representation

```
# Plain value fields

download_date
link_text
url
org_study_id
nct_id
brief_title
acronym
official_title
source
brief_summary
detailed_description
overall_status
why_stopped
start_date
completion_date_actual
completion_date_anticipated
primary_completion_date_actual
primary_completion_date_anticipated
phase
study_type
study_design
target_duration
number_of_arms
number_of_groups
enrollment_actual
enrollment_anticipated
biospec_retention
biospec_descr
verification_date
lastchanged_date
firstreceived_date
is_fda_regulated
is_section_801
has_expanded_access

# Dict value fields

oversight_info
eligibility
overall_contact
overall_contact_backup
responsible_party
clinical_results
condition_browse
intervention_browse

# List value fields

secondary_ids
nct_aliases
sponsors
primary_outcomes
secondary_outcomes
other_outcomes
conditions
arm_groups
interventions
overall_officials
locations
location_countries
removed_countries
links
references
results_references
keywords
```

## Warehouse Data Model

## Primary Identifiers

## Data Update Strategy

## License Terms

https://clinicaltrials.gov/ct2/about-site/terms-conditions
