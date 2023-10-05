from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def handle_single_target_variable(self):
    """Handle the logic for when there's only one target variable."""
    unique_values = anvil.server.call('get_unique_values_for_feature', self.target_variable_picker.selected_value)
    self.class_picker.items = unique_values

  def csv_uploader_change(self, file, **event_args):
    """This method is called when a file is loaded into the csv_uploader."""
    # Call the server function to process the uploaded file and populate the target_variable_picker
    categorical_features = anvil.server.call('process_data', file)
    self.target_variable_picker.items = categorical_features

      # If there's only one categorical feature, set the target_variable_picker to that feature
    # and manually invoke the logic you want to execute
    if len(categorical_features) == 1:
        self.target_variable_picker.selected_value = categorical_features[0]
        self.handle_single_target_variable()


  def submit_button_for_processing_click(self, **event_args):
      """This method is called when the get_shap_for_class_button is clicked."""
      # Call the server function to get the SHAP summary plot for the selected class
      plot_media = anvil.server.call('train_and_get_shap', self.target_variable_picker.selected_value, self.class_picker.selected_value)
      self.shap_summary_displayer.source = plot_media


  def target_variable_picker_change(self, **event_args):
      """This method is called when a target variable is selected."""
      # Call the server function to get unique values for the selected target variable and populate the class_picker dropdown
      unique_values = anvil.server.call('get_unique_values_for_feature', self.target_variable_picker.selected_value)
      self.class_picker.items = unique_values

















