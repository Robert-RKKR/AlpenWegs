GLOBAL_JAZZMIN_SETTINGS = {

    # Base application configuration:
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
    'user_avatar': None,

    # Links to put along the top menu:
    'topmenu_links': [
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},
        {'name': 'Tokens',  'model': 'authtoken.token', 'permissions': ['auth.view_user']},
        {'model': 'auth.User', 'permissions': ['auth.view_user']},
    ],
    'show_sidebar': True,
    'navigation_expanded': False,
    'hide_models': [
        'auth.user',
        'auth.group',
    ],
    'order_with_respect_to': [
        'profiles',
        'notifications',
        'explorers',
        'compendiums',
        'assets',
        'django_celery_beat',
    ],
    'icons': {
        # Profiles app:
        'profiles': 'fas fa-users',
        'profiles.UserModel': 'fas fa-user',
        'profiles.GroupModel': 'fas fa-users-cog',
        # Notifications app:
        'notifications': 'fas fa-bell',
        'notifications.NotificationModel': 'fas fa-envelope-open-text',
        'notifications.ChangeLogModel': 'fas fa-history',
        # Explorers app:
        'explorers': 'fas fa-hiking',
        'explorers.TrackModel': 'fas fa-shoe-prints',
        'explorers.JourneyModel': 'fas fa-passport',
        'explorers.SectionModel': 'fas fa-route',
        'explorers.RouteModel': 'fas fa-map-marked-alt',
        'explorers.TripModel': 'fas fa-mountain',
        # Compendiums app:
        'compendiums': 'fas fa-book',
        'compendiums.RegionModel': 'fas fa-globe-europe',
        'compendiums.CardModel': 'fas fa-id-card',
        'compendiums.PoiModel': 'fas fa-map-pin',
        # Assets app:
        'assets': 'fas fa-folder-open',
        'assets.PhotoModel': 'fas fa-image',
        'assets.FileModel': 'fas fa-file-alt',
        # Celery (system tasks):
        'django_celery_beat': 'fas fa-sitemap',
        'django_celery_beat.Clocked': 'fas fa-clock',
        'django_celery_beat.Crontab': 'fas fa-calendar-alt',
        'django_celery_beat.Interval': 'fas fa-hourglass-half',
        'django_celery_beat.PeriodicTask': 'fas fa-tasks',
        'django_celery_beat.SolarEvent': 'fas fa-sun',
        # Default icons (fallbacks):
        'default_icon_parents': 'fas fa-chevron-circle-right',
        'default_icon_children': 'fas fa-circle',
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
