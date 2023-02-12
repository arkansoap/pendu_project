<template>
    <div>
        <footer>
            <div id="findme">
                <p>Find Me!</p>
                <a href="https://facebook.com/yourusername">
                    <img :src="icon_fb" alt="Facebook Icon">
                </a>
                <a href="https://github.com/yourusername">
                    <img :src="icon_gh" alt="Github Icon">
                </a>
                <a href="https://twitter.com/yourusername">
                    <img :src="icon_twitter" alt="Twitter Icon">
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

export default {

    data() {
        return {
            icon_fb: "../src/assets/icons8-facebook-48.png",
            icon_gh: "../src/assets/icons8-github-50.png",
            icon_twitter: "../src/assets/icons8-twitter-circled-48.png"
        }
    }
}
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
    flex: 1
}

#contactme {
    flex: 1
}
</style>