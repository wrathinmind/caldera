from aiohttp import web
from app.api.api2.baseview import baseview

class SourceView(BaseView):
    async def get(self):
        access = await self.auth_svc.get_permissions(self.request)
        return dict(sources=[s.display for s in await self.data_svc.locate('sources', match=dict(access=tuple(access)))])

    async def enable(self)
        routes = web.RouteTableDef()
        @routes.view('/api/api2/sources')
        app.router.add_routes(routes)

