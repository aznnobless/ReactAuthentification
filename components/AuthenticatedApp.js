'use strict';

import React from 'react';
//import LoginStore from "../stores/LoginStore"
import { Route, RouteHandler, Link} from 'react-router';
//import AuthService from "../services/AuthService"

export default class AuthenticateApp extends React.Component {

  // Constructor
  constructor() {
    super()
    this.state = this._getLoginState();
  }

  // Helper method
  _getLoginState() {
    return {
      userLoggedIn: false//LoginStore.isLoggedIn()
    };
  }

  // componentDidMount() {
  //   this.changeListener = this._onChange.bind(this);
  //   //LoginStore.addChangeListener(this.changeListener);
  // }

  // // Helper method
  // _onChange() {
  //   this.setState(this._getLoginState());
  // }

  // componentWillUnmount() {
  //   //LoginStore.removeChangeListener(this.changeListener);
  // }

  render() {

    return (
      <div className="container">
        <nav clsasName="navbar navbar-default">
          <div className="navbar-header">
            <a className="navbar-brand" href="/">React Flux app withh JWT authentication</a>
          </div>
          {this.headerItems}
        </nav>
        AuthenticatedApp.js
        {this.props.children}
        
      </div>
    );
  }

  logout(e) {
    e.preventDefault();
    //AuthService.logout();
  }

  get headerItems() {

    if(!this.state.userLoggedIn) {
      return (
        <ul className="nav navbar-nav navbar-right">
          <li>
            <Link to="login">Login</Link>
          </li>
          <li>
            <Link to="signup">Signup</Link>
          </li>
        </ul>

      )
    } else {
      return (
        <ul className="nav navbar-nav navbar-right">
          <li>
            <Link to="home">Home</Link>
          </li>
          <li>
            <a href="" onClick={this.logout}>Logout</a>
          </li>
        </ul>
      )
    }

  }

}