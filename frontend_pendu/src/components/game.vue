<template>
    <div>
        <div v-if="pendu && !pendu.endgame">
            <div id="ToGuess">
                <p>Mot à deviner</p>
                <p> {{ pendu.etat }} </p>
            </div>
            <div id="middleContainer">
                <div id="inputGame">
                    <div>
                        <input v-model="letter_proposed" />
                        <button v-on:click="pendu.checkLettre(letter_proposed)">valider lettre</button>
                        <h4> Informations </h4>
                        <p>{{ pendu.message }}</p>
                    </div>
                </div>
                <div id="paramsGame">
                    <button @click="reloadPage">New Game</button>
                    <div>
                        <select v-model="selectedValue"> Item 1
                            <option disabled value="">Please select one</option>
                            <option>easy</option>
                            <option>medium</option>
                            <option>hard</option>
                        </select>
                        <button @click="submitDiff">Envoyer</button>
                    </div>
                    <div>
                        <p>Level: {{ this.pendu.mot.params.diff.data.params }}</p>
                    </div>
                </div>
            </div>
            <div id="nbErreurs">
                <p> Nombre d'erreurs: {{ pendu.nbErreur }}</p>
                <img :src="image_pendu[pendu.nbErreur]" />
            </div>
        </div>
        <div v-if="pendu && pendu.endgame">
            <div v-if="pendu.loose">
                <h1> You Loose !!</h1>
                <h3> Le mot était: {{ pendu.mot.motStr }}</h3>
                <img :src=image_loose />
            </div>
            <div v-if="!pendu.loose">
                <h1> You Win !!</h1>
                <h3> Le mot était: {{ pendu.mot.motStr }}</h3>
                <img :src=image_win />
            </div>
            <ul>
                <li v-for="def in definition">{{ def }}</li>
            </ul>
            <div>
                Un nom pour la postérité: <input v-model="player_pseudo" />
            </div>
        </div>

    </div>
</template>

<script>
import axios from '../plugins/axios';
import { Pendu } from '../class/pendu';
import 'regenerator-runtime/runtime';

export default {

    data() {
        return {
            selectedValue: "",
            pendu: null,
            letter_proposed: "",
            image_pendu: [
                "../src/assets/pendu1.jpg",
                "../src/assets/pendu2.jpg",
                "../src/assets/pendu3.jpg"
            ],
            image_loose: "../src/assets/penduEnd.jpg",
            image_win: "../src/assets/penduWin.jpg",
            definition: null,
            player_pseudo: ""
        }
    },
    methods: {
        reloadPage() {
            window.location.reload();
        },
        submitDiff() {
            const data = { value: this.selectedValue }
            axios.put('/submit', null, { params: { value: JSON.stringify(this.selectedValue) } }
            );
        }
    },
    async created() {
        // const params = new params() ## params à rentrer ds l objet pendu ## pris en compte qd on fait newgame... ?
        // params à une valeur par défaut. On peu la changer pr la partie suivante 
        // parames est donné au cinstructeur Pendu pour déterminer certaines valeur : nb d'essai, choix mot, ...
        const pendu = await new Pendu();
        this.pendu = pendu;
        const definition = await axios.get(`definitions?mot=${pendu.mot.motStr}`);
        this.definition = definition.data;
        console.log(this.definition)
    }

}

</script>

<style scoped>
div {
    background-color: #333;
    color: #fff;
    padding: 5px;
    text-align: center;
    margin: 5px;
}

#ToGuess {

    border-width: 4px;
    border-style: double;
    border-color: white;
    padding: 5px;
    font-size: x-large;
}

ul {
    list-style-type: none;
    /* remove the bullet point */
}

#middleContainer {
    display: flex;
}

#inputGame {
    flex: 2;
    border-width: 4px;
    border-style: double;
    border-color: white;
    margin-right: 5px;
    /* takes up 1/2 of the container's width */
}

#paramsGame {
    flex: 1;
    border-width: 4px;
    border-style: double;
    border-color: white;
    margin-left: 5px;
    padding: 10px;
    /* takes up 1/2 of the container's width */
}
</style>