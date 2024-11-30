import React from 'react'
import './Navbar.css'
import Logo from '../../assets/logo.png';
import Button from 'react-bootstrap/Button';
import Languageselect from '../LanguageSelector';

const Navbar = () => {
  return (
    <div className="header">
      <a href="/" className="Logo"><img src={Logo} alt="" /></a>

      <nav className="custom-navbar">
        <a href="/">Home</a>
        <a href="/">Services</a>
        <a href="/">About us</a>
        <a href="/">Contact us</a>
        <a href="/">FAQ</a>
      </nav>

      <div className='buttons'>
      <Languageselect/>
      
      <Button  variant="light">Start now</Button>
      </div>
      
    </div>
  )
}

export default Navbar