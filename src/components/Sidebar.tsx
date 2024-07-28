import { Button } from '@chakra-ui/react';
import { useEffect, useState } from 'react';
import { MdBuild, MdAccountCircle, MdHelp   } from "react-icons/md";

type SidebuttonProps = {
    title: string;
    icon: JSX.Element;
    label: string;
}

const subMenu: SidebuttonProps[] = [
    {
        title:'account',
        icon: <MdAccountCircle size={18}/>,
        label: 'Conta'
    },
    {
        title:'config',
        icon: <MdBuild size={18}/>,
        label: 'Configurações'
    },
    {
        title:'help',
        icon: <MdHelp size={18}/>,
        label: 'Ajuda'
    },

];

function Sidebar(){
    const [isCollapsed, setIsCollapsed] = useState(false);

    useEffect(() => {
        const sidebarContent = document.getElementById('sidebarContent');

        if(!isCollapsed){
            sidebarContent?.classList.add('w-[300px]');
        }else{
            sidebarContent?.classList.remove('w-[300px]');
        }

    }, [isCollapsed])

    return(
        <nav id='sidebarContainer' className='max-w-fit'>
            <div id='sidebarContent' className='flex flex-col justify-between h-full ease-in-out duration-300 stretch-button'>

                <ul className='flex flex-col p-4 gap-4'>
                    <Button onClick={() => setIsCollapsed(!isCollapsed)}/>
                    <Button></Button>
                    <Button></Button>
                    <Button></Button>
                    <Button></Button>
                    <Button></Button>
                    <Button></Button>
                </ul>

                <ul className='flex flex-col p-4 gap-4'>
                    {
                        subMenu.map((button) => (
                            <Button>
                                {
                                    isCollapsed 
                                        ? button.icon 
                                        : <>{button.icon}<span className='pl-1'>{button.label}</span></>
                                }
                            </Button>
                        ))
                    }
                </ul>
            </div>

        </nav>
    );
}

export default Sidebar;