import React from 'react'
import './css/app-footer.css'

function AppFooter(props) {
    console.log(props);
    return (
        <div className="app-footer">
            <hr />
            <p>Copy Right reserved - Walmart - {props.year}
                company: {props.company} -
                <a href={props.website}>website</a> </p>
        </div>
    )
}
export default AppFooter; 