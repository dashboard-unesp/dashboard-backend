import { Button, FormControl, FormErrorMessage, FormLabel, Input } from "@chakra-ui/react";
import { useState } from "react";
import axios from "@/config/Axios";
import { useNavigate } from 'react-router-dom';
import useToken from "@/hooks/useToken";

type LoginForm = {
    email: string;
    password: string;
}

function LoginForm() {
    const {token, setToken} = useToken();
    const [emailError, setEmailError] = useState('');
    const [passwordError, setPasswordError] = useState('');
    const [loginForm, setLoginForm] = useState({email: '', password: ''})

    const navigate = useNavigate()

    const handleEmailChange = (event:React.ChangeEvent<HTMLInputElement>) => {
        const newEmail = event.target.value;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        if (!emailRegex.test(newEmail)) {
            setEmailError('Email inválido');
        } else {
            setEmailError('');
        }
        setLoginForm({email: newEmail, password: loginForm.password});
    };

    const handlePasswordChange = (event:React.ChangeEvent<HTMLInputElement>) => {
        setLoginForm({email: loginForm.email, password: event.target.value});
    };

    const handleSubmit = async () => {
        await axios.post('/users/login/', JSON.stringify(loginForm))
            .then((res)=>{
                if(res.status === 200){
                    const {token} = JSON.parse(res.data)
                    try{
                        setToken({user: loginForm.email, token});
                        navigate('/dashboard')
                    }catch(err) {
                        console.error(err)
                        setPasswordError('invalid email or password')
                    }
                }
            })
       
    };

    return(
        <>
            <div className="flex flex-col gap-8 p-10">
                <FormControl isInvalid={!!emailError}>
                    <FormLabel>Email</FormLabel>
                    <Input type="email" value={loginForm.email} onChange={handleEmailChange} />
                    <FormErrorMessage>{emailError}</FormErrorMessage>
                </FormControl>
                <FormControl>
                    <FormLabel>Password</FormLabel>
                    <Input type="password" value={loginForm.password} onChange={handlePasswordChange} />
                    <FormErrorMessage>{}</FormErrorMessage>
                </FormControl>
                <span  className="flex flex-col items-center">
                    <Button type="submit" className="mt-4 w-full" onClick={() => handleSubmit()}>Login</Button>
                    <a className="text-blue-800 font-semibold text-sm hover:underline pt-4"
                        href="http://">Esqueci a senha</a>
                </span>
            </div>
        </>
    );
}

export default LoginForm;