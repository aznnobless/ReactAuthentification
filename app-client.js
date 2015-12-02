import React from "react";
import { render } from "react-dom"
import { Router, Route, IndexRoute} from "react-router"

import createBrowserHistory from 'history/lib/createBrowserHistory'


/** Page Component **/
import AuthenticatedApp from "./components/AuthenticatedApp"
import Login from "./components/Login";
import Signup from "./components/Signup";
import Home from "./components/Home";

import RouterContainer from "./services/RouterContainer";
//import LoginActions from "./actions/LoginActions";

let history = createBrowserHistory();

var appRouter = (

  <Router history={history}> 
    <Route component={AuthenticatedApp}>
      <Route path="/" component={Home}/>
      <Route path="login" component={Login}/>
      <Route path="signup" component={Signup}/>
    </Route>
  </Router>

);

// store router information to RouterContainer
RouterContainer.set(appRouter);

let jwt = localStorage.getItem('jwt');
if(jwt) {
  console.log("jwt exist");
  //LoginActions.loginUser(jwt);
}else {
  console.log("jwt NOT exist");
}

// Start render APP
render(
  appRouter,
  document.getElementById("react-container")
);