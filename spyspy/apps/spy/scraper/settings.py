import sys
import os.path

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path = sys.path + [os.path.join(PROJECT_ROOT, '../../../..'), os.path.join(PROJECT_ROOT, '../../..')]

from django.core.management import setup_environ
import spyspy.settings
setup_environ(spyspy.settings)

BOT_NAME = 'spyspy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'scraper',]
NEWSPIDER_MODULE = 'scraper'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.ValidationPipeline',
    'scraper.pipelines.DjangoWriterPipeline',
]