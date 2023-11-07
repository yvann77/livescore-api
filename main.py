from fastapi import FastAPI

# Documentation
from documentations.description import api_description
from documentations.tags import tags_metadata


# Import des routers
import routers.router_leagues
import routers.router_matches
import routers.router_auth
import routers.router_stripe



#Lancement de l'API
app = FastAPI(
    title="Livescore API",
    description= api_description,
    openapi_tags= tags_metadata # Tags metadata
)

# Routers dédiés
app.include_router(routers.router_leagues.router)
app.include_router(routers.router_matches.router)
app.include_router(routers.router_auth.router)
app.include_router(routers.router_stripe.router)