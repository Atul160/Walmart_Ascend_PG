import React from 'react';




// stateless component 
const Btn = ({ caption, handler }) => (
    <button className='btn btn-warning' onClick={handler}>{caption}</button>
);

export default Btn; 