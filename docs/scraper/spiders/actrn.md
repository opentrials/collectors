# ACTRN

http://www.anzctr.org.au/

The ANZCTR is an online registry of clinical trials being
undertaken in Australia, New Zealand and elsewhere.

## Source Data Model

Data could be accessed thru the web interface.
Example - https://www.anzctr.org.au/Trial/Registration/TrialReview.aspx?id=369698&isReview=true.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

For more information - http://www.anzctr.org.au/docs/ANZCTR%20Data%20field%20explanation.pdf

## Warehouse Data Model

See item definition for the full data model:

https://github.com/opentrials/scraper/blob/master/scraper/spiders/actrn/item.py

## Primary Identifiers

Trial identifier: `trial_id`

## Data Update Strategy

Web interface and source model doesn't have something like
`updated` field. So to stay up to date full scan is needed.

## License Terms

http://www.anzctr.org.au/Support/Terms.aspx
