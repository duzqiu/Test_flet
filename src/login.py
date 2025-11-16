import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.START
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
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    ft2 = ft.Container(
                margin=30,
                padding=10,
                alignment=ft.alignment.center,
                width=page.width * 0.8,
                # bgcolor=ft.Colors.LIGHT_BLUE_100,
                height=80,
            )
    ft2.content = ft.Column([
        ft.Text("登录在线学习", size=24, weight="bold"),
        ft.Text("请输入您的信息进行登陆", size=12)
    ],  
    alignment=ft.MainAxisAlignment.START,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=10,
    )
    ft3 = ft.Container(
            margin=30,
            padding=10,
            alignment=ft.alignment.center,
            width=page.width * 0.8,
            # bgcolor=ft.Colors.LIGHT_BLUE_100,
            height=150,
        )
    ft3.content = ft.Column([
        ft.TextField(
            hint_text="请输入用户名",
            border_width=0.5,
            max_length=20,
            width=page.width * 0.8 - 20,
        ),
        ft.TextField(
            hint_text="请输入密码",
            password=True,
            border_width=0.5, 
            can_reveal_password=True,
            max_length=20,
            width=page.width * 0.8 - 20,
        )
    ],
    alignment=ft.MainAxisAlignment.START,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=20,
    )
    ft4 = ft.Container(
            margin=30,
            # padding=10,
            alignment=ft.alignment.center_left,
            width=page.width * 0.8,
            # bgcolor=ft.Colors.LIGHT_BLUE_100,
            height=50,
        )
    
    ft4.content = ft.ElevatedButton(
        text="立即登陆",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
        width=page.width * 0.8,
        height=50,
    )  

    ft5 = ft.Container(
        content=ft.Text("还没有账号？去注册", size=12),
        margin=30,
        # padding=10,
        alignment=ft.alignment.center,
        width=page.width * 0.8,
        # bgcolor=ft.Colors.LIGHT_BLUE_100,
        height=80,
    )  


    page.add(ft.Column(controls=[ft1, ft2, ft3, ft4, ft5]))

ft.app(target=main)