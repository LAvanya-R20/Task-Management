from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/',views.add, name='addtask'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('delete-all/', views.delete_all_tasks, name='delete_all_tasks'),
    #new
    path('history/', views.history, name='history'),
    path('restore/<int:id>', views.restore, name='restore'),
    path('delete_restore/<int:id>', views.delete_restore, name='delete_restore'),
    path('restore_all/', views.restore_all, name='restore_all'),
    path('delete_history/', views.delete_history, name='delete_history'),
]