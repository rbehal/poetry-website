import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex); 

const Store = new Vuex.Store({
    plugins: [createPersistedState({ storage: window.sessionStorage })],
    state: {
        isCorrectPassword: false,
        lastPath: ""
    },
    getters: {
        getIsCorrectPassword(state) {
            return state.isCorrectPassword;
        },
        getLastPath(state) {
            return state.lastPath; 
        }
    },
    mutations: {
        auth_success(state) {
            state.isCorrectPassword = true; 
        },
        auth_failure(state) {
            state.isCorrectPassword = false;
        },
        last_path(state, path) {
            state.lastPath = path; 
        }
    },
    actions: {
        authSuccess({ commit }) {
            commit("auth_success");
        },
        authFailure({ commit }) {
            commit("auth_failure");
        },
        lastPath({ commit }, path) {
            commit("last_path", path);
        }
    }
});

export default Store; 