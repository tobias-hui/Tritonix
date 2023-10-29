import { ref, reactive, Ref, onMounted } from "vue";
type ServiceFn<T> = (currentPage: number, currentPageSize: number) => Promise<T[]>
type Options = {
  defaultPageSize?: number
  defaultPage?: number
}
type Pagination = {
  current: number
  pageSize: number
  total: number
  totalPage: number
  changeCurrent: (current: number) => void
}
export default function usePagination<T>(serviceFn: ServiceFn<T>, { defaultPage = 1, defaultPageSize = 10 }: Options) {
  const loading = ref(false)
  const data = reactive<T[]>([])
  const pagination = reactive<Pagination>({
    current: defaultPage,
    pageSize: defaultPageSize,
    total: 0,
    totalPage: 0,
    changeCurrent
  })
  onMounted(async()=>{
    try {
      const res=await serviceFn(defaultPage,defaultPageSize)
      Object.assign(data,res)
    }catch(err){
      console.log('usePagination',err);
    }
  })
  function changeCurrent(current: number) {

  }
}