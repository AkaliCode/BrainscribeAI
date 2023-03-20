<template>
  <!-- Das Logo links oben auf der Webseite in weiß mit blauem AI -->
  <h2 class="brainscribe_logo">
    <a href="/" style="text-decoration: none; color: white">
      BR<span style="color: #45a0f5">AI</span>NSCRIBE
    </a>
  </h2>
  <nav>
    <!-- Unsere Unterseiten in der Navbar -->
    <router-link to="/">Home</router-link>
    <router-link to="/about">About</router-link>
    <router-link to="/pricing">Pricing</router-link>
    <router-link to="/generate">Generate</router-link>
    <!-- Button für Login verschwindet wenn Logged in TODO umleitung auf Login-page, Login page erstellen-->
    <button
      id="login_button"
      @click="hideButton('login_button')"
      class="navbar_login"
      href="/login"
    >
      Login
    </button>
  </nav>
  <router-view />
  <!-- Amount der Verfügbaren Tokens aus einer variable (aus der Datenbank) rechts oben neben dem Profilicon sobald man eingelogged ist -->
  <div class="tokenProfile">
    <h2 id="tokens" class="hidden">
      <span style="color: #45a0f5">{{ tokens }}</span> Tokens
    </h2>
    <!--Icon und das dropdown-menü sobald man über das Profilicon hovered -->
    <div class="dropdown">
      <img
        id="iconProfile"
        class="hidden"
        src="../pictures/profileIcon.png"
        alt="profileIcon"
      />
      <div id="dropdown" class="dropdown-content">
        <a id="top_dropdown">signed in as: {{ profilename }}</a>
        <!-- profilname aus einer Datenbank bzw Variable -->
        <a href="#">Your Profile</a>
        <a href="#">Lorem ipsum</a>
        <a id="bottom_dropdown" href="#" @click="showButton('login_button')">Loggout</a>
        <!-- Loggout Button mit function Loggout -->
      </div>
    </div>
  </div>
</template>
<!-- Import des Stylesheets App.css -->
<style src="../css/App.css"></style>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      tokens: 4, //TODO die Verfügbaren Tokens aus der Datenbank auslesen hier als beispiel gesetzt
      profilename: "ConfusedTea", //TODO den Profilnamen aus der Datenbank auslesen hier als beispiel gesetzt
    };
  },
  created(): void {},
  //Methoden für die Webseite
  methods: {
    hideButton(buttonId: string): void {
      //wenn du eingelogged bist dann
      const button = document.getElementById(buttonId) as HTMLButtonElement; //Login Button hidden
      button.classList.add("hidden");
      const token = document.getElementById("tokens") as HTMLHeadingElement; //Verfügbare tokens sichtbar
      token.classList.remove("hidden");
      const icon = document.getElementById("iconProfile") as HTMLImageElement; //ProfilIcon sichtbar
      icon.classList.remove("hidden");
      const dropdown = document.getElementById("dropdown") as HTMLDivElement; //Dropdown falls hover sichtbar
      dropdown.classList.remove("hidden");
    },
    showButton(buttonId: string): void {
      //wenn du ausgelogged bist dann
      const button = document.getElementById(buttonId) as HTMLButtonElement; //Login Button Sichtbar
      button.classList.remove("hidden");
      const token = document.getElementById("tokens") as HTMLHeadingElement; //Verfügbare tokens hidden
      token.classList.add("hidden");
      const icon = document.getElementById("iconProfile") as HTMLImageElement; //ProfilIcon hidden
      icon.classList.add("hidden");
      const dropdown = document.getElementById("dropdown") as HTMLDivElement; //Dropdown hidden
      dropdown.classList.add("hidden");
    },
  },
});
</script>
