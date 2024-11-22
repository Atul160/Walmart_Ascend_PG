import React, { Component } from 'react';

// HOC should not mutate the actual component 
function loading(OldComponent) {
    return class NewComponent extends Component {
        render() {
            let output = <OldComponent {...this.props} />

            if (this.props.contacts.length === 0) {
                output = <p className='text-center'>Loading please wait... </p>
            }

            return output;
        }
    }
}

export default loading;