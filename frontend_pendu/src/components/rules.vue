<template>
  <div>
    <h1>Rules of the game and Score system</h1>
    <img :src="image_acceuil" width="400px" />
  </div>
</template>

<script>
import imgRules from "@/assets/rules.png";
export default {
  data() {
    return {
      image_acceuil: imgRules,
    };
  },
};
</script>

<style scoped>
div {
  background-color: #333;
  color: #fff;
  padding: 5px;
  text-align: center;
  margin: 5px;
}
</style>
