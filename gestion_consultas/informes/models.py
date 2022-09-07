# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbAlarma(models.Model):
    id_device = models.IntegerField(db_column='Id_Device', blank=True, null=True)  # Field name made lowercase.
    alarma = models.TextField(db_column='Alarma', blank=True, null=True)  # Field name made lowercase.
    billingtransaciondate = models.CharField(db_column='BillingTransacionDate', max_length=300, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.alarma
    
    class Meta:
        managed = False
        db_table = 'Tb_Alarma'


class TbAppstate(models.Model):
    id_appstate = models.IntegerField(db_column='Id_AppState', blank=True, null=True)  # Field name made lowercase.
    appsatedescription = models.CharField(db_column='AppSateDescription', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.appsatedescription
    
    class Meta:
        managed = False
        db_table = 'Tb_AppState'


class TbBilling(models.Model):
    id_billing = models.BigAutoField(db_column='Id_Billing', primary_key=True)  # Field name made lowercase.
    id_device = models.ForeignKey('TbDevice', models.DO_NOTHING, db_column='Id_Device')  # Field name made lowercase.
    id_client = models.ForeignKey('TbClient', models.DO_NOTHING, db_column='Id_Client')  # Field name made lowercase.
    billingnumber = models.DecimalField(db_column='BillingNumber', max_digits=18, decimal_places=0)  # Field name made lowercase.
    billingtransaciondate = models.DateTimeField(db_column='BillingTransacionDate')  # Field name made lowercase.
    billingtotal = models.DecimalField(db_column='BillingTotal', max_digits=18, decimal_places=0)  # Field name made lowercase.
    billingtax = models.DecimalField(db_column='BillingTax', max_digits=18, decimal_places=0)  # Field name made lowercase.
    id_paymentmethod = models.ForeignKey('TbPaymentmethod', models.DO_NOTHING, db_column='Id_PaymentMethod')  # Field name made lowercase.
    ibillingpaymentdata = models.TextField(db_column='IBillingPaymentData', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.id_billing)
    
    class Meta:
        managed = False
        db_table = 'Tb_Billing'


class TbBillingdetail(models.Model):
    id_billingdetail = models.BigAutoField(db_column='Id_BillingDetail', primary_key=True)  # Field name made lowercase.
    id_billing = models.BigIntegerField(db_column='Id_Billing')  # Field name made lowercase.
    billinglinenumber = models.IntegerField(db_column='BillingLineNumber')  # Field name made lowercase.
    id_product = models.ForeignKey('TbProduct', models.DO_NOTHING, db_column='Id_Product')  # Field name made lowercase.
    productquantity = models.IntegerField(db_column='ProductQuantity')  # Field name made lowercase.
    productoprice = models.DecimalField(db_column='ProductoPrice', max_digits=18, decimal_places=0)  # Field name made lowercase.
    totallinebilling = models.DecimalField(db_column='TotalLineBilling', max_digits=18, decimal_places=0)  # Field name made lowercase.
    billinlinedate = models.DateTimeField(db_column='BillinLineDate')  # Field name made lowercase.
    billinlinedata = models.TextField(db_column='BillinLineData', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.id_billingdetail
    
    class Meta:
        managed = False
        db_table = 'Tb_BillingDetail'


class TbCatalogproducts(models.Model):
    id_catalogue = models.ForeignKey('TbCatalogue', models.DO_NOTHING, db_column='Id_Catalogue')  # Field name made lowercase.
    id_product = models.ForeignKey('TbProduct', models.DO_NOTHING, db_column='Id_Product')  # Field name made lowercase.

    def __str__(self):
        return self.id_catalogue
    
    class Meta:
        managed = False
        db_table = 'Tb_CatalogProducts'


class TbCatalogue(models.Model):
    id_catalogue = models.AutoField(db_column='Id_Catalogue', primary_key=True)  # Field name made lowercase.
    cataloguename = models.CharField(db_column='CatalogueName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cataloguedescription = models.CharField(db_column='CatalogueDescription', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cataloguedata = models.TextField(db_column='CatalogueData', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.cataloguename
    
    class Meta:
        managed = False
        db_table = 'Tb_Catalogue'


class TbCategory(models.Model):
    id_category = models.AutoField(db_column='Id_Category', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    categorydata = models.TextField(db_column='CategoryData', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.categoryname
    
    class Meta:
        managed = False
        db_table = 'Tb_Category'


class TbCity(models.Model):
    id_city = models.IntegerField(db_column='Id_City', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    id_country = models.ForeignKey('TbCountry', models.DO_NOTHING, db_column='Id_Country')  # Field name made lowercase.
    citydistrict = models.CharField(db_column='CityDistrict', max_length=20)  # Field name made lowercase.

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'Tb_City'
        
    


class TbClient(models.Model):
    id_client = models.BigAutoField(db_column='Id_Client', primary_key=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=50)  # Field name made lowercase.

    def __str__(self):
        return self.clientname
    
    class Meta:
        managed = False
        db_table = 'Tb_Client'


class TbCompany(models.Model):
    id_company = models.AutoField(db_column='Id_Company', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250)  # Field name made lowercase.
    oid = models.CharField(db_column='OID', max_length=100)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=250, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=500, blank=True, null=True)  # Field name made lowercase.
    id_country = models.ForeignKey('TbCountry', models.DO_NOTHING, db_column='Id_Country', blank=True, null=True)  # Field name made lowercase.
    id_city = models.ForeignKey(TbCity, models.DO_NOTHING, db_column='Id_City', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'Tb_Company'


class TbCountry(models.Model):
    id_country = models.CharField(db_column='Id_Country', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'Tb_Country'


class TbDevice(models.Model):
    id_device = models.AutoField(db_column='ID_Device', primary_key=True)  # Field name made lowercase.
    id_devicetype = models.ForeignKey('TbDevicetype', models.DO_NOTHING, db_column='Id_DeviceType')  # Field name made lowercase.
    devicename = models.CharField(db_column='DeviceName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_devizezone = models.ForeignKey('TbDevicezone', models.DO_NOTHING, db_column='Id_DevizeZone')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    id_catalogo = models.ForeignKey(TbCatalogue, models.DO_NOTHING, db_column='Id_Catalogo')  # Field name made lowercase.
    id_company = models.ForeignKey(TbCompany, models.DO_NOTHING, db_column='Id_Company', blank=True, null=True)  # Field name made lowercase.
    devicelastconnect = models.DateTimeField(db_column='DeviceLastConnect', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.id_device)
    
    class Meta:
        managed = False
        db_table = 'Tb_Device'


class TbDevicetype(models.Model):
    id_devicetype = models.AutoField(db_column='Id_DeviceType', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'Tb_DeviceType'


class TbDevicezone(models.Model):
    id_devicezone = models.AutoField(db_column='Id_DeviceZone', primary_key=True)  # Field name made lowercase.
    devicezonename = models.CharField(db_column='DeviceZoneName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.devicezonename)
    
    class Meta:
        managed = False
        db_table = 'Tb_DeviceZone'


class TbPaymentmethod(models.Model):
    id_paymentmethod = models.AutoField(db_column='Id_PaymentMethod', primary_key=True)  # Field name made lowercase.
    paymentmethodname = models.CharField(db_column='PaymentMethodName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.paymentmethodname
    
    class Meta:
        managed = False
        db_table = 'Tb_PaymentMethod'


class TbProduct(models.Model):
    id_product = models.AutoField(db_column='Id_Product', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_category = models.ForeignKey(TbCategory, models.DO_NOTHING, db_column='Id_Category')  # Field name made lowercase.
    productpicture = models.TextField(db_column='ProductPicture', blank=True, null=True)  # Field name made lowercase.
    productprice = models.DecimalField(db_column='ProductPrice', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    productdata = models.TextField(db_column='ProductData', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.productname
    
    class Meta:
        managed = False
        db_table = 'Tb_Product'


class TbResolutions(models.Model):
    id_resolution = models.IntegerField(db_column='Id_Resolution', primary_key=True)  # Field name made lowercase.
    resolutionnumber = models.CharField(db_column='ResolutionNumber', max_length=50)  # Field name made lowercase.
    dateiniresolution = models.DateField(db_column='DateIniResolution')  # Field name made lowercase.
    dateendresolution = models.DateField(db_column='DateEndResolution')  # Field name made lowercase.
    billingininumber = models.IntegerField(db_column='BillingIniNumber')  # Field name made lowercase.
    billingendnumber = models.IntegerField(db_column='BillingEndNumber')  # Field name made lowercase.
    id_device = models.ForeignKey(TbDevice, models.DO_NOTHING, db_column='Id_Device')  # Field name made lowercase.
    billingnumber = models.IntegerField(db_column='BillingNumber')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    prefijo = models.CharField(db_column='Prefijo', max_length=10, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.resolutionnumber
    
    class Meta:
        managed = False
        db_table = 'Tb_Resolutions'


class TbStatistics(models.Model):
    id_statistics = models.CharField(db_column='Id_Statistics', max_length=36)  # Field name made lowercase.
    id_device = models.IntegerField(db_column='Id_device')  # Field name made lowercase.
    statisticsdate = models.DateTimeField(db_column='StatisticsDate')  # Field name made lowercase.
    id_appstate = models.IntegerField(db_column='Id_AppState')  # Field name made lowercase.
    statisticsdata = models.TextField(db_column='StatisticsData', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.statisticsdata
    
    class Meta:
        managed = False
        db_table = 'Tb_Statistics'


class TbTransactiontype(models.Model):
    id_transactiontype = models.AutoField(db_column='Id_TransactionType', primary_key=True)  # Field name made lowercase.
    transactiontypename = models.CharField(db_column='TransactionTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.transactiontypename
    
    class Meta:
        managed = False
        db_table = 'Tb_TransactionType'


class TbTransactions(models.Model):
    id_transaction = models.BigAutoField(db_column='Id_transaction', primary_key=True)  # Field name made lowercase.
    id_transactiontype = models.IntegerField(db_column='Id_TransactionType')  # Field name made lowercase.
    id_device = models.IntegerField(db_column='Id_Device')  # Field name made lowercase.
    id_catalogue = models.IntegerField(db_column='Id_Catalogue')  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TransactionDate')  # Field name made lowercase.
    id_billing = models.BigIntegerField(db_column='ID_Billing', blank=True, null=True)  # Field name made lowercase.
    transactionimage = models.TextField(db_column='TransactionImage', blank=True, null=True)  # Field name made lowercase.
    transactiondeep = models.IntegerField(db_column='TransactionDeep', blank=True, null=True)  # Field name made lowercase.
    transactionmessage = models.TextField(db_column='TransactionMessage', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.id_transaction
    
    class Meta:
        managed = False
        db_table = 'Tb_Transactions'


class TbTrazabilidad(models.Model):
    id_device = models.CharField(db_column='Id_Device', max_length=100, blank=True, null=True)  # Field name made lowercase.
    transacciondate = models.CharField(db_column='TransaccionDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    route = models.CharField(db_column='Route', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.state
    
    class Meta:
        managed = False
        db_table = 'Tb_Trazabilidad'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
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


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)