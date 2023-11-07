import instance from "../instance";
import { UserInfo } from "@/types/user";
import qs from "qs"

export type RegisterProps = {
  email: string
  username: string
  avatar: string
  password: string
}
export async function register({ email, username, avatar, password }: RegisterProps) {
  try {
    const res = await instance.post(`/api/v1/users/register`, {
      email,
      username,
      avatar,
      password
    })
    const { data }: { data: UserInfo } = res
    console.log('register', data);
    return data
  } catch (e) {
    // console.error(e)
    alert("此用户已被注册！")
  }
}

type LoginProps = {
  email: string
  password: string
}
type TokenReturnType =
  { access_token: string; token_type: string }
export async function login({ email, password }: LoginProps) {
  const data = qs.stringify({
    username: email,
    password,
  })
  const config = {
    method: 'post',
    url: '/api/v1/users/login',
    data: data
  };
  try {
    // instance(config)
    const res = await instance(config)
    const { data: returnData }: { data: TokenReturnType } = res
    console.log('login', returnData);

    return returnData
  } catch (e) {
    console.error(e)
    alert('密码错误')
  }
}

export async function getUserInfo(){
  try {
    const res = await instance.get(`/api/v1/users/me`, )
    const { data }: { data: UserInfo } = res
    console.log('getUserInfo', data);
    return data
  } catch (e) {
    console.error(e)
  }
}