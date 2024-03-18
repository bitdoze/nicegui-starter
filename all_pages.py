from nicegui import ui
from pages.title_generator import title_generator
from pages.script_generator import script_generator

def create() -> None:
    ui.page('/youtube-title-generator/')(title_generator)
    ui.page('/youtube-script/')(script_generator)

if __name__ == '__main__':
    create()
