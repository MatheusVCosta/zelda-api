from typing import Type
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship, Session

from app.database.database import Base


class Game(Base):
    __tablename__ = "games"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    developer = Column(String)
    publisher = Column(String)
    relesed_year = Column(Date)

    # items = relationship("Item", back_populates="owner")
    
    @classmethod
    def get_game(self, db: Session, name: str):
        return db.query(self).filter(self.name == name).first()
    
    @classmethod
    def create_user(db: Session, game):
        db_user = (
            game.name,
            game.description,
            game.developer,
            game.publisher,
            game.relesed_year,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    # return db_user

    # @classmethod
    # def create_game(self, db: Session):