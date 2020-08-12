from aiohttp import web
from app.api.api2.baseview import baseview

class OperationView(BaseView):
    async def get(self):
        data = self.request
        op_id = data.pop('op_id')
        op = (await self.get_service('data_svc').locate('operations', match=dict(id=int(op_id))))[0]
        return await op.report(file_svc=self.get_service('file_svc'), data_svc=self.get_service('data_svc'),
                               output=data.get('agent_output'))

    async def post(self):
        data = self.request
        access = await self.auth_svc.get_permissions(self.request)
        operation = await self._build_operation_object(access, data)
        operation.set_start_details()
        await self.get_service('data_svc').store(operation)
        self.loop.create_task(operation.run(self.get_services()))
        return [operation.display]

    async def put(self):
        data = self.request
        async def helper(self, op_id, state=None, autonomous=None, obfuscator=None): 
            async def validate(op):
                try:
                    if not len(op):
                        raise web.HTTPNotFound
                    elif await op[0].is_finished():
                        raise web.HTTPBadRequest(body='This operation has already finished.')
                    elif state not in op[0].states.values():
                        raise web.HTTPBadRequest(body='state must be one of {}'.format(op[0].states.values()))
                except Exception as e:
                    self.log.error(repr(e))
            operation = await self.get_service('data_svc').locate('operations', match=dict(id=op_id))
            if state:
                await validate(operation)
                operation[0].state = state
                if state == operation[0].states['FINISHED']:
                    operation[0].finish = self.get_current_timestamp()
                self.log.debug('Changing operation=%s state to %s' % (op_id, state))
            if autonomous:
                operation[0].autonomous = 0 if operation[0].autonomous else 1
                self.log.debug('Toggled operation=%s autonomous to %s' % (op_id, bool(operation[0].autonomous)))
            if obfuscator:
                operation[0].obfuscator = obfuscator
                self.log.debug('Updated operation=%s obfuscator to %s' % (op_id, operation[0].obfuscator))
        
        helper(self, **data)

    async def delete(self):
        data = self.request
        await self.get_service('data_svc').remove('operations', data)
        await self.get_service('data_svc').remove('sources', dict(id=str(data.get('id'))))
        for f in glob.glob('data/results/*'):
            if '%s-' % data.get('id') in f:
                os.remove(f)
        for f in glob.glob('data/facts/*.yml'):
            if '%s' % data.get('id') in f:
                os.remove(f)
        return 'Delete action completed'

    async def enable(self)
        routes = web.RouteTableDef()
        @routes.view('/api/api2/operation')
        app.router.add_routes(routes)

