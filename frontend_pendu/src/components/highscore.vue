<template>
  <div>
    <div>
      <img :src="image_acceuil" width="400px" />
    </div>
    <div class="table-container">
      <table class="table-auto w-full">
        <thead>
          <tr>
            <th class="px-4 py-2">Pseudo</th>
            <th class="px-4 py-2">Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in users" :key="index">
            <td class="border px-4 py-2">{{ user.player_name }}</td>
            <td class="border px-4 py-2">{{ user.score }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { axiosIns as axios } from "../plugins/axios";
import imgHighscore from "@/assets/highscore.png";
export default {
  data() {
    return {
      image_acceuil: imgHighscore,
      users: [],
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

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 15px;
  border: 1px solid #ddd;
  background-color: black; /* Make all table cells black */
  color: white; /* Make text color white */
}

th {
  background-color: black; /* Make header cells black */
  color: white; /* Make header text color white */
}
</style>
