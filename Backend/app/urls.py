from django.urls import path

from app.views import authentication
from app.views.login import CustomTokenObtainPairView
from app.views.admin import AdminView
from app.views.users import RegisterView, ListUsersView
from app.views.dpi import AddDPIView, ListDPIsView
from app.views.soins import AddSoinView, ListSoinsView
from app.views.dpi import AddDPIView
from app.views.soins import AddSoinView
from app.views import DiagnosticControler, ConsultationControler, OrdananceControler, ExamenCompControler

urlpatterns = [
    path('POST/', authentication.index_POST, name='index_POST'),
    path('GET/', authentication.index_GET, name='index_GET'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('SignUp/', authentication.SignUp, name='SignUp'),
    path('token_test/', authentication.token_test, name='token_test'),
    path('users/add/', RegisterView.as_view(), name="register_view"),
    path('dpi/add/', AddDPIView.as_view(), name="add_dpi_view"),
    path('soins/add/', AddSoinView.as_view(), name="add_soins"),
    path('soins/', ListSoinsView.as_view(), name="list_soins"),
    path('users/', ListUsersView.as_view(), name="list_users"),
    path('dpi/', ListDPIsView.as_view(), name="list_dpis"),
    path('soins/add/', AddSoinView.as_view(), name="add_soins"),
    path('users/add', RegisterView.as_view(), name="register_view"),
    path('create_diagnostic/', DiagnosticControler.crea_Diagnostic , name="create_diagnostic"),
    path('create_consultation/', ConsultationControler.crea_Consultation , name="create_consultation"),
    path('create_ordanance/', OrdananceControler.crea_ordanance , name="create_ordanance"),
    path('add_diagnostic/', DiagnosticControler.ajout_diagnostic , name="add_diagnostic"),
    path('add_medicament/', OrdananceControler.ajout_medicament , name="add_medicament"),
    path('add_resume/', ConsultationControler.ajout_resume , name="add_resume"),
    path('add_resultat_bio/', ExamenCompControler.ajout_Resultat_Biologique , name="add_resultat_bio"),
    path('add_bilan_bio/', ExamenCompControler.ajout_Bilan_Biologique , name="add_bilan_bio"),
    path('add_bilan_radio/', ExamenCompControler.ajout_bilan_radiologique , name="add_bilan_radio"),
    path('add_examen_comp/', ExamenCompControler.ajout_ExamenComplementaire , name="add_examen_comp"),
    path('add_examen_radio/', ExamenCompControler.ajout_examen_radiologique, name="bilan_bio"),
    path('add_resultat_radio/', ExamenCompControler.ajout_resultat_radiologique, name="resultat_radio"),
    path('examen_comp/', ExamenCompControler.ExamenComplementaireListView.as_view(), name="examen_comp"),
    path('diagnostics/', DiagnosticControler.DiagnosticListView.as_view(), name="diagnostics"),
    path('consultations/', ConsultationControler.ConsultationListView.as_view(), name="consultations"),
    path('resumes/', ConsultationControler.ResumeListView.as_view(), name="resumes"),
    path('ordanances/', OrdananceControler.OrdananceListView.as_view(), name="ordanances"),
    path('medicaments/', OrdananceControler.MedicamentListView.as_view(), name="medicaments"),
    path('bilan_bio/', ExamenCompControler.BilanBiologiqueListView.as_view(), name="bilan_bio"),
    path('bilan_radio/', ExamenCompControler.BilanRadiologiqueListView.as_view(), name="bilan_radio"),
    path('resultats_bio/', ExamenCompControler.ResultatBiologiqueListView.as_view(), name="resultats_bio"),
    path('resultats_radio/', ExamenCompControler.ResultatRadiologiqueListView.as_view(), name="resultats_radio"),
    path('examens_radio/', ExamenCompControler.ExamenRadiologiqueListView.as_view(), name="examens_radio"),
]