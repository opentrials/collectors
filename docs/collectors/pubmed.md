# Pubmed

http://www.ncbi.nlm.nih.gov/pubmed

PubMed comprises more than 26 million citations for biomedical literature from MEDLINE, life science journals, and online books. Citations may include links to full-text content from PubMed Central and publisher web sites.

## Source Data model

Data could be accessed via [E-Utilities](http://www.ncbi.nlm.nih.gov/books/NBK25497/).
Data model of publication - https://www.nlm.nih.gov/bsd/licensee/elements_descriptions.html.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

[See table definition](https://github.com/opentrials/collectors/blob/master/collectors/pubmed/record.py)
for the full data model.

## Primary Identifiers

Trial identifier: `pmid`

## Data Update Strategy

Tha last recent modified data could be searched.
After initial scraping we should use the last 2 days searches
to stay up to date.

## License Terms

http://www.ncbi.nlm.nih.gov/home/about/policies.shtml
