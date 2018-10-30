import Cookie from 'js-cookie';

export default {
    setAuth(state, token) {
        state.auth = token;
    },

    setLoggedInUser(state, user) {
        state.loggedInUser = user;
    },

    logoutUser(state) {
        state.loggedInUser = {};
        state.auth = '';
        Cookie.remove('auth');
    },
};
