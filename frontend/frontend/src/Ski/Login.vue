<template>
  <!-- <div class="row">
        <div class="col-md-6 offset-md-3"><form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
    <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <div class="form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form></div>
    </div> -->
  <div class="top-container">
    <div class="container">
      <p class="heading">Login !</p>
      <div class="login-container">
        <form>
          <label class="labels">Email</label>
          <div class="input-box">
            <input type="email" placeholder="Email" required v-model="email" />
          </div>
          <label class="labels">Password</label>
          <div class="input-box">
            <input
              type="password"
              placeholder="Password"
              required
              v-model="pwd"
            />
          </div>
          <button class="submit-btn" type="submit" v-on:click="tryUser()">
            Login
          </button>
        </form>
      </div>
    </div>
    <p>password : {{ pwd }}</p>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      email: "",
      pwd: "",
    };
  },
  methods: {
    async tryUser() {
      let result = await axios.post("\api", {
        type: "user",
        email: this.email,
        password: this.pwd,
      });
      console.warn(result);
      if (result.data.success) {

      this.$router.push('/login');
    } else {

      console.log("User doesnot exist or incorrect password");
    }
  } catch (error) {
    // Handle errors (e.g., network error)
    console.error('An error occurred:', error);
    },
  },
};
</script>
<style scoped>
.top-container {
  min-height: 100vh;
  min-width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
}
.heading {
  padding: 20px;
  font-size: 30px;
}
.container {
  min-height: 50vh;
  min-width: 20vw;
  background-color: aliceblue;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.login-container {
  display: flex;
  flex-direction: column;
}
.input-box {
  padding: 20px;
}
.labels {
  padding: 20px;
}
.input {
  min-height: 6vh;
}
.submit-btn {
  width: 10vw;
  height: 3vh;
  margin: 18px;
  border-radius: 10px;
}
</style>
