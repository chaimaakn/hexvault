import React from 'react'
import './Navbar.css'
import Logo from '../../assets/logo.png';
import Button from 'react-bootstrap/Button';
import Languageselect from '../LanguageSelector';
import { TbSquareArrowRightFilled } from 'react-icons/tb'; 

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
      
      <Button  className="enlarge" variant="light">Start now <TbSquareArrowRightFilled style={{ marginLeft: '8px',color:'#0CB074' }} /></Button>
      </div>
      
    </div>
  )
}

export default Navbar