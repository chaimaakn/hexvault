import React from 'react'
import { motion } from 'framer-motion';
import '../styles/Sections.css'

function Section2() {
  return (
    <div className='section-2'>
       <h1 id='sec2-title'>why choose us?</h1>
       <div className='circles'>
        <motion.div className='circle' drag dragConstraints={{ left: -200, top: -100, right: 200, bottom: 100 }} dragElastic={1}>
        <h1>10</h1>
        <p>items</p>
        </motion.div>
        <motion.div className='circle' drag dragConstraints={{ left: -200, top: -100, right: 200, bottom: 100 }} dragElastic={1}>
        <h1>10</h1>
        <p>items</p>
        </motion.div>
        <motion.div className='circle' drag dragConstraints={{ left: -200, top: -100, right: 200, bottom: 100 }} dragElastic={1}>
        <h1>10</h1>
        <p>items</p>
        </motion.div>
         
       </div>
    </div>
    
  )
}

export default Section2