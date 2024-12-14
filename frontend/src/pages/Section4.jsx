import React from 'react'
import '../styles/Sections.css'

function Section4() {
  return (
    <div className='section-4'>
       <h1 id='sec4-title'>our services</h1>
       <div className='services'>
         <div className='service'>
          <h1>Password Testing</h1>
          <p>Check the strength of your passwords and receive personalized tips to make them more secure.</p>
       </div>
       <div className='service'>
          <h1>Attack Simulations</h1>
          <p> Put your passwords to the test against common attack methods like brute force or dictionary attacks to assess their resilience.</p>
       </div>
       <div className='service'>
        <h1>Encryption and Decryption</h1>
        <p>Secure your messages effortlessly with powerful encryption and decryption tools.</p>
       </div>
       <div className='service'>
        <h1>Time Estimation</h1>
        <p>Get an accurate estimate of how long different attacks would take to crack your passwords.</p>
       </div>
       </div>
      
    </div>
  )
}

export default Section4