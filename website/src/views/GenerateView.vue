<template>
  <div class="generate">
    <h1>Generate</h1>
  </div>
  <label for="inputField">Input Field:</label>
    <form @submit.prevent="">
      <input type="text" id="inputField" v-model="message" />
      <button type="submit" @click="">Submit</button>
    </form>
</template>

<script lang="ts">
  import { defineComponent } from 'vue';

  export default defineComponent({
    data(){
      return{
        message: "" as string
      }
      methods: {

    }},
    created(){

    }
  });
</script>