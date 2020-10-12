# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import os

from ZZDPDPORDMU.settings import SCRAPED_DATA_LOCATION


class DeclarationsRegisterPipeline:
    def process_item(self, item, spider):
        if len(item['contracts']) > 0:
            file_name = '%s (ЕИК %s).json' % (item['legal_entity_name'], item['legal_entity_id'])
            file_path = os.path.join(SCRAPED_DATA_LOCATION, file_name)
            with open(file_path, 'w', encoding='utf-8') as fp:
                json.dump(item, fp, ensure_ascii=False, indent=4, separators=(',', ': '))
