import React from 'react'
import '../styles/Sections.css'
import { IoLogoGithub } from "react-icons/io";
import { ImMail4 } from "react-icons/im";
import { FaLinkedin } from "react-icons/fa";

function Section6() {
  return (
    <div className='section-6'>
       <h1 id='sec6-title'>Contact us</h1>
       <div className='icons'>
              <a className="socials-icons" href=""><IoLogoGithub/></a>
              <a className="socials-icons" href="" ><FaLinkedin/></a>
              <a className="socials-icons" href=""><ImMail4/></a>
       </div>
    </div>
  )
}

export default Section6