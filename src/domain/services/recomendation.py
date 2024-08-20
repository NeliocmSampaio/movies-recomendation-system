from ..entities import visualization
from sqlalchemy.orm import Session


def get_visualization_history(db: Session):
    data = visualization.VisualizationHistory()

    data.get_history(db)
