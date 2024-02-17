from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
    path('newtodolist//', views.AddToDoList.as_view(), name="newtodolist"),
    path('updatetodolist/<int:pk>/', views.UpdateToDoList.as_view(), name="updatetodolist"),
    path('deletetodolist/<int:pk>', views.DeleteToDoList.as_view(), name="deletetodolist"),

    #rest framework
    path('api/', views.getRoutes, name='api'),
    # path('register/', views.RegisterView.as_view(), name='auth_register'),
    # path('login/', views.UserLoginView.as_view(), name='auth_login'),
    path('test/', views.testEndPoint, name='test'),
    path('api/list/', views.TodoListView.as_view(), name='list_todo'),
    path('api/list/<todo_id>', views.TodoDetailView.as_view(), name='list_todo'),
    path('api/register/', views.RegisterView.as_view(), name='auth_register'),
    path('api/login/', views.UserLoginView.as_view(), name='auth_login'),
    path('logout/',views.userlogout, name="logout"),
]