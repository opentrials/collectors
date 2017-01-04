# NCT

https://clinicaltrials.gov/

ClinicalTrials.gov is a registry and results database of publicly and privately supported clinical studies of human participants conducted around the world.

## Source Data model

Analysis of NCT data model:
- copy text from `https://www.clinicaltrials.gov/ct2/html/images/info/public.xsd`
- past text to `http://xmlgrid.net/` and click `Submit`
- now you can discover the whole data model, data types etc

> Only around 10% of studies have a `clinical_results` section - https://www.clinicaltrials.gov/ct2/help/how-find/find-study-results

---

![](https://cloud.githubusercontent.com/assets/557395/10075868/d77548fe-62e0-11e5-84e0-c81ec6badcfe.png)

## Warehouse Data Model

[See table definition](https://github.com/opentrials/collectors/blob/master/collectors/nct/record.py)
for the full data model.

## Primary Identifiers

Trial identifier: `nct_id`

## Data Update Strategy

Trials could be serched with `lastchanges_date` filter.
After initial scraping we should use the last 2 days searches
to stay up to date (`recent` stack).

## License Terms

https://clinicaltrials.gov/ct2/about-site/terms-conditions
