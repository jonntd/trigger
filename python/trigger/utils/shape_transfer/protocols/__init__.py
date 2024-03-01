import os
import glob
import importlib
import inspect
from trigger.utils.shape_transfer.protocol_core import ProtocolCore

classes = []
modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))

exceptions = ["__init__.py"]

for mod in modules:
    file_name = os.path.basename(mod)
    if file_name not in exceptions and not file_name.startswith("_"):
        module_name = file_name[:-3]
        module_path = os.path.join(os.path.dirname(__file__), module_name)
        module = importlib.import_module("{0}.{1}".format(__name__, module_name))

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, ProtocolCore) and obj != ProtocolCore:
                classes.append(obj)
