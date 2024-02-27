from database.database import get_session
from sqlalchemy.orm import Session
from database.models import Difficulty


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
        print(f"Row with id={id} not found.")


def get_params(db: Session, id: int):
    # Query the row with the specified id
    row_to_retrieve = db.query(Difficulty).filter_by(id=id).first()

    if row_to_retrieve:
        # Check which level is set to True
        if row_to_retrieve.easy:
            return "easy"
        elif row_to_retrieve.medium:
            return "medium"
        elif row_to_retrieve.hard:
            return "hard"
        else:
            return "No level selected"
    else:
        return "Row with id={} not found.".format(id)


if __name__ == "__main__":
    # db = get_session()
    # update_params(db, id=2, level="medium")
    # print(get_params(db, id=2))

    db = get_session()
    init_params(db, level="easy")
    print(get_params(db, id=1))
    init_params(db, level="medium")
    print(get_params(db, id=2))
