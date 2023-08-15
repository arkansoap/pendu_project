import axios from '../plugins/axios';

export class Params {
    constructor() {
        return (async () => {
            this.diff = await this.getParams();
            console.log(`From class Params, this.diff: ${this.diff}`);
            this.diff_dict = await this.getDictParams()

            return this;
        })();
    }

    async getDictParams() {
        const result = {}
        if (this.diff = "easy") {
            result = { tentatives: 8, word_diff: 1 }
        } else if (this.diff = "medium") {
            result = { tentatives: 5, word_diff: 2 }
        } else if (this.diff = "medium") {
            result = { tentatives: 3, word_diff: 3 }
        }
        return result
    }

    async getParams() {
        const result = await axios.get("/params");
        return result
    }
}