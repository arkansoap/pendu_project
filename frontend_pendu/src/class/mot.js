import axios from '../plugins/axios';
import 'regenerator-runtime/runtime';

export class Mot {
    constructor() {
        return (async () => {
            this.motStr = await this.selectionMot2();
            console.log(`From class Mot, this.motStr: ${this.motStr}`);
            this.lenMot = this.motStr.length;
            this.diffMot();
            return this;
        })();
    }

    async selectionMot2() {
        let result = await axios.get("/selectionMot");
        let mot = result.data.mot;
        return mot
    }

    diffMot() {
        if (this.motStr.length > 6) {
            this.diffLenMot = 2;
        } else {
            this.diffLenMot = 1;
        }
        this.coeffDiffMot = this.diffLenMot;
    }
}
