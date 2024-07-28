import { Avatar } from '@chakra-ui/react';

function Header() {

    return(
        <header className='flex flex-row justify-between items-center align-center h-full'>
            <div className='flex items-center gap-[8px] font-bold px-[2%] py-[4%] w-[20%]'>
                <Avatar size='md' name='G' bg={'#707FDD'} />
                <p>Unesp Dashboard</p>
            </div>

            <div className='flex items-center gap-[8px] font-bold px-[2%] py-[4%] w-[25%]'>
                <Avatar size='md' name='Anonimo' bg={'#C8CBD9'} />
                <p className='text-xl'>Conta Anonima</p>
            </div>
        </header>
    );
}

export default Header;