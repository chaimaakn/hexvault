import React from 'react'
import './Navbar.css'
import Logo from '../../assets/logo.png';
import Button from 'react-bootstrap/Button';
import { Dropdown, DropdownButton } from 'react-bootstrap';
import Languageselect from '../LanguageSelector';
import { TbSquareArrowRightFilled } from 'react-icons/tb';
import { FaAngleDown } from 'react-icons/fa';
import { Link } from 'react-router';
import { useKeycloak } from '@react-keycloak/web';
import { useCallback } from 'react';

const Navbar = () => {
  const { keycloak, initialized } = useKeycloak();

  const login = useCallback(() => {
    keycloak.login({
      redirectUri: 'http://localhost:3000/#/F',
      responseMode: 'query',
      prompt: 'login'
    });
  }, [keycloak]);

  const logout = useCallback(() => {
    keycloak.logout({
      redirectUri: window.location.origin
    });
  }, [keycloak]);

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
      <Link className="Logo" to='/#home' onClick={() => scrollToSection('home')}><img src={Logo} alt="" /></Link>

      <nav className="custom-navbar">
        <Link className="links" to='/#home' onClick={() => scrollToSection('home')}>Home</Link>

        <div className="services-dropdown">
          <Link to='/#services' onClick={() => scrollToSection('services')} className="services-link">
            Services <FaAngleDown className="dropdown-arrow" />
          </Link>
          <div className="dropdown-menu">
            <Link to="/Page1">Encryption/Decryption</Link>
            <a href="/">Attack simulation</a>
            <a href="/">Password testing</a>
            <a href="/">Time prediction</a>
          </div>
        </div>
        <Link className="links" to='/#about' onClick={() => scrollToSection('about')} >About us</Link>
        <Link className="links" to='/#contact' onClick={() => scrollToSection('contact')} >Contact us</Link>
        <Link className="links" to='/#faq' onClick={() => scrollToSection('faq')} >FAQ</Link>
      </nav>

      <div className='buttons'>
        <Languageselect />
        {keycloak.authenticated ? ( //here conditional rendering of component,if hes logged in we show logout button else login button
          <Button
            className="enlarge"
            variant="light"
            onClick={logout}
          >
            Logout
          </Button>
        ) : (
          <Button
            className="enlarge"
            variant="light"
            onClick={login}
          >
            Start now <TbSquareArrowRightFilled style={{ marginLeft: '8px', color: '#0CB074' }} />
          </Button>
        )}

      </div>

    </div>
  )
}

export default Navbar