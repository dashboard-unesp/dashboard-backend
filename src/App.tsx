import { Grid, GridItem } from '@chakra-ui/react'
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Home from './pages/Home';
import './globals.css';

function App() {
  
  return (
    
    <Grid templateAreas={`"header" "main"`}
        gridTemplateRows={'10% 1fr'} h='100vh' fontWeight='bold'>

      <GridItem area={'header'} >
        <Header />
      </GridItem>

      <GridItem area={'main'} borderTop={'1px'} borderColor={'#C8CBD9'}>
        <section className='flex flex-row bg-[#C8CBD9]'>
          <Sidebar />
          <Home /> 
        </section>
      </GridItem>
      
    </Grid>
    
  )
}

export default App
