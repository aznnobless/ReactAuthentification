import AppDispatcher from '../dispatchers/AppDispatcher.js';
import {LOGIN_USER, LOGOUT_USER} from '../constants/LoginConstants.js';
import RouterContainer from '../services/RouterContainer'

export default {

  /*
   *  Login Action
   */
  loginUser: (jwt) => {
    
    /** To check JWT exist in local storage **/
    var savedJwt = localStorage.getItem('jwt');
    console.log("current jwt in localStorage : " + savedJwt)

    AppDispatcher.dispatch({
      actionType: LOGIN_USER,
      jwt: jwt
    });

    // *** TODO: ??? ***

    // if saveJwt does not match fresh jwt
    if(savedJwt !== jwt) {

      var router = RouterContainer.get();
      var history = router.props.history;

      // This will redirect to '/' path
      history.pushState(null, '/')

      // Store JWT into localStorage
      localStorage.setItem('jwt', jwt);
    }

    console.log("JWT saved to localStorage. + " + localStorage.getItem('jwt'));
  },

  /*
   *  Logout Action
   */
  logoutUser: () => {

    var router = RouterContainer.get();
    var history = router.props.history;

    //RouterContainer.get().transitionTo('/login'); // Deprecated. Use blow statement
    history.pushState(null, 'login');

    // Remove JWT from localStorage
    localStorage.removeItem('jwt');

    AppDispatcher.dispatch({
      actionType: LOGOUT_USER
    });

  }


}