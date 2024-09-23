import React, { useState } from 'react'
import { TUserSession } from '@/types/User'

const useToken = () => {

    const getToken = () => {
        const tokenString = sessionStorage.getItem('userData')
        try{
          const userToken = JSON.parse(String(tokenString)) as TUserSession;
          return userToken.token
        }catch(err){
          return null;
        }
    } 

    const [token, setToken] = useState(getToken())
    
    const saveToken = (userToken:TUserSession) => {
        sessionStorage.setItem('userData', JSON.stringify(userToken))
        setToken(userToken.token)
    }

    return {
      setToken: saveToken,
      token
    }

}

export default useToken