import React, { Component } from 'react'
import { createRoot } from 'react-dom/client'
import ContactCard from './contacts-app/contacts-card';


import 'bootstrap/dist/css/bootstrap.css';
import ContactList from './contacts-app/contact-list';


class App extends Component {

    state = {
        contacts: []
    }

    // get the data from end point 

    componentDidMount() {
        // we can use jQuery, axios, fetch ..... 
        fetch("http://localhost:4000/contact")
            .then(resp => resp.json())
            .then(data => this.setState({ contacts: data }))

    }

    render() {
        const contact = {
            id: 101,
            name: "Peter",
            email: "peter@druker.com",
            phone: "7897897897",
            picture: "https://randomuser.me/api/portraits/men/1.jpg"
        };

        // working with arrays 

        console.log(this.state.contacts);

        // const contactCards = contacts.map(c => c.name);
        // console.log(contactCards);

        // const contactCards = contacts.map(c => <ContactCard contact={c} key={c.id} />)

        return (
            <div>
                <ContactCard contact={contact} />
                {/* {contactCards} */}

                <ContactList contacts={this.state.contacts} />
            </div>
        );
    }
}

const rootElement = document.getElementById("root");
const root = createRoot(rootElement);

root.render(<App />);