from django.conf.urls.defaults import *

urlpatterns = patterns('labgeeks_horae.views',
                       url(r'^view_preferences/$', 'view_preferences', name="Schedule-View_Prefs"),
                       url(r'^shifts/$', 'view_shifts', name="Schedule-View_Shifts"),
                       url(r'^available/$', 'view_available_shifts', name="Schedule-View_Avail"),
                       url(r'^timeperiods/$', 'view_timeperiods', name="Schedule-View_Timeperiods"),
                       url(r'^timeperiods/edit/$', 'edit_timeperiods', name="Schedule-Edit_Timeperiods"),
                       (r'^people/$', 'view_people'),
                       (r'^timeperiods/info/$', 'view_timeperiod_data'),
                       (r'^$', 'list_options'),
                       )
