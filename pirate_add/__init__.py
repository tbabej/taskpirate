import os
import glob
import importlib

__all__ = [os.path.basename(f)[:-3]
           for f in glob.glob(os.path.dirname(__file__)+"/*.py")
           if os.path.isfile(f) and not os.path.basename(f).startswith('_')]

hooks = []

for module_name in __all__:
    module = importlib.import_module('pirate_add.%s' % module_name)
    module_hooks = [
        getattr(module, hook_name)
        for hook_name in dir(module)
        if hook_name.startswith('hook_')
    ]
    hooks += module_hooks
