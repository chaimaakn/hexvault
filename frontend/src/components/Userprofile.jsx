import React, { useState } from 'react';
import { FaUserCircle } from 'react-icons/fa'; // User icon
import { Offcanvas } from 'react-bootstrap'; // Import Offcanvas from React Bootstrap
import { useKeycloak } from '@react-keycloak/web';
import '../styles/Userprofile.css';

const Userprofile = () => {
  const [show, setShow] = useState(false);
  const { keycloak } = useKeycloak();
  const userInfo = keycloak.tokenParsed;

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <div className="user-menu">
      {/* User Icon */}
      <FaUserCircle 
        size={30} 
        onClick={handleShow} 
        style={{ cursor: 'pointer', marginLeft: '15px', color: '#0CB074' }} 
      />

      {/* Offcanvas */}
      <Offcanvas show={show} onHide={handleClose} placement="end" className="offcanvas-main" scroll={true}>
        <Offcanvas.Header closeButton>
          <Offcanvas.Title>My profile</Offcanvas.Title>
        </Offcanvas.Header>
        <Offcanvas.Body>
            <div className="container-menu-profile">
          <div className="user-profile">
              <h4>User Information</h4>
              <p><strong>Email:</strong> {userInfo.email}</p>
              <p><strong>First Name:</strong> {userInfo.given_name}</p>
              <p><strong>Last Name:</strong> {userInfo.family_name}</p>
              <p><strong>Username:</strong> {userInfo.preferred_username}</p>
          </div>
          <div className="history">
            <h4>History</h4>
            <div className="history-titles">
                <div class="hist1">
               
                <div class="main-hist-content">
                    <div className="icon-line"> 
                        <div class="line"></div>
                        <div class="service-icon">
                    logo 
                    </div>
                    </div>
                    
                <div class="history-content">
                   <p>password </p>
                   <p>result </p>  
                   <p>service-name</p>
                   <p>time</p>
                    </div>
                    </div>
                     
                    </div>
                
            </div>
          
          </div>
          </div>
        </Offcanvas.Body>
      </Offcanvas>
    </div>
  );
};

export default Userprofile;
