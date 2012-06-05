from django.db.models import *
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy.contrib_exp.djangoitem import DjangoItem

class Base(Model):
    """
    Abstract base model class which other models are based on.
    Includes crud date meta data and active/inactive state
    """

    class Meta:
            abstract = True
                    
    created     = DateTimeField(auto_now_add=True, editable=False)
    updated     = DateTimeField(auto_now=True, editable=False)
    
    def __unicode__ (self):
        if hasattr(self, "author") and self.author:
            return self.author
        else:
            return "%s" % (type(self))


class NewsWebsite(Base):
    name            = CharField(max_length=200)
    url             = URLField()
    scraper         = ForeignKey(Scraper, blank=True, null=True, on_delete=SET_NULL)
    scraper_runtime = ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=SET_NULL)

    def __unicode__(self):
        return self.name


class Article(Base):
    news_website    = ForeignKey(NewsWebsite)
    title           = CharField(max_length=200)
    subheader       = CharField(max_length=200, blank=True, null=True)
    published       = CharField(max_length=200, blank=True, null=True)
    authors         = CharField(max_length=200, blank=True, null=True)
    copy            = TextField(blank=True)
    url             = URLField()
    checker_runtime = ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=SET_NULL)    

    def __unicode__(self):
        return self.title
        

class ArticleItem(DjangoItem):
    django_model = Article