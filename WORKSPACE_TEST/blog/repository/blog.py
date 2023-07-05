from sqlalchemy.orm import Session 
import sys
sys.path.append("../..")
import models
def get_all(db:Session):
  blogs=db.query(models.Blog).all