 <! Landing Page -->
<template>
  <div class="hello">
    <div class="header">
        <div class="header-menu">
          <router-link to="/">
            <div class="header-text1">
              To Do Application
            </div>
            </router-link>
        </div>
        <v-btn class="button1">
          <router-link to="/Login">
            <div class="btn1">
              Login
            </div>
          </router-link>
        </v-btn>
        <v-btn class="button2">
           <router-link to="/Signup">
            <div class="btn1">
              SignUp
            </div>
          </router-link>
        </v-btn>
      </div>
      <div class="background">
        <img src="@/assets/welcome-right.png" alt="img" class="image-fit">
      </div>
      <div class="Description">
      Organize activities using our To Do Application
      <div class="st">
        <v-btn>
          <router-link to="/Login">
              Get Started
          </router-link>
        </v-btn>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* CSS styles for website styling */
h1, h2 {
  font-weight: normal;
}
a {
  color: #ffffff;
}
/*Background styling*/
.background{
  color: white;
  background: rgb(255, 255, 255);;
  align-content: right;
}
.image-fit{
  background-position:top;
  position:relative;
  color: white;
  align-content: right;
  margin-left:880px;
  margin-top: 50px;
  width:300px;
  height:600px;
  opacity: 0.95;
}
.Description
{
  justify-content:center;
  text-align: center;
  color:rgb(0, 0, 0);
  font-size: 30px;
  position: absolute;
  top:220px;
  left:300px;
  width: fit-content;
  margin-right: 600px;
  padding-left: 20px;
  padding-top:20px;
  padding-bottom:20px;
  align-content: center;
}
.st{
  font-size: 20px;
  background:  rgb(45, 202, 176);
  cursor: pointer;
  padding:10px;
  align-content: center;
  margin-top: 7px;
  margin-bottom: 7px;
  text-align: center;
}
/*Header styling*/
.header {
  display:flex;
  align-items: center;
  margin-top: 7px;
  margin-bottom: 7px;
  height: 60px;
  background-color: rgb(255, 255, 255);
}
.header-menu {
  flex: 0.5;
  text-align: left;
  display: flex;
  justify-content:left;
  align-items:flex-start;
  position: relative;
}
.header-text1{
  font-size: 20px;
  color:rgb(0, 0, 0);
  cursor: pointer;
  padding: 10px;
  width: fit-content;
  margin-left: 75px;
}

/* Add a hover effect for buttons */
v-btn:hover{
  filter:drop-shadow(0px 0px 7px rgb(3, 107, 104))
}
/*Button styling*/
.btn1{
  font-size: 18px;
  color:rgb(255, 255, 255);
  cursor: pointer;
  padding: 10px;
  width:60px;
  text-align: center;
}
/*Login button*/
.button1
{
  color:white;
  background:  rgba(15, 235, 125, 0.726);
  margin:10px;
  margin-top: 7px;
  margin-bottom: 7px;
  text-align: center;
  margin-left: 900px;
}
/*Signup button*/
.button2
{
  color:white;
  background: rgba(255, 0, 0, 0.76);
  margin:10px;
  margin-top: 7px;
  margin-bottom: 7px;
  text-align: center;
}
</style>
