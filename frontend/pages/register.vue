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
                <input type="text" class="form-control" placeholder="Username" v-model="form.username">
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
                <input type="password" class="form-control" :class="confirmed ? '' : 'is-invalid'" placeholder="Repeat password" v-model="passwordConfirmation">
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
export default {
    name: 'Register',
    layout: 'clean',

    data() {
        return {
            form: {
                username: '',
                email: '',
                password: '',
            },
            passwordConfirmation: '',
        };
    },

    computed: {
        confirmed() {
            return this.passwordConfirmation === this.form.password ? true : false;
        },

        emptyFields() {
            if (!this.form.username || !this.form.email || !this.form.password || !this.confirmed) {
                return true;
            }

            return false;
        }
    },

    methods: {
        register() {
            return this.$axios.post('/users/sign-up', this.form)
                .then(res => {
                    console.log('response', res);
                    this.$router.replace('/login');
                });
        },
    },
}
</script>
