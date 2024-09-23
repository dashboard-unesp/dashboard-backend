// import { Grid, GridItem } from '@chakra-ui/react'
// import Header from './components/Header';
// import Sidebar from './components/Sidebar';
// import Home from './pages/Home';
import './globals.css';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Layout from './Layout';
import Home from './pages/Home';
import Login from './pages/Login';

function App() {

  return (
    <Router>
      <Routes>
        <Route path='/' element={<Login />} />
        <Route path='/dashboard' element={<Layout />}>
          <Route index element={<Home />} />
          {/* put new routes here */}
        </Route>
      </Routes>
    </Router>
  );
  
}

export default App
