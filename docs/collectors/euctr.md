# Euctr

https://www.clinicaltrialsregister.eu/

The EU Clinical Trials Register contains information on interventional clinical trials on medicines conducted in the European Union (EU), or the European Economic Area (EEA) which started after 1 May 2004.

## Source Data Model

Data could be accessed thru the web interface.
Example - https://www.clinicaltrialsregister.eu/ctr-search/trial/2004-000534-36/SK.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

Additional information - https://eudract.ema.europa.eu/

## Warehouse Data Model

[See table definition](https://github.com/opentrials/collectors/blob/master/collectors/euctr/record.py)
for the full data model.

## Primary Identifiers

Trial identifier: `eudract_number_with_country`

## Data Update Strategy

Web interface and source model doesn't have something like
`updated` field. So to stay up to date full scan is needed.

Proposed solution - use [feed](https://www.clinicaltrialsregister.eu/ctr-search/rest/feed/bydates?query=&dateFrom=2000-01-01&dateTo=2015-01-02) of created/updated in the last 7 days items matching the filter parameters.

## License Terms

https://www.clinicaltrialsregister.eu/disclaimer.html
