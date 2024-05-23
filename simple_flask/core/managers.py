from abc import ABC
from typing import List, Dict

from flask_sqlalchemy.session import Session


class BaseManager(ABC):
    model = None
    read_only_fields = ['id']

    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def as_dict(obj):
        return obj._asdict()

    def get_all(self):
        return list(self.db.query(self.model).all())

    def get_by_id(self, _id):
        return self.db.query(self.model).get(_id)

    def save_all(self, data: List[Dict]):
        self.db.add_all([self.model(**item) for item in data])
        self.db.commit()
