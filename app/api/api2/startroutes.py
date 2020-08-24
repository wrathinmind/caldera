import os
import asyncio

from app.api.api2.configuration import ConfigurationView
from app.api.api2.adversary import AdversaryView 
from app.api.api2.operation import OperationView
from app.api.api2.sources import SourceView
from app.api.api2.agent import AgentView
from app.api.api2.contact import ContactView
from app.api.api2.planner import PlannerView
from app.api.api2.obfuscator import ObfuscatorView
from app.api.api2.schedule import ScheduleView

class StartRoute(BaseWorld):
    def StartStuff(self, services):
        asyncio.get_event_loop().create_task(ConfigurationView(services).enable())
        asyncio.get_event_loop().create_task(AdversaryView(services).enable())
        asyncio.get_event_loop().create_task(OperationView(services).enable())
        asyncio.get_event_loop().create_task(SourceView(services).enable())
        asyncio.get_event_loop().create_task(AgentView(services).enable())
        asyncio.get_event_loop().create_task(ContactView(services).enable())
        asyncio.get_event_loop().create_task(PlannerView(services).enable())
        asyncio.get_event_loop().create_task(ObfuscatorView(services).enable())
        asyncio.get_event_loop().create_task(ScheduleView(services).enable())




