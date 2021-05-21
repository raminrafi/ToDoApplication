<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background: rgb(255, 255, 255);
  background-color: rgb(255, 255, 255);
  height:50%;
  margin-top: -9px;
  margin-left: -9px;
  padding:-5px;
  background-size:cover;
  object-fit: cover;
  opacity: 0.95;
}
body {
  background: rgb(255, 255, 255);
}
</style>
