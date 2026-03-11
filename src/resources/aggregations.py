from flask_restful import Resource
from sqlalchemy import func

from src import db
from src.models import Film, Actor


class AggregationApi(Resource):
    """"""

    def get(self):
        films_count = db.session.query(func.count(Film.id)).scalar()
        max_rating = db.session.query(func.max(Film.rating)).scalar()
        min_rating = db.session.query(func.min(Film.rating)).scalar()
        avg_rating = db.session.query(func.avg(Film.rating)).scalar()
        sum_rating = db.session.query(func.sum(Film.rating)).scalar()

        actor_count = db.session.query(func.count(Actor.id)).scalar()
        count_isactive = db.session.query(func.count()).filter(Actor.is_active == 1).scalar()
        count_nonactive = db.session.query(func.count()).filter(Actor.is_active == 0).scalar()

        return {
            "result":
                {
                    'films': {
                        'count': films_count,
                        'max_rating': max_rating,
                        'min_rating': min_rating,
                        'avg_rating': avg_rating,
                        'sum_rating': sum_rating
                    },
                    'actors': {
                        'count': actor_count,
                        'count_isactive': count_isactive,
                        'count_nonactive': count_nonactive
                    }
                }
        }
