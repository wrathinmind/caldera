from aiohttp import web
from app.api.api2.baseview import baseview

class ConatcView(BaseView):
    async def get(self):
        contacts = [dict(name=c.name, description=c.description) for c in self.contact_svc.contacts]
        return dict(contacts=contacts)

async def enable(self)
        routes = web.RouteTableDef()
        @routes.view('/api/api2/contacts')
        app.router.add_routes(routes)

