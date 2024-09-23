import { TUserSession } from '@/types/User'

export const getUser = ():string => {
    const tokenString = sessionStorage.getItem('userData');
    const userToken = JSON.parse(String(tokenString)) as TUserSession;
    return userToken.user
}

