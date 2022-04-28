import logo from './logo.svg';
import './App.css';

import React, { useEffect } from 'react';
import axios from "axios"

function App() {

  // retrieve user access token and store in local browser storage

  useEffect(() => {
    axios.get("/.auth/me")
      .then((response) => {
        console.log(response.data[0]);
        localStorage.setItem("authToken", response.data[0].access_token);
      })
  }, []);

  const authToken = localStorage.getItem("authToken");
  console.log({ authToken });

  // set user access token as default Authorization header

  axios.defaults.headers.common['Authorization'] = "Bearer " + localStorage.getItem("authToken");

  // call backend api and write response to console

  useEffect(() => {
    axios.get("https://awcacewebbackend.azurewebsites.net/")
      .then((response) => {
        console.log(response.data);
      })
  }, []);


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React!
        </a>
      </header>
    </div>
  );
}

export default App;