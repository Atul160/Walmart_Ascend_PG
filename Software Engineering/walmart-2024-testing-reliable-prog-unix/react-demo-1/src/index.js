// import React, {Component} from 'react';
// import ReactDOM from 'react-dom/client';
// import './index.css';
// import App from './App';
// import reportWebVitals from './reportWebVitals';

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );

// // If you want to start measuring performance in your app, pass a function
// // to log results (for example: reportWebVitals(console.log))
// // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();


import React, { Component } from 'react';
import { createRoot } from 'react-dom';

class App extends Component {

  render() {
    return <div>
      <p>
        Hello React
      </p>
    </div>
  }
}

const rootElement = createRoot(document.getElementById('root'))

rootElement.render(<App />)