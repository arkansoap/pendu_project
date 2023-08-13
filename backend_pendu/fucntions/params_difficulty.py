from database.database import get_session
from sqlalchemy.orm import Session
from database.models import Difficulty  # Import the Difficulty model from your module


# if no row in the table
def init_params(db: Session, level: str):
    if level == "easy":
        new_difficulty = Difficulty(easy=True)
    elif level == "medium":
        new_difficulty = Difficulty(medium=True)
    elif level == "hard":
        new_difficulty = Difficulty(hard=True)
    # Add the new instance to the session and commit the changes
    db.add(new_difficulty)
    db.commit()


def update_params(db: Session, id: int, level: str):
    # Query the row with id=1
    row_to_update = db.query(Difficulty).filter_by(id=id).first()

    if row_to_update:
        # Update the columns
        row_to_update.easy = False
        row_to_update.medium = False
        row_to_update.hard = False

        if level == "easy":
            row_to_update.easy = True
        elif level == "medium":
            row_to_update.medium = True
        elif level == "hard":
            row_to_update.hard = True
        else:
            print("please select easy, medium ou hard")

        # Commit the changes
        db.commit()
        print("Row updated successfully.")
    else:
        print("Row with id=1 not found.")


if __name__ == "__main__":
    db = get_session()
    update_params(db, id=2, level="medium")
