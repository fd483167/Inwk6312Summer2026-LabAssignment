# import Jinja2 library and PyYAML
from jinja2 import Environment, FileSystemLoader
import yaml

# Declare template environment
ENV = Environment(loader=FileSystemLoader('.'))
def get_interface_speed(interface_name):
    """ get_interface_speed returns the default Mbps value for a given
    network interface by looking for certain keywords in the name
    """
    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100
