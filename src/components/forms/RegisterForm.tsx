import { Button, FormControl, FormLabel, Input, Select } from "@chakra-ui/react";
import { useState } from "react";

const RegisterForm = () => {
    const [name, setName] = useState('');
    const [gender, setGender] = useState('');
    const [birthDate, setBirthDate] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
  
    // TODO: perform registration flow
    const handleSubmit = (event: React.FormEvent) => {
      event.preventDefault(); 
      // Handle form submission here, e.g., send data to server
      console.log('Form submitted:', { name, gender, birthDate, email, password });
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