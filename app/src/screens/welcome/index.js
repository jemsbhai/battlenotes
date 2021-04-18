import React from "react";
import { Link } from "react-router-dom";
import './index.css';
export default function Welcome(props) {
    return(
        <div>
    <div className="title"><h1>BATTELNOTES</h1></div>
    <div className="buttons">
    <svg style={{float:'left'}} class="shadow" id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
        <g>
        <rect x="190" y="0" width="70%" height="80%" fill="#FFF"  transform="skewX(-20)" className="box"/>
        <Link to={{pathname: "/join",}}><text className="h2" 
        x="60%"
        y="40"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">JOIN A ROOM</text></Link></g>
    
    
    </svg>

    <svg style={{float:'right'}} class="shadow" id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
    <g>
    <rect x="190" y="0" width="70%" height="80%" fill="#FFF"  transform="skewX(-20)" className="box"/>
    <Link to={{pathname: "/create",}}><text className="h2" 
        x="60%"
        y="40"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">CREATE A ROOM</text></Link></g>
    </svg>
    </div>
    </div> 
    );
  }