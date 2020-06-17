<template>
<div>
    <!-- The Modal -->
    <div id="myModal" class="modal">

    <!-- Modal content -->
    <div class="modal-content">
        <div class="form">
            <label for="password" style="padding-right: 10px;">Password</label>
            <input v-model="password" type="password" class="input" /> 
            <button class="btn" :submit="authenticate()">Authenticate</button>
        </div>
    </div>

    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            password: null
        };
    },
    methods: {
        authenticate(isAdd) {
            let lastPath = this.$store.getters.getLastPath
            if (this.password == "suman123456789") {
                this.$store.dispatch("authSuccess");
                if (lastPath == "Add") {
                    this.$router.push("/add");  
                } else {
                    this.$router.push("/upload");
                }
            } else {
                this.$store.dispatch("authFailure");
            }
        }
    }
}
</script>

<style>
/* The Modal (background) */
.modal {
  display: block; 
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
  text-align: center;
}

/* Modal Content/Box */
.modal-content {
  background-color: #fefefe;
  color: black;
  margin: 15% auto; /* 15% from the top and centered */
  padding: 20px;
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}

.input {
    margin-right: 10px;
}
</style>