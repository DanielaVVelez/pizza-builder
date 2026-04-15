import flet as ft

def main(app: ft.Page):
    app.title = "Pizza Creator"
    app.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    app.window_width = 500
    app.window_height = 700
    app.bgcolor = ft.Colors.BLACK

    def update_toppings(e):
        pepperoni_layer.visible = pepperoni_toggle.value
        corn_layer.visible = corn_toggle.value
        tomato_layer.visible = tomato_toggle.value
        app.update()

    base_img = ft.Image(src="images/base.png", width=700, height=700)
    pepperoni_layer = ft.Image(src="images/pepperoni.png", width=100, height=100, visible=False, top=150, left=150)
    corn_layer = ft.Image(src="images/corn.png", width=400, height=400, visible=False)
    tomato_layer = ft.Image(src="images/tomato.png", width=100, height=100, visible=False, top=150, left=150)

    pizza_display = ft.Stack(
        width=400,
        height=400,
        controls=[base_img, pepperoni_layer, corn_layer, tomato_layer]
    )

    pepperoni_toggle = ft.Switch(label="Pepperoni", on_change=update_toppings)
    corn_toggle = ft.Switch(label="Maíz", on_change=update_toppings)
    tomato_toggle = ft.Switch(label="Tomate", on_change=update_toppings)

    app.add(pizza_display, pepperoni_toggle, corn_toggle, tomato_toggle)

ft.app(target=main, assets_dir="assets")