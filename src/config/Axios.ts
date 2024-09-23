import { Axios } from 'axios';

const { VITE_API_URL } = import.meta.env

const axios = new Axios({
    baseURL: VITE_API_URL,
    headers: {
        'Content-Type': 'application/json'
    }
})

export default axios