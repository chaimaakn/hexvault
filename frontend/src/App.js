import Landingpage from './pages/Landingpage';
import Page from './pages/Page1';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';


function App() {
  return (
    
    <BrowserRouter>
    <Routes>
      <Route exact path="/" element={<Landingpage />} />
      <Route path="/page1" element={<Page />} />
    </Routes>
  </BrowserRouter>
    
  );
}

export default App;