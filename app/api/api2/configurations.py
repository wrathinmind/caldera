from aiohttp import web
from app.api.api2.baseview import baseview


class ConfigurationView(BaseView):
    async def get(self):
        return dict(config=self.get_config(), plugins=[p for p in await self.data_svc.locate('plugins')])


    async def enable(self)
        routes = web.RouteTableDef()
        @routes.view('/api/api2/configurations')
        app.router.add_routes(routes)

