"""Boiler Plate template for actions"""

from trigger.core import filelog


log = filelog.Filelog(logname=__name__, filename="trigger_log")


ACTION_DATA = {
    "some_property": "some_default_data",
    "some_more_property": "some_more_default_data",
}

# Name of the class MUST be the capitalized version of file name. eg.
# morph.py => Morph, split_shapes.py => Split_shapes


class ActionCore(object):
    action_data = ACTION_DATA
    def __init__(self, vcs=None):
        """Initialize the action instance"""
        self.vcs = vcs

    def feed(self, action_data, *args, **kwargs):
        """Mandatory Method - Feeds the instance with the action data
        stored in actions session.
        """
        pass

    def action(self):
        """Mandatory Method - Execute Action"""
        # everything in this method will be executed automatically.
        # This method does not accept any arguments.
        # all the user variable must be defined to the instance before
        pass

    def save_action(self, file_path=None, *args, **kwargs):
        """Mandatory Method - Save Action"""
        # This method will be called automatically and accepts no arguments.
        # If the action has an option to save files, this method will be used by the UI.
        # Else, this method can stay empty
        pass

    def ui(self, ctrl, layout, handler, *args, **kwargs):
        """
        Mandatory Method - UI setting definitions

        Args:
            ctrl: (model_ctrl) ctrl object instance of /ui/model_ctrl.
                                Updates UI and Model
            layout: (QLayout) The layout object from the main ui.
                                All setting widgets should be added to this layout
            handler: (actions_session) An instance of the actions_session.
                                TRY NOT TO USE HANDLER UNLESS ABSOLUTELY NECESSARY
            *args:
            **kwargs:

        Returns: None

        """

        pass
