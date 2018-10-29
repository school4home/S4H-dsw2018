import Cookie from 'js-cookie';

export default function ({ store, redirect, route }) {
    const auth_token = Cookie.get('auth');

    if (!auth_token && route.name !== 'login') {
        return redirect('/login');
    }

    if (auth_token && !store.state.auth.loggedInUser.id) {
        store.dispatch('auth/fetchLoggedInUser', auth_token)
            .then(res => {
                store.commit('auth/setLoggedInUser', res);
            });
    }
}