import React, { useEffect } from "react";
import { Link, useHistory } from "react-router-dom";
import './index.css';

import Musician from '../../assets/musician.png';
import Fitfreak from '../../assets/fitfreak.png';
import Typemaster from '../../assets/typemaster.png';
import D from '../../assets/d.png';


export default function Game(props) {
    useEffect(() => {
      
        setTimeout(() => {
            navigateTo();
        }, 2000);
      });
    const history = useHistory();
    const navigateTo = () => history.push('/move');
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
   


    <div className="chars" style={{marginTop:'70%'}}>
        <div style={{float:'left', marginRight:'50%', marginTop:'30%'}}>
            <img src={Fitfreak} alt=""></img>
   
  </div>

    <div style={{float:'right', marginTop:'30%'}}>
            <img src={Musician}  alt=""></img>
   
    
    
  </div>


    </div>
    
   

    </div> 
    );
  }