<template>

  <!-- Das Input Field. mit dem doppelpunkt kann man den string danach statt string
       eine referenz auf eine variable geben. hier zB auf den savedLink. Ansonten 
       führt der button die SaveLink methode aus, welche den eingegebenen Wert local
       speichert.
   -->
  <div class="input">
    <label for="inputField">Input Field:</label>
    <form @submit.prevent="submit">
      <input type="text" id="inputField" :placeholder="savedlink" v-model="link" />
      <button type="submit" @click="saveLink">Submit</button>
    </form>
  </div>

  <!-- Das Output Div kann dann basically den Output als Klartext anzeigen
       Es gibt kein Output "FIELD" in dem Sinne man kann es dann hald noch stylen
       aber MVP ist das hier genug da der Wert der output ts variable dynamisch 
       angezeigt werden kann. Das macht man mit der Doppelten Klammer.
   -->
  <div class="output">
    <h3>OUTPUT:</h3>
    <p>{{ output }}</p>
  </div>
</template>

<script lang="ts">
  import { defineComponent } from 'vue';

  export default defineComponent({
    data(){
      return{
        link: "" as string,
        savedlink: "" as string,
        output: "    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." as string

      }
    },
    // Es wird onCreate der gesavte link gegetted damit er dann gesetzt 
    // und displayed werden kann
    created(): void {
        this.savedlink = localStorage.getItem("savedlink") || "";
    },
    methods: {
      submit() {
        //Nur nötig falls man mit dem router auf eine andere View pushen will
        // this.$router.push({ path: "/view", query: { message: this.link } });
      },
      // saved den eingegebenen link in den localStorage
      saveLink() {
        localStorage.setItem("savedlink", this.link);
        this.savedlink = this.link;
      },
    },
  });
</script>