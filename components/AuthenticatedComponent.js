/*
 *  Wrapper component called AuthenticatedComponent.
 *  It will make suere the user is authenticated before displaying its content.
 *  If the user isn't authenticated, it'll redirect him or her to the logi page.
 */
import React from 'react';
import LoginStore from '../stores/LoginStore';
import RouterContainer from '../services/RouterContainer'

export default (ComposedComponent) => {
  return class AuthenticatedComponent extends React.Component {

    /** willTransitionTo() is deprecated **/
    // static willTransitionTo() {
    //   if (!LoginStore.isLoggedIn()) {
    //     var router = RouterContainer.get();
    //     var history = router.props.history;
    //     history.pushState(null, 'login');

    //   }
    // }

    componentWillMount() {
      if (!LoginStore.isLoggedIn()) {
        var router = RouterContainer.get();
        var history = router.props.history;
        history.pushState(null, 'login');
      }
    }

    constructor() {
      super()
      this.state = this._getLoginState();
    }

    _getLoginState() {
      return {
        userLoggedIn: LoginStore.isLoggedIn(),
        user: LoginStore.user,
        jwt: LoginStore.jwt
      };
    }

    componentDidMount() {
      this.changeListener = this._onChange.bind(this);
      LoginStore.addChangeListener(this.changeListener);
    }

    _onChange() {
      this.setState(this._getLoginState());
    }

    componentWillUnmount() {
      LoginStore.removeChangeListener(this.changeListener);
    }

    render() {
      console.log("DEBUG POINT");
      console.log("username : " + this.state.user );
      console.log("jwt : " + this.state.jwt);
      return (
        <ComposedComponent
        {...this.props}
        user={this.state.user}
        jwt={this.state.jwt}
        userLoggedIn={this.state.userLoggedIn} />
      );
    }
  }
};