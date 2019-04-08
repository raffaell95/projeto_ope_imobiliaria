from django.db import models


class Aluguel(models.Model):
    id_aluguel = models.IntegerField()
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_imovel = models.ForeignKey('Imovel', models.DO_NOTHING, db_column='id_imovel', blank=True, null=True)
    id_corretor = models.ForeignKey('Corretor', models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    data_aluguel = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    contrato = models.CharField(max_length=100, blank=True, null=True)
    valor_aluguel = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluguel'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boleto(models.Model):
    id_boleto = models.IntegerField()
    id_aluguel = models.ForeignKey(Aluguel, models.DO_NOTHING, db_column='id_aluguel', blank=True, null=True)
    id_venda = models.ForeignKey('Venda', models.DO_NOTHING, db_column='id_venda', blank=True, null=True)
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    data_vencimento = models.DateField(blank=True, null=True)
    valor_boleto = models.FloatField(blank=True, null=True)
    multa_juros = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleto'


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nome_cliente = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Contato(models.Model):
    id_contato = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='propietario', blank=True, null=True)
    id_corretor = models.ForeignKey('Corretor', models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    telefone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contato'


class Corretor(models.Model):
    id_corretor = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=100, blank=True, null=True)
    registro = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corretor'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Endereco(models.Model):
    id_endereco = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_imovel = models.ForeignKey('Imovel', models.DO_NOTHING, db_column='id_imovel', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endereco'


class Imovel(models.Model):
    id_imovel = models.IntegerField(db_column='Id_imovel')  # Field name made lowercase.
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='Id_propietario', blank=True, null=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    matricula = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    iptu = models.CharField(max_length=100, blank=True, null=True)
    metro_quadrado = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imovel'


class LoginUsuario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    senha = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'login_usuario'


class Mensagens(models.Model):
    id_mensagens = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    assunto = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data_envio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensagens'


class Propietario(models.Model):
    id_propietario = models.IntegerField(primary_key=True)
    nome_propietario = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propietario'


class Venda(models.Model):
    id_venda = models.IntegerField()
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_propietario = models.ForeignKey(Propietario, models.DO_NOTHING, db_column='id_propietario', blank=True, null=True)
    id_imovel = models.ForeignKey(Imovel, models.DO_NOTHING, db_column='Id_imovel', blank=True, null=True)  # Field name made lowercase.
    id_corretor = models.ForeignKey(Corretor, models.DO_NOTHING, db_column='id_corretor', blank=True, null=True)
    data_venda = models.DateField(blank=True, null=True)
    valor_imovel = models.FloatField(blank=True, null=True)
    valor_venda = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venda'
