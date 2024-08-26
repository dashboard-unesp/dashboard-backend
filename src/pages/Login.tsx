import { Button, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, useDisclosure } from "@chakra-ui/react";
import LoginForm from "@/components/forms/LoginForm";
import { useState } from "react";
import RegisterForm from "@/components/forms/RegisterForm";

function Login(){
    
    const { isOpen, onOpen, onClose } = useDisclosure()
    const [isLogin, setIsLogin] = useState(true)

    return (
        <>
            <section className='w-screen h-screen flex items-center justify-center gap-8'>
                <main className="max-w-[40%] rounded-xl">
                    <div className='flex flex-col text-center p-4 gap-12'>
                        <h1 className='font-extrabold text-4xl'>
                            Monitoramento Meteorológico Acessivel
                        </h1>
                        <p className='text-xl w-50'>
                            Desde o aumento do nível de chuva até mudanças nos padrões climáticos, nosso painel 
                            oferece uma visão abrangente, clara e direta das alterações climáticas de São José dos Campos. 
                            Com visualizações interativas e dados acessíveis, compreenda profundamente o panorama 
                            climático e ambiental da famosa cidade do bolinho caipira.
                        </p>
                        <span className="flex space-between w-full gap-2 items-center justify-center">
                            <Button className="w-fit hover:text-black" fontSize="large" fontWeight={'500'} padding={'25px'} 
                                backgroundColor={'#8884d8'} textColor={'#FFF'} onClick={() => ( setIsLogin(true), onOpen())}>
                                <span className="font-serif">ENTRAR</span>
                            </Button>
                            <a className="text-blue-800 font-semibold text-sm hover:underline"
                            href={undefined}onClick={() => (setIsLogin(false), onOpen())}>
                                Cadastre-se
                            </a>
                        </span>
                    </div>
                </main>
                <div>
                    <img 
                        src="https://f005.backblazeb2.com/file/debbuggers/simplistic-woman-using-augmented-reality-and-mixed-reality-technology.png" 
                        alt="woman in tech" 
                        width={500} loading="lazy"
                        />
                </div>
            </section>

            <Modal onClose={onClose} isOpen={isOpen} isCentered>
                    <ModalOverlay />
                    <ModalContent>
                    <ModalBody>
                        {
                            isLogin 
                                ? <LoginForm /> 
                                : <RegisterForm />
                        }
                    </ModalBody>
                    </ModalContent>
                </Modal>

        </>
    );
}

export default Login;