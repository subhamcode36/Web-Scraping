import pymongo

class MongodbPipeline:
    collection_name = 'transcript'

    def open_spider(self,spider):
        self.client = pymongo.MongoClient("mongodb+srv://subhamshreyash90:subham7451@cluster0.ktlrphs.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client['My_Database']
    
    def close_spider(self,spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
    
