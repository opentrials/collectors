# ISRCTN

http://www.isrctn.com/

The ISRCTN registry is a primary clinical trial registry recognised by WHO and ICMJE that accepts all clinical research studies (whether proposed, ongoing or completed), providing content validation and curation and the unique identification number necessary for publication. All study records in the database are freely accessible and searchable.

## Source Data Model

Data could be accessed thru the web interface.
Example - http://www.isrctn.com/ISRCTN13619480.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

[See table definition](https://github.com/opentrials/collectors/blob/master/collectors/isrctn/record.py)
for the full data model.

## Primary Identifiers

Trial identifier: `isrctn_id`

## Data Update Strategy

Trials could be serched with `last_edited` filter.
After initial scraping we should use the last 2 days searches
to stay up to date (`recent` stack).

## License Terms

http://www.isrctn.com/page/terms
