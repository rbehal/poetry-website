import Vue from 'vue'
import Router from 'vue-router'
import Upload from '../src/Upload.vue'
import Add from '../src/Add.vue'

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
        },
        {
            path: '/add',
            name: 'Add',
            component: Add
        }
    ]
})