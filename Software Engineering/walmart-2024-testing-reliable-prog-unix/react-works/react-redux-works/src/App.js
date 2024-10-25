import React, { Component } from 'react';

import 'bootstrap/dist/css/bootstrap.css';

import { createStore, applyMiddleware } from 'redux';
import rootReducer from './reducers/root-reducer';

// this should not be inproduction 
// import { composeWithDevTools } from 'redux-devtools-extension';
import { thunk } from 'redux-thunk';

import { Provider } from 'react-redux';
import ContactForm from './components/ContactForm';
import ContactsList from './components/ContactList';



let store = createStore(rootReducer, applyMiddleware(thunk));

class App extends Component {

  render() {
    return (
      <Provider store={store}>
        <div className="container">
          <div className="row">
            <div className="col">

              <ContactForm />
            </div>
            <div className="col">
              <ContactsList />
            </div>
          </div>
        </div>
      </Provider>
    );
  }
}

export default App;