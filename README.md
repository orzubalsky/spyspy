## spyspy ##

at the moment, spyspy is simply an implementation of django-dynamic-scraper + scrapy.
it let's you create scraper objects and scrapers that work with django models.
the scrapers are used with the scrapy command-line interface to insert data to the django db.

### Installation ###

* $ python bootstrap.py
* $ ./bin/buildout 
* $ cp spyspy/local_settings_sample.py spyspy/local_settings.py 
* edit local_settings.py 

### Running locally ###
* $ ./bin/django runserver


### Scraping ###

* $ cd  <project_dir>/spyspy/apps/spy
* $ ../../../bin/scrapy crawl <spider_name> -a id=<model_id> -a do_action=<yes|no>
* do_action is a boolean that determines whether the scraped data in inserted into the db or not
