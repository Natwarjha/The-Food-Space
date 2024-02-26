from django.urls import path, include
from food import views

app_name = 'food'

urlpatterns = [

    # Function based index view 
    # ----------------------------------------------------------------------------
    path('home/',views.index, name='index'),

    # class based index view 
    # ----------------------------------------------------------------------------
    # path('home/', views.indexClassView.as_view(), name='index'),

    # Function based detail view 
    # ----------------------------------------------------------------------------
    path('detail/<int:item_id>/', views.detail, name= 'detail'),

    # class based detail view 
    # ----------------------------------------------------------------------------
    #path('detail/<int:pk>/', views.FoodDetail.as_view(),name='detail'),


    # Function based create_item view 
    # ----------------------------------------------------------------------------
    # path('add/', views.create_item, name='create_item'),


    # class based create_item view 
    # ----------------------------------------------------------------------------
    path('add/', views.CreateItem.as_view(),name='create_item'),
    

    # Function based update_item view 
    # ----------------------------------------------------------------------------
    path('update/<int:id>/', views.update_item, name='update_item'),

    # Function based delete_item view 
    # ----------------------------------------------------------------------------
    path('delete/<int:id>/', views.delete_item, name='delete_item'),

    #  namv formview 
    # ----------------------------------------------------------------------------
    path('navform/', views.NavForm, name='navform'),


]