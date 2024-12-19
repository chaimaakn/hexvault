import React, { useState } from 'react';
import { BsFillPlusSquareFill, BsFillDashSquareFill } from "react-icons/bs"; 
import '../styles/Sections.css';

function Section5() {
  const [activeIndex, setActiveIndex] = useState(null);

  const questions = [
    { question: "What is HexVault?", answer: "HexVault is a web platform dedicated to password security." },
    { question: "How do I test my passwords?", answer: "You can use HexVault to simulate common attack methods like brute force and dictionary attacks to test the strength of your passwords." },
    { question: "Is my data secure?", answer: "Yes, all your data is processed securely and is never shared. We use state-of-the-art encryption to protect your information." }
  ];

  const handleToggle = (index) => {
    if (index === activeIndex) {
      setActiveIndex(null); // Close the active item if clicked again
    } else {
      setActiveIndex(index); // Open the clicked item
    }
  };

  return (
    <div className="section-5">
      <h1 id='sec5-title'>Frequently Asked Questions</h1>
      <div className="accordion">
        {questions.map((item, index) => (
          <div key={index} className="accordion-item">
            <div className="accordion-header" onClick={() => handleToggle(index)}>
              <h3>{item.question}</h3>
              <span className="accordion-icon">{activeIndex === index ? <BsFillDashSquareFill /> : <BsFillPlusSquareFill />}</span>
            </div>
            {activeIndex === index && (
              <div className="accordion-content">
                <p>{item.answer}</p>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Section5;
