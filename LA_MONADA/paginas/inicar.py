import reflex as rx

@rx.page(route="/iniciar", title="inicia secion")
def iniciar() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Bienvenido a la Monada"),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Iniciar", value="inicio"),
                    rx.tabs.trigger("Registrar", value="registro"),
                ),
                rx.tabs.content(
                    rx.vstack(
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="email",
                            type="email",
                            size="3",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            placeholder="contraseña",
                            type="password",
                            size="3",
                            width="100%",
                        ),
                        rx.button("iniciar", size="3", width="100%",on_click=rx.redirect("/menu")),
                        margin_top="4em",
                        spacing="3",
                    ),
                    value="inicio",
                ),
                rx.tabs.content(
                    rx.vstack(
                        rx.input(
                            rx.input.slot(rx.icon("user")),
                            placeholder="email",
                            type="email",
                            size="3",
                            width="100%",
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock")),
                            placeholder="contraseña",
                            type="password",
                            size="3",
                            width="100%",
                        ),
                        rx.button("registrar", size="3", width="100%",on_click=rx.redirect("/menu")),
                        margin_top="4em",
                        spacing="3",
                    ),
                    value="registro",
                ),
                default_value="inicio",
            ),
        ),
    )
