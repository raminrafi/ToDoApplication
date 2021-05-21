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
          <router-link to="/">
            <div class="btn1">
                Logout
            </div>
          </router-link>
        </v-btn>
      </div>
    <div class="Description">
      Welcome to your to do list!
      <div id="id02" class="modal">
        <form class="modal-content animate" @submit.prevent="func">
            <div class="imgcontainer">
            <span onclick="document.getElementById('id02').style.display='none'" class="close" title="Close Modal">&times;</span>
            </div>
            <div class="container1">
            <h2>New Task</h2>
            <label for="title"><b>Task Title</b></label>
            <input type="text" placeholder="Enter Task Title" name="title" required>
            <label for="priority"><b>Priority</b></label>
            <label class="container">High
            <input type="radio" checked="checked" name="radio" v-model="picked">
            <span class="checkmark"></span>
            </label>
            <label class="container">Medium
            <input type="radio" name="radio" v-model="picked">
            <span class="checkmark"></span>
            </label>
            <label class="container">Low
            <input type="radio" name="radio" v-model="picked">
            <span class="checkmark"></span>
            </label>
            <label for="label"><b>Labels</b></label>
            <input type="text" placeholder="Enter Labels" name="label">
            <button type="submit" >Create Task</button>
            </div>
        </form>
      </div>
      </div>
      <button class= "btn" onclick="document.getElementById('id02').style.display='block'">Create New Task</button>
      <div class="containerr">
        <ul>
          <li>
            Laundry - High<span>x</span>
          </li>
          <li>
            Reading - High<span>x</span>
          </li>
          <li>
            Cycling - Low<span>x</span>
          </li>
        </ul>

      </div>
</div>

</template>

<script>
export default {
  name: 'Main',
  data () {
    return {


    }
  },
  methods:{
    /*This function takes user input and add it to the list of tasks on the page*/
    func(){
    const inputTextTitle=document.querySelector('#title');
    const myButton=document.querySelector('btn-list');
    const list=document.querySelector('.containerr ul');
    myButton.addEventListener('click',(e)=>{
        if(inputTextTitle.value!="")
        {
            e.preventDefault();
            const myLi = document.createElement('li');
            myLi.innerHTML=inputTextTitle.value;
            list.appendChild(myLi);

            const mySpan=document.createElement('span');
            mySpan.innerHTML='x';
            myLi.appendChild(mySpan);
        }
        const close=document.querySelectorAll('span');
        for(let i=0; i<close.length;i++)
        {
          close[i].addEventListener('click',()=>{
            close[i].parentElement.style.display="none";
          })
        }
    });
    }
  }
}
/*Close modal when close button is clicked*/
var modal2 = document.getElementById('id02');
window.onclick = function(event) {
    if (event.target == modal2) {
        modal.style.display = "none";
    }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
a {
  color: #ffffff;
}
/*Style sheet for background*/
.Description
{
  justify-content:center;
  text-align: center;
  color:rgb(0, 0, 0);
  font-size: 24px;
  position: absolute;
  top:80px;
  width: fit-content;
  padding-left: 20px;
  padding-top:20px;
  padding-bottom:20px;
  left:350px;
  align-content: center;
}
.container{
  margin-top: 50px;
}
/*Style sheet for lists*/
ul{
  list-style: none;
  width:500px;
  color: black;
}
ul li{
  width:100%;
  background: rgb(248, 248, 248);
  height: 40px;
  line-height: 40px;
  padding: 0 5px;
  position: relative;
  cursor:pointer;
  display:block;
  margin:5px 0;
  margin-left: 325px;
  text-align: left;
  padding-left: 20px;
}

ul li span{
  position: absolute;
  top:0;
  right: 0;
  width:50px;
  text-align: center;
  background: crimson;
}
/*Style sheet for header*/
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
/* Style sheet for Buttons*/
button {
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  display:flex;
  justify-content: center;
  font-size: 20px;
  background:  rgb(45, 202, 176);
  cursor: pointer;
  padding:10px;
  margin-top: 36px;
  margin-bottom: 7px;
  margin-left:450px;
  text-align: center;
}
.btn{
margin-left: 700px;
margin-right: 350px;
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
button:hover {
  filter:drop-shadow(0px 0px 7px rgb(188, 238, 235))
}
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}
.container1 {
  padding:30px 20px;
}
/* The Modal (background) */
.modal {
  display: none;
  position: fixed;
  z-index: 1;
  padding-top: 100px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}
.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}
/* The Close Button */
.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
</style>
