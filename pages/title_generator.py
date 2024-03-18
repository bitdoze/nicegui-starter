import theme
from nicegui import ui


def title_generator():
    with theme.frame('YouTube Title Generator'):
        ui.page_title('YouTube Title Generator')
        ui.markdown('# This is My Title Generator Page')
