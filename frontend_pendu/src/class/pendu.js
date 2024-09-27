import { Mot } from "./mot"
export class Pendu {

    constructor() {
        return (async () => {

            this.mot = await new Mot();
            console.log(this.mot)
            this.etat = "*".repeat(this.mot.lenMot);
            this.nbErreur = 0;
            this.endgame = false;
            this.loose = null;
            this.score = 0;
            this.message = "Bonjour";

            return this;
        })();
    }

    replaceLettreInGuess(lettreProposee) {
        let position = 0;
        const etatListe = this.etat.split("");
        for (const lettre of this.mot.motStr) {
            if (lettreProposee === lettre) {
                etatListe[position] = lettreProposee;
            }
            position += 1;
        }
        this.etat = etatListe.join("");
        console.log(`\n______________\n\n${this.etat}\n______________`);
        return this.etat;
    }

    checkLettre(lettreProposee) {
        this.message = ""
        if (this.etat.includes(lettreProposee)) {
            console.log("\nProposition déja faite\n");
            this.message = "Proposition déjà faite"
        } else if (this.mot.motStr.includes(lettreProposee)) {
            this.replaceLettreInGuess(lettreProposee);
        } else if (!this.mot.motStr.includes(lettreProposee)) {
            this.nbErreur += 1;
        }
        this.check_endgame()
    }

    check_endgame() {
        if (this.nbErreur === this.mot.params.diff_dict.tentatives) {
            this.score = 0;
            this.endgame = true;
            this.loose = true;
        }
        if (this.etat === this.mot.motStr) {
            this.score = (this.mot.params.diff_dict.word_diff + (1 / this.mot.params.diff_dict.tentatives)) * (10 - this.mot.params.diff_dict.tentatives - this.nbErreur);
            this.endgame = true;
            this.loose = false;
        }
    }

}