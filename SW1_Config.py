import getpass
from pprint import pprint
from jnp.junos import Device

dev = Device(host= '192.168.32.2', user='automation' ,password='Juniper')
