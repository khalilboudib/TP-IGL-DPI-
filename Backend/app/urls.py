from django.urls import path

from app.views import authentication
from app.views.login import CustomTokenObtainPairView
from app.views.admin import AdminView
from app.views.register import RegisterView
from app.views import DiagnosticControler, ConsultationControler, OrdananceControler, ExamenCompControler

urlpatterns = [
    path('POST/', authentication.index_POST, name='index_POST'),
    path('GET/', authentication.index_GET, name='index_GET'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('SignUp/', authentication.SignUp, name='SignUp'),
    path('token_test/', authentication.token_test, name='token_test'),
    path('users/add', RegisterView.as_view(), name="register_view"),
    path('create_diagnostic/', DiagnosticControler.crea_Diagnostic , name="create_diagnostic"),
    path('create_consultation/', ConsultationControler.crea_Consultation , name="create_consultation"),
    path('create_ordanance/', OrdananceControler.crea_ordanance , name="create_ordanance"),
    path('add_diagnostic/', DiagnosticControler.ajout_diagnostic , name="add_diagnostic"),
    path('add_medicament/', OrdananceControler.ajout_medicament , name="add_medicament"),
    path('add_resume/', ConsultationControler.ajout_resume , name="add_resume"),
    path('add_resultat_bio/', ExamenCompControler.ajout_Resultat_Biologique , name="add_resultat_bio"),
    path('add_bilan_bio/', ExamenCompControler.ajout_Bilan_Biologique , name="add_bilan_bio"),
    path('add_examen_comp/', ExamenCompControler.ajout_ExamenComplementaire , name="add_examen_comp"),
    path('add_examen_radio/', ExamenCompControler.ajout_examen_radiologique, name="bilan_bio"),
    path('examen_comp/', ExamenCompControler.ExamenComplementaireListView.as_view(), name="examen_comp"),
    path('diagnostics/', DiagnosticControler.DiagnosticListView.as_view(), name="diagnostics"),
    path('consultations/', ConsultationControler.ConsultationListView.as_view(), name="consultations"),
    path('resumes/', ConsultationControler.ResumeListView.as_view(), name="resumes"),
    path('medicaments/', OrdananceControler.MedicamentListView.as_view(), name="medicaments"),
    path('bilan_bio/', ExamenCompControler.BilanBiologiqueListView.as_view(), name="bilan_bio"),
    path('bilan_radio/', ExamenCompControler.BilanRadiologiqueListView.as_view(), name="bilan_radio"),
]