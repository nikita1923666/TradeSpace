import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vuex from 'vuex';
import {store} from './store/store'
import firebase from 'firebase';

const firebaseConfig = {
    apiKey: "AIzaSyDXj-1A4-KiCMtxbqgkEh6uJnwdN2Bb-40",
    authDomain: "tradespace-22f37.firebaseapp.com",
    databaseURL: "https://tradespace-22f37.firebaseio.com",
    projectId: "tradespace-22f37",
    storageBucket: "tradespace-22f37.appspot.com",
    messagingSenderId: "944470248571",
    appId: "1:944470248571:web:3a41d49f600a204833a6de",
    measurementId: "G-L3ET2V5R9L"
};

firebase.initializeApp(firebaseConfig);

Vue.use(Vuex);
Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount('#app');
