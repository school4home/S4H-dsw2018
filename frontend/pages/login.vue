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
                  <input type="text" class="form-control" placeholder="Email" v-model="form.email">
                </b-input-group>
                <b-input-group class="mb-4">
                  <b-input-group-prepend><b-input-group-text><i class="icon-lock"></i></b-input-group-text></b-input-group-prepend>
                  <input type="password" class="form-control" placeholder="Password" v-model="form.password">
                </b-input-group>

                <b-row>
                  <b-col cols="6">
                    <b-button variant="primary" class="px-4" @click="login" :disabled=!disableLogin>Login</b-button>
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
                  <p>Create your own account to enjoy all the benefits from School4Home!</p>
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
import { mapActions } from 'vuex';

export default {
    layout: 'clean',

    data() {
        return {
            form: {
                email: '',
                password: '',
            },
        };
    },

    computed: {
        disableLogin() {
            return !!this.form.email && !!this.form.password;
        },
    },

    methods: {
        ...mapActions({
            loginUser: 'auth/login',
        }),

        login() {
            this.loginUser(this.form).then(res => {
                this.$router.push('/');
            });
        },
    },
};
</script>
