# GSK

http://www.gsk-clinicalstudyregister.com/

The GlaxoSmithKline  (GSK)  Clinical Study Register provides an easily accessible repository of data from GSK-Sponsored Clinical Studies, supplementing communication in journals, at scientific meetings, in letters to healthcare professionals, and in approved prescribing information. It is important to emphasise that approved prescribing information must continue to guide appropriate use of GSK medicines. This information may vary from country to country.

## Source Data Model

Data could be accessed thru the web interface.
Example - http://www.gsk-clinicalstudyregister.com/study/100901.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

See item definition for the full data model:

https://github.com/opentrials/scraper/blob/master/scraper/spiders/gsk/item.py

## Primary Identifiers

Trial identifier: `study_id`

## Data Update Strategy

Trials could be serched with `last_updated` filter.
After initial scraping we should use the last 2 days searches
to stay up to date (`recent` stack).

## License Terms

http://www.gsk.com/en-gb/terms-of-use/
