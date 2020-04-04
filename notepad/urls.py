from django.urls import path
from .views import (
	create_view,
	list_view,
	delete_view,
	update_view)


app_name = 'notes'

urlpatterns = [
	path('create/',create_view,name='creat_view'),
	path('list/',list_view,name='list'),
	path('<int:id>/delete/',delete_view,name='delete'),
	#url(r'^(?P<id>\d+)/delete/',delete_view,name='delete'),
	path('<int:id>/update/',update_view,name="update"),

]
