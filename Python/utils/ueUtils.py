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

# -----------------------------------------------------------
# REPLACE SELECTED ACTORS ))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

def rename_assets():
    """"""

    # Access UE's System Library to create class instances.
    system_lib = unreal.SystemLibrary()
    # Access UE's Editor Utility Library to perform operations
    # within UE's Editor.
    editor_util = unreal.EditorUtilityLibrary()
    # Access UE's own String Library, to be used in lieu of
    # default Python's string functions.
    string_lib = unreal.StringLibrary()

    # Collect the assets selected by user and log their count.
    selected_assets = editor_util.get_selected_assets()
    num_of_assets = len(selected_assets)
    # Counter to track replaced assets.
    replaced_assets = 0

    # Debug log
    unreal.log("Selected {} assets.".format(num_of_assets))

# -----------------------------------------------------------
# REPLACE SELECTED ACTORS ))))))))))))))))))))))))))))))} END
# -----------------------------------------------------------