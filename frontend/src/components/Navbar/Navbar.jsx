import React from 'react'
import './Navbar.css'
import Logo from '../../assets/logo.png';
import Button from 'react-bootstrap/Button';
import { Dropdown, DropdownButton } from 'react-bootstrap';
import Languageselect from '../LanguageSelector';
import { TbSquareArrowRightFilled } from 'react-icons/tb'; 

const Navbar = () => {
  return (
    <div className="header">
      <a href="/" className="Logo"><img src={Logo} alt="" /></a>

      <nav className="custom-navbar">
        <a href="/">Home</a>
        <Dropdown className="services-dropdown">
          <DropdownButton 
            variant="link" 
            id="dropdown-basic-button" 
            title="Services"
            className="services-button"
          >
            <Dropdown.Item href="#/action-1">Encryption/Decryption</Dropdown.Item>
            <Dropdown.Item href="#/action-2">Attack simulation</Dropdown.Item>
            <Dropdown.Item href="#/action-3">Password testing</Dropdown.Item>
            <Dropdown.Item href="#/action-4">Time prediction</Dropdown.Item>
          </DropdownButton>
        </Dropdown>
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