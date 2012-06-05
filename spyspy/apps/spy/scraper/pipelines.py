from django.db.utils import IntegrityError
from scrapy import log
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime
from datetime import datetime


class DjangoWriterPipeline(object):

    def process_item(self, item, spider):
        try:
            item['news_website'] = spider.ref_object

            checker_rt = SchedulerRuntime(runtime_type='C')
            checker_rt.save()
            item['checker_runtime'] = checker_rt

            item.save()
            spider.action_successful = True
            spider.log("Item saved.", log.INFO)

        except IntegrityError, e:
            spider.log(str(e), log.ERROR)
            raise DropItem("Missing attribute.")

        return item
        
        
class DatePipeline(object):
        
    vat_factor = 1.15

    def process_item(self, item, spider):
        if item['pub_date']:
            item['pub_date'] = datetime.strptime(item['pub_date'], "%Y-%m-%d")
            return item