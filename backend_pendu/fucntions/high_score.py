from database.database import get_session
from sqlalchemy.orm import Session
from database.models import High_score
from datetime import date


def save_score(db: Session, pseudo: str, score: float):
    # Create an instance of High_score
    new_score = High_score(player_name=pseudo, score=score, date=date.today())
    # Add the instance to the session and commit the changes
    db.add(new_score)
    db.commit()


if __name__ == "__main__":
    save_score()
