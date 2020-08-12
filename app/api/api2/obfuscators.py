from aiohttp import web
from app.api.api2.baseview import baseview

class ObfuscatorView(BaseView):
    async def get(self):
        obfuscators = [o.display for o in await self.data_svc.locate('obfuscators')]
        return dict(obfuscators=obfuscators)

    async def enable(self)
        routes = web.RouteTableDef()
        @routes.view('/api/api2/obfuscators')
        app.router.add_routes(routes)

