import instance from "../instance";

import { Categories, VideoInformation } from "@/types/video";

export async function getCategories() {
  try {
    const res = await instance.get('/api/v1/categories')
    const { data, status }: { data: Categories[]; status: number } = res
    if (status !== 200) {
      throw new Error('getCategories Error')
    } else {
      console.log('getCategories', data);
    }
    return data
  } catch (e) {
    console.error(e);
  }
}


export async function getVideos({
  category_id, page, size
}: {
  category_id: string
  page: number
  size: number
}) {
  try {
    const res = await instance.get(`/api/v1/categories/${category_id}/videos`, {
      params: {
        skip: page,
        limit: size
      }
    })
    const { data }: { data: VideoInformation[] } = res
    console.log('getVideos', data);
    return data
  } catch (e) {
    console.error(e)
  }

}

export async function getRecommendVideos({
  page, size
}: {
  page: number
  size: number
}) {
  try {
    const res = await instance.get(`/api/v1/videos/recommend`, {
      params: {
        page,
        size
      }
    })
    const { data }: { data: VideoInformation[] } = res
    console.log('getRecommendVideos', data);
    return data
  } catch (e) {
    console.error(e)
  }

}


export async function searchVideo(keyword: string) {
  try {
    const res = await instance.get(`/api/v1/videos/search`, {
      params: {
        keyword
      }
    })
    const { data }: { data: VideoInformation[] } = res
    console.log('getVideos', data);
    return data
  } catch (e) {
    console.error(e)
  }
}

export async function getVideoById(videoId: string) {
  try {
    const res = await instance.get(`/api/v1/videos/${videoId}`, {
      params: {
        video_id: videoId
      }
    })
    const { data }: { data: VideoInformation[] } = res
    console.log('getVideos', data);
    return data
  } catch (e) {
    console.error(e)
  }
}

/* export async function insertVideo(videoId: string) {
  try {
    const res = await instance.get(`/api/v1/videos/${videoId}`, {
      params: {
        video_id: videoId
      }
    })
    const { data }: { data: VideoInformation[] } = res
    console.log('getVideos', data);
    return data
  } catch (e) {
    console.error(e)
  }
} */
