import unreal

# -----------------------------------------------------------
# HOT RELOADING IN UE ))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Include the following to allow for hot reload in UE Python console.
# In console simply type the following to load the module:
#       Syntax                  Example
#       import <module>         import ueUtils
# Then to reload any edits made to the module:
#       Syntax                  Example
#       reload(<module>)        reload(ueUtils)

import importlib

__builtins__['reload'] = importlib.reload

# -----------------------------------------------------------
# HOT RELOADING IN UE ))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

def testprint(string):
    print(string + "00100")

# -----------------------------------------------------------
# LOG SELECTED ACTORS ))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

def logSelectedActors():
    """Log names of selected scene actors to console."""

    @unreal.uclass()
    class ueUtility(unreal.GlobalEditorUtilityBase):
        pass

    selectedActors = ueUtility().get_selection_set()

    for actor in selectedActors:
        unreal.log("Selected Actors:")
        unreal.log(actor.get_name())

# -----------------------------------------------------------
# LOG SELECTED ACTORS ))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------