from src import api
from src.views import (
    Smoke,
    FilmsListApi,
    ActorListApi,
    AggregationApi,
    AuthRegister, AuthLogin,
    PopulateDB, PopulateDBThreaded, PopulateDBThreadPoolExecutor
)

api.add_resource(Smoke, "/smoke", strict_slashes=False)

api.add_resource(FilmsListApi, "/films", "/films/<uuid>", strict_slashes=False)
api.add_resource(ActorListApi, "/actors", "/actors/<uuid>", strict_slashes=False)

api.add_resource(AggregationApi, "/aggregations", strict_slashes=False)

api.add_resource(AuthRegister, "/register", strict_slashes=False)
api.add_resource(AuthLogin, "/login", strict_slashes=False)

api.add_resource(PopulateDB, "/populate_db", strict_slashes=False)
api.add_resource(PopulateDBThreaded, "/populate_db_threaded", strict_slashes=False)
api.add_resource(PopulateDBThreadPoolExecutor, "/populate_db_executor", strict_slashes=False)
