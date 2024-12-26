import React, { useEffect, useRef, useState } from 'react';
import Swiper from 'swiper';
import 'swiper/css';
import Navbar2 from '../components/Navbar/Navbar2';
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import '../styles/Services.css';
import { PiSpinnerGapBold } from "react-icons/pi";
import { VscDebugRestart } from "react-icons/vsc";

function Page1() {
  const swiperRef = useRef(null);
  const prevButtonRef = useRef(null);
  const nextButtonRef = useRef(null);

  const [flippedCardId, setFlippedCardId] = useState(null);
  const [clickedCardId, setClickedCardId] = useState(null);
  const [canFlip, setCanFlip] = useState(true);
  const [showHashMethod, setShowHashMethod] = useState(false); // État pour afficher le champ de sélection
  const [selectedHashMethod, setSelectedHashMethod] = useState('md5'); // Par défaut, md5 est sélectionné
  const [loading, setLoading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [inputValue, setInputValue] = useState(""); // To manage the input value
  const [saltValue, setSaltValue] = useState("");

  const handleCardClick = (id, event) => {
    // Prevent flipping if canFlip is false (disabling flip on back)
    if (!canFlip) return;

    event.stopPropagation(); // Prevent the card flip when clicking the card itself

    if (clickedCardId === id) {
      setClickedCardId(null); // If the same card is clicked again, unblur all
    } else {
      setClickedCardId(id); // Set the clicked card
    }
    setFlippedCardId(flippedCardId === id ? null : id); // Flip the card
  };

  // Handle clicks outside the card to flip it back, unless disabled
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (
        flippedCardId &&
        !event.target.closest('.back') && // Check if the click is outside the card
        !event.target.closest('.swiper-button-prev') && // Check if the click is outside the prev button
        !event.target.closest('.swiper-button-next') && // Check if the click is outside the next button
        canFlip === false // Ensure that the flip is disabled
      ) {
        setFlippedCardId(null); // Flip the card back
        setClickedCardId(null);
      }
    };

    document.addEventListener('click', handleClickOutside);

    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  }, [flippedCardId, canFlip]); // Depend on flippedCardId and canFlip

  useEffect(() => {
    const swiper = new Swiper('.swiper', {
        effect: 'coverflow',
        loop:true,
      slidesPerView: 3,
      spaceBetween: 10,
      navigation: {
        nextEl: nextButtonRef.current,
        prevEl: prevButtonRef.current,
      },
    });

    const handlePrevClick = () => {
      swiper.slidePrev();
    };

    const handleNextClick = () => {
      swiper.slideNext();
    };

    if (prevButtonRef.current) {
      prevButtonRef.current.addEventListener('click', handlePrevClick);
    }
    if (nextButtonRef.current) {
      nextButtonRef.current.addEventListener('click', handleNextClick);
    }

    return () => {
      if (prevButtonRef.current) {
        prevButtonRef.current.removeEventListener('click', handlePrevClick);
      }
      if (nextButtonRef.current) {
        nextButtonRef.current.removeEventListener('click', handleNextClick);
      }
    };
  }, []);

  // Handle enabling flip behavior when "click to start" button in Card 1 is clicked
 /* const enableFlip = (id) => {
    setCanFlip(true); // Re-enable flipping when the button is clicked
    setFlippedCardId(id);
    setClickedCardId(null);
  };*/

  useEffect(() => {
    if (flippedCardId) {
      setCanFlip(false); // Disable flip-back when the card is flipped
    } else {
      setCanFlip(true); // Enable flip-back when the card is not flipped
    }
  }, [flippedCardId]);

  const handleIconClick = () => {
    // Reset the input and button after clicking the icon
    setInputValue(""); // Reset hashed password input
    setSaltValue(""); // Reset salt input
    setResponseMessage(""); // Clear response message
    setIsSubmitted(false); // Reset submission state
    setLoading(false); // Reset loading state
  };

  const handleHashMethodChange = (e) => {
    setSelectedHashMethod(e.target.value); // Mettre à jour la méthode sélectionnée
  };

  const [responseMessage, setResponseMessage] = useState(""); // Initialise le message de réponse

  const handleSubmitbrutforce = () => {
    setIsSubmitted(true);
    setLoading(true);
    const hashedPassword = document.getElementById(`hash-${flippedCardId}`).value;
    const salt = document.getElementById(`salt-${flippedCardId}`).value;

  
    const requestBody = {
      hashed_password: hashedPassword,
      hash_algorithm: selectedHashMethod,
    };
  
    if (salt) {
      requestBody.salt = salt; // Ajouter le champ "salt" uniquement s'il est rempli
    }
    
    fetch('http://127.0.0.1:8001/attaque/bruteForce', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    })
    
      .then((response) => response.json())
      .then((data) => {
        console.log('Request body:', data);
        if (data.success) {
          setResponseMessage(`Your password is : ${data.password_found}`); // Stocker le mot de passe trouvé
        } else {
          setResponseMessage("Password not found !");
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setResponseMessage("Une erreur est survenue lors de la requête !");
        setLoading(false); 
      });
  };
  const [responseMessage2, setResponseMessage2] = useState(""); // Initialise le message de réponse
  const handleSubmitDictionnary = () => {
    setIsSubmitted(true);
    setLoading(true);
    const hashedPassword = document.getElementById(`hash-${flippedCardId}`).value;
    const salt = document.getElementById(`salt-${flippedCardId}`).value;
  
    const requestBody = {
      hashed_password: hashedPassword,
      hash_algorithm: selectedHashMethod,
    };
  
    if (salt) {
      requestBody.salt = salt; // Ajouter le champ "salt" uniquement s'il est rempli
    }
  
    fetch('http://127.0.0.1:8001/attaque/Dictionnaire', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          setResponseMessage2(`Your password is : ${data.password_found}`); // Stocker le mot de passe trouvé
        } else {
          setResponseMessage2("Password not found !");
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setResponseMessage2("Une erreur est survenue lors de la requête !");
        setLoading(false);
      });
  };


  const [responseMessage3, setResponseMessage3] = useState(""); // Initialise le message de réponse
  const handleSubmitImprovedDictionnary = () => {
    setIsSubmitted(true);
    setLoading(true);
    const hashedPassword = document.getElementById(`hash-${flippedCardId}`).value;
    const salt = document.getElementById(`salt-${flippedCardId}`).value;
  
    const requestBody = {
      hashed_password: hashedPassword,
      hash_algorithm: selectedHashMethod,
    };
  
    if (salt) {
      requestBody.salt = salt; // Ajouter le champ "salt" uniquement s'il est rempli
    }
  
    fetch('http://127.0.0.1:8001/attaque/DictionnaireAmeliorer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          console.log(data.password_found)
          setResponseMessage3(`Your password is : ${data.password_found}`); // Stocker le mot de passe trouvé
        } else {
          setResponseMessage3("Password not found !");
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setResponseMessage3("Une erreur est survenue lors de la requête !");
        setLoading(false);
      });
  };

  const [responseMessage4, setResponseMessage4] = useState(""); // Initialise le message de réponse
  const handleSubmitHybrid = () => {
    setIsSubmitted(true);
    setLoading(true);
    const hashedPassword = document.getElementById(`hash-${flippedCardId}`).value;
    const salt = document.getElementById(`salt-${flippedCardId}`).value;
  
    const requestBody = {
      hashed_password: hashedPassword,
      hash_algorithm: selectedHashMethod,
    };
  
    if (salt) {
      requestBody.salt = salt; // Ajouter le champ "salt" uniquement s'il est rempli
    }
  
    fetch('http://127.0.0.1:8001/attaque/hybrid', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          
          setResponseMessage4(`Your password is : ${data.password_found}`); // Stocker le mot de passe trouvé
        } else {
          setResponseMessage4("Password not found !");
        }
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setResponseMessage4("Une erreur est survenue lors de la requête !");
        setLoading(false);
      });
  };
  return (
    <div id="Attacks">
      <div className="navbar-container">
        <Navbar2 />
      </div>

      <div className="swiper-container">
        <div className="swiper">
          <div className="swiper-wrapper">
            {/* Card 1 */}
            <div
              className={`swiper-slide ${
                flippedCardId === '1' ? 'flipped' : ''
              } ${clickedCardId && clickedCardId !== '1' ? 'blurry' : ''} ${
                clickedCardId === '1' ? 'selected' : ''
              }`}
              onClick={(e) => handleCardClick('1', e)}
            >
              <div className="slide-content">
                <div className="front">
                  <div className="about">
                    <h1 className="front-title">Brute force</h1>
                    <h1 id="ab">about</h1>
                    <p>
                      A brute force attack involves testing numerous
                      combinations of passwords or keys until the correct one
                      is found.
                    </p>
                  </div>
                </div>
                <div className="back">
                  <div className="input-content">
                    <h1 id="attack-title">Brute force</h1>
                    <input
                      type="text"
                      id="hash-1"
                      placeholder="enter your hashed password..."
                      value={inputValue} 
                      onChange={(e) => setInputValue(e.target.value)} 
                    />
                    <h1 id="salt-title">Salt</h1>
                    <input
                      type="text"
                      id="salt-1"
                      placeholder="enter your salt...(optional)"
                      value={saltValue} // Bind to salt input state
                      onChange={(e) => setSaltValue(e.target.value)} 
                    />
                        <select 
                          value={selectedHashMethod}
                          onChange={handleHashMethodChange}
                          className='select-attacks'
                        >
                          <option value="md5">MD5</option>
                          <option value="sha256">SHA-256</option>
                          <option value="sha1">SHA-1</option>
                        </select>
                        {!isSubmitted && !loading && (
                        <button  onClick={(e) => {e.stopPropagation(); handleSubmitbrutforce()}}>
                            Click to start</button>
                        )}  
                        {/* Message de réponse */}
                        {loading ? (
                        <div className="response-message">
                            <PiSpinnerGapBold style={ {fontSize: "20px" }} /> {/* Show loading message while request is being processed */}
                        </div>
                        ) : (
                        <div className="response-message">

                            <p>{responseMessage}</p>
                            {responseMessage && !loading && (
                            <VscDebugRestart style={{ fontSize: "20px", cursor: "pointer" }} onClick={(e) => {e.stopPropagation();handleIconClick()} }/>
                            )}
                            
                        </div>
                        )}
                  </div>
                </div>
              </div>
            </div>

            {/* Card 2 */}

            <div
              className={`swiper-slide ${flippedCardId === '2' ? 'flipped' : ''} 
                ${clickedCardId && clickedCardId !== '2' ? 'blurry' : ''} 
                ${clickedCardId === '2' ? 'selected' : ''}`}
              onClick={(e) => handleCardClick('2', e)} // Pass the event to prevent propagation
            >
              <div className="slide-content">
                <div className="front">
                <div className='about'>
                    <h1 className='front-title'>Dictionnary</h1>
                    <h1  id='ab'>about</h1>
                    <p>
                    
                   A dictionary attack is a method to crack passwords by testing a list of commonly used
                     combinations of passwords or keys until the correct one is found.
                    </p>
                  </div>
                </div>
                <div className="back"><div className="input-content"> 
                    <h1 id='attack-title'>Dictionnary</h1>
                    <input type="text"  id='hash-2' placeholder='enter your hashed password...' value={inputValue} 
                      onChange={(e) => setInputValue(e.target.value)} />
                    <h1 id='salt-title'>Salt</h1>
                    <input type="text" id='salt-2' placeholder='enter your salt...(optional)' value={saltValue} 
                      onChange={(e) => setSaltValue(e.target.value)} />
                    <select 
                          value={selectedHashMethod}
                          onChange={handleHashMethodChange}
                          className='select-attacks'
                        >
                          <option value="md5">MD5</option>
                          <option value="sha256">SHA-256</option>
                          <option value="sha1">SHA-1</option>
                        </select>
                        {!isSubmitted && !loading && (
                        <button  onClick={(e) => {e.stopPropagation(); handleSubmitDictionnary()}}>
                            Click to start</button>
                        )}  
                        {/* Message de réponse */}
                        {loading ? (
                        <div className="response-message2">
                            <PiSpinnerGapBold style={ {fontSize: "20px" }} /> {/* Show loading message while request is being processed */}
                        </div>
                        ) : (
                        <div className="response-message2">

                            <p>{responseMessage2}</p>
                            {responseMessage2 && !loading && (
                            <VscDebugRestart style={{ fontSize: "20px", cursor: "pointer" }} onClick={(e) => {e.stopPropagation();handleIconClick()} }/>
                            )}
                            
                        </div>
                        )}
                  </div></div>
              </div>
            </div>
              {/* Card 3 */}
              <div
              className={`swiper-slide ${flippedCardId === '3' ? 'flipped' : ''} 
                ${clickedCardId && clickedCardId !== '3' ? 'blurry' : ''} 
                ${clickedCardId === '3' ? 'selected' : ''}`}
              onClick={(e) => handleCardClick('3', e)} // Pass the event to prevent propagation
            >
              <div className="slide-content">
                <div className="front">
                <div className='about'>
                    <h1 className='front-title'>Improved dict</h1>
                    <h1  id='ab'>about</h1>
                    <p>
                    An improved dictionary attack enhances the basic approach by applying transformations, 
                    such as adding numbers, symbols, or capitalizing letters, to common passwords, making 
                    it more effective against slightly stronger passwords.
                    </p>
                  </div>
                </div>
                <div className="back"><div className="input-content"> 
                    <h1 id='attack-title'>Improved Dict</h1>
                    <input type="text"  id='hash-3' placeholder='enter your hashed password...' value={inputValue} 
                      onChange={(e) => setInputValue(e.target.value)} />
                    <h1 id='salt-title'>Salt</h1>
                    <input type="text" id='salt-3' placeholder='enter your salt...(optional)' value={saltValue} // Bind to salt input state
                      onChange={(e) => setSaltValue(e.target.value)} />
                    <select 
                          value={selectedHashMethod}
                          onChange={handleHashMethodChange}
                          className='select-attacks'
                        >
                          <option value="md5">MD5</option>
                          <option value="sha256">SHA-256</option>
                          <option value="sha1">SHA-1</option>
                        </select>
                        {!isSubmitted && !loading && (
                        <button  onClick={(e) => {e.stopPropagation(); handleSubmitImprovedDictionnary()}}>
                            Click to start</button>
                        )}  
                        {/* Message de réponse */}
                        {loading ? (
                        <div className="response-message3">
                            <PiSpinnerGapBold style={ {fontSize: "20px" }} /> {/* Show loading message while request is being processed */}
                        </div>
                        ) : (
                        <div className="response-message3">

                            <p>{responseMessage3}</p>
                            {responseMessage3 && !loading && (
                            <VscDebugRestart style={{ fontSize: "20px", cursor: "pointer" }} onClick={(e) => {e.stopPropagation();handleIconClick()} }/>
                            )}
                            
                        </div>
                        )}
                  </div></div>
              </div>
            </div>

           {/* Card 4  */}
           <div
              className={`swiper-slide ${flippedCardId === '4' ? 'flipped' : ''} 
                ${clickedCardId && clickedCardId !== '4' ? 'blurry' : ''} 
                ${clickedCardId === '4' ? 'selected' : ''}`}
              onClick={(e) => handleCardClick('4', e)} // Pass the event to prevent propagation
            >
              <div className="slide-content">
                <div className="front">
                <div className='about'>
                    <h1 className='front-title'>Hybrid</h1>
                    <h1 id='ab'>about</h1>
                    <p>
                    A hybrid attack combines the strengths of both dictionary and brute force 
                    techniques by first testing common passwords from a dictionary and then 
                    extending those passwords with additional characters or variations.</p>
                  </div>
                </div>
                <div className="back">
                <div className="input-content"> 
                    <h1 id='attack-title'>Hybrid</h1>
                    <input type="text"  id='hash-4' placeholder='enter your hashed password...' value={inputValue} 
                      onChange={(e) => setInputValue(e.target.value)} />
                    <h1 id='salt-title'>Salt</h1>
                    <input type="text" id='salt-4' placeholder='enter your salt...(optional)' value={saltValue} // Bind to salt input state
                      onChange={(e) => setSaltValue(e.target.value)} />
                    <select 
                          value={selectedHashMethod}
                          onChange={handleHashMethodChange}
                          className='select-attacks'
                        >
                          <option value="md5">MD5</option>
                          <option value="sha256">SHA-256</option>
                          <option value="sha1">SHA-1</option>
                        </select>
                        {!isSubmitted && !loading && (
                        <button  onClick={(e) => {e.stopPropagation(); handleSubmitHybrid()}}>
                            Click to start</button>
                        )}  
                        {/* Message de réponse */}
                        {loading ? (
                        <div className="response-message4">
                            <PiSpinnerGapBold style={ {fontSize: "20px" }} /> {/* Show loading message while request is being processed */}
                        </div>
                        ) : (
                        <div className="response-message4">

                            <p>{responseMessage4}</p>
                            {responseMessage4 && !loading && (
                            <VscDebugRestart style={{ fontSize: "20px", cursor: "pointer" }} onClick={(e) => {e.stopPropagation();handleIconClick()} }/>
                            )}
                            
                        </div>
                        )}
                    
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <div className="swiper-button-prev" ref={prevButtonRef}>
          <FaChevronLeft size={40} color="#fff" />
        </div>
        <div className="swiper-button-next" ref={nextButtonRef}>
          <FaChevronRight size={40} color="#fff" />
        </div>
      </div>
    </div>
  );
}

export default Page1;
