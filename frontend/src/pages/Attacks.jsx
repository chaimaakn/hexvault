import React, { useEffect, useRef, useState } from 'react';
import Swiper from 'swiper';
import 'swiper/css';
import Navbar from '../components/Navbar/Navbar';
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import '../styles/Services.css';

function Page1() {
  const swiperRef = useRef(null);
  const prevButtonRef = useRef(null);
  const nextButtonRef = useRef(null);

  const [flippedCardId, setFlippedCardId] = useState(null);
  const [clickedCardId, setClickedCardId] = useState(null); // Track the clicked card
  const [canFlip, setCanFlip] = useState(true); // Control whether the card can be flipped

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
  const enableFlip = (id) => {
    setCanFlip(true); // Re-enable flipping when the button is clicked
    setFlippedCardId(id);
    setClickedCardId(null);
  };

  useEffect(() => {
    if (flippedCardId) {
      setCanFlip(false); // Disable flip-back when the card is flipped
    } else {
      setCanFlip(true); // Enable flip-back when the card is not flipped
    }
  }, [flippedCardId]);

  return (
    <div id="Attacks">
      <div className="navbar-container">
        <Navbar />
      </div>

      <div className="swiper-container">
        <div className="swiper">
          <div className="swiper-wrapper">
            {/* Card 1 */}
            <div
              className={`swiper-slide ${flippedCardId === '1' ? 'flipped' : ''} 
                ${clickedCardId && clickedCardId !== '1' ? 'blurry' : ''} 
                ${clickedCardId === '1' ? 'selected' : ''}`}
              onClick={(e) => handleCardClick('1', e)} // Pass the event to prevent propagation
            >
              <div className="slide-content">
                <div className="front">
                  <h1>Brute force</h1>
                  {/* Added tabs section */}
                  <div
                    className="tabs"
                    onClick={(e) => e.stopPropagation()} // Prevent flipping on tabs click
                  >
                    
                  </div>
                </div>
                <div className="back">
                  <h1>Brute force</h1>
                  <div className="input-content">
                    <input type="text" />
                    <h1>Salt</h1>
                    <input type="text" />
                    {/* Button to enable flip-back */}
                    <button onClick={enableFlip}>Click to start</button>
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
                  <h1>Dictionary</h1>
                </div>
                <div className="back">Back Content 2</div>
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
                  <h1>Improved Dict</h1>
                </div>
                <div className="back">Back Content 3</div>
              </div>
            </div>

            {/* Card 4 */}
            <div
              className={`swiper-slide ${flippedCardId === '4' ? 'flipped' : ''} 
                ${clickedCardId && clickedCardId !== '4' ? 'blurry' : ''} 
                ${clickedCardId === '4' ? 'selected' : ''}`}
              onClick={(e) => handleCardClick('4', e)} // Pass the event to prevent propagation
            >
              <div className="slide-content">
                <div className="front">
                  <h1>Hybrid</h1>
                </div>
                <div className="back">Back Content 4</div>
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
