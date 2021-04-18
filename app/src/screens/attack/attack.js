import React, { useEffect, useState } from "react";
import { Link, useHistory } from "react-router-dom";
import './index.css';

import Musician from '../../assets/musician.png';
import Fitfreak from '../../assets/fitfreak.png';
import Typemaster from '../../assets/typemaster.png';
import BG from '../../assets/turn.png';

export default function Attack() {

    return(
        
        <div className="body4">
        <img src={BG} style={{height:'100%', width:'100%'}}></img>   
    </div>
    );
  }