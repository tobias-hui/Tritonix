import instance from "./instance";


export async function getRecommendVideo({ currentPage, currentPageSize }: { currentPage: number; currentPageSize: number }) {
  const res = await instance.get('/mock/recommendVideo', {
    params: {
      currentPage, currentPageSize
    }
  })
  console.log('getRecommendVideo', res);

  return res
}