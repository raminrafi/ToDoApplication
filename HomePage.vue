<template>
    <div>
        <h1>Hi {{account.user.firstName}}!</h1>
        <p>Welcome to your To Do Application</p>
        <button class="btn btn-primary" onclick="document.getElementById('id02').style.display='block'">Create New Task</button>
        <router-link to="/login"><button class="btn btn-primary">Logout</button></router-link>
        <ul>
        </ul>
        <div class="Description">
        <div id="id02" class="modal">
        <form class="modal-content animate" @submit.prevent="handleSubmit">
            <div class="imgcontainer">
            <span onclick="document.getElementById('id02').style.display='none'" class="close" title="Close Modal">&times;</span>
            </div>
            <div class="container1">
            <h2>New Task</h2>
            <div class="form-group">
              <label for="enter">Title</label>
              <input type="text" v-model="title" id="enter" v-validate="'required'" class="form-control" :class="{ 'is-invalid': submitted && errors.has('title') }" />
              <div v-if="submitted && errors.has('title')" class="invalid-feedback">{{ errors.first('title') }}</div>
            </div>
            <div class="form-group">
              <label for="enter1">Label</label>
              <input type="text" v-model="label" id="enter1" v-validate="'required'" class="form-control" :class="{ 'is-invalid': submitted && errors.has('label') }" />
              <div v-if="submitted && errors.has('label')" class="invalid-feedback">{{ errors.first('label') }}</div>
            </div>
            <div class="form-group">
              <label for="picked">Priority (High/Medium/Low)</label>
              <input type="text" v-model="picked" id="picked" v-validate="'required'" class="form-control" :class="{ 'is-invalid': submitted && errors.has('picked') }" />
              <div v-if="submitted && errors.has('picked')" class="invalid-feedback">{{ errors.first('picked') }}</div>
                <button class="btn btn-primary" v-on:click="addItem">Create Task</button>
                </div>
                </div>
        </form>

      </div>
      </div>
    </div>


</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    data(){
        return{
           task:{
            title:[],
            label:[],
            priority:[]
           },
           title:'',
           label:'',
           picked:'',
           submitted: false
        }
    },
    computed: {
        ...mapState({
            account: state => state.account,
            users: state => state.users.all,
            tasks: state =>state.tasks.all
        })
    },
    created () {
        this.getAllUsers();
        this.getAllTasks();
    },
    methods: {
        ...mapActions('account', ['createTask']),
        ...mapActions('tasks',{
            getAllTasks:'getAllTask',
            deleteTask:'deleteTask'
        }),
        handleSubmit(e) {
            var modal = document.getElementById('id02');
            this.submitted = true;
            this.createTask(this.task);
            modal.style.display = "none";
        },
        addItem: function()
        {
            var input = document.getElementById('enter');
            var input1 = document.getElementById('enter1');
            var input2=document.getElementById('picked');
            var list=document.querySelector('ul');
            if(input.value !== '')
            {
              const myLi = document.createElement('li');
              myLi.innerHTML=input.value + ' - '+input1.value+' - '+input2.value;
              list.appendChild(myLi);
              this.task.title.push(input.value);
              this.task.label.push(input1.value);
              this.task.priority.push(input2.value);
              localStorage.setItem("title",input.value);
              localStorage.setItem("label",input1.value)

              const mySpan=document.createElement('span');
              mySpan.innerText=" => Delete Task";
              myLi.appendChild(mySpan);

              const mySpan1=document.createElement('button');
              mySpan1.innerText=" Update Task ";
              myLi.appendChild(mySpan1);

              mySpan1.addEventListener('click',()=>{
                document.getElementById('id02').style.display='block';
              })

              const closee=document.querySelectorAll('span');
              for(let i=0; i<closee.length;i++)
              {
                closee[i].addEventListener('click',()=>{
                  closee[i].parentElement.style.display="none";
                })
              }
            }
        },
        deleteItem()
        {
          const closee=document.querySelectorAll('span');
            for(let i=0; i<closee.length;i++)
            {
              closee[i].addEventListener('click',()=>{
                closee[i].parentElement.style.display="none";
              })
            }
        }

    }
};


</script>

<style scoped>
/* The Modal (background) */
a{
    color:white;
}
h2{
    margin-bottom:16px;
    font:100;
}
label{
    text-align: left;
    font: 100;
    font-weight: bold;
}
ul{
  list-style: none;
  width:500px;
  color: black;
  background: rgb(248, 248, 248);
  margin:5px 0;
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
  text-align: left;
  padding-left: 20px;
  margin-left: -50px;
}
ul li span{
  position: absolute;
  top:0;
  right: 0;
  width:50px;
  text-align: center;
  background: rgb(245, 182, 182);
}
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
.Description
{
  justify-content:center;
  text-align: left;
  color:rgb(0, 0, 0);
  font-size: 14px;
  position: absolute;
  width: fit-content;
  align-content: center;
}
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
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

/* Style sheet for Buttons*/
button:hover {
  filter:drop-shadow(0px 0px 7px rgb(188, 238, 235))
}
</style>


