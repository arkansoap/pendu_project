<template>
    <div>
        <!-- <div>
            <h1> High Score Board</h1>
            <img :src="image_acceuil" width="400px" />
        </div> -->
        <div>
            <v-data-table :headers="headers" :items="users" :search="search"></v-data-table>
        </div>
    </div>
</template>
    



<script>
export default {

    data() {
        return {
            image_acceuil: "../src/assets/highscore.png",
            headers: [
                { text: 'Name', value: 'name' },
                { text: 'Email', value: 'email' },
            ],
            users: [
                { id: 1, name: 'John Doe', email: 'john@example.com' },
                { id: 2, name: 'Jane Smith', email: 'jane@example.com' },
                { id: 3, name: 'Bob Johnson', email: 'bob@example.com' },
            ],
            search: '',

        }
    }
}
</script >

<style scoped>
div {
    background-color: #333;
    color: #fff;
    padding: 5px;
    text-align: center;
    margin: 5px;
}
</style>

