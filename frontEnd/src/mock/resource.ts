// import video0 from "@/assets/video/qq0.mp4"
// import video1 from "@/assets/video/qq1.mp4"
// import video2 from "@/assets/video/qq2.mp4"
// import video3 from "@/assets/video/qq3.mp4"
// import video4 from "@/assets/video/qq4.mp4"
// import video5 from "@/assets/video/qq5.mp4"
// import video6 from "@/assets/video/qq6.mp4"
// import video7 from "@/assets/video/qq7.mp4"
// import video8 from "@/assets/video/qq8.mp4"
// import video9 from "@/assets/video/qq9.mp4"
// import video10 from "@/assets/video/qq10.mp4"
// import video11 from "@/assets/video/qq11.mp4"
// import video12 from "@/assets/video/qq12.mp4"
// import video13 from "@/assets/video/qq13.mp4"
// import video14 from "@/assets/video/qq14.mp4"
// import video15 from "@/assets/video/qq15.mp4"

import { RecommendVideo, VideoInfo } from "@/types/video"
import getUid from "@/utils/getUid"


export function getLocalVideos(currentPage: number, currentPageSize: number): RecommendVideo {
  const videos: VideoInfo[] = []

  for (let i = 0; i < 16; i++) {
    videos.push({
      id: getUid(),
      url: `/src/assets/video/qq${i}.mp4`
    })
  }
  // [start,end)
  const start = (currentPage - 1) * currentPageSize
  const end = start + currentPageSize

  const part = videos.slice(start, end)
  // console.log('part', part, start, end);

  return {
    total: 16,
    videos: part
  }
}