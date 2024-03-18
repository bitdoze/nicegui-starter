import theme
from nicegui import ui


def script_generator():
    with theme.frame('YouTube Script Generator'):
        ui.page_title('YouTube Script Generator')
        ui.markdown('# This is My YouTube Script Generator Page')
