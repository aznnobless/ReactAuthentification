import React from 'react';

// import Auth from '../services/AuthService'

export default class Signup extends React.Component {

  constructor() {
    super();
  }

  signup(e) {
    e.preventDefault();
    console.log("singup pressed");
    // Auth.signup(this.state.user, this.state.password, this.state.extra)
    //   .catch(function(err) {
    //     alert("There's an error logging in");
    //     console.log("Error logging in", err);
    //   });
  }

  render() {
    return (
      <div className="login jumbotron center-block">
        <h1>Signup</h1>
        <form role="form">
        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input type="text" className="form-control" id="username" ref="username" placeholder="Username" />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input type="password" className="form-control" id="password" ref="password" placeholder="Password" />
        </div>
        <div className="form-group">
          <label htmlFor="extra">Extra</label>
          <input type="text" className="form-control" id="extra" ref="extra" placeholder="Some extra information" />
        </div>
        <button type="submit" className="btn btn-default" onClick={this.signup.bind(this)}>Submit</button>
      </form>
    </div>
    );
  }
}

