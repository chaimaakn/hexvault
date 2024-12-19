import React from 'react'
import '../styles/Sections.css';
import Icon1 from '../assets/icon1.svg';
import Icon2 from '../assets/icon2.svg';
import Icon3 from '../assets/icon3.svg';
import Icon4 from '../assets/icon4.svg';
import Icon5 from '../assets/icon5.svg';

function Hero() {
  return (
    <div>
        <div className='slogan'>
            <h1 id='main-slogan'>Crack, Test, Encrypt</h1>
            <h1 id='slogan-shiny'>All in One Vault</h1>

        </div>
        <div className='serv'>
            <label className='serv-icons'><img src={Icon5}  />encrypt   </label>
            <label className='serv-icons'><img src={Icon4}  />decrypt</label>
            <label className='serv-icons'><img src={Icon3}  />attack simulation</label>
            <label className='serv-icons'><img src={Icon2}  />test your password</label>
            <label className='serv-icons'> <img src={Icon1}  />time prediction</label>
        </div>
        
    </div>
  )
}

export default Hero