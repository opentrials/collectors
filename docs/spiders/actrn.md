# ACTRN

http://www.isrctn.com/

The ANZCTR is an online registry of clinical trials being
undertaken in Australia, New Zealand and elsewhere.

## Source Data Model

Data could be accessed thru the web interface.
Example - https://www.anzctr.org.au/Trial/Registration/TrialReview.aspx?id=369698&isReview=true.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

See item definition for the full data model:

https://github.com/opentrials/scraper/blob/master/scraper/spiders/actrn/item.py

## Primary Identifiers

Trial identifier: `trial_id`

## Data Update Strategy

Trials could be serched with `date_registered` filter.
After initial scraping we should use the last 2 days searches
to stay up to date (`recent` stack).

## License Terms

http://www.anzctr.org.au/Support/Terms.aspx
