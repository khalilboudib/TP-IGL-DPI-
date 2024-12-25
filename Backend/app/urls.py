from django.urls import path

from app.views import authentication
from app.views.login import CustomTokenObtainPairView
from app.views.admin import AdminView
from app.views.register import RegisterView
from app.views import DiagnosticControler, ConsultationControler

urlpatterns = [
    path('POST/', authentication.index_POST, name='index_POST'),
    path('GET/', authentication.index_GET, name='index_GET'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('SignUp/', authentication.SignUp, name='SignUp'),
    path('token_test/', authentication.token_test, name='token_test'),
    path('users/add', RegisterView.as_view(), name="register_view"),
    path('create_diagnostic/', DiagnosticControler.crea_Diagnostic , name="create_diagnostic"),
    path('create_consultation/', ConsultationControler.crea_Consultation , name="create_consultation"),
    path('add_ordanance/', DiagnosticControler.ajout_ordanance , name="add_ordanance"),
    path('add_diagnostic/', DiagnosticControler.ajout_diagnostic , name="add_diagnostic"),
]