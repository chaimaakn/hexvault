import React from 'react'
import '../styles/Sections.css'
import Globe from '../components/three.js'

function Section3() {
  return (
    <div className='section-3'>
      <div className='globe'>
      <Globe/>
      </div>

       <div className='intro-text'>
        <h1>what is hexvault?</h1>
        <div>
          <p>
          HexVault is a web platform dedicated to password security.
           It tests password strength through realistic attack simulations and
            provides advanced encryption and decryption tools. Our goal is 
            to raise awareness about the importance of choosing secure passwords
             while offering a comprehensive solution to protect data and stay ahead of cyber threats.
          </p>
        </div>
       </div>
       
    </div>
  )
}

export default Section3