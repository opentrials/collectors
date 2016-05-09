FROM python:2.7
WORKDIR /service
COPY requirements.txt requirements.txt
RUN pip install --upgrade -r requirements.txt
COPY collectors collectors
COPY migrations migrations
COPY alembic.ini alembic.ini
COPY Makefile Makefile
COPY scrapy.cfg scrapy.cfg
