from nicegui import ui

estado = ui.label('Estado actual: Rojo')

def cambiar_estado():
    estado.text = 'Estado actual: Verde'

ui.button(
    'Cambiar estado',
    on_click=cambiar_estado
)

ui.run()
