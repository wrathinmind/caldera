from aiohttp import web, routes
from app.api.api2.baseview import baseview

class ScheduleView(BaseView):
    async def get(self):
        data = request
        access = await self.auth_svc.get_permissions(self.request)
        if index not in options[request.method]:
                search = {**data, **access}
                return web.json_response(await self.rest_svc.display_objects(index, search))
            return web.json_response(await options[request.method][index](data))
        except ma.ValidationError as e:
            raise web.HTTPBadRequest(content_type='application/json', text=json.dumps(e.messages))
        except Exception as e:
            self.log.error(repr(e), exc_info=True)


    async def post(self):
        data = self.request
        access = await self.auth_svc.get_permissions(self.request)
        operation = await self._build_operation_object(access, data['operation'])
        schedules = await self.get_service('data_svc').locate('schedules', match=dict(name=operation.name))
        if schedules:
            self.log.debug('A scheduled operation with the name "%s" already exists, skipping' % operation.name)
        else:
            scheduled = await self.get_service('data_svc').store(
                Schedule(name=operation.name,
                         schedule=time(data['schedule']['hour'], data['schedule']['minute'], 0),
                         task=operation)
            )
            self.log.debug('Scheduled new operation (%s) for %s' % (operation.name, scheduled.schedule))
    
    async def enable(self)
        routes = web.RouteTableDef()
        @routes.view('/api/api2/schedule')
        app.router.add_routes(routes)
