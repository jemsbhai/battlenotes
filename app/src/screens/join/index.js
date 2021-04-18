import React from "react";
import './join.css';
export default function Join(props) {
    return(
    <div>
    <div className="title"><h1>JOIN A ROOM</h1></div>
    <div className="button">
 

    <svg style={{float:'right'}}  id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
  
    <rect x="190" y="0" width="70%" height="50%" fill="#8a79ad"  transform="skewX(-20)" className="box"/>
    
      <g>
    <rect x="550" y="0" width="20%" height="40%" fill="#FFF"  transform="skewX(-20)" className="box"/>
    <text className="h23" 
        x="87.5%"
        y="25"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">SEARCH</text></g>
    </svg>
    <input className="code" placeholder="TYPE ROOM CODE" color="#A384E2"></input>
    </div>
    </div> 
    );
  }