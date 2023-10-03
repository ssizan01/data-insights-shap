from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



def csv_uploader_change(self, file, **event_args):
    """This method is called when a file is loaded into the csv_uploader."""
    # Call the server function to process the uploaded file
    categorical_features = anvil.server.call('process_data', file)
    
    # Populate the target_variable_picker with the list of categorical features
    self.target_variable_picker.items = categorical_features

def submit_button_for_processing_click(self, **event_args):
    """This method is called when the submit_button_for_processing is clicked."""
    # Call the server function to process the data, train the model, and get SHAP values
    plot_media, shap_summary_data = anvil.server.call('train_and_get_shap', self.csv_uploader.file, self.target_variable_picker.selected_value)
    
    # Display the SHAP summary plot in the shap_displayer
    self.shap_displayer.source = plot_media
    
    # If you have a DataGrid or other component to display the SHAP summary DataFrame, you can set its items here
    # For example:
    # self.data_grid_1.items = shap_summary_data

