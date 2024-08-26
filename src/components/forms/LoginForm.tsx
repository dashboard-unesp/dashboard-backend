import { Button, FormControl, FormErrorMessage, FormLabel, Input } from "@chakra-ui/react";
import { useState } from "react";

function LoginForm() {

    const [email, setEmail] = useState('');
    const [emailError, setEmailError] = useState('');
    const [password, setPassword] = useState('');
    // const [passwordError, setPasswordError] = useState('');

    const handleEmailChange = (event:React.ChangeEvent<HTMLInputElement>) => {
        const newEmail = event.target.value;
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        if (!emailRegex.test(newEmail)) {
            setEmailError('Email inválido');
        } else {
            setEmailError('');
        }
        setEmail(newEmail);
    };

    const handlePasswordChange = (event:React.ChangeEvent<HTMLInputElement>) => {
        setPassword(event.target.value);
    };

    const handleSubmit = (event:React.ChangeEvent<HTMLInputElement>) => {
        event.preventDefault();
        // if (emailError || passwordError) {
        //     // Handle validation errors
        //     console.error('Validation errors:', emailError, passwordError);
        // } else {
        //     console.log('Login successful with email:', email, 'and password:', password);
        // }
    };

    return(
        <>
            <div className="flex flex-col gap-8 p-10">
                <FormControl isInvalid={!!emailError}>
                    <FormLabel>Email</FormLabel>
                    <Input type="email" value={email} onChange={handleEmailChange} />
                    <FormErrorMessage>{emailError}</FormErrorMessage>
                </FormControl>
                <FormControl>
                    <FormLabel>Password</FormLabel>
                    <Input type="password" value={password} onChange={handlePasswordChange} />
                    <FormErrorMessage>{}</FormErrorMessage>
                </FormControl>
                <span  className="flex flex-col items-center">
                    <Button type="submit" className="mt-4 w-full">Login</Button>
                    <a className="text-blue-800 font-semibold text-sm hover:underline pt-4"
                        href="http://">Esqueci a senha</a>
                </span>
            </div>
        </>
    );
}

export default LoginForm;