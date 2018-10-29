<template>
    <div class="app">
        <AppHeader/>

        <div class="app-body">
            <Sidebar :navItems="nav"/>
            <main class="main">
                <breadcrumb :list="list"/>
                <div class="container-fluid">
                    <nuxt />
                </div>
            </main>
            <AppAside/>
        </div>

        <AppFooter/>
    </div>
</template>

<script>
import { mapActions } from 'vuex';

import nav from './menu'
import { Header as AppHeader, Sidebar, Aside as AppAside, Footer as AppFooter, Breadcrumb } from '~/components/'

export default {
    components: {
        AppHeader,
        Sidebar,
        AppAside,
        AppFooter,
        Breadcrumb,
    },

    data() {
        return {
            nav: nav.items,
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
