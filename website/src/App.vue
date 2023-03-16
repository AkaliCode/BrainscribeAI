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
        <a>signed in as: {{ profilename }}</a>
        <!-- profilname aus einer Datenbank bzw Variable -->
        <a href="#">Your Profile</a>
        <a href="#">Lorem ipsum</a>
        <a href="#" @click="showButton('login_button')">Loggout</a>
        <!-- Loggout Button mit function Loggout -->
      </div>
    </div>
  </div>
</template>

<style>
/* 
Hintergrundfarbe für die Webseite
*/
body {
  background-color: #0f0f0f;
}

/*
Dropdwon klasse als inline-block
*/
.dropdown {
  display: inline-block;
}

/*
Dropdownmenü hidden setzen sowie position, sichtbarkeit und größe
*/
.dropdown-content {
  display: none;
  position: absolute;
  right: 0px;
  top: 69px;
  float: right;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

/*
Dropdown links anpassen
*/
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/*
Wenn ein link vom Dropdown gehover wird ändert sich die Farbe
*/
.dropdown-content a:hover {
  background-color: #ddd;
}

/*
Wenn man über das Icon hovered wird das Dropdownmenü angezeigt
*/
.dropdown:hover .dropdown-content {
  display: block;
}

/*
Klasse hidden macht etwas unsichtbar und nicht mehr interagierbar
*/
.hidden {
  display: none;
  pointer-events: none;
}

/*
Der login button rechts oben in der navbar
*/
button.navbar_login {
  background-color: white;
  color: black;
  float: right;
  border-radius: 15%;
  padding: 10px 30px;
  text-align: center;
  text-decoration: none;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

/*
Das Logo Links oben in der Navbar
*/
h2.brainscribe_logo {
  margin-top: 25px;
  margin-left: 25px;
  font-size: 35px;
  text-align: left;
  float: left;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

/*
Amount von den verfügbaren Tokens Rechts oben wenn Loggedin
*/
.tokenProfile h2 {
  position: absolute;
  padding-top: 0px;
  margin: 0px;
  right: 80px;
  top: 30px;
  font-size: 20px;
  text-align: right;
  float: right;
  font-family: Avenir, Helvetica, Arial, sans-serif;
}

/*
Profile icon rechts oben in Navbar
*/
.tokenProfile img {
  position: absolute;
  padding-top: 0px;
  margin: 0px;
  right: 25px;
  top: 20px;
  float: right;
  width: 50px;
}

/*
Grund werte für die schrift der webseite
*/
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}

/*
Die Navbar
*/
nav {
  padding: 25px;
  margin-left: 20%;
  position: relative;
  left: 5px;
  font-size: 30px;
  text-align: left;
}

/*
Navbar links
*/
nav a {
  font-weight: bold;
  color: #ffffff;
  text-decoration: none;
  margin-left: 20px;
}

/*
Die aktuelle Unterseite hervorheben
*/
nav a.router-link-exact-active {
  color: #ffffff;
  text-decoration-line: underline;
  text-decoration-thickness: 3px;
}
</style>

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
