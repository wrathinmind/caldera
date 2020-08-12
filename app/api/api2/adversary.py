from aiohttp import web
from app.api.api2.baseview import baseview


class AdversaryView(baseview):
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
        data = self.request:
        return await self._delete_data_from_memory_and_disk(ram_key='adversaries', identifier='adversary_id', data=data)


     async def enable(self)
        routes = web.RouteTableDef()
        @routes.view('/api/api2/adversary')
        app.router.add_routes(routes)

