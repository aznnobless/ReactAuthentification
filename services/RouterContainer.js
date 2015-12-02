var _router = null;

export default {
  
  /*
   * same as
   *    set : function(router) { _router = router }
   */

  set: (router) => _router = router,
  
  get: () => _router
}