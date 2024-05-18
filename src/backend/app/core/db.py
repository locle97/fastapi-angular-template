from sqlmodel import create_engine

from app.core.config import settings

print(str(settings.SQLALCHEMY_DATABASE_URI))
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
