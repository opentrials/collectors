# JPRN

http://www.umin.ac.jp/ctr/

UMIN was establshed in 1989 as a cooperative organization for national medical schools in Japan, sponsored by the Ministry of Education, Culsutre, Science, Sports and Technology (MEXT), Japan. Its most services are now made available to other heath care researchers via the Internet.

## Source Data Model

Data could be accessed thru the web interface.
Example - https://upload.umin.ac.jp/cgi-open-bin/ctr/ctr.cgi?function=brows&action=brows&type=summary&recptno=R000023978&language=E.
Data is moving to the warehouse as it is with additional type casting.
See the next section for more details.

## Warehouse Data Model

[See table definition](https://github.com/opentrials/collectors/blob/master/collectors/jprn/record.py)
for the full data model.

## Primary Identifiers

Trial identifier: `unique_trial_number`

## Data Update Strategy

Trials have `date_and_time_of_last_update` field.
Newly created and updated trials have to be searched
using desc last_updated ordering (by default).
After initial scraping we should use the last 2 pages of search results
to stay up to date (`recent` stack).

## License Terms

http://www.umin.ac.jp/ctr/UMIN-CTR_e_FAQ.htm
