import { deleteContact } from '../actions/contacts-action';
import { connect } from 'react-redux';

const ContactCard = ({ contact, removeContact }) => (
    <div className="card">
        <div className="row">

            <div className="col-md-4">
                <img src={contact.pic} alt={contact.first_name} className="card-img"
                    style={{ width: "120px", height: "120px" }} />
            </div>
            <div className="col-md-8">
                <div className="card-body">
                    <h4 className="card-title">{contact.gender === 'Male' ? "Mr. " : "Ms/Mrs. "}{contact.first_name}
                        <button className="btn btn-danger"
                            onClick={() => {
                                removeContact(contact.id)
                            }}
                        >X</button>
                    </h4>
                    <h4 className="card-text">{contact.email}</h4>
                    <h4 className="card-text">{contact.phone}</h4>
                </div>
            </div>

        </div>
    </div>
)
export default connect(null, { removeContact: deleteContact })(ContactCard); 