/*
 *  AuthService is in charge of calling login API.
 *  The server will validate the username and password and return a JWT
 *  back to our app. Once we get it, we'll create a LoginAction and send
 *  it to all the Stores using the Dispatcher from Flux.
 */

import request from "reqwest";
import when from "when";
import {LOGIN_URL, SIGNUP_URL} from "../constants/LoginConstants"
import LoginActions from "../actions/LoginActions"

class AuthService {

  /*
   *  Login Ajax call
   */
  login(username, password) {

    // NOTE THIS AJAX CALL DATA IS FORM DATA
    return this.handleAuth(when(request({
      url: LOGIN_URL,
      method: "POST",
      crossOrgin: true,
      type: "json",
      data: {
        username, password
      }
    })));
  }

  logout() {
    // Invoke logoutUser method in LoginActions 
    LoginActions.logoutUser();
  }

  // signup(username, password, extra) {
  //   return this.handleAuth(when(request({
  //     url: SIGNUP_URL,
  //     method: "POST",
  //     crossOrgin: true,
  //     type: "json",
  //     data: {
  //       username, password, extra
  //     }
  //   })));
  // }

  handleAuth(loginPromise) {
    return loginPromise.then(function(response) {
      
      console.log("$$$$$$??????? IF this statment is executed that means ajax call success!");
      
      // Retrieve JWT from response 
      var jwt = response.id_token;
      console.log("jwt : " + jwt); // DEBUG PURPOSE

      // Trigger the LoginAction with that JWT.. store jwt
      LoginActions.loginUser(jwt);
      return true;
    });
  }

}

export default new AuthService()