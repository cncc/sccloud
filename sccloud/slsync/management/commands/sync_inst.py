from django.core.management.base import BaseCommand, CommandError
from slsync.models import Inst
class Command(BaseCommand):
    #empty the staging table for import
    Inst.objects.all().delete()
from SoftLayer import Client, CCIManager
from SoftLayer.CLI.helpers import (NestedDict)
import os
sl_api_user=os.environ['SL_API_USER']
sl_api_key=os.environ['SL_API_KEY']
client = Client(username=sl_api_user, api_key=sl_api_key)

cci = CCIManager(client)
guests = cci.list_instances()
for guest in guests:
    guest = NestedDict(guest)
    a = Inst(inst_id=guest['id'], pub_ip=guest['primaryIpAddress'], pri_ip=guest['primaryBackendIpAddress'],fulldomainname=guest['fullyQualifiedDomainName'])
    a.save()
