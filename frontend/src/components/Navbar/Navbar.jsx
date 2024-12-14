import React from 'react'
import './Navbar.css'
import Logo from '../../assets/logo.png';
import Button from 'react-bootstrap/Button';
import { Dropdown, DropdownButton } from 'react-bootstrap';
import Languageselect from '../LanguageSelector';
import { TbSquareArrowRightFilled } from 'react-icons/tb'; 
import { FaAngleDown } from 'react-icons/fa';

const Navbar = () => {
  return (
    <div className="header">
      <a href="/" className="Logo"><img src={Logo} alt="" /></a>

      <nav className="custom-navbar">
        <a href="/">Home</a>

        <div className="services-dropdown">
            <a href="/" className="services-link">
                 Services <FaAngleDown className="dropdown-arrow" />
            </a>
            <div className="dropdown-menu">
            <a href="/">Encryption/Decryption</a>
            <a href="/">Attack simulation</a>
            <a href="/">Password testing</a>
            <a href="/">Time prediction</a>
            </div>
        </div>
        <a href="/">About us</a>
        <a href="/">Contact us</a>
        <a href="/">FAQ</a>
      </nav>

      <div className='buttons'>
      <Languageselect/>
      
        <Button  className="enlarge" variant="light" >Start now <TbSquareArrowRightFilled style={{ marginLeft: '8px',color:'#0CB074' }} /></Button>
   
      
      </div>
      
    </div>
  )
}

export default Navbar