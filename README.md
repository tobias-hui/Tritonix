# Tritonix
七牛云1024创作节web端短视频参赛项目
![tritonix](http://cdn.tritonix.xyz/tritonix_project.png)

tritonix是一款基于

### Demo 体验地址：
http://118.31.56.248/

#### 后端应用体验地址：
http://118.31.56.248:7860/

demo视频： http://cdn.tritonix.xyz/eedb1ec09451ffda696525eea5e3de3f.mp4

# 🎥 Tritonix 后端

## 🌟 项目概述
Tritonix 是一个具有现代风格的 Web 短视频平台，类似于抖音，支持视频观看、上传和分享。这个平台致力于为用户提供流畅且富有互动性的视频体验。

## 🚀 快速开始

### 前提条件
- MongoDB
- Python 3.10+
- Poetry
- qiniu

### 安装与启动

克隆仓库并安装依赖：

```bash
git clone https://github.com/tobias-hui/Tritonix.git
cd Tritonix/backend
poetry install
```
在 /backend/app/core/ 下创建 .env 文件并配置必要的环境变量。

启动应用：
```bash
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 7860
```

在浏览器中访问 http://localhost:7860/docs 以探索 API 文档。

### 📂 目录结构
```css
backend/
├─ api/
├─ core/
├─ db/
├─ models/
├─ schemas/
├─ services/
└─ main.py
```
- api/ - 存放路由和控制器。
- core/ - 应用的核心配置。
- db/ - 数据库操作封装。
- models/ - 数据库模型定义。
- schemas/ - 数据验证和转换模型。
- services/ - 业务逻辑实现。

### 📘 API 文档
通过 /docs 路径查看完整的 Swagger UI 文档，了解所有可用的 API 端点。

### 👨‍💻 贡献
目前该项目不接受外部贡献，感谢理解。

### 📜 许可证
项目将在比赛结束后根据 MIT 许可证开源。

### 📮 联系我们
遇到任何问题或有任何建议，欢迎通过 huik99298@gamil.com 联系我们。

# Tritonix 前端

## 技术栈
vue3.2、vite、typescript

## 启动
`npm i` 安装依赖
`npm run dev` 启动开发服务器

## 上下滑动
支持鼠标点击上下拖动切换与键盘方向键切换

视频使用列表渲染，往下滑动时监测当前显示的index与总长度，接近总长度时执行loadMore获取更多视频。

拖动时记录起始位置与结束位置，差距大于某一临界值时执行上下滑动逻辑，每个视频通过定位来放到各自的位置，可视区域通过translate来滑动
```typescript
function getDistance(index: number) {
  // 滑动到整数倍视频模块高度
  return -index * slideState.wrapper.height;
}
```