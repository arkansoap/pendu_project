import axios from '../plugins/axios';
import 'regenerator-runtime/runtime'; // A effacer ?? 

import { Params } from "./params"

export class Mot {
    constructor() {
        return (async () => {
            this.params = await new Params()
            this.motStr = await this.selectionMot();
            console.log(`From class Mot, this.motStr: ${this.motStr}`);
            this.lenMot = this.motStr.length;
            this.diffMot();
            return this;
        })();
    }

    async getMot() {
        let result = await axios.get("/selectionMot");
        let mot = result.data.mot;
        return mot
    }

    async selectionMot() {
        let result = await this.getMot();

        if (this.params.diff_dict.word_diff === 3) {
            return result;
        }

        while (true) {
            const uniqueCharacters = new Set(result);

            if (this.params.diff_dict.word_diff === 2 && uniqueCharacters.size < 5) {
                result = this.getNewWord();
            } else if (this.params.diff_dict.word_diff === 3 && uniqueCharacters.size < 8) {
                result = this.getNewWord();
            } else {
                break; // Conditions are respected, exit the loop
            }
        }

        return result;
    }


    // nb de caractère différent et longueur du mot
    // diffMot() {
    //     if (this.motStr.length > 6) {
    //         this.diffLenMot = 2;
    //     } else {
    //         this.diffLenMot = 1;
    //     }
    //     this.coeffDiffMot = this.diffLenMot;
    // }
}


