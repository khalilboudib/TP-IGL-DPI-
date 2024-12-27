# Generated by Django 5.0.7 on 2024-12-26 21:24

import datetime
import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('patient', 'Patient'), ('medecin', 'Medecin'), ('infirmier', 'Infirmier'), ('radiologue', 'Radiologue'), ('laborantin', 'Laborantin')], default='admin', max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='utilisateurs', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='utilisateurs', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Decompte_des_frais',
            fields=[
                ('id_decompte', models.AutoField(primary_key=True, serialize=False)),
                ('date_decompte', models.DateField()),
                ('montant_total', models.FloatField()),
                ('montant_rembourse', models.FloatField()),
                ('montant_a_payer', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id_diagnostic', models.AutoField(primary_key=True, serialize=False)),
                ('diagnostic', models.TextField()),
                ('date_creation', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='ImageMedicale',
            fields=[
                ('id_image', models.AutoField(primary_key=True, serialize=False)),
                ('chemin_fichier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='admin_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id_consultation', models.AutoField(primary_key=True, serialize=False)),
                ('date_consultation', models.DateTimeField(default=datetime.datetime.now)),
                ('diagnostic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultations', to='app.diagnostic')),
            ],
        ),
        migrations.CreateModel(
            name='DPI',
            fields=[
                ('id_dpi', models.AutoField(primary_key=True, serialize=False)),
                ('date_creation', models.DateTimeField(default=datetime.datetime.now)),
                ('nss', models.CharField(max_length=30)),
                ('mutuelle', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='dpi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diagnostics', to='app.dpi'),
        ),
        migrations.CreateModel(
            name='Examen_Complementaire',
            fields=[
                ('id_examen_complementaire', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('diagnostic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='examen_Complementaires', to='app.diagnostic')),
            ],
        ),
        migrations.CreateModel(
            name='Bilan_Radiologique',
            fields=[
                ('id_bilan_radiologique', models.AutoField(primary_key=True, serialize=False)),
                ('date_bilan', models.DateTimeField(default=datetime.datetime.now)),
                ('examen_complementaire', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bilan_radiologique', to='app.examen_complementaire')),
            ],
        ),
        migrations.CreateModel(
            name='Bilan_Biologique',
            fields=[
                ('id_bilan_biologique', models.AutoField(primary_key=True, serialize=False)),
                ('date_bilan', models.DateTimeField(default=datetime.datetime.now)),
                ('examen_complementaire', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bilan_biologique', to='app.examen_complementaire')),
            ],
        ),
        migrations.CreateModel(
            name='Examen_Consultation',
            fields=[
                ('id_examen_consultation', models.AutoField(primary_key=True, serialize=False)),
                ('outils', models.CharField(choices=[('STETHOSCOPE', 'Stethoscope'), ('OTOSCOPE', 'Otoscope'), ('THERMOMETRE', 'Thermometre'), ('OXYMETRE', 'Oxymetre'), ('AUTRES', 'Autres')], max_length=20)),
                ('description', models.TextField()),
                ('consultation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='examens_consultations', to='app.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='Examen_Radiologique',
            fields=[
                ('id_examen', models.AutoField(primary_key=True, serialize=False)),
                ('date_examen', models.DateField()),
                ('TypeRadio', models.TextField(choices=[('IRM', 'Irm'), ('ECHOGRAPHIE', 'Echographie'), ('RADIOGRAPHIE', 'Radiographie'), ('SCANNER', 'Scanner'), ('AUTRES', 'Autres')])),
                ('bilan_radiologique', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='examen_radiologiques', to='app.bilan_radiologique')),
                ('resultat', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.imagemedicale')),
            ],
        ),
        migrations.CreateModel(
            name='Hospitalisation',
            fields=[
                ('id_hospitalisation', models.AutoField(primary_key=True, serialize=False)),
                ('date_entree', models.DateField()),
                ('date_sortie', models.DateField()),
                ('nbr_chamisation', models.IntegerField()),
                ('etablissement_hospitalier', models.CharField(max_length=100)),
                ('decompte_des_frais', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.decompte_des_frais')),
                ('dpi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospitalisations', to='app.dpi')),
            ],
        ),
        migrations.CreateModel(
            name='Infirmier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='infirmier_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='laborantin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medecin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CertificatMedical',
            fields=[
                ('id_certificat', models.AutoField(primary_key=True, serialize=False)),
                ('date_emission', models.DateTimeField()),
                ('date_debut_validite', models.DateField()),
                ('date_fin_validite', models.DateField()),
                ('type_certificat', models.CharField(choices=[('ARRET_TRAVAIL', 'Arret Travail'), ('APTITUDE', 'Aptitude'), ('INCAPACITE_TEMPORAIRE', 'Incapacite Temporaire'), ('INAPTITUDE', 'Inaptitude'), ('SUIVI_MEDICAL', 'Suivi Medical'), ('AUTRE', 'Autre')], max_length=21)),
                ('duree_arret_travail', models.IntegerField()),
                ('recommandations', models.TextField()),
                ('etablissement', models.CharField(max_length=100)),
                ('signature_numerique', models.CharField(max_length=255)),
                ('chemin_fichier', models.CharField(max_length=255)),
                ('dpi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='certificats', to='app.dpi')),
                ('medecin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.medecin')),
            ],
        ),
        migrations.CreateModel(
            name='Ordonnance',
            fields=[
                ('id_ordonnance', models.AutoField(primary_key=True, serialize=False)),
                ('date_creation', models.DateField(default=datetime.datetime.now)),
                ('validated', models.TextField(choices=[('EN_ATTENTE', 'En Attente'), ('VALIDEE', 'Validee'), ('REJETEE', 'Rejetee')])),
                ('diagnostic', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordonnance', to='app.diagnostic')),
            ],
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id_medicament', models.AutoField(primary_key=True, serialize=False)),
                ('nom_medicament', models.CharField(max_length=100)),
                ('dose', models.CharField(max_length=50)),
                ('duree_traitement', models.CharField(max_length=50)),
                ('ordannance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medicaments', to='app.ordonnance')),
            ],
        ),
        migrations.CreateModel(
            name='Radiologue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='radiologue_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Compte_Rendu',
            fields=[
                ('id_compte_rendu', models.AutoField(primary_key=True, serialize=False)),
                ('date_creation', models.DateTimeField(default=datetime.datetime.now)),
                ('texte', models.TextField()),
                ('dpi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compte_rendus', to='app.dpi')),
                ('examen_Radiologique', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.examen_radiologique')),
                ('radiologue', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.radiologue')),
            ],
        ),
        migrations.CreateModel(
            name='Resultat_Biologique',
            fields=[
                ('id_resultat', models.AutoField(primary_key=True, serialize=False)),
                ('parametre', models.TextField(choices=[('HEMOGLOBINE', 'Hemoglobine'), ('GLYCEMIE', 'Glycemie'), ('CHOLESTEROL', 'Cholesterol'), ('TRIGLYCERIDES', 'Triglycerides'), ('ACIDE_URIQUE', 'Acide Urique'), ('CREATININE', 'Creatinine'), ('UREE', 'Uree'), ('TSH', 'Tsh'), ('T4', 'T4'), ('T3', 'T3'), ('PSA', 'Psa'), ('CRP', 'Crp'), ('FERRITINE', 'Ferritine')])),
                ('valeur', models.FloatField()),
                ('unite', models.CharField(max_length=20)),
                ('bilan_biologique', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resultats_biologiques', to='app.bilan_biologique')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id_resume', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('antecedents', models.JSONField(default=list)),
                ('consultation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resume', to='app.consultation')),
            ],
        ),
        migrations.CreateModel(
            name='Soin',
            fields=[
                ('id_soin', models.AutoField(primary_key=True, serialize=False)),
                ('date_soin', models.DateTimeField(default=datetime.datetime.now)),
                ('soin_infirmier', models.CharField(blank=True, choices=[('i', 'injection'), ('p', 'pansement'), ('s', 'prelevement_sanguin'), ('f', 'perfusion')], default='i', max_length=1)),
                ('observation_patient', models.TextField(max_length=200)),
                ('dpi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='soins', to='app.dpi')),
                ('infirmier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='soins', to='app.infirmier')),
            ],
        ),
        migrations.CreateModel(
            name='AdminMedicament',
            fields=[
                ('id_admin_medicament', models.AutoField(primary_key=True, serialize=False)),
                ('advice', models.TextField(max_length=1000)),
                ('soin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_medicament', to='app.soin')),
            ],
        ),
        migrations.AddField(
            model_name='decompte_des_frais',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.admin'),
        ),
    ]
