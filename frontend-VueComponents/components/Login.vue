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
        <v-btn class="button2">
           <router-link to="/Signup">
            <div class="btn1">
              SignUp
            </div>
          </router-link>
        </v-btn>
    </div>
    /* Login Form */
     <form @submit.prevent="submitForm" method="post">
        <div class="container">
            <h2>Login</h2>
            <p>New User? <a><router-link to="/Signup">Create an account</router-link></a></p>
            <label for="username"><b>Username</b></label>
            <input type="text" placeholder="Enter Username" v-model="username" required>

            <label for="password"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" v-model="password" required>
            <router-link  to="/Main">
            <button type="submit">Login</button>
            </router-link>
        </div>
        </form>

  </div>

</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      //input fields
      username:'',
      password:'',
      errors: []
    }
  },
  methods:{
    //function sending Django API request using axios
    submitForm(){
      this.errors=[]
      //if any of the field is empty display alert message stating that the required field is missing
      if(this.email==="")
      {
        this.errors.push('Email is missing');
        alert("Email is missing");
      }
      if(this.password==="")
      {
        this.errors.push('Password is missing');
        alert("Password is missing");
      }
      //if there is no error send a API request to Django server
      if(this.errors.length)
      {
        console.log(this.email)
        console.log(this.password)
        axios.post(`http://127.0.0.1:8000/api/login/`,
        {
          Email:this.email,
          Password:this.password,
        })
        .then(response=>{
        })
        .catch(error=>{
          if(error.response){
            for(const property in error.response.data){
              this.errors.push('${property}:${error.response.data[property]}')
            }
            console.log(JSON.stringify(error.response.data))
          }
          else if (error.message)
          {
            this.errors.push('Something went wrong. Please try again')
            console.log(JSON.stringify(error))
          }

        })
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
  color: #000000;
}
a {
  color: #ff0000af;
}
p{
    color: #000000;
}
label{
  display:flex;
  text-align:center;
  color: #000000;
  font-weight:normal;
}
/*Style sheets for header*/
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
button:hover {
  filter:drop-shadow(0px 0px 7px rgb(3, 107, 104))
}
/* Set a style for all buttons */
button {
  background-color: #04AA6D;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}
.btn1{
  font-size: 18px;
  color:rgb(255, 255, 255);
  cursor: pointer;
  padding: 10px;
  width:60px;
  text-align: center;
}
.button2
{
  color:white;
  background: rgba(255, 0, 0, 0.76);
  margin:10px;
  margin-top: 7px;
  margin-bottom: 7px;
  text-align: center;
  margin-left: 1000px
}
/* Style sheet for HTML forms */
input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}
form {
  border: 3px solid #f1f1f1;
  margin-left: 400px;
  margin-right: 400px;
  margin-top: 50px;
}
/* Add padding to containers */
.container {
  padding: 16px;
  align-content: center;
}
/* The "Forgot password" text */
span.psw {
  float: right;
  padding-top: 16px;
  color: black;
}
/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
    display: block;
    float: none;
  }
}
</style>
