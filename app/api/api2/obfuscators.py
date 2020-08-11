from aiohttp import web
from app.api.api2.baseview import baseview
routes = web.RouteTableDef()

@routes.view('/api/api2/obfuscators')
class OperationView(BaseView):
    async def get(self):
        obfuscators = [o.display for o in await self.data_svc.locate('obfuscators')]
        return dict(obfuscators=obfuscators)

app.router.add_routes(routes)
