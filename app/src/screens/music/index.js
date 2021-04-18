import React from "react";
import { Link } from "react-router-dom";
import './index.css';

import Musician from '../../assets/musician.png';
import Fitfreak from '../../assets/fitfreak.png';
import Typemaster from '../../assets/typemaster.png';
import D from '../../assets/d.png';
import Note from '../../assets/note.png';

export default function Music(props) {
    return(
        <div className="body2">
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
   <div style={{position:'absolute', borderRadius:20, width:1100, height:450, backgroundColor:'#FFF', top:'25%', left:'25%'}}>
       <img></img>
       <marquee direction="left"><img src={Note} style={{marginTop:'5%', marginBottom:'5%'}}></img></marquee>
   </div>


    
  <div className="buttons2" style={{float:'right', marginTop:'35%'}}>
    <svg style={{float:'left'}} class="shadow" id="main-box" viewBox="0 0 700 100" preserveAspectRatio="none" 
    xmlns="http://www.w3.org/2000/svg">
        <g>
        <rect x="190" y="0" width="20%" height="25%" fill="#FFF"  transform="skewX(-20)" className="box"/>
        <Link to={{pathname: "/attack",}}><text style={{fontSize:'2vh'}}
        x="37.5%"
        y="15"
        fill="#552DAA"
        text-anchor="middle"
        alignment-baseline="middle">PLAY</text></Link></g>
    
    
    </svg>


    </div>

</div>
    
    
   


    );
  }