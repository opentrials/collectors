# Scraper

Terminology:
- scraper - Scrapy project (the core python package)
- spider - object with rules and extractors to scrape concrete register
- item - dictionary based on data model with scraped data for register
- pipeline - item processor (like store item in database)
- utils - collection of utils for register
- stack - collection of scrapy process containers to run on Tutum
- warehouse - database to store collected data

## Scraper

Scraper is a valid `Scrapy` project so it uses all well-known
design patterns and follows the framework architecture.

To scrape a register it need:
- spider
- item (data model)
- utils (optionally)

While scraping `pipelines.Database` will store item data to the warehouse.

## Stacks

Stacks provide different scraping strategies and tasks.
For example to implement initial scraping and then only
update warehouse to stay up to date could be used:
- entire stack (processes like `scrapy crawl <register> -a date_from=2001-01-01`)
- recent stack (processes like `scrapy crawl <register>` - last 2 days be default)

## Warehouse

Warehouse is a database to store scraped data:
- table per register
- fields are typed when possible
- as primary keys trial identifiers is used
- meta data: created(timestamp), updated(timestam), source (url)

## Deployment

Deployment process:
- CI/CD server builds Docker image from scraper package and push
it to opentrials account on Docker hub.
- CI/CD server updates stacks on Tutum.

## Management

To start/stop an actual scraping Tutum dashboard is used:

![Dashboard Storage](https://raw.githubusercontent.com/opentrials/scraper/master/files/dashboard.png)
