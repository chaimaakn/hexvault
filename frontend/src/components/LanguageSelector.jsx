import React, { useState } from 'react';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import { FaGlobe } from 'react-icons/fa';


function LanguageSelector() {
    const [language, setLanguage] = useState('English'); 

    const handleSelect = (selectedLanguage) => {
      setLanguage(selectedLanguage);
    };
  
    return (
      <DropdownButton
        variant="outline-light"
        id="dropdown-basic-button"
        title={
            <>
              <FaGlobe style={{ marginRight: '8px' }} /> {language}
            </>
          }
        onSelect={handleSelect} 
        
      >
        <Dropdown.Item eventKey="English">English</Dropdown.Item>
        <Dropdown.Item eventKey="French">French</Dropdown.Item>
      </DropdownButton>
    )
}

export default LanguageSelector