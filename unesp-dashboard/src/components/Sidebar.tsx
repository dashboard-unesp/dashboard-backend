import { Accordion, AccordionButton, AccordionIcon, AccordionItem, AccordionPanel, Box, Button } from '@chakra-ui/react';

<Accordion>
  <AccordionItem>
    <h2>
      <AccordionButton _expanded={{ bg: 'tomato', color: 'white' }}>
        <Box as='span' flex='1' textAlign='left'>
          Click me to see a different style
        </Box>
        <AccordionIcon />
      </AccordionButton>
    </h2>
    <AccordionPanel>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
      veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
      commodo consequat.
    </AccordionPanel>
  </AccordionItem>
</Accordion>

function Sidebar(){
    
    return(
        <nav className='flex flex-col p-4'>
           <Button />
        </nav>
    );
}

export default Sidebar;