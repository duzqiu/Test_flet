import flet as ft


def main(page: ft.Page):
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.GREY_200
    ft1 = ft.Container(
            margin=ft.margin.only(top=30), 
            padding=10,
            alignment=ft.alignment.center,
            width=page.width,
            # bgcolor=ft.Colors.BLUE,
            height=50,
                )
    ft1.content = ft.Row([
        ft.Container(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.HOME,size=24,color=ft.Colors.BLACK),
                    ft.Text("首页", color=ft.Colors.BLACK, size=18, weight="bold")
                    ]
                )
                ),
        ft.Container(
            content=ft.Row(
                [
                    # ft.Icon(ft.Icons.SEARCH,size=24,color=ft.Colors.BLACK),
                    ft.Icon(ft.Icons.PERSON,size=24,color=ft.Colors.BLACK),
                ]
            )
        )
    ],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # 关键：两端对齐
    spacing=10,
    )

    # 创建多个可滑动的 Container
    container_list = ft.Row(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("2025-11-15", size=14, color=ft.Colors.BLACK),
                        ft.Text("多云转晴", color=ft.Colors.BLACK54, size=14),
                        ft.Text("9°C-18°C", color=ft.Colors.GREEN, size=14),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=2,
                ),
                width=100,
                height=100,
                bgcolor=ft.Colors.WHITE,
                # bgcolor=ft.Colors.BLUE_300 if i % 2 == 0 else ft.Colors.GREEN_300,
                border_radius=15,
                padding=10,
                alignment=ft.alignment.center,
                ink=True,  # 点击水波纹效果
                # on_click=lambda e: print(f"点击了项目 {i}")
            )
            for i in range(1, 8)
        ],
        spacing=10,          # Container 之间的间距
        scroll="hidden",         # ✅ 关键：启用水平滚动
        alignment=ft.MainAxisAlignment.START,
    )

    ft2 = ft.Container(
        content=container_list,
        height=100,          # 必须设置高度，否则无法显示
        padding=10,
        bgcolor=ft.Colors.GREY_100,
        border_radius=12,
        )

    ft3 = ft.Container( 
            padding=10,
            alignment=ft.alignment.center,
            width=page.width,
            bgcolor=ft.Colors.GREY_100,
            height=80,
            border_radius=12,
                )
    progress_value = 100  # 示例中的进度为75%
    ft3.content = ft.Row([
        ft.Container(
            content=ft.Column(
                [ft.Row([
                    ft.Container(
                        width=10,  # 宽度
                        height=10,  # 高度
                        border_radius=10,  # 圆角半径为宽/高的1/2，使其成为圆形
                        bgcolor=ft.Colors.GREEN,  # 背景颜色设为绿色
                    ),
                    ft.Text("最新气温", size=12, weight="bold")
                ]
                ),
                    ft.Text("28°C", color=ft.Colors.BLACK, size=30, weight="bold"),
                    ],        
                )
                ),  
        ft.Container(
            width=200,  # 进度条宽度
            height=10,  # 进度条高度
            border_radius=10,  # 圆角程度
            bgcolor=ft.Colors.GREY_300,  # 背景颜色
            alignment=ft.alignment.bottom_left,
            content=ft.Container(
                width=(progress_value / 100) * 100,  # 根据进度值计算宽度
                height=10,
                bgcolor=ft.Colors.GREEN,  # 已完成部分的颜色
                border_radius=10,  # 确保已完成部分也是圆角
        )
        )
    ],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # 关键：两端对齐
    spacing=10,
    )

    scrollable_items = [
        ft.Container(
            content=ft.Column([
                ft.Text("18:00", size=12, weight="bold"),
                ft.Icon(ft.Icons.WB_SUNNY, size=20, color=ft.Colors.ORANGE_500),
                ft.Text("25°C", size=12),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=4),
            padding=10,
            bgcolor=ft.Colors.BLUE_50,
            border_radius=8,
            width=60,
            alignment=ft.alignment.center,
        )
        for _ in range(10)  # 生成10个可滑动项
    ]
    ft4 = ft.Container(
            padding=10,
            alignment=ft.alignment.center,
            width=page.width,
            bgcolor=ft.Colors.GREY_100,
            height=410,
            border_radius=12,
                ) 
    ft4.content = ft.Row([
        ft.Container(
            alignment=ft.alignment.center,
            width=page.width * 0.6,
            content=ft.Column([
                ft.Container(
                    alignment=ft.alignment.center,
                    height=220,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=12,
                    padding=10,
                    content=ft.Column([
                        ft.Container(
                            ft.Row([
                                ft.Text("我的位置", size=18, color=ft.Colors.GREY_600, weight="bold"),
                                ft.Icon(ft.Icons.LOCATION_ON,size=16,color=ft.Colors.GREY_600),
                                ft.Text("上海", size=16),   
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            )),
                        ft.Divider(color=ft.Colors.GREY_300, height=1, thickness=1),
                        ft.Text("今日天气概况", size=12, color=ft.Colors.GREY_600),
                        ft.Container(
                            ft.Row([
                            ft.Icon(ft.Icons.WB_SUNNY,size=16,color=ft.Colors.YELLOW_900),
                            ft.Text("多云转晴，微风", size=14) 
                        ],
                        # alignment=ft.MainAxisAlignment.START,
                        )),
                        ft.Container(
                            ft.Row([
                                ft.Container(
                                    ft.Column([
                                    ft.Icon(ft.Icons.THERMOSTAT,size=16,color=ft.Colors.RED),
                                    ft.Text("28°C", size=14) 
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                )),
                                ft.Container(
                                    ft.Column([
                                    ft.Icon(ft.Icons.WATER_DROP,size=16,color=ft.Colors.BLUE),
                                    ft.Text("湿度60%", size=14) 
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                )),
                            ],
                            # alignment=ft.MainAxisAlignment.CENTER,
                            spacing=50,
                            )
                    ),
                        ft.Container(
                            ft.Row([
                                ft.Container(
                                    ft.Column([
                                    ft.Icon(ft.Icons.THERMOSTAT,size=16,color=ft.Colors.GREEN),# 最低温度
                                    ft.Text("12°C", size=14) 
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                )),
                                ft.Container(
                                    ft.Column([
                                    ft.Icon(ft.Icons.THERMOSTAT,size=16,color=ft.Colors.RED),# 最高温度
                                    ft.Text("18°C", size=14) 
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                )),
                                ft.Container(
                                    ft.Column([
                                    ft.Icon(ft.Icons.THERMOSTAT,size=16,color=ft.Colors.RED),#体感温度
                                    ft.Text("18°C", size=14) 
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                )),
                            ],
                            # alignment=ft.MainAxisAlignment.CENTER,
                            spacing=50,
                            )
                    ),
                    ],
                    # alignment=ft.MainAxisAlignment.CENTER,
                    )
                ),
                ft.Container(
                    alignment=ft.alignment.top_left,
                    height=160,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=12,
                    padding=10,
                    content=ft.Column([
                        ft.Text("预计四小时后会天黑", size=12, color=ft.Colors.GREY_600, weight="bold"),
                        ft.Divider(color=ft.Colors.GREY_300, height=1, thickness=1), 
                        ft.Container(
                            content=ft.ListView(
                                controls=scrollable_items,
                                horizontal=True,          # 水平滚动
                                height=110,               # 固定高度，避免布局塌陷
                                spacing=6,               # 项目间距
                                padding=ft.padding.only(top=10, bottom=10),
                            ),
                            # 可选：加个背景或边框便于观察
                            # bgcolor=ft.colors.GREY_100,
                        ),
                    ])
                ),
            ]),
        ),
        ft.Container(
            alignment=ft.alignment.center,
            width=page.width * 0.4 - 30,
            # bgcolor=ft.Colors.GREEN_100,
            content=ft.Column([
                ft.Container(
                    alignment=ft.alignment.center,
                    height=170,
                    # width=page.width * 0.4,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=12,
                    margin=ft.margin.only(right=20),  # ✅ 右侧外边距
                    content=ft.Column([
                        ft.Text("能见度", size=14, color=ft.Colors.GREY_600, weight="bold"),
                        ft.Container(
                            ft.Row([
                            ft.Icon(ft.Icons.VISIBILITY,size=14,color=ft.Colors.GREEN),
                            ft.Text("30km", size=14)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        )),
                        ft.Container(
                            ft.Row([
                            ft.Icon(ft.Icons.CLOUD,size=14,color=ft.Colors.BLUE),
                            ft.Text("60%", size=14),  
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),),
                        ft.Text("降水量", size=14, color=ft.Colors.GREY_600, weight="bold"),
                        ft.Container(
                            ft.Row([
                            ft.Icon(ft.Icons.WATER_DROP,size=14,color=ft.Colors.GREEN_500),
                            ft.Text("18mm", size=14)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ))
                        ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ),
                ft.Container(
                    alignment=ft.alignment.center,
                    height=100,
                    # width=page.width * 0.4,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=12,
                    margin=ft.margin.only(right=20),  # ✅ 右侧外边距
                    content=ft.Column([
                        ft.Text("风力风速", size=14, color=ft.Colors.GREY_600, weight="bold"),
                        ft.Container(
                            ft.Row([
                            ft.Icon(ft.Icons.AIR,size=14,color=ft.Colors.GREEN_500),
                            ft.Text("东北风2级", size=14)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        )),
                        ft.Container(
                            ft.Row([
                            ft.Icon(ft.Icons.COMPASS_CALIBRATION,size=14,color=ft.Colors.AMBER_700),
                            ft.Text("27km/h", size=14),  
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        )],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ),

                # ft.Container(
                #     alignment=ft.alignment.center,
                #     height=60,
                #     # width=page.width * 0.4,
                #     bgcolor=ft.Colors.BLUE_100,
                #     border_radius=12,
                #     margin=ft.margin.only(right=20),  # ✅ 右侧外边距
                #     content=ft.Column([
                #         ft.Text("体感温度", size=14, color=ft.Colors.GREY_600, weight="bold"),
                #         ft.Container(
                #             ft.Row([
                #             ft.Icon(ft.Icons.THERMOSTAT,size=14,color=ft.Colors.GREEN_500),
                #             ft.Text("18°C", size=14)
                #         ],
                #         alignment=ft.MainAxisAlignment.CENTER,
                #         ))],
                #     alignment=ft.MainAxisAlignment.CENTER,
                #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                #     ),
                #     ),
                ft.Container(
                    alignment=ft.alignment.center,
                    height=100,
                    # width=page.width * 0.4,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=12,
                    margin=ft.margin.only(right=20),  # ✅ 右侧外边距
                    content=ft.Column([
                        ft.Text("日出日落", size=14, color=ft.Colors.GREY_600, weight="bold"),
                        ft.Container(
                            ft.Row([
                            ft.Icon(ft.Icons.WB_SUNNY,size=14,color=ft.Colors.YELLOW_900),
                            ft.Text("05:01", size=14)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        )),
                        ft.Container(
                            ft.Row([
                            ft.Icon(ft.Icons.NIGHTLIGHT,size=14,color=ft.Colors.BLACK),
                            ft.Text("18:02", size=14),  
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        )],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ),
            ]),
        ),
    ],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # 关键：两端对齐
    spacing=10,
    )

    # 定义导航栏项目
    nav_items = [
        ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
        ft.NavigationBarDestination(icon=ft.Icons.BUSINESS, label="Business"),
        ft.NavigationBarDestination(icon=ft.Icons.SCHOOL, label="School"),
    ]

    # 处理导航切换事件
    def on_navigation_change(e):
        index = e.control.selected_index
        if index == 0:
            print("Home Page")
        elif index == 1:
            print("Business Page")
        elif index == 2:
            print("School Page")
        page.update()

    # 创建导航栏
    navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_navigation_change,
        destinations=nav_items,
        bgcolor=ft.Colors.GREY_100,
        height=100,
    )

    # 将导航栏添加到页面底部
    page.navigation_bar = navigation_bar

    page.add(ft.Column(controls=[ft1,ft2,ft3,ft4]))

ft.app(target=main)