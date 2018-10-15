<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="8">
          <b-card-group>
            <b-card no-body class="p-4">
              <b-card-body>
                <h1>Login</h1>

                <p class="text-muted">Sign In to your account</p>

                <b-input-group class="mb-3">
                  <b-input-group-prepend><b-input-group-text><i class="icon-user"></i></b-input-group-text></b-input-group-prepend>
                  <input type="text" class="form-control" placeholder="Username" v-model="form.username">
                </b-input-group>

                <b-input-group class="mb-4">
                  <b-input-group-prepend><b-input-group-text><i class="icon-lock"></i></b-input-group-text></b-input-group-prepend>
                  <input type="password" class="form-control" placeholder="Password" v-model="form.password">
                </b-input-group>

                <b-row>
                  <b-col cols="6">
                    <b-button variant="primary" class="px-4" @click="login">Login</b-button>
                  </b-col>

                  <b-col cols="6" class="text-right">
                    <b-button variant="link" class="px-0">Forgot password?</b-button>
                  </b-col>
                </b-row>
              </b-card-body>
            </b-card>

            <b-card no-body class="text-white bg-primary py-5 d-md-down-none" style="width:44%">
              <b-card-body class="text-center">
                <div>
                  <h2>Sign up</h2>
                  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
                  <b-button variant="primary" class="active mt-3" @click="$router.push('/register')">Register Now!</b-button>
                </div>
              </b-card-body>
            </b-card>
          </b-card-group>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
const Cookie = process.client ? require('js-cookie') : undefined;

export default {
    name: 'Login',
    layout: 'clean',
    // middleware: 'notAuthenticated',

    data() {
        return {
            form: {
                username: '',
                password: '',
            },
        };
    },

    created() {
        //
    },

    methods: {
        login() {
            return this.$axios.post('/login', this.form)
                .then(res => {
                    console.log('response', res);
                    // Cookie.set('auth', res);
                    this.$router.push('/');
                });
        },
        // async login() {
        //     try {
        //         this.$toast.show('Logging in...', { icon: "fingerprint" });
                
        //         await this.$auth.loginWith('local', {
        //             data: {
        //                 "username": this.form.username,
        //                 "password": this.form.password
        //             }
        //         }).catch(e => {
        //             this.$toast.error('Failed logging in', { icon: "error_outline" });
        //         });
                
        //         if (this.$auth.loggedIn) {
        //             this.$toast.success('Successfully logged in', { icon: "done" });
        //         }
        //     } catch (e) {        
        //         this.$toast.error('Wrong username or password', { icon: "error" });
        //     }
        // },

        check(){
            console.log(this.$auth.loggedIn)
        },

        logout() {
            // this.$toast.show('Logging out...', {icon: "fingerprint"});
            // this.$auth.logout()
        },
    },
};
</script>
