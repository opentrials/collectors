FROM python:2.7
WORKDIR /service
COPY requirements.txt requirements.txt
RUN pip install --upgrade -r requirements.txt
COPY scraper scraper
COPY warehouse warehouse
COPY alembic.ini alembic.ini
COPY scrapy.cfg scrapy.cfg
