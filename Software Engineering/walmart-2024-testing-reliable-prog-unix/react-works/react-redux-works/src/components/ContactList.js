import React, { Component } from 'react'
import { connect } from 'react-redux';
import { fetchContacts } from '../actions/contacts-action';
import ContactCard from './ContactCard'

class ContactsList extends Component {

    componentDidMount() {
        this.props.getContacts();
    }

    render() {
        let list = null;
        let { contacts } = this.props;
        if (contacts instanceof Array && contacts.length > 0) {
            list = contacts.map(c => <ContactCard contact={c} key={c.id} />)
        }
        return (
            <div className="container">
                <h3>Contact List</h3>
                {list}
            </div>
        );
    }
}
let mapStateToProps = (reducer) => {
    return {
        contacts: reducer.contactsReducer.contacts
    }
};
let mapDispatchToProps = { getContacts: fetchContacts }
export default connect(mapStateToProps, mapDispatchToProps)(ContactsList);