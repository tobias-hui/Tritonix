import instance from "../instance";
import { UserInfo } from "@/types/user";

export type RegisterProps = {
  email: string
  username: string
  avatar: string
  password: string
}
export async function register({ email, username, avatar, password }: RegisterProps) {
  try {
    const res = await instance.post(`/api/v1/users/register`, {
      data: {
        email,
        username,
        avatar,
        password
      }

    })
    const { data }: { data: UserInfo } = res
    console.log('register', data);
    return data
  } catch (e) {
    console.error(e)
  }
}

type LoginProps = {
  username: string
  password: string
}
export async function login({ username, password }: LoginProps) {
  try {
    const res = await instance.post(`/api/v1/users/login`, {
      data: {
        username,
        password
      },
    })
    const { data }: { data: string } = res
    console.log('login', data);
    return data
  } catch (e) {
    console.error(e)
  }
}