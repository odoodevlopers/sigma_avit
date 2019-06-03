{
    'name': 'Emplyee Master Data',
    'version': '1.0',
    'depends': ['base','hr'],
    'data': [
                'security/ir.model.access.csv',
                'view/employee_view.xml',
                'data/ir_sequence_data.xml',
            ],

    # 'qweb': [
    #     'static/src/xml/reminder_topbar.xml', ],
    # 'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': True,
    'application': False,
}
