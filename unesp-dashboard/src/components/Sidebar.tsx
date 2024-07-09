import { Button } from '@chakra-ui/react';
import { useEffect, useState } from 'react';

function Sidebar(){
    const [isCollapsed, setIsCollapsed] = useState(false);

    useEffect(() => {
        const sidebar = document.getElementById('sidebarContent');

        if(!isCollapsed){
            sidebar?.classList.add('w-[300px]');
        }else{
            sidebar?.classList.remove('w-[300px]');
        }

    }, [isCollapsed])

    return(
        <nav className='max-w-fit'>
            <div id='sidebarContent' className='flex flex-col justify-between h-full'>

                <ul className='flex flex-col p-4 gap-4'>
                    <Button onClick={() => setIsCollapsed(!isCollapsed)}/>
                    <Button />
                    <Button />
                    <Button />
                    <Button />
                    <Button />
                    <Button />
                </ul>

                <ul className='flex flex-col p-4 gap-4'>
                    <Button />
                    <Button />
                    <Button />
                </ul>
            </div>

        </nav>
    );
}

export default Sidebar;