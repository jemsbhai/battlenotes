import React, { useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom";
import './index.css';

import Musician from '../../assets/musician.png';
import Fitfreak from '../../assets/fitfreak.png';
import Typemaster from '../../assets/typemaster.png';


export default function Wait(props) {

    useEffect(() => {
        console.log(props.location.state.char);
        setTimeout(() => {
            setP2(true);
        }, 2000);
        setTimeout(() => {
            navigateTo();
        }, 5000);
      });

    const [p2,setP2] = useState(false);
    const history = useHistory();
    const navigateTo = () => history.push('/game');
    return(
        
        <div>
    
    <div className="char">
        <div>
            <img src={props.location.state.char} alt=""></img>
    <svg style={{float:'left'}} class="shadow" id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
        <g>
        <rect x="190" y="0" width="70%" height="80%" fill="#FFF"  transform="skewX(-20)" className="box"/>
        <Link to={{pathname: "/join",}}><text className="h2" 
        x="60%"
        y="40"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">PLAYER 1</text></Link></g>
    
    
    </svg></div>
    <div className="title1"><h1 className="h11">VS</h1></div>
    
    {p2 &&<div>
            <img src={Fitfreak} style={{height:400}} alt=""></img>
    <svg style={{float:'left'}} class="shadow" id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
        <g>
        <rect x="190" y="0" width="70%" height="80%" fill="#FFF"  transform="skewX(-20)" className="box"/>
        <Link to={{pathname: "/join",}}><text className="h2" 
        x="60%"
        y="40"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">PLAYER 2</text></Link></g>
    
    
    </svg></div>}
    {!p2 &&<h2 className="h222">WAITING FOR SOMEONE TO JOIN</h2>}


    </div>
    

    </div> 
    );
  }