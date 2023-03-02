<script setup lang="ts">
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Fabis Mama</template>

    Fabis Mama ist übergewichtig aber geil. 
    <a href="https://cornhub.website/" target="_blank" rel="noopener">nudes</a>
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Gratis Sexting</template>

    Chat jetzt auf 
    <a href="https://pointerpointer.com/" target="_blank" rel="noopener">suseLive</a>!
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading>Danke Fabi für alles</template>
  </WelcomeItem>
</template>
