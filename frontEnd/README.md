# Tritonix FE
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