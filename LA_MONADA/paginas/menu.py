import reflex as rx

@rx.page(route="/menu")
def menu()->rx.Component:
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
                        rx.button("login", size="3", width="100%"),
                        margin_top="4em",
                        spacing="3",
                    ),
                    value="inicio",
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
                        rx.button("registrar", size="3", width="100%"),
                        margin_top="4em",
                        spacing="3",
                    ),
                    value="registro",
                ),
                default_value="inicio",
            ),
        ),
    )
