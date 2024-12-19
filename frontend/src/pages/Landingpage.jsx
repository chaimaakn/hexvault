import React from 'react';
import {motion} from 'framer-motion';
import Navbar from '../components/Navbar/Navbar';
import '../styles/Landingpage.css';
import Section1 from './Section1';
import Section2 from './Section2';
import Section3 from './Section3';
import Section4 from './Section4';
import Section5 from './Section5';
import Section6 from './Section6';
import Footer from '../components/Footer';


function LandingPage() {
  return (
    <div ClassName="landing-page">
      <div className='nb'>
        <Navbar />
      </div>
      
     <div id='home'>
      <Section1/>
     </div>
     <div >
      <Section2/>
     </div>
     <div id='about'>
      <Section3/>
     </div>
     <div id='services'>
      <Section4/>
     </div>
     <div id='faq'>
      <Section5/>
     </div>
     <div id='contact'>
      <Section6/>
     </div>
     <div>
      <Footer/>
     </div>
      
      
      
    </div>
     
    
  );
}

export default LandingPage;