import Vue from 'vue'
import Router from 'vue-router'
import store from '../src/store/index'
import Upload from '../src/Upload.vue'
import Add from '../src/Add.vue'
import Authenticate from '../src/Authenticate.vue'

Vue.use(Router)


const router = new Router({
    routes: [
        {
            path: '/',
            name: 'Main'
        },
        {
            path: '/authenticate',
            name: 'Authenticate',
            component: Authenticate,
        },
        {
            path: '/upload',
            name: 'Upload',
            component: Upload,
            beforeEnter: (to, from, next) => {
                store.dispatch("lastPath", to.name);
                if (store.getters.getIsCorrectPassword) {
                    next();
                } else {
                    next({
                        path: "/authenticate"
                    });
                }
            }
        },
        {
            path: '/add',
            name: 'Add',
            component: Add,
            beforeEnter: (to, from, next) => {
                store.dispatch("lastPath", to.name);
                if (store.getters.getIsCorrectPassword) {
                    next();
                } else {
                    next({
                        path: "/authenticate"
                    });
                }
            }
        }
    ]
});

export default router;