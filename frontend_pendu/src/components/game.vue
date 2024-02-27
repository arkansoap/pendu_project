<template>
  <div>
    <div v-if="pendu && !pendu.endgame">
      <div id="ToGuess">
        <p>Mot à deviner</p>
        <p>{{ pendu.etat }}</p>
      </div>
      <div id="middleContainer">
        <div id="inputGame">
          <div>
            <input v-model="letter_proposed" />
            <button v-on:click="pendu.checkLettre(letter_proposed)">
              valider lettre
            </button>
            <h4>Informations</h4>
            <p>{{ pendu.message }}</p>
          </div>
        </div>
        <div id="paramsGame">
          <button @click="reloadPage">New Game</button>
          <div>
            <select v-model="selectedValue">
              Item 1
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
        <p>Nombre d'erreurs: {{ pendu.nbErreur }}</p>
        <img :src="image_pendu[pendu.nbErreur]" />
      </div>
    </div>
    <div v-if="pendu && pendu.endgame">
      <div v-if="pendu.loose">
        <h1>You Loose !!</h1>
        <h3>Le mot était: {{ pendu.mot.motStr }}</h3>
        <img :src="image_loose" />
      </div>
      <div v-if="!pendu.loose">
        <h1>You Win !!</h1>
        <h3>Le mot était: {{ pendu.mot.motStr }}</h3>
        <img :src="image_win" />
      </div>
      <div>
        <div>Ton score: {{ pendu.score }}</div>
        <div>
          Un nom pour la postérité: <input v-model="player_pseudo" />
          <button @click="saveScore">save it</button>
        </div>
      </div>
      <div>
        <h3>Définition</h3>
        <ul>
          <li v-for="(def, index) in definition" :key="index">{{ def }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { axiosIns as axios } from "../plugins/axios";
import { Pendu } from "../class/pendu";
import "regenerator-runtime/runtime";
import pendu1 from "@/assets/pendu1.jpg";
import pendu2 from "@/assets/pendu2.jpg";
import pendu3 from "@/assets/pendu3.jpg";
import penduEnd from "@/assets/penduEnd.jpg";
import penduWin from "@/assets/penduWin.jpg";

export default {
  data() {
    return {
      selectedValue: "",
      pendu: null,
      letter_proposed: "",
      image_pendu: [pendu1, pendu2, pendu3],
      image_loose: penduEnd,
      image_win: penduWin,
      definition: null,
      player_pseudo: "",
    };
  },
  methods: {
    reloadPage() {
      window.location.reload();
    },
    submitDiff() {
      axios.put("/submit", null, {
        params: { value: JSON.stringify(this.selectedValue) },
      });
    },
    saveScore() {
      axios.put("/savescore", {
        value: this.pendu.score,
        name: this.player_pseudo,
      });
    },
  },
  async created() {
    const pendu = await new Pendu();
    this.pendu = pendu;
    const definition = await axios.get(`definitions/?mot=${pendu.mot.motStr}`);
    this.definition = definition.data;
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
