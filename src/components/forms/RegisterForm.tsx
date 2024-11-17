import axios from "@/config/Axios";
import useToken from "@/hooks/useToken";
import { Button, FormControl, FormLabel, Input, Select } from "@chakra-ui/react";
import { useState } from "react";
import { useNavigate } from 'react-router-dom';

const { VITE_API_URL } = import.meta.env

const RegisterForm = () => {
    const navigate = useNavigate()
    const {token, setToken} = useToken()
    const [name, setName] = useState('');
    const [gender, setGender] = useState('other');
    const [birthDate, setBirthDate] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    // TODO: perform registration flow
    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault(); 
        try {

            const newUser = {
                name,
                gender,
                birthDate,
                email,
                password
            }

            await fetch(`${VITE_API_URL}/users/register/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                  },
                body: JSON.stringify(newUser)
            }).then(response => response.json());

            await axios.post('/users/login/', JSON.stringify({email, password}))
                .then((res)=>{
                    if(res.status === 200){
                        const {token} = JSON.parse(res.data)
                        try{
                            setToken({user: email, token});
                            navigate('/dashboard')
                        }catch(err) {
                            console.error(err)
                        }
                    }
            })
          
            console.log('Form submitted:', { name, gender, birthDate, email, password });
        } catch (error) {
            console.error(error)
        }
    };
  
    return (
        <>
            <form onSubmit={handleSubmit} className="flex flex-col gap-4 p-10">
                <FormControl>
                    <FormLabel>Name</FormLabel>
                    <Input type="text" value={name} onChange={(e) => setName(e.target.value)}/>
                </FormControl>
                <FormControl>
                    <FormLabel>Gender</FormLabel>
                    <Select value={gender} onChange={(e) => setGender(e.target.value)}>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </Select>
                </FormControl>
                <FormControl>
                    <FormLabel>Birth Date</FormLabel>
                    <Input type="date" value={birthDate} onChange={(e) => setBirthDate(e.target.value)} />
                </FormControl>
                <FormControl>
                    <FormLabel>Email</FormLabel>
                    <Input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
                </FormControl>
                <FormControl>
                    <FormLabel>Password</FormLabel>
                    <Input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                </FormControl>
                <span  className="flex flex-col items-center">
                    <Button type="submit" className="mt-4 w-full">Cadastrar</Button>
                </span>
            </form>
      </>
    );
  };
  
  export default RegisterForm;