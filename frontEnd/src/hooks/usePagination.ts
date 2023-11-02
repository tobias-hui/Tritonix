import { ref, reactive, Ref, onMounted, watch } from "vue";
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
  onMounted(async () => {
    handleService()
  })
  watch(() => pagination.current, (curr, prev) => {
    handleService()
  })

  async function handleService() {
    loading.value = true
    try {
      const res = await serviceFn(pagination.current, pagination.pageSize)
      Object.assign(data, res)
    } catch (err) {
      console.log('usePagination', err);
    } finally {
      loading.value = false
    }
  }

  function changeCurrent(current: number) {

  }
  return {
    data, loading,
    pagination
  }
}