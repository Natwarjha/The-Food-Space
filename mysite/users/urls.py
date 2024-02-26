from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    # customer orders
    path('orders/<int:itemid>/<int:pdcd>/<str:user>/', views.Orders, name='orders'),

    # update customer orders
    path('updorders/<int:orderid>/<int:itemid>/', views.Updateorders, name='updorders'),

    # customer ratings and feedback
    path('crf/<int:itemid>/<int:pc>/', views.CusRatFeedView, name='crf'),

    # updating customer ratings and feedbacks
    path('updcrf/<int:detailid>/<int:crfid>/', views.UpdateCRF, name='updcrf'),

    # deleting customer ratings and feedbacks
    path('delcrf/<int:detailid>/<int:crfid>/', views.DeleteCRF, name='delcrf'),
     # paypal checkout button
    path('buy/<int:amt>/<int:qnt>/', views.Payment, name='buy'),

      # paypal on approve
    path('oa/', views.OnApprove, name='oa'),

    # paypal payment success
    path('ps/', views.PaymentSuccess, name='ps'),
     # paypal payment success
    path('psvar/<int:var>/', views.PaymentSuccessVar, name='psvar'),
]






















