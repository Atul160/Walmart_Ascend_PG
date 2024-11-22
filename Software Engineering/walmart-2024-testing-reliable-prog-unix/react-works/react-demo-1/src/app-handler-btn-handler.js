import React, { Component } from 'react'
import Btn from './button';



class AppComponentBtnHandler extends Component {

    // constructor() {
    //     super();
    //     this.btnHandler = this.btnHandler.bind(this);
    // }

    btnHandler = () => {
        console.log("Button Handler called...", this)
    }

    increment = () => {
        // if you call setState function then render is implicity called.
        this.setState({ num: this.state.num + 1 })
    }

    decrement = () => {
        this.setState({ num: this.state.num - 1 })
    }

    incrementOrDecrement = (val) => {
        this.setState({ num: this.state.num + val });
    }

    state = {
        num: 0
    }
    render() {
        console.log("render for state value of ", this.state.num)
        return (
            <div className="alert alert-primary">
                <h1>Button Handler </h1>

                <button onClick={this.btnHandler}
                    className="btn btn-primary">Button Handler</button>
                <hr />
                <button onClick={this.increment} className='btn btn-success'>Increment</button>
                <button onClick={this.decrement} className='btn btn-success'>Decrement</button>
                <hr />

                <button onClick={() => this.incrementOrDecrement(1)}
                    className='btn btn-danger'>Increment</button>

                <button onClick={() => this.incrementOrDecrement(-1)}
                    className='btn btn-danger'>Decrement</button>

                <hr />
                <Btn caption="Increment" handler={() => this.incrementOrDecrement(1)} />
                <Btn caption="Decrement" handler={() => this.incrementOrDecrement(-1)} />
                <h2>The value of Num : {this.state.num} </h2>

            </div>
        );
    }
}

export default AppComponentBtnHandler;