from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from bson import ObjectId 


# class OID(str):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         try:
#             return ObjectId(str(v))
#         except InvalidId:
#             raise ValueError("Not a valid ObjectId")
# class PyObjectId(str):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate
    
#     @classmethod
#     def validate(cls, v):  # 移除了values和**kwargs参数
#         if not ObjectId.is_valid(v):
#             raise ValueError(f"Not a valid ObjectId: {v}")
#         return str(v)
    
class Video(BaseModel):
    #id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    #id: str = Field(description="Video id", alias="_id")
    create_time: str
    favoriting_count: int
    follower_count: int
    description: str
    collect_count: int
    comment_count: int
    digg_count: int
    share_count: int
    qiniuKey: str
    uploadedAt: datetime
    categories: Optional[str] = Field(None)
    game: Optional[str] = Field(None)
    frame_url: Optional[str] = Field(None)


    # class Config:
    #     # json_encoders = {
    #     #     ObjectId: lambda v: str(v),
    #     #     PyObjectId: lambda v: str(v),
    #     # }
    #     json_encoders = {ObjectId: str}
    #     allow_population_by_field_name = True
    #     arbitrary_types_allowed = True

    # class Config:
    #     json_encoders = {
    #         ObjectId: lambda v: str(v),
    #         PyObjectId: lambda v: str(v),
    #     }
    #     json_schema_extra = {
    #         "example": {
    #             "_id": "507f1f77bcf86cd799439011",
    #             # ... 其他字段的示例 ...
    #         }
    #     }
    #     allow_population_by_field_name = True

class Category(BaseModel):
    name: str