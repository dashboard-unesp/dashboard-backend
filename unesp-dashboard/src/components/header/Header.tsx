import { Avatar } from '@chakra-ui/react';
import './Header.css';


function Header() {

    return(
        <header className='header-container'>
            <div className='header-card'>
                <Avatar size='md' name='G' bg={'#707FDD'} />
                <p>Unesp Dashboard</p>
            </div>

            <div className='header-account'>
                <Avatar size='md' name='Anonimo' bg={'#C8CBD9'} />
                <p>Conta Anonima</p>
            </div>
        </header>
    );
}

export default Header;