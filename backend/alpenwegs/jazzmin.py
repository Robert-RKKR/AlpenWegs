GLOBAL_JAZZMIN_SETTINGS = {
    'site_title': 'AlpenWegs',
    'site_header': 'AlpenWegs',
    'site_brand': 'AlpenWegs',
    'site_logo': 'logo/logo_contours.svg',
    'login_logo': 'logo/logo_contours.svg',
    'site_logo_classes': 'img-circle',
    'site_icon': 'ico/favicon/favicon-32x32.png',
    'welcome_sign': 'Welcome to the AlpenWegs',
    'custom_css': 'css/custom_admin.css',
    'copyright': 'Copyright (c) 2025 Robert Tadeusz Kucharski RKKR - AlpenWegs',
    #'search_model': 'auth.User',
    'user_avatar': None,

    # Links to put along the top menu:
    'topmenu_links': [
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},
        {'name': 'Home',  'model': 'inventory.Device', 'permissions': ['auth.view_user']},
        {'name': 'Tokens',  'model': 'authtoken.token', 'permissions': ['auth.view_user']},
        {'model': 'auth.User', 'permissions': ['auth.view_user']},
    ],
    'show_sidebar': True,
    'navigation_expanded': False,
    'hide_models': [],
    'order_with_respect_to': [
        'inventory',
        'authtoken',
        'connections',
        'management',
        'notifications'],
    'icons': {
        # Authentication:
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
        # profiles:
        'invenprofilestory': 'fas fa-server',
        'profiles.UserModel': 'fas fa-database',
        # Notifications:
        'notifications': 'fas fa-envelope',
        'notifications.ChangeLogModel': 'fas fa-clock',
        'notifications.NotificationModel': 'fas fa-envelope-open',
        # Celery:
        'django_celery_beat': 'fas fa-sitemap',
        'django_celery_beat.Clocked': 'fas fa-code',
        'django_celery_beat.Crontab': 'fas fa-code',
        'django_celery_beat.Interval': 'fas fa-code',
        'django_celery_beat.PeriodicTask': 'fas fa-code',
        'django_celery_beat.SolarEvent': 'fas fa-code',
    },
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',
    'related_modal_active': False,
    'custom_css': None,
    'custom_js': None,
    'show_ui_builder': False,
    'changeform_format': 'horizontal_tabs',
    'changeform_format_overrides': {
        'auth.user': 'collapsible',
        'auth.group': 'vertical_tabs'},
}
