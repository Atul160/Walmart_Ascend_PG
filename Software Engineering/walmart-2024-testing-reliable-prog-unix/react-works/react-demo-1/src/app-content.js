import React, { Component } from 'react'
import './css/app-content.css';

class AppContent extends Component {


    render() {

        const msg = "Hi this is my message in component";

        return (
            <div className="content">
                <h2>This is App Content</h2>
                <h3>{msg}</h3>
                <h3>Location: {this.props.location}</h3>
            </div>
        );
    }
}

export default AppContent;