import React from 'react'
import './Navbar.css'
import Logo from '../../assets/logo.png';


const Navbar = () => {
  return (
    <header className="header">
      <a href="/" className="Logo"><img src={Logo} alt="" /></a>

      <nav className="navbar">
        <a href="/">Home</a>
        <a href="/">Services</a>
        <a href="/">About us</a>
        <a href="/">Contact us</a>
        <a href="/">FAQ</a>
      </nav>

      <div className='buttons'>
        <select name="" id="">
        <option value="">english</option>
        <option value="">french</option>
      </select>
      <button>Start now </button>
      </div>
      
    </header>
  )
}

export default Navbar