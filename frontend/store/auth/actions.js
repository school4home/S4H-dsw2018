import Cookie from 'js-cookie';

export default {
    register({dispatch}, form) {
        return new Promise((resolve, reject) => {
            this.$axios
                .$post('/auth/register', form)
                .then(res => resolve(res.data))
                .catch(err => reject(err));
        });


        return data;
    },

    login({ dispatch, commit }, user) {
        return new Promise((resolve, reject) => {
            this.$axios
                .$post('/auth/login', user)
                .then(res => {
                    Cookie.set('auth', res.access_token, { expires: 7 });

                    dispatch('authenticate');
                    commit('setLoggedInUser', res.user);

                    return resolve(res.user);
                })
                .catch(err => reject(err));
        });
    },

    authenticate({ commit }) {
        let token = Cookie.get('auth');

        commit('setAuth', token);
        this.$axios.setToken(token, 'Bearer');
    },

    fetchLoggedInUser({}, auth_token) {
        this.$axios.setToken(auth_token, 'Bearer');

        return new Promise((resolve, reject) => {
            this.$axios
                .$get('/auth/user')
                .then(res => resolve(res))
                .catch(err => reject(err));
        });
    },

    async logout({ commit }) {
        let { data } = await this.$axios.get('/auth/logout');

        return data;
    }
};
