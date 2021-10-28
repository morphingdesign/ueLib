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



def rename_assets(search_pattern, replaced_pattern, case_sensitivity=True):
    # -----------------------------------------------------------
    # REPLACE SELECTED ACTORS ))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
    r"""
        Replace search pattern in selected assets with new string.

        Args:
            search_pattern:
                string
            replaced_pattern:
                string
            case_sensitivity:
                bool

        Returns:
            None
    """

    # Instantiate classes
    # Accessing UE's System Library.
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
        if string_lib.contains(asset_name, search_pattern, use_case=case_sensitivity):
            # Specify new asset name by replacing matched search
            # pattern with new replaced pattern. Note that replace()
            # function includes arg to specify case sensitivity
            # with UE's SearchCase enum. Case enum toggles between
            # user spec'd use_case arg.
            # Ref: https://docs.unrealengine.com/4.27/en-US/PythonAPI/class/SearchCase.html
            case_enum = unreal.SearchCase.CASE_SENSITIVE if case_sensitivity else unreal.SearchCase.IGNORE_CASE
            new_asset_name = string_lib.replace(asset_name, search_pattern, replaced_pattern, search_case=case_enum)
            # Aggregate replaced asset counter.
            replaced_assets += 1
            # Execute renaming operation using UE's Editor Utility
            # rename_asset() function.
            editor_util.rename_asset(asset, new_asset_name)
            # Debug log for found search pattern and rename.
            unreal.log("Search pattern found in {}, renamed to {}".format(asset_name, new_asset_name))
        # Debug log for instances where search pattern was not
        # found in selected assets' name.
        else:
            unreal.log("Search pattern not found in {}, therefore, skipped.".format(asset_name))

    # Log number of selected assets that were successfully renamed.
    unreal.log("Renamed {}/{} assets".format(replaced_assets, num_of_assets))

    # -----------------------------------------------------------
    # REPLACE SELECTED ACTORS ))))))))))))))))))))))))))))))) END
    # -----------------------------------------------------------



def org_world_outliner():
    # -----------------------------------------------------------
    # ORGANIZE WORLD OUTLINER ))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
    r"""
        Organize world outliner based on actor type and categorize
        into corresponding folders.

        Args:
            None

        Returns:
            None
    """

    # Access UE's Editor Level & Filter Libraries to access level
    # content.
    editor_level_lib = unreal.EditorLevelLibrary()
    editor_filter_lib = unreal.EditorFilterLibrary()

    # Retrieve all actors in current level; store in array.
    actors = editor_level_lib.get_all_level_actors()

    # Filter thru array and isolate by class. Each filter focuses
    # on each type of actor being isolated, such as by class, string
    # or other method.
    static_mesh = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)
    lighting = editor_filter_lib.by_class(actors, unreal.Light)
    # Rather than by class, filter BP's by string in name.
    blueprint = editor_filter_lib.by_id_name(actors, "BP")
    # For tagged actors, specify the tag as a Name object and spec
    # Filter Type. If set to 'INCLUDE', then it will only include
    # actors with the spec'd tag. With 'EXCLUDE', all non-tagged
    # actors will be assigned to array variable.
    tag_name = unreal.Name("tagged")
    tagged = editor_filter_lib.by_actor_tag(actors, tag_name, filter_type=unreal.EditorScriptingFilterType.INCLUDE)
    untagged = editor_filter_lib.by_actor_tag(actors, tag_name, filter_type=unreal.EditorScriptingFilterType.EXCLUDE)

    # Counter to track number of moved actors.
    moved_actors = 0

    # Create map that matches spec'd folder names to each of the
    # filters created above.
    folders = {
        "StaticMesh": static_mesh,
        "Lighting": lighting,
        "BP": blueprint,
        "Tagged": tagged,
        "Untagged": untagged
    }

    # Iterate thru each folder within the map.
    for folder_name in folders:
        # Iterate thru each actor based on folder name.
        for actor in folders[folder_name]:
            # Get name of spec'd actor instance.
            actor_name = actor.get_fname()
            # Redefine the path to the actor so that it is now
            # within its respective folder, as spec'd in the arg.
            #actor.set_folder_path(folder_name)
            unreal.log("{} moved into {} folder.".format(actor_name, folder_name))

            # Aggregate actors moved into folder.
            moved_actors += 1

    # Debug log total number of actors moved into folders.
    unreal.log("Moved {} actors into folders.".format(moved_actors))

    # -----------------------------------------------------------
    # ORGANIZE WORLD OUTLINER ))))))))))))))))))))))))))))))) END
    # -----------------------------------------------------------



def log_bp_components():
    # -----------------------------------------------------------
    # LOG BP COMPONENTS ))))))))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
    r"""
        Access components within selected blueprint actors.

        Args:
            None

        Returns:
            None
    """

    # Access UE's Editor Level Library to access level content.
    editor_level_lib = unreal.EditorLevelLibrary()

    # Retrieve selected bp actors in current level; store in array.
    bp_actors = editor_level_lib.get_selected_level_actors()

    # Counter to track identified actors and children.
    num_of_actors = 0

    # Iterate thru each static mesh actor.
    for actor in bp_actors:
        # Get root component property for current actor.
        scene_component = actor.root_component
        # Get all children within current bp.
        children = scene_component.get_children_components(True)
        # Get num of children for current root scene component.
        # Note that this number includes itself as array item 0.
        num_of_children = len(children)
        # Alt built-in method in scene component class to log
        # num of children.
        alt_num_of_children = scene_component.get_num_children_components()
        current_child = 0

        # Iterate through each child component.
        for child in children:
            child_name = child.get_fname()
            current_child += 1
            unreal.log("{}: {}".format(current_child, child_name))

        num_of_actors += 1

        unreal.log("Documented {} ({}) children.".format(num_of_children, alt_num_of_children))

    # -----------------------------------------------------------
    # LOG BP COMPONENTS ))))))))))))))))))))))))))))))))))))) END
    # -----------------------------------------------------------