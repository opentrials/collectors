# JPRN

http://www.umin.ac.jp/ctr/

UMIN was establshed in 1989 as a cooperative organization for national medical schools in Japan, sponsored by the Ministry of Education, Culsutre, Science, Sports and Technology (MEXT), Japan. Its most services are now made available to other heath care researchers via the Internet.

## Source Data Model

Data could be accessed thru the web interface.
Example - https://upload.umin.ac.jp/cgi-open-bin/ctr/ctr.cgi?function=brows&action=brows&type=summary&recptno=R000023978&language=E.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

See item definition for the full data model:

https://github.com/opentrials/scraper/blob/master/scraper/spiders/jprn/item.py

## Primary Identifiers

Trial identifier: `unique_trial_number`

## Data Update Strategy

Trials could be serched with `date_and_time_of_last_update` filter.
After initial scraping we should use the last 2 days searches
to stay up to date (`recent` stack).

## License Terms

http://www.umin.ac.jp/ctr/UMIN-CTR_e_FAQ.htm
