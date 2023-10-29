import instance from "./instance";


export async function getRecommendVideo({ pageCount, pageSize }: { pageCount: number; pageSize: number }) {
  const res = await instance.get('/mock/recommendVideo', {
    data: {
      pageCount, pageSize
    }
  })
  console.log('getRecommendVideo:', res);

  return res
}