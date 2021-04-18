import React from "react";
import { Link } from "react-router-dom";
import './index.css';

import Musician from '../../assets/musician.png';
import Fitfreak from '../../assets/fitfreak.png';
import Typemaster from '../../assets/typemaster.png';
import D from '../../assets/d.png';


export default function Move(props) {
    return(
        <div className="body">
    <div className="players"><h1 className="h11">PLAYER 1</h1>
    <h1 className="h12">PLAYER 2</h1></div>

    <div className="players" style={{float:'left', marginLeft:'-15%'}}>
        <img src={D}></img>
        <img src={D}></img>
        <img src={D}></img>
        <img src={D}></img>
        <img src={D}></img>
    </div>
    <div className="players" style={{float:'right', marginRight:'-16%'}}>
        <img src={D}></img>
        <img src={D}></img>
        <img src={D}></img>
        <img src={D}></img>
        <img src={D}></img>
    </div>
   


    
  <div className="buttons2" style={{float:'right'}}>
    <svg style={{float:'left'}} class="shadow" id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
        <g>
        <rect x="190" y="0" width="70%" height="80%" fill="#FFF"  transform="skewX(-20)" className="box"/>
        <Link to={{pathname: "/music",}}><text className="h2" 
        x="60%"
        y="40"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">ATTACK</text></Link></g>
    
    
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
        alignment-baseline="middle">PASS</text></Link></g>
    </svg>
    </div>

</div>
    
    
   


    );
  }