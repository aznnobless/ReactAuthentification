import React from 'react';
import Auth from '../services/AuthService';

export default class Login extends React.Component {
  
  constructor() {
    super();
  }

  login(e) {
    e.preventDefault();
    console.log("Login button pressed");

    let username = this.refs.username.value.trim();
    let password = this.refs.password.value.trim();

    /** DEBUG PURPOSE **/
    console.log(username);
    console.log(password);

    /** Login auth process here **/
    Auth.login(username, password)
      .catch(function(err) {
        alert("There's an error logging in");
        console.log("Error logging in", err);
      });
  } 

  render() {
    return (
      <div className="login jumbotron center-block">
        <h1>Login</h1>
        <form role="form">
        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input type="text" className="form-control" id="username" ref="username" placeholder="Username" />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input type="password"  className="form-control" id="password" ref="password" placeholder="Password" />
        </div>
        <button type="submit" className="btn btn-default" onClick={this.login.bind(this)}>Submit</button>
        </form>
      </div>
      );

  }
}
