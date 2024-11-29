import reflex as rx
from .paginas.inicar import iniciar
def index() -> rx.Component:
    return rx.flex(
        rx.image(src="https://i.pinimg.com/736x/ec/31/e4/ec31e481f6d645e971fdb1690ec99b1d.jpg"),
        rx.button(rx.icon(tag="chevron-right"),bg="black",on_click=rx.redirect("/iniciar")),
        background_color="white",
        height="100vh",
        width="100vw",
        direction="column",
        align="center",
        justify="center"
    ),


app = rx.App()
app.add_page(index)

