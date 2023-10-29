import Mock from 'mockjs'

import { getLocalVideos } from './resource'

Mock.mock(/mock\/recommendVideo/, 'get', options => {
  const { url } = options
  const currentPage = ~~getParam(url, 'currentPage')
  const currentPageSize = ~~getParam(url, 'currentPageSize')
  const videos = getLocalVideos(currentPage, currentPageSize)
  return Mock.mock({
    code: 200,
    data: {
      total: 16,
      videos
    },
    msg: ''
  })
})

function getParam(url: string, name: string) {
  const exp = new RegExp(`${name}=(\\w+)`)
  return exp.exec(url)![1]
}