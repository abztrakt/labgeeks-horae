from django.conf.urls.defaults import *

urlpatterns = patterns('labgeeksrpg.schedule.views',
    url(r'^view_preferences/$', 'view_preferences', name="Schedule-View_Prefs"),
    url(r'^create/default/$', 'create_default_schedule', name="Schedule-Create_Schedule"),
    url(r'^create/base/$', 'create_base_schedule', name="Schedule-Create_Base_Schedule"),
    url(r'^shifts/$', 'view_shifts', name="Schedule-View_Shifts"),
    url(r'^available/$', 'view_available_shifts', name="Schedule-View_Avail"),
    url(r'^timeperiods/$', 'view_timeperiods', name="Schedule-View_Timeperiods"),
    (r'^create/default/save/$', 'save_default_hours'),
    (r'^create/base/save/$', 'save_base_hours'),
    (r'^people/$', 'view_people'),
    (r'^timeperiods/info/$', 'view_timeperiod_data'),
    (r'^$', 'list_options'),
)
