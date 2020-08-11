from aiohttp import web
from app.api.api2.baseview import baseview
routes = web.RouteTableDef()

@routes.view('/api/api2/planner')
class OperationView(BaseView):
    async def get(self):
        planners = [p.display for p in await self.data_svc.locate('planners')]
        return dict(planners=planners)

app.router.add_routes(routes)
