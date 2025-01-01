import React from 'react'
import './Navbar.css'
import Logo from '../../assets/logo.png';
import Button from 'react-bootstrap/Button';
import { Dropdown, DropdownButton } from 'react-bootstrap';
import Languageselect from '../LanguageSelector';
import { TbSquareArrowRightFilled } from 'react-icons/tb'; 
import { FaAngleDown } from 'react-icons/fa';
import { Link} from 'react-router';
import { useKeycloak } from '@react-keycloak/web';
import Userprofile from '../Userprofile';

const Navbar2 = () => {
  const { keycloak, initialized } = useKeycloak();
  
//these two lines for debugging to check if its initialized or no in the console
  console.log("Keycloak initialized:", initialized);
  console.log("Keycloak instance:", keycloak);

  const scrollToSection = (id) => {
    const element = document.getElementById(id);
    if (element) {
      window.scrollTo({
        top: element.offsetTop,
        behavior: 'smooth',
      });
    }
  };
  return (
    <div className="header">
      <Link  className="Logo" to='/#home'  onClick={() => scrollToSection('home')}><img src={Logo} alt="" /></Link>

      <nav className="custom-navbar">
        <Link className="links" to='/#home' onClick={() => scrollToSection('home')}>Home</Link>

        <Link className="links" to='/EncryptDecrypt' >Encrypt/Decrypt</Link>
        <Link className="links" to='/Attacks' >Attack simulation</Link>
        <Link className="links" to='/Passwordtesting' >Password testing</Link>
        <Link className="links" to='/Timeprediction'  >Time prediction</Link>
      </nav>

      <div className='buttons'>
      <Languageselect/>
      {keycloak.authenticated ? ( //here conditional rendering of component,if hes logged in we show logout button else login button
          <Button 
            className="enlarge" 
            variant="light" 
            onClick={() => keycloak.logout()}
          >
            Logout
          </Button>
        ) : (
          <Button 
            className="enlarge" 
            variant="light" 
            onClick={() => keycloak.login()}
          >
            Start now <TbSquareArrowRightFilled style={{ marginLeft: '8px', color: '#0CB074' }} />
          </Button>
          
        )}
         {keycloak.authenticated && <Userprofile />}
      
      </div>
      
    </div>
  )
}

export default Navbar2