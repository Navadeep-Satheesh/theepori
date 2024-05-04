<template>

  <NavBar></NavBar>
  <router-view></router-view>
 
</template>

<script>

// import AllRooms from "./components/AllRooms.vue"
import NavBar from "./components/Navbar.vue"

export default {
  name: 'App',
  components: {

    // AllRooms : AllRooms,
    NavBar: NavBar
  }
}
</script>

<style>

*{
  padding: 0px;
  margin: 0px;
  font-family: sans-serif
}

</style>
