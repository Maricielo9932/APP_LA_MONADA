import reflex as rx

class State(rx.State):
    text: str = "la monada"

@rx.page(route="/menu")
def menu()->rx.Component:
    return rx.vstack(
        rx.heading("la monada"),
        rx.input(
            rx.input.slot(
                rx.icon(tag="search"),
            ),
            placeholder="Search here...",
        ), 
        rx.hstack(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("CATEGORIAS")
                ),
                rx.menu.content(
                rx.menu.item("Elegante"),
                rx.menu.item("Deportivo"),
                rx.menu.item("Romantico"),
                rx.menu.item("clasico"),
                rx.menu.item("casual"),
                
                ),
               
            ), 
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("TALLA")
                ),
                rx.menu.content(
                rx.menu.item("S"),
                rx.menu.item("M"),
                rx.menu.item("L"),
                rx.menu.item("XL"),
                
                ),
               
            ),  
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("MATERIAL")
                ),
                rx.menu.content(
                rx.menu.item("Algodon"),
                rx.menu.item("Lino"),
                rx.menu.item("Lycra"),
                rx.menu.item("Poliester"),
                rx.menu.item("Lana"),
                rx.menu.item("nylon"),

                ),
               
            ), 
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("PRECIO")
                ),
                rx.menu.content(
                rx.menu.item("S/50"),
                rx.menu.item("S/100"),
                rx.menu.item("S/250"),
                rx.menu.item("S/500"),
                rx.menu.item("S/1000"),
                rx.menu.item("S/2000"),

                ),
               
            ),
        ),
        rx.flex(
            rx.card(
                rx.image(src="https://www.atributo.co/cdn/shop/files/235.png?crop=center&height=803&v=1693517213&width=600"),
                rx.text("vestido corte velgrade S/190"), 
                size="5",
                width="45%"
            ),
            rx.card(
                rx.image(src="https://shersboutique.com/wp-content/uploads/2024/07/m.jpeg"),
                rx.text("vestido de encaje S/88"), 
                size="5",
                width="45%"
            ),
             rx.card(
                rx.image(src="https://dvicioshop.com/cdn/shop/files/WhatsAppImage2024-04-27at15.45.50_1_1.jpg?v=1714257038&width=1080"),
                rx.text("vestido romantico S/150"), 
                size="5",
                width="45%"
            ),
             rx.card(
                rx.image(src="https://i.pinimg.com/736x/08/67/64/086764ac4bd6926d4d58b8119156f09f.jpg"),
                rx.text("vestido corto S/100"), 
                size="5",
                width="45%"
            ),
            spacing="2",
            align_items="flex-start",
            flex_wrap="wrap",
        )
        
    ),