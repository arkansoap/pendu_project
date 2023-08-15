import { Mot } from "./mot"
export class Pendu {

    constructor() {
        return (async () => {

            this.mot = await new Mot();
            console.log(`from class pendu, this.mot: ${this.mot}`);
            console.log(this.mot)
            this.etat = "*".repeat(this.mot.lenMot);
            console.log(this.etat);
            this.nbErreur = 0;
            this.endgame = false;
            this.loose = null;
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
            //this.affichePendu(params);
            this.nbErreur += 1;
        }
        this.check_endgame()
    }

    check_endgame() {
        if (this.nbErreur === 3) {
            this.endgame = true;
            this.loose = true;
        }
        if (this.etat === this.mot.motStr) {
            this.endgame = true;
            this.loose = false;
        }
    }

}