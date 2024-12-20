import React from 'react'
import './Navbar.css'
import Logo from '../../assets/logo.png';
import Button from 'react-bootstrap/Button';
import { Dropdown, DropdownButton } from 'react-bootstrap';
import Languageselect from '../LanguageSelector';
import { TbSquareArrowRightFilled } from 'react-icons/tb'; 
import { FaAngleDown } from 'react-icons/fa';
import { Link } from 'react-scroll';

const Navbar = () => {
  return (
    <div className="header">
      <Link  className="Logo" to='home' smooth={true} duration={500}><img src={Logo} alt="" /></Link>

      <nav className="custom-navbar">
        <Link className="links" to='home'>Home</Link>

        <div className="services-dropdown">
            <Link to='services' smooth={true} duration={500} className="services-link">
                 Services <FaAngleDown className="dropdown-arrow" />
            </Link>
            <div className="dropdown-menu">
            <a href="/Page1">Encryption/Decryption</a>
            <a href="/">Attack simulation</a>
            <a href="/">Password testing</a>
            <a href="/">Time prediction</a>
            </div>
        </div>
        <Link className="links" to='about' smooth={true} duration={500}>About us</Link>
        <Link className="links" to='contact' smooth={true} duration={500}>Contact us</Link>
        <Link className="links" to='faq' smooth={true} duration={500}>FAQ</Link>
      </nav>

      <div className='buttons'>
      <Languageselect/>
      
        <Button  className="enlarge" variant="light" >Start now <TbSquareArrowRightFilled style={{ marginLeft: '8px',color:'#0CB074' }} /></Button>
   
      
      </div>
      
    </div>
  )
}

export default Navbar