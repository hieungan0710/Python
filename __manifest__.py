# -*- coding: utf-8 -*-
{
    'name': "Purchase Custom",
    'summary': """ Quản lý yêu cầu mua hàng """,
    'description': """ Quản lý yêu cầu mua hàng""",
    'author': "NganNH",
    'website': "https://www.ngannh.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['purchase','hr','product'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/menu_purchase.xml',
        'views/purchase_request_views.xml',
        'views/purchase_request_line_views.xml'

        # 'views/templates.xml',

    ],

}
