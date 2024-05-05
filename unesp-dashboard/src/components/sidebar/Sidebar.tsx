import { Button } from '@chakra-ui/react';
import './Sidebar.css';

function Sidebar(){
    
    return(
        <nav className='flex flex-col p-4'>
            <div className='p-8'>
                <h3>Menu</h3>
                <ul>
                    <li>
                        <Button width={'100%'} paddingY={'8%'} color={'#707FDD'} fontSize={'20px'} fontWeight={600}>
                            Dashboard
                        </Button>
                    </li>
                </ul>
            </div>
            <div className='sidebar-menu'>
                <h3>Opções</h3>
                <ul>
                    <li>
                        <Button width={'100%'} paddingY={'8%'} color={'#707FDD'} fontSize={'20px'} fontWeight={600}>
                           Configuração
                        </Button>
                    </li>
                    <li>
                        <Button width={'100%'} paddingY={'8%'} color={'#707FDD'} fontSize={'20px'} fontWeight={600}>
                            Conta
                        </Button>
                    </li>
                    <li>
                        <Button width={'100%'} paddingY={'8%'} color={'#707FDD'} fontSize={'20px'} fontWeight={600}>
                            Ajuda
                        </Button>
                    </li>
                </ul>
            </div>
        </nav>
    );
}

export default Sidebar;