import React from "react";
import { Link } from "react-router-dom";
import './index.css';

import Musician from '../../assets/musician.png';
import Fitfreak from '../../assets/fitfreak.png';
import Typemaster from '../../assets/typemaster.png';


export default function Chooose(props) {
    return(
        <div>
    <div className="title1"><h1 className="h11">CHOOSE YOUR CHARACTER</h1></div>
    <div className="charpick">
        <div>
            <img src={Musician} alt=""></img>
    <svg style={{float:'left'}} class="shadow" id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
        <g>
        <rect x="190" y="0" width="70%" height="80%" fill="#FFF"  transform="skewX(-20)" className="box"/>
        <Link to={{pathname: "/wait", state:{char:Musician}}}><text className="h2" 
        x="60%"
        y="40"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">MUSICIAN</text></Link></g>
    
    
    </svg></div>

    <div>
            <img src={Fitfreak}  alt=""></img>
    <svg style={{float:'left'}} class="shadow" id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
        <g>
        <rect x="190" y="0" width="70%" height="80%" fill="#FFF"  transform="skewX(-20)" className="box"/>
        <Link to={{pathname: "/wait", state:{char:Fitfreak}}}><text className="h2" 
        x="60%"
        y="40"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">FITFREAK</text></Link></g>
    
    
    </svg></div>

<div>
<img src={Typemaster} alt=""></img>
    <svg style={{float:'right'}} class="shadow" id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
    <g>
    <rect x="190" y="0" width="70%" height="80%" fill="#FFF"  transform="skewX(-20)" className="box"/>
    <Link to={{pathname: "/wait", state:{char:Typemaster}}}><text className="h2" 
        x="60%"
        y="40"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">TYPEMASTER</text></Link></g>
    </svg></div>
    </div>
    <h1 className="h111">BATTLENOTES</h1>
    <h2 className="h222">Fun Fact: On Good Friday in 1930, the BBC reported, “There is no news.” Instead, they played piano music.</h2>
   

    </div> 
    );
  }