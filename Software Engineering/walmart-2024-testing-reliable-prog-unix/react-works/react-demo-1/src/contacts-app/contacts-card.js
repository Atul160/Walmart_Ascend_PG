import React from 'react'


const ContactCard = ({ contact }) => (
    <div className='card'>
        <div className="row">
            <div className="col-md-4">
                <img src={contact.picture} alt={contact.name}
                    style={{ width: 100, height: 100 }}
                    className="card-img" />
            </div>

            <div className="col-md-8">
                <div className="card-body">
                    <h4 className="card-title">Name: {contact.name}</h4>
                    <div className="card-text">Email: {contact.email}</div>
                    <div className="card-text">Phone: {contact.phone}</div>
                </div>
            </div>
        </div>
    </div>
);

export default ContactCard;