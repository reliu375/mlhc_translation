from ._anvil_designer import TranslateTemplate
from anvil import *

class Translate(TranslateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.appt_panel.remove_from_parent()
    self.pcp_panel.remove_from_parent()
    self.mode = "TRANSLATE"

  def translate_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.translated.visible = True
    self.translated_label.visible = True
    self.translated.text = self.report.text

  def clear_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.translated.visible = False
    self.translated_label.visible = False
    self.translated.text = ""
    self.report.text = ""

  def translate_link_click(self, **event_args):
    if self.mode == "TRANSLATE": return
    self.add_component(self.translate_panel)
    self.appt_panel.remove_from_parent()
    self.pcp_panel.remove_from_parent()
    self.mode = "TRANSLATE"

  def appt_link_click(self, **event_args):
    if self.mode == "APPT": return
    self.translate_panel.remove_from_parent()
    self.add_component(self.appt_panel)
    self.pcp_panel.remove_from_parent()
    self.mode = "APPT"
    
  def pcp_link_click(self, **event_args):
    if self.mode == "PCP": return
    self.translate_panel.remove_from_parent()
    self.appt_panel.remove_from_parent()
    self.add_component(self.pcp_panel)
    self.mode = "PCP"

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    # send email!
    self.email.text = ""
    self.message.text = ""
    self.success.visible = True

  def email_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.success.visible = False










