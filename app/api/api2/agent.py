from aiohttp import web
from app.api.api2.baseview import baseview

class AgentView(BaseView):
    async def get(self):
        data = self.request
        access = await self.auth_svc.get_permissions(self.request)
        if index not in options[request.method]:
                search = {**data, **access}
                return web.json_response(await self.rest_svc.display_objects(index, search))
            return web.json_response(await options[request.method][index](data))
        except ma.ValidationError as e:
            raise web.HTTPBadRequest(content_type='application/json', text=json.dumps(e.messages))
        except Exception as e:
            self.log.error(repr(e), exc_info=True)

    async def delete(self):
        data = self.request
        await self.get_service('data_svc').remove('agents', data)
        return 'Delete action completed'
    
    async def put(self):
        data = self.request
        paw = data.pop('paw', None)
        if paw is None:
            await self._update_global_props(**data)
        for agent in await self.get_service('data_svc').locate('agents', match=dict(paw=paw)):
            await agent.gui_modification(**data)
            return agent.display

    async def enable(self)
        routes = web.RouteTableDef()
        @routes.view('/api/api2/agent')
        app.router.add_routes(routes)

