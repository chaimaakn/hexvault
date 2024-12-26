import React from 'react'
import Navbar2 from '../components/Navbar/Navbar2';
import '../styles/Services.css';
function EncryptDecrypt() {
  return (
    <div id='encryptdecrypt'>

    <div className="navbar-container">
            <Navbar2 />
        </div>

        <div className='container'>
            <div className='encrypt'>
                <h1>Encryption</h1>
                <textarea name="" className="entry" rows={5} placeholder='enter text to encrypt here...'></textarea>
                <select name="" className="select">
                <option value="">AES</option>
                <option value="">3DES</option>
                <option value="">RC4</option>
                <option value="">RSA</option>
                <option value="">CHACHA20</option>
            </select>
            <div className='key-container'>
            <input type="text" className='key' placeholder='enter your key or generate one...' />
            <button className='gen-key-btn'>generate key</button>
            </div>
                <textarea name="" className="output" rows={5} placeholder='encrypted value will appear here...' disabled></textarea>
                <button className='sub-btn'>Encrypt</button>
            </div>

            <div className='decrypt'>
            <h1>Decryption</h1>
            <textarea name="" className="entry" rows={5} placeholder='enter text to decrypt here...'></textarea>
            <select name="" className="select">
                <option value="">AES</option>
                <option value="">3DES</option>
                <option value="">RC4</option>
                <option value="">RSA</option>
                <option value="">CHACHA20</option>
            </select>
            <input type="text" className='key'  placeholder='enter your key...'/>
            <textarea name="" className="output" rows={5} placeholder='decrypted value will appear here...' disabled></textarea>
            <button className='sub-btn'>Decrypt</button>
            </div>
        </div>
   
</div>
  )
}

export default EncryptDecrypt