import React, { Component } from 'react'

class AppHeader extends Component {

    render() {
        console.log(this.props);
        return (
            <div>
                <h1>Company Name - {this.props.companyName}</h1>
                <h3>City {this.props.city}</h3>
                <hr />
            </div>
        );
    }
}

export default AppHeader;