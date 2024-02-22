from django.conf import settings
from django.urls import include, path

from nstm.apps.core import views as core_views

urlpatterns = [
    path('', core_views.dashboard, name='dashboard'),
    path('', include('nstm.apps.subscribers.urls', namespace='subscribers')),
    path('setup/', core_views.setup, name='setup'),
    path('setup/account/', core_views.setup_account, name='setup_account'),
    path('settings/', core_views.SiteUpdateView.as_view(), name='settings'),
    path('accounts/', include('nstm.apps.accounts.urls')),
    path('lists/', include('nstm.apps.lists.urls', namespace='lists')),
    path('notifications/', include('nstm.apps.notifications.urls', namespace='notifications')),
    path('templates/', include('nstm.apps.templates.urls', namespace='templates')),
    path('campaigns/', include('nstm.apps.campaigns.urls', namespace='campaigns')),
    path('<slug:mailing_list_slug>/', core_views.subscribe_shortcut, name='subscribe_shortcut'),
    path('<slug:mailing_list_slug>/unsubscribe/', core_views.unsubscribe_shortcut, name='unsubscribe_shortcut'),
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
