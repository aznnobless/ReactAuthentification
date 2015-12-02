

import React from 'react';
import AuthenticatedComponent from "./AuthenticatedComponent"

export default AuthenticatedComponent(class home extends React.Component {
  render() {
    return (<h1> Hello !  Here is HOME </h1>);
  }
});