from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QSlider, QTextEdit
import tracker_config as tkc
from logger_setup import logger


class SettingsManagersomefailwin:
    """
    A class that manages the settings for the somefailwin module in the Agenda application.
    """

    def __init__(self):
        self.settings = QSettings(tkc.ORGANIZATION_NAME, tkc.AGENDA_NAME)
    
    def save_somefailwin(self, to_do_textedit: QTextEdit, extra_sun: QTextEdit, extra_mon: QTextEdit, extra_tues: QTextEdit, extra_wed: QTextEdit, extra_thurs: QTextEdit, extra_fri: QTextEdit, extra_sat: QTextEdit):
        """
        Save the contents of the text edits to the settings.

        Args:
            to_do_textedit (QTextEdit): The text edit for the to-do list.
            extra_sun (QTextEdit): The text edit for extra tasks on Sunday.
            extra_mon (QTextEdit): The text edit for extra tasks on Monday.
            extra_tues (QTextEdit): The text edit for extra tasks on Tuesday.
            extra_wed (QTextEdit): The text edit for extra tasks on Wednesday.
            extra_thurs (QTextEdit): The text edit for extra tasks on Thursday.
            extra_fri (QTextEdit): The text edit for extra tasks on Friday.
            extra_sat (QTextEdit): The text edit for extra tasks on Saturday.
        """
        try:
            self.settings.setValue('to_do_textedit', to_do_textedit.toHtml())
            self.settings.setValue('extra_sun', extra_sun.toHtml())
            self.settings.setValue('extra_mon', extra_mon.toHtml())
            self.settings.setValue('extra_tues', extra_tues.toHtml())
            self.settings.setValue('extra_wed', extra_wed.toHtml())
            self.settings.setValue('extra_thurs', extra_thurs.toHtml())
            self.settings.setValue('extra_fri', extra_fri.toHtml())
            self.settings.setValue('extra_sat', extra_sat.toHtml())
        except AttributeError as e:
            logger.error(f"error happened in MODULE save_somefailwin: {e}", exc_info=True)
    
    def restore_somefailwin(self, to_do_textedit: QTextEdit, extra_sun: QTextEdit, extra_mon: QTextEdit, extra_tues: QTextEdit, extra_wed: QTextEdit, extra_thurs: QTextEdit, extra_fri: QTextEdit, extra_sat: QTextEdit):
        """
        Restore the contents of the text edits from the settings.

        Args:
            to_do_textedit (QTextEdit): The text edit for the to-do list.
            extra_sun (QTextEdit): The text edit for extra tasks on Sunday.
            extra_mon (QTextEdit): The text edit for extra tasks on Monday.
            extra_tues (QTextEdit): The text edit for extra tasks on Tuesday.
            extra_wed (QTextEdit): The text edit for extra tasks on Wednesday.
            extra_thurs (QTextEdit): The text edit for extra tasks on Thursday.
            extra_fri (QTextEdit): The text edit for extra tasks on Friday.
            extra_sat (QTextEdit): The text edit for extra tasks on Saturday.
        """
        try:
            to_do_textedit.setHtml(self.settings.value('to_do_textedit', "", type=str))
            extra_sun.setHtml(self.settings.value('extra_sun', "", type=str))
            extra_mon.setHtml(self.settings.value('extra_mon', "", type=str))
            extra_tues.setHtml(self.settings.value('extra_tues', "", type=str))
            extra_wed.setHtml(self.settings.value('extra_wed', "", type=str))
            extra_thurs.setHtml(self.settings.value('extra_thurs', "", type=str))
            extra_fri.setHtml(self.settings.value('extra_fri', "", type=str))
            extra_sat.setHtml(self.settings.value('extra_sat', "", type=str))
        except AttributeError as e:
            logger.error(f"error happened in MODULE save_somefailwin: {e}", exc_info=True)
