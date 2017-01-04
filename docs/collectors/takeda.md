# Takeda

http://www.takedaclinicaltrials.com/

This website is designed to advance Takeda's commitment to the health of patients and the science of medicine by providing greater access to information on Takeda's clinical trials while safeguarding patients' confidentiality.

## Source Data Model

Data could be accessed thru the web interface.
Example - http://www.takedaclinicaltrials.com/browse/summary/01-00-TL-OPI-501#overview.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

[See table definition](https://github.com/opentrials/collectors/blob/master/collectors/takeda/record.py)
for the full data model.

## Primary Identifiers

Trial identifier: `takeda_trial_id`

## Data Update Strategy

Web interface and source model doesn't have something like
`updated` field. So to stay up to date full scan is needed.

## License Terms

http://www.takedaclinicaltrials.com/legal/terms
