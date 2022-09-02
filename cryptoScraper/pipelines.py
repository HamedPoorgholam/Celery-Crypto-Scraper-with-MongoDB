# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from pymongo import MongoClient
from itemadapter import ItemAdapter


class MongoDbPipeline(object):
    collection = 'Cryptos'

    def __init__(self):

        self.mongo_uri =  'mongodb+srv://hamedpoor:81980630@hpcluster.2yhbryy.mongodb.net/?retryWrites=true&w=majority'
        self.mongo_db = 'crypto'
    def open_spider(self,spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection].insert_one(dict(item))
        return item
