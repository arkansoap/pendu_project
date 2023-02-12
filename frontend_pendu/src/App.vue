<template>
  <div>
    <app-header></app-header>
    <router-view></router-view>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from './components/header.vue'
import Footer from './components/footer.vue'
export default {

  data() {
    return {

    }
  },
  components: {
    'app-header': Header,
    'app-footer': Footer,
  }
}
</script>

<style>

</style>
