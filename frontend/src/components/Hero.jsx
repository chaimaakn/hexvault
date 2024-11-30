import React from 'react'
import '../styles/Sections.css';

function Hero() {
  return (
    <div>
        <div className='slogan'>
            <h1>Crack, Test, Encrypt</h1>
            <h1>All in One Vault</h1>

        </div>
        <div className='serv'>
            <label >encrypt</label>
            <label >decrypt</label>
            <label >attack simulation</label>
            <label >test your password</label>
            <label >time prediction</label>
        </div>
        
    </div>
  )
}

export default Hero