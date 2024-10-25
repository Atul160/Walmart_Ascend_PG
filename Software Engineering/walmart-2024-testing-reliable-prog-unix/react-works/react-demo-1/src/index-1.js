import React, { Component } from 'react'
import { createRoot } from 'react-dom/client'
// import AppHeader from './app-header';
// import AppFooter from './app-footer';
// import AppContent from './app-content';
// // import EventComponent from './event-component';
// import AppComponentBtnHandler from './app-handler-btn-handler';

import EmployeeForm from './employee-form';

import 'bootstrap/dist/css/bootstrap.css';


class App extends Component {
  render() {

    const footerProps = {
      year: 2024,
      company: 'walmart',
      website: 'http://walmart.com'
    }

    return <div>
      {/* <AppHeader companyName="walmart" city="Bengaluru" />

      <div className="container">
        {/* <div className="row"><EventComponent /></div> */}
      {/* <AppComponentBtnHandler />
        <div className="row"><AppContent location="White Field" /></div>
      </div> */}



      {/* <AppFooter {...footerProps} /> */}


      <div className="row">
        <div className="col">
          <EmployeeForm />
        </div>
        <div className="col">
          <h2>Other Details </h2>
        </div>
      </div>




    </div >
  }
}

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(<App />);