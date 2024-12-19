import React from 'react'
import '../styles/Sections.css'
import Icon6 from '../assets/icon6.svg';
import Icon7 from '../assets/icon7.svg';
import Icon8 from '../assets/icon8.svg';
import Icon9 from '../assets/icon9.svg';

function Section4() {
  return (
    <div className='section-4'>
       <h1 id='sec4-title'>our services</h1>
       <div className='services'>
         <div className='service'>
            <img src={Icon8}  className='img-serv' />
          <h1>Password Testing </h1>
          <p>Check the strength of your passwords and receive personalized tips to make them more secure.</p>
       </div>
       <div className='service'>
          <img src={Icon6}  className='img-center' />
          <h1>Attack Simulations</h1>
          <p> Put your passwords to the test against common attack methods like brute force or dictionary attacks to assess their resilience.</p>
       </div>
       <div className='service'>
       <img  className='img-serv' src={Icon9}  />
        <h1>Encryption and Decryption</h1>
        <p>Secure your messages effortlessly with powerful encryption and decryption tools.</p>
       </div>
       <div className='service'>
       <img src={Icon7} className='img-center'  />
      
        <h1>Time Estimation</h1>
        <p>Get an accurate estimate of how long different attacks would take to crack your passwords.</p>
       
        
       </div>
       </div>
      
    </div>
  )
}

export default Section4