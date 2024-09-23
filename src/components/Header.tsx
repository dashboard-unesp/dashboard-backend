import { getUser } from '@/utils/userData';
import { Avatar } from '@chakra-ui/react';
import { useNavigate } from 'react-router-dom';

function Header() {

    const user = getUser();
    const navigate = useNavigate();

    const userLogout = () => {
        sessionStorage.removeItem('userData');
        navigate('/');
    }

    return(
        <header className='flex flex-row justify-between items-center align-center h-full'>
            <div className='flex items-center gap-[8px] font-bold px-[2%] py-[4%] w-[20%]'>
                <Avatar size='md' name='U' bg={'#707FDD'} />
                <p>Unesp Dashboard</p>
            </div>

            <div className='flex items-center gap-[8px] font-bold px-[2%] py-[4%] w-[25%] cursor-pointer'>
                <Avatar size='md' name={user} bg={'#C8CBD9'} />
                <p className='text-xl'>{user}</p>
                <Avatar size='sm' name='X' bg={'transparent'} color={'#FF0000'} onClick={() => userLogout()}/>
            </div>
        </header>
    );
}

export default Header;