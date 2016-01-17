FROM python:2.7
WORKDIR /service
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY scraper scraper
COPY scrapy.cfg scrapy.cfg
CMD scrapy list | xargs -n 1 scrapy crawl
