# ICTRP

http://apps.who.int/trialsearch/Default.aspx

The Clinical Trials Search Portal provides access to a central database containing the trial registration data sets provided by the registries listed on the right. It also provides links to the full original records.

## Source Data Model

Data could be accessed thru the web interface (http basic auth is required for crawling).
Example - http://apps.who.int/trialsearch/Trial3.aspx?trialid=NCT00399620.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

See item definition for the full data model:

https://github.com/opentrials/scraper/blob/master/scraper/spiders/ictrp/item.py

## Primary Identifiers

Trial identifier: `main_id`

## Data Update Strategy

Web interface and source model doesn't have something like
`updated` field. So to stay up to date full scan is needed.

Proposed solution - add algorithm based on `main_id` intervals showed on
index page for crawling.

## License Terms

http://www.who.int/about/copyright/en/
