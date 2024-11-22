import React, { Component } from 'react'

import 'bootstrap/dist/css/bootstrap.css';

class EventComponent extends Component {
    state = {
        num: 0
    }

    increment = () => {
        // you cannot mutate the state variables directly 

        // this.state.num ++;

        this.setState({ num: this.state.num + 1 })
    }

    decrement = () => { this.setState({ num: this.state.num - 1 }) }


    render() {
        return (

            // dont use setstate inside render function 
            // this will get into infinite loop 
            <div>
                {  /*<button className="btn btn-primary" onClick={this.setState({ num: this.state.num + 1 })}>
                    Increment</button>

                <button className="btn btn-danger" onClick={this.setState({ num: this.state.num - 1 })}>
                    Decrement</button>*/
                }
                <hr></hr>
                <button className='btn btn-primary' onClick={this.increment}>INC</button>

                <button className='btn btn-primary' onClick={this.decrement}>DEC</button>

                <h2>The value of Number: {this.state.num}</h2>
                <br /> <hr />
            </div >
        );
    }
}

export default EventComponent;