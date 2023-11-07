from pymongo import MongoClient, UpdateOne

from app.core.config import Config

client = MongoClient(Config.MONGODB_URL)
db = client[Config.MONGO_DB]
collection = db[Config.MONGO_COLLECTION]
#collection = db['pet_videos']


def batch_update_add_id_field():
    operations = []
    for document in collection.find({'id': {'$exists': False}}):  # 只查询没有 'id' 字段的文档
        operations.append(
            UpdateOne(
                {'_id': document['_id']},
                {'$set': {'id': str(document['_id'])}}
            )
        )
    
    if operations:  # 如果有需要更新的操作
        result = collection.bulk_write(operations)
        print(f"Updated {result.modified_count} documents.")
    else:
        print("No documents to update.")

#def batch_update_add_author_field():


# 执行批量更新
batch_update_add_id_field()

