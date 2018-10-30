<template>
    <div class="app">
        <AppHeader/>

        <div class="app-body">
            <Sidebar :navItems="nav"/>
            <main class="main">
                <div class="container-fluid">
                    <nuxt />
                </div>
            </main>
        </div>

        <AppFooter/>
    </div>
</template>

<script>
import { mapActions } from 'vuex';

import menu from './menu'
import { Header as AppHeader, Sidebar, Footer as AppFooter } from '~/components/theme'

export default {
    components: {
        AppHeader,
        Sidebar,
        AppFooter,
    },

    data() {
        return {
            nav: menu,
        };
    },

    computed: {
        name() {
            return this.$route.name;
        },

        list() {
            return this.$route.matched;
        },
    },

    created() {
        this.authenticateUser();
    },

    methods: {
        ...mapActions({
            authenticateUser: 'auth/authenticate', 
        }),
    },
};
</script>
