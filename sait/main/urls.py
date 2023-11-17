from django.urls import path
from .views import main, add_to_do, del_To_do,list,add_item_list,del_item_list

urlpatterns = [
    path('', list, name='list'),
    path('addTodoItem/<str:name>/', add_to_do),
    path('deleteTodoItem/<int:i>/', del_To_do),
    path('addItemList/',add_item_list),
    path('deleteItemList/<int:i>/', del_item_list),
    path('<str:name>/', main, name='main'),
]