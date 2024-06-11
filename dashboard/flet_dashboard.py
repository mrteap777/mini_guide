import flet as ft



def main(page: ft.Page):
    page.title = "Flet Dashboard"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    # Заголовок
    header = ft.Text("Flet Dashboard", style="headlineMedium")


    # Кнопка
    button = ft.ElevatedButton(text="Нажми меня", on_click=lambda e: page.add(ft.Text("Кнопка нажата!")))


    # Поле ввода
    text_field = ft.TextField(label="Введите что-то")


    # Выпадающий список
    dropdown = ft.Dropdown(
        label="Выберите вариант",
        options=[
            ft.dropdown.Option("Option 1"),
            ft.dropdown.Option("Option 2"),
            ft.dropdown.Option("Option 3"),
        ],
    )


    # Переключатель
    switch = ft.Switch(label="Переключатель")


    # Слайдер
    slider = ft.Slider(min=0, max=100, divisions=10, label="Слайдер")


    # Таблица
    table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Колонка 1")),
            ft.DataColumn(label=ft.Text("Колонка 2")),
        ],
        rows=[
            ft.DataRow(cells=[ft.DataCell(ft.Text("Ячейка 1-1")), ft.DataCell(ft.Text("Ячейка 1-2"))]),
            ft.DataRow(cells=[ft.DataCell(ft.Text("Ячейка 2-1")), ft.DataCell(ft.Text("Ячейка 2-2"))]),
        ]
    )


    # Создание макета для расположения элементов
    layout = ft.Column(
        controls=[
            header,
            button,
            text_field,
            dropdown,
            switch,
            slider,
            table,
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=20
    )


    # Добавление всех элементов на страницу
    page.add(layout)

ft.app(target=main, view=ft.WEB_BROWSER)
