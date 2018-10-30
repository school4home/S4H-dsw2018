<template>
  <div class="app flex-row align-items-center">
    <div class="container">
      <b-row class="justify-content-center">
        <b-col md="6" sm="8">
          <b-card no-body class="mx-4">
            <b-card-body class="p-4">
              <h1>Register</h1>
              <p class="text-muted">Create your account</p>
              <b-input-group class="mb-3">
                <b-input-group-prepend>
                  <b-input-group-text><i class="icon-user"></i></b-input-group-text>
                </b-input-group-prepend>
                <input type="text" class="form-control" placeholder="Name" v-model="form.name">
              </b-input-group>

              <b-input-group class="mb-3">
                <b-input-group-prepend>
                  <b-input-group-text>@</b-input-group-text>
                </b-input-group-prepend>
                <input type="email" class="form-control" placeholder="Email" v-model="form.email">
              </b-input-group>

              <b-input-group class="mb-3">
                <b-input-group-prepend>
                  <b-input-group-text><i class="icon-lock"></i></b-input-group-text>
                </b-input-group-prepend>
                <input type="password" class="form-control" placeholder="Password" v-model="form.password">
              </b-input-group>

              <b-input-group class="mb-4">
                <b-input-group-prepend>
                  <b-input-group-text><i class="icon-lock"></i></b-input-group-text>
                </b-input-group-prepend>
                <input type="password" class="form-control" :class="confirmed ? '' : 'is-invalid'" placeholder="Confirm password" v-model="form.password_confirmation">
                <div class="invalid-feedback">
                    Password confirmation doesn't match.
                </div>
              </b-input-group>

              <b-button variant="success" block @click="register" :disabled="emptyFields">Create Account</b-button>
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex';

export default {
    name: 'Register',
    layout: 'clean',

    data() {
        return {
            form: {
                name: '',
                email: '',
                password: '',
                password_confirmation: '',
            },
        };
    },

    computed: {
        confirmed() {
            return this.form.password_confirmation === this.form.password ? true : false;
        },

        emptyFields() {
            if (!this.form.name || !this.form.email || !this.form.password || !this.confirmed) {
                return true;
            }

            return false;
        }
    },

    methods: {
        ...mapActions({
            registerUser: 'auth/register',
            loginUser: 'auth/login',
        }),

        register() {
            this.registerUser(this.form).then((user) => {
                this.loginUser({email: user.email, password: this.form.password}).then(() => {
                    this.$router.push('/');
                });
            });
        },
    },
}
</script>
