<template>
    <div>
        <header>
            <h1>The Flex Pendu Game</h1>
            <nav>
                <ul>
                    <li><router-link to="/" exact>Acceuil</router-link></li>
                    <li><router-link to="/highscore" exact>High Score</router-link></li>
                    <li><router-link to="/rules" exact> Rules</router-link> </li>
                    <li><router-link to="/game" exact>Game</router-link></li>
                </ul>
            </nav>
        </header>
    </div>
</template>



<script>

export default {

    data() {
        return {

        }
    }
}
</script>

<style scoped>
header {
    background-color: #333;
    color: #fff;
    padding: 5px;
    text-align: center;
    margin: 5px;

}

h1 {
    text-align: center;

}

nav {
    /* background-color: #333; */
    color: #fff;
    padding: 5px;
    display: flex;
    justify-content: center;
    margin: 5px;
    text-decoration: none;
    /* enlève le soulignement */
    outline: none;
    /* enlève le surlignage */
}

nav li {
    color: #fff;
    text-decoration: none;
    padding: 10px 20px;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 0 10px;
}

nav li:hover {
    background-color: #444;
    border-radius: 5px;
}
</style>