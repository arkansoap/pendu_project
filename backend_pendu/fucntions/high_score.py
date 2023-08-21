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


def get_score(db: Session):
    # Get all the scores from the database
    scores = db.query(High_score).all()
    # Sort the scores by score
    scores.sort(key=lambda x: x.score, reverse=True)
    # Return the 10 best scores
    scores_list = scores[:10] if len(scores) >= 10 else scores
    data = []
    for i in range(len(scores_list)):
        datum = {
            "player_name": scores_list[i].player_name,
            "score": scores_list[i].score,
            "date": scores_list[i].date,
        }
        data.append(datum)
    return {"users": data}


if __name__ == "__main__":
    data = get_score(get_session())
    print(data)
