import Vue from 'vue'
import Router from 'vue-router'
import Upload from '../src/Upload.vue'

Vue.use(Router)

export default new Router ({
    routes: [
        {
            path: '/',
            name: 'Main'
        },
        {
            path: '/upload',
            name: 'Upload',
            component: Upload
        }
    ]
})