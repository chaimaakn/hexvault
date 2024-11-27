import React from 'react';
import Navbar from '../components/Navbar/Navbar';
import '../styles/Landingpage.css';
import Background from '../components/Background';


function LandingPage() {
  return (
    <div ClassName="landing-page">
      <div className='nb'>
        <Navbar />
      </div>
      
      <div className='bg'>
        <Background />
      </div>
      
      
      
    </div>
     
    
  );
}

export default LandingPage;