import axios from '../plugins/axios';

export class Params {
    constructor() {
        return (async () => {
            this.diff = await this.getParams();
            console.log(this.diff.data.params);
            this.diff_dict = await this.getDictParams()

            return this;
        })();
    }

    async getDictParams() {
        let result = {}
        if (this.diff.data.params === "easy") {
            result = { tentatives: 3, word_diff: 1 }
        } else if (this.diff.data.params === "medium") {
            result = { tentatives: 2, word_diff: 2 }
        } else if (this.diff.data.params === "hard") {
            result = { tentatives: 1, word_diff: 3 }
        }
        return result
    }

    async getParams() {
        const result = await axios.get("/params");
        return result
    }
}