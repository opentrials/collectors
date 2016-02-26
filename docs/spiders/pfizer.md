# GSK

http://www.pfizer.com/research/clinical_trials

Pfizer works to discover and develop innovative, safe, and effective ways to prevent or treat some of the world’s most challenging diseases. We are committed to the safety of patients who take part in our trials, and uphold the highest ethical standards in all of our research initiatives.

## Source Data Model

Data could be accessed thru the web interface.
Example - http://www.pfizer.com/research/clinical_trials/find_a_trial/NCT00795938.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

See item definition for the full data model:

https://github.com/opentrials/scraper/blob/master/scraper/spiders/pfizer/item.py

## Primary Identifiers

Trial identifier: `nct_id`

## Data Update Strategy

Web interface and source model doesn't have something like
`updated` field. So to stay up to date full scan is needed.

## License Terms

http://www.pfizer.com/general/terms
