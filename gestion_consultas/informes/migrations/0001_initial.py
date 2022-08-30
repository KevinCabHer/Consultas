# Generated by Django 3.0.14 on 2022-08-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbAlarma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_device', models.IntegerField(blank=True, db_column='Id_Device', null=True)),
                ('alarma', models.TextField(blank=True, db_column='Alarma', null=True)),
                ('billingtransaciondate', models.CharField(blank=True, db_column='BillingTransacionDate', max_length=300, null=True)),
            ],
            options={
                'db_table': 'Tb_Alarma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbAppstate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_appstate', models.IntegerField(blank=True, db_column='Id_AppState', null=True)),
                ('appsatedescription', models.CharField(blank=True, db_column='AppSateDescription', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Tb_AppState',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBilling',
            fields=[
                ('id_billing', models.BigAutoField(db_column='Id_Billing', primary_key=True, serialize=False)),
                ('billingnumber', models.DecimalField(db_column='BillingNumber', decimal_places=0, max_digits=18)),
                ('billingtransaciondate', models.DateTimeField(db_column='BillingTransacionDate')),
                ('billingtotal', models.DecimalField(db_column='BillingTotal', decimal_places=0, max_digits=18)),
                ('billingtax', models.DecimalField(db_column='BillingTax', decimal_places=0, max_digits=18)),
                ('ibillingpaymentdata', models.TextField(blank=True, db_column='IBillingPaymentData', null=True)),
            ],
            options={
                'db_table': 'Tb_Billing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbBillingdetail',
            fields=[
                ('id_billingdetail', models.BigAutoField(db_column='Id_BillingDetail', primary_key=True, serialize=False)),
                ('id_billing', models.BigIntegerField(db_column='Id_Billing')),
                ('billinglinenumber', models.IntegerField(db_column='BillingLineNumber')),
                ('productquantity', models.IntegerField(db_column='ProductQuantity')),
                ('productoprice', models.DecimalField(db_column='ProductoPrice', decimal_places=0, max_digits=18)),
                ('totallinebilling', models.DecimalField(db_column='TotalLineBilling', decimal_places=0, max_digits=18)),
                ('billinlinedate', models.DateTimeField(db_column='BillinLineDate')),
                ('billinlinedata', models.TextField(blank=True, db_column='BillinLineData', null=True)),
            ],
            options={
                'db_table': 'Tb_BillingDetail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCatalogproducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Tb_CatalogProducts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCatalogue',
            fields=[
                ('id_catalogue', models.AutoField(db_column='Id_Catalogue', primary_key=True, serialize=False)),
                ('cataloguename', models.CharField(blank=True, db_column='CatalogueName', max_length=50, null=True)),
                ('cataloguedescription', models.CharField(blank=True, db_column='CatalogueDescription', max_length=200, null=True)),
                ('cataloguedata', models.TextField(blank=True, db_column='CatalogueData', null=True)),
            ],
            options={
                'db_table': 'Tb_Catalogue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCategory',
            fields=[
                ('id_category', models.AutoField(db_column='Id_Category', primary_key=True, serialize=False)),
                ('categoryname', models.CharField(blank=True, db_column='CategoryName', max_length=50, null=True)),
                ('categorydata', models.TextField(blank=True, db_column='CategoryData', null=True)),
            ],
            options={
                'db_table': 'Tb_Category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCity',
            fields=[
                ('id_city', models.IntegerField(db_column='Id_City', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('citydistrict', models.CharField(db_column='CityDistrict', max_length=20)),
            ],
            options={
                'db_table': 'Tb_City',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbClient',
            fields=[
                ('id_client', models.BigAutoField(db_column='Id_Client', primary_key=True, serialize=False)),
                ('clientname', models.CharField(db_column='ClientName', max_length=50)),
            ],
            options={
                'db_table': 'Tb_Client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCompany',
            fields=[
                ('id_company', models.AutoField(db_column='Id_Company', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=250)),
                ('oid', models.CharField(db_column='OID', max_length=100)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=500, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=50, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=250, null=True)),
                ('note', models.CharField(blank=True, db_column='Note', max_length=500, null=True)),
            ],
            options={
                'db_table': 'Tb_Company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbCountry',
            fields=[
                ('id_country', models.CharField(db_column='Id_Country', max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100)),
            ],
            options={
                'db_table': 'Tb_Country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbDevice',
            fields=[
                ('id_device', models.AutoField(db_column='ID_Device', primary_key=True, serialize=False)),
                ('devicename', models.CharField(blank=True, db_column='DeviceName', max_length=50, null=True)),
                ('isactive', models.BooleanField(db_column='IsActive')),
                ('devicelastconnect', models.DateTimeField(blank=True, db_column='DeviceLastConnect', null=True)),
            ],
            options={
                'db_table': 'Tb_Device',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbDevicetype',
            fields=[
                ('id_devicetype', models.AutoField(db_column='Id_DeviceType', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=150)),
            ],
            options={
                'db_table': 'Tb_DeviceType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbDevicezone',
            fields=[
                ('id_devicezone', models.AutoField(db_column='Id_DeviceZone', primary_key=True, serialize=False)),
                ('devicezonename', models.CharField(blank=True, db_column='DeviceZoneName', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Tb_DeviceZone',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbPaymentmethod',
            fields=[
                ('id_paymentmethod', models.AutoField(db_column='Id_PaymentMethod', primary_key=True, serialize=False)),
                ('paymentmethodname', models.CharField(blank=True, db_column='PaymentMethodName', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Tb_PaymentMethod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbProduct',
            fields=[
                ('id_product', models.AutoField(db_column='Id_Product', primary_key=True, serialize=False)),
                ('productname', models.CharField(blank=True, db_column='ProductName', max_length=50, null=True)),
                ('productpicture', models.TextField(blank=True, db_column='ProductPicture', null=True)),
                ('productprice', models.DecimalField(blank=True, db_column='ProductPrice', decimal_places=0, max_digits=18, null=True)),
                ('productdata', models.TextField(blank=True, db_column='ProductData', null=True)),
            ],
            options={
                'db_table': 'Tb_Product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbResolutions',
            fields=[
                ('id_resolution', models.IntegerField(db_column='Id_Resolution', primary_key=True, serialize=False)),
                ('resolutionnumber', models.CharField(db_column='ResolutionNumber', max_length=50)),
                ('dateiniresolution', models.DateField(db_column='DateIniResolution')),
                ('dateendresolution', models.DateField(db_column='DateEndResolution')),
                ('billingininumber', models.IntegerField(db_column='BillingIniNumber')),
                ('billingendnumber', models.IntegerField(db_column='BillingEndNumber')),
                ('billingnumber', models.IntegerField(db_column='BillingNumber')),
                ('isactive', models.BooleanField(blank=True, db_column='IsActive', null=True)),
                ('prefijo', models.CharField(blank=True, db_column='Prefijo', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Tb_Resolutions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_statistics', models.CharField(db_column='Id_Statistics', max_length=36)),
                ('id_device', models.IntegerField(db_column='Id_device')),
                ('statisticsdate', models.DateTimeField(db_column='StatisticsDate')),
                ('id_appstate', models.IntegerField(db_column='Id_AppState')),
                ('statisticsdata', models.TextField(blank=True, db_column='StatisticsData', null=True)),
            ],
            options={
                'db_table': 'Tb_Statistics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbTransactions',
            fields=[
                ('id_transaction', models.BigAutoField(db_column='Id_transaction', primary_key=True, serialize=False)),
                ('id_transactiontype', models.IntegerField(db_column='Id_TransactionType')),
                ('id_device', models.IntegerField(db_column='Id_Device')),
                ('id_catalogue', models.IntegerField(db_column='Id_Catalogue')),
                ('transactiondate', models.DateTimeField(db_column='TransactionDate')),
                ('id_billing', models.BigIntegerField(blank=True, db_column='ID_Billing', null=True)),
                ('transactionimage', models.TextField(blank=True, db_column='TransactionImage', null=True)),
                ('transactiondeep', models.IntegerField(blank=True, db_column='TransactionDeep', null=True)),
                ('transactionmessage', models.TextField(blank=True, db_column='TransactionMessage', null=True)),
            ],
            options={
                'db_table': 'Tb_Transactions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbTransactiontype',
            fields=[
                ('id_transactiontype', models.AutoField(db_column='Id_TransactionType', primary_key=True, serialize=False)),
                ('transactiontypename', models.CharField(blank=True, db_column='TransactionTypeName', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Tb_TransactionType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TbTrazabilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_device', models.CharField(blank=True, db_column='Id_Device', max_length=100, null=True)),
                ('transacciondate', models.CharField(blank=True, db_column='TransaccionDate', max_length=100, null=True)),
                ('route', models.CharField(blank=True, db_column='Route', max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Tb_Trazabilidad',
                'managed': False,
            },
        ),
    ]
