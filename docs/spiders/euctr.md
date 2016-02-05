# Euctr

https://www.clinicaltrialsregister.eu/

The EU Clinical Trials Register contains information on interventional clinical trials on medicines conducted in the European Union (EU), or the European Economic Area (EEA) which started after 1 May 2004.

## Source Data Model

Data could be accessed thru the web interface.
Example - https://www.clinicaltrialsregister.eu/ctr-search/trial/2004-000534-36/SK.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

See item definition for the full data model:

https://github.com/opentrials/scraper/blob/master/scraper/spiders/euctr/item.py

## Primary Identifiers

Trial identifier: `eudract_number_with_country`

## Data Update Strategy

Trials could be serched with `dateFrom/dateTo` filter.
After initial scraping we should use the last 2 days searches
to stay up to date (`recent` stack).

## License Terms

https://www.clinicaltrialsregister.eu/disclaimer.html
