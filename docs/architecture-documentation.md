## Tritonix Web视频播放工具架构设计
<img src="https://media.discordapp.net/attachments/1111594227298730015/1171460504309477507/3.png?ex=655cc29c&is=654a4d9c&hm=8cdfd8cabd3ec705a66f5531186dd2f3ef0c1c2654612c07c7f6fad44096c857&=&width=1126&height=378" width="300" height="100">  


#### 概述:
---
Tritonix 是一个基于 Vue.js 和 FastAPI 的Web视频播放应用。它旨在通过用户驱动的内容推荐系统，给用户提供一个个性化和富有洞察力的视频观看体验。
-----

## 系统架构
<img src="https://cdn.discordapp.com/attachments/1111594227298730015/1171477489382608998/How_it_worksAWS2.png?ex=655cd26e&is=654a5d6e&hm=0e2707ac688795fdbd167c6129e992cf988e5004c594bcff65911ba86417553e&"> 
#### 前端
互动demo： http://118.31.56.248/

    技术栈: 
    - Vue.js: 提供动态用户界面构建能力。
    功能: 
    - 视频播放浏览: 允许用户流畅地播放视频内容。
    用户交互: 
    - 支持用户注册、登录、点赞、收藏等互动功能。

#### 后端
互动demo： http://118.31.56.248:7860/

    技术栈:
    - FastAPI: 提供快速、高效的后端服务开发。
    身份验证:
    - JWT认证: 保护用户相关接口，确保交互的安全性。
    数据存储:
    - MongoDB: 提供灵活的文档存储，便于快速迭代和开发。
    对象存储：
    - 七牛云Kodo：爬虫后的视频存储
    - 七牛云视频截帧：视频的缩略图和封面图
    - 七牛云高斯模糊：视频播放时的模糊背景

### API 设计
根据OpenAPI规范，我们定义了如下主要接口：

视频信息相关接口
```
GET /api/v1/categories
GET /api/v1/categories/{category_id}/videos
GET /api/v1/videos/search
GET /api/v1/videos/recommend
GET /api/v1/videos/{video_id}
```

视频上传与播放
```
POST /api/v1/videos
GET /api/v1/videos/{video_id}/playback-url (Deprecated)
GET /api/v1/videos/{video_id}/share-link
```

用户相关接口
```
POST /api/v1/users/register
POST /api/v1/users/login
```

用户互动相关接口
```
PUT /api/v1/users/{user_id}/like/{video_id}: 
DELETE /api/v1/users/{user_id}/like/{video_id}: 

PUT /api/v1/users/{user_id}/collect/{video_id}: 
DELETE /api/v1/users/{user_id}/collect/{video_id}: 

GET /api/v1/users/{user_id}/like: 
GET /api/v1/users/{user_id}/collect: 
```

### 安全措施
- JWT认证: 使用JWT令牌来验证和授权用户操作。
- 密码加密: 密码在存储前会被转换成哈希值，确保用户信息的安全。

### 数据模型
视频 (Video)
```
    id: Optional[str] = Field(None)
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
    cover_url: Optional[str] = Field(None)
    playback_url: Optional[str] = Field(None)
```
    统计信息：播放次数、点赞数、分享数。
    存储：关联七牛云存储的key用于视频文件存储。
    动态链接：动态生成的播放URL、封面图片URL。
用户 (User)
```
    id: Optional[str] = Field(None, description="Unique identifier in the database")
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    collection: List[str] = []  # 用户收藏的视频ID列表
    like: List[str] = []  # 用户点赞的视频ID列表
    follow: List[str] = []  # 用户关注的用户ID列表
```
    身份信息：邮箱、用户名和加密后的密码。
    公共信息：头像和个人资料。