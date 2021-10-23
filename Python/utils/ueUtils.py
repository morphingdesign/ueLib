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


def logSelectedActors():
    # -----------------------------------------------------------
    # LOG SELECTED ACTORS ))))))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
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



def rename_assets(search_pattern):
    # -----------------------------------------------------------
    # REPLACE SELECTED ACTORS ))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
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

    # Iterate thru each selected asset and rename.
    for asset in selected_assets:
        # Get asset name as clear text. This is the display
        # name for the asset as seen in the Content Browser.
        asset_name = system_lib.get_object_name(asset)
        # Debug log retrieved name.
        unreal.log(asset_name)

        # Check if asset name contains the string spec'd to
        # be searched and replaced using UE's String Lib's
        # contains() function. 3rd arg spec's if case-sensitive.
        if string_lib.contains(asset_name, search_pattern, use_case = False):
            unreal.log("Search pattern found in {}.".format(asset_name))
        # Debug log for instances where search pattern was not
        # found in selected assets' name.
        else:
            unreal.log("Search pattern not found in {}, therefore, skipped.".format(asset_name))

    # -----------------------------------------------------------
    # REPLACE SELECTED ACTORS ))))))))))))))))))))))))))))))} END
    # -----------------------------------------------------------