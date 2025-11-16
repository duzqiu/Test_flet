
import flet as ft


def main(page: ft.Page):
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    ft1 = ft.Container(
                    margin=30,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=page.width * 0.8,
                    height=50,
                )
    ft1.content = ft.Row([
        ft.Icon(ft.Icons.LOCK_CLOCK_OUTLINED, size=20,color=ft.Colors.BLUE),
        ft.Button("帮助", bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
    ],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # 关键：两端对齐
    spacing=10,
    )

    ft2 = ft.Container(
                margin=30,
                padding=10,
                alignment=ft.alignment.center_left,
                width=page.width * 0.8,
                # bgcolor=ft.Colors.LIGHT_BLUE_100,
                height=110,
            )
    ft2.content = ft.Column([
        ft.Text("欢迎\n回来!", color=ft.Colors.BLACK, size=24),
        ft.Text("请输入您的密码以解锁", color=ft.Colors.BLACK, size=12)
    ],  
    alignment=ft.MainAxisAlignment.START,
    horizontal_alignment=ft.CrossAxisAlignment.START,
    spacing=10,
    )

    ft3 = ft.Container(
            margin=30,
            padding=10,
            alignment=ft.alignment.center_left,
            width=page.width * 0.8,
            # bgcolor=ft.Colors.LIGHT_BLUE_100,
            height=80,
        )
    ft3.content = ft.TextField(
        hint_text="请输入密码",
        password=True,
        border_width=0.5,
        can_reveal_password=True,
        max_length=20,
        width=page.width * 0.8 - 20,
    )

    ft4 = ft.Container(
            margin=30,
            padding=10,
            alignment=ft.alignment.center_left,
            width=page.width * 0.8,
            # bgcolor=ft.Colors.LIGHT_BLUE_100,
            height=80,
        )
    
    ft4.content = ft.ElevatedButton(
        text="解锁",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
        width=page.width * 0.8 - 20,
        height=50,
    )
    
    page.add(ft.Column(controls=[ft1, ft2, ft3, ft4]))

ft.app(target=main)