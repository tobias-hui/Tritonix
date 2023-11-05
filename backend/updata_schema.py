from pymongo import MongoClient
from bson import ObjectId

from app.core.config import Config

client = MongoClient(Config.MONGODB_URL)
db = client[Config.MONGO_DB]
collection = db[Config.MONGO_COLLECTION]

def batch_update_add_id_field():
    # 遍历集合中的所有文档
    for document in collection.find({}):
        # 只有当文档没有'id'字段时才进行更新
        if 'id' not in document:
            # 将'_id'字段的ObjectId转换为字符串，并设置为'id'字段
            collection.update_one(
                {'_id': document['_id']},
                {'$set': {'id': str(document['_id'])}}
            )

# 执行批量更新
batch_update_add_id_field()
