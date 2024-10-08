import { axiosIns as axios } from '../plugins/axios';
import 'regenerator-runtime/runtime'; // A effacer ?? 

import { Params } from "./params"

export class Mot {
    constructor() {
        return (async () => {
            this.params = await new Params()
            console.log("this.params", this.params)
            this.motStr = await this.selectionMot();
            this.lenMot = this.motStr.length;
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
        let uniqueCharacters = new Set(result);
    
        if (this.params.diff_dict.word_diff === 1) {
            console.log("N'importe quel mot fera l'affaire");
            return result;
        }
    
        while ((this.params.diff_dict.word_diff === 2 && uniqueCharacters.size < 8) || 
               (this.params.diff_dict.word_diff === 3 && uniqueCharacters.size < 11)) {
            if (this.params.diff_dict.word_diff === 2 && uniqueCharacters.size < 8) {
                console.log("Mot trop facile, on en cherche un autre moyen");
            } else if (this.params.diff_dict.word_diff === 3 && uniqueCharacters.size < 11) {
                console.log("Mot trop facile, on en cherche un autre difficile");
            }
            result = await this.getMot();
            uniqueCharacters = new Set(result);
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


