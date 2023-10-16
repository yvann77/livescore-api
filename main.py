from fastapi import FastAPI

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata


# Import des routers
import routers.routers_leagues
import routers.routers_matches

#Lancement de l'API
app = FastAPI(
    title="Livescore API",
    description= api_description,
    openapi_tags= tags_metadata # Tags metadata
)

# Routers dédiés
app.include_router(routers.routers_leagues.router)
app.include_router(routers.routers_matches.router)