from django.conf.urls import url
from TakeNotes import views
# SET THE NAMESPACE!
app_name = 'TakeNotes'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'TakeNotesForm/$', views.add_note, name='add_note')
]