import './App.css'
import { Grid, GridItem } from '@chakra-ui/react'
import Header from './components/header/Header';
import Sidebar from './components/sidebar/Sidebar';
import Home from './pages/home/Home';


function App() {
  
  return (
    
    <Grid templateAreas={`"header header" "nav main"`}
        gridTemplateRows={'10% 1fr'}
        gridTemplateColumns={'20% 1fr'} h='100vh' fontWeight='bold'>

      <GridItem area={'header'} >
        <Header />
      </GridItem>

      <GridItem area={'nav'} bgColor={'#F1F2F7'} borderTop={'1px'} borderColor={'#C8CBD9'} >
        <Sidebar />
      </GridItem>

      <GridItem area={'main'} borderTop={'1px'} borderColor={'#C8CBD9'} >
        <Home /> 
      </GridItem>
        
    </Grid>
    
  )
}

export default App
