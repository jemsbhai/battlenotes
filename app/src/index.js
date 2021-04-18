import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Attack from "./screens/attack/attack";
import Chooose from "./screens/choose";
import Create from "./screens/create";
import Game from "./screens/game";
import Join from "./screens/join";
import Move from "./screens/move";
import Music from "./screens/music";
import Name from "./screens/name";
import Wait from "./screens/wait";

// import components
import Welcome from "./screens/welcome";


ReactDOM.render(
  <Router>
    <div className="App">
      <Route exact path="/" component={Welcome} />
      <Route exact path="/join" component={Join} />
      <Route exact path="/create" component={Create} />
      <Route exact path="/name" component={Name} />
      <Route exact path="/choose" component={Chooose} />
      <Route exact path="/wait" component={Wait} />
      <Route exact path="/game" component={Game} />
      <Route exact path="/move" component={Move} />
      <Route exact path="/music" component={Music} />
      <Route exact path="/attack" component={Attack} />
      
      
    </div>
  </Router>,
  document.getElementById("root")
);