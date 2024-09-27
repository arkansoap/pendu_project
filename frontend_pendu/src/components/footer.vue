<template>
  <div>
    <footer>
      <div id="findme">
        <p>Find Me!</p>
        <a href="https://facebook.com/yourusername">
          <img :src="icon_fb" alt="Facebook Icon" />
        </a>
        <a href="https://github.com/yourusername">
          <img :src="icon_gh" alt="Github Icon" />
        </a>
        <a href="https://twitter.com/yourusername">
          <img :src="icon_twitter" alt="Twitter Icon" />
        </a>
      </div>
      <div id="contactme">
        <p>Contact Me!</p>
        <a href="mailto:youremail@example.com">youremail@example.com</a>
      </div>
    </footer>
  </div>
</template>

<script>
import iconFb from "@/assets/icons8-facebook-48.png";
import iconGh from "@/assets/icons8-github-50.png";
import iconTw from "@/assets/icons8-twitter-circled-48.png";
export default {
  data() {
    return {
      icon_fb: iconFb,
      icon_gh: iconGh,
      icon_twitter: iconTw,
    };
  },
};
</script>

<style scoped>
footer {
  display: flex;
  text-decoration: none;
  /* enlève le soulignement */
  outline: none;
  /* enlève le surlignage */
}

div {
  background-color: #333;
  color: #fff;
  padding: 5px;
  text-align: center;
  margin: 5px;
}

#findme {
  flex: 1;
}

#contactme {
  flex: 1;
}
</style>
