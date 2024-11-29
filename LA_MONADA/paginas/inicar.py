import reflex as rx

@rx.page(route="/iniciar", title="inicia secion",font_family="tangerine",)
def iniciar()->rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Bienvenido a la Monada"),
            rx.hstack(
                rx.tabs.root(
                    rx.tabs.list(
                        rx.tabs.trigger(rx.button("iniciar"),value="inicio"),
                        rx.tabs.trigger(rx.button("registrar"),value="registro")
                    ),
                    rx.tabs.content(
                        rx.vstack(
                                rx.input(
                                rx.input.slot(rx.icon("user")),
                                placeholder="user@reflex.dev",
                                type="email",
                                size="3",
                                width="100%",
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("lock")),
                                placeholder="Enter your password",
                                type="password",
                                size="3",
                                width="100%",
                            ),
                            margin_top="4em",
                            spacing="3"
                        ),
                        value="inicio",
                    ),
                    rx.tabs.content(
                        rx.text("registro"),
                        value="registro",
                    ),
                    default_value="inicio"
                ),
            ),
        ),
    )