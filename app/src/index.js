import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Chooose from "./screens/choose";
import Create from "./screens/create";
import Join from "./screens/join";
import Name from "./screens/name";

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
      
      
    </div>
  </Router>,
  document.getElementById("root")
);