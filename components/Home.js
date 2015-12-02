

import React from 'react';
import AuthenticatedComponent from "./AuthenticatedComponent"

export default AuthenticatedComponent(class home extends React.Component {
  render() {
    return (<h1> Hello ! {this.props.user ? this.props.user.username : ""} Here is HOME! {this.props.userLoggedIn ? "logged in" : ""} </h1>);
  }
});