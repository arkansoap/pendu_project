<template>
  <div>
    <div>
      <img :src="image_acceuil" width="400px" />
      <!-- <h1> High Score Board</h1> -->
    </div>
    <div class="table-container">
      <!-- <v-data-table
        :headers="headers"
        :items="users"
        :search="search"
        hide-default-footer
        class="v-data-table"
      ></v-data-table> -->
    </div>
  </div>
</template>

<script>
import axios from "../plugins/axios";
import imgHighscore from "@/assets/highscore.png";
export default {
  data() {
    return {
      image_acceuil: imgHighscore,
      headers: [
        { text: "pseudo", value: "player_name" },
        { text: "Score", value: "score" },
      ],
      users: [],
      search: "",
    };
  },
  methods: {
    async getScore() {
      const { data } = await axios.get("/highscore");
      console.log(data.users);
      this.users = data.users;
    },
  },
  created() {
    this.getScore();
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

.table-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px auto;
  padding: 10px;
  border: 1px solid white;
  border-radius: 5px;
}
</style>
