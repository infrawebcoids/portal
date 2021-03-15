# Generated by Django 3.0.8 on 2021-03-03 19:25

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=255, null=True, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=255, null=True, verbose_name='Modelo')),
                ('serie', models.CharField(max_length=255, null=True, verbose_name='Serial')),
                ('patrimonio', models.CharField(max_length=255, null=True, verbose_name='Patrimônio')),
                ('descricao', models.CharField(max_length=255, null=True, verbose_name='Descrição')),
                ('garantia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Garantia')),
                ('status', models.CharField(default='Ativo', max_length=255, null=True, verbose_name='Status')),
                ('rack_tamanho', models.IntegerField(default=2, null=True, verbose_name='Tamanho em U')),
                ('rack_posicao', models.IntegerField(default=0, null=True, verbose_name='Posição no Rack')),
                ('consumo', models.CharField(max_length=255, null=True, verbose_name='Consumo nominal (Watts)')),
                ('tipo', models.CharField(max_length=255, verbose_name='Tipo')),
                ('tipo_uso', models.CharField(choices=[('', ''), ('OPERACIONAL', 'OPERACIONAL'), ('DESENVOLVIMENTO', 'DESENVOLVIMENTO'), ('PESQUISA', 'PESQUISA'), ('DOCUMENTO', 'DOCUMENTO')], max_length=255, verbose_name='Tipo de Uso')),
            ],
        ),
        migrations.CreateModel(
            name='Rede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rede', models.CharField(max_length=255, verbose_name='Rede')),
                ('ip', models.CharField(max_length=255, null=True, unique=True, verbose_name='IP')),
                ('prioridade_montagem', models.IntegerField(help_text='A prioridade de montagem é utilizada quando o Portal cria o Automount Locations e o equipamento possui mais de uma rede com NFS de discos, o MAIOR VALOR tem a prioridade', null=True, verbose_name='prioridade de montagem')),
            ],
        ),
        migrations.CreateModel(
            name='StorageArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255, verbose_name='Area')),
                ('tipo', models.CharField(choices=[('Disk Space', 'Disk Space'), ('Quota', 'Quota')], max_length=255)),
                ('capacidade', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Capacidade (T)')),
            ],
            options={
                'verbose_name': 'StorageArea',
                'verbose_name_plural': 'StorageArea',
            },
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='infra.Equipamento')),
                ('nome', models.CharField(blank=True, max_length=255, null=True, verbose_name='hostname')),
                ('configuracao', models.TextField(blank=True, null=True, verbose_name='Configuração')),
                ('ldap', models.BooleanField(blank=True, default=False, null=True, verbose_name='ldap')),
            ],
            options={
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
                'ordering': ['nome'],
            },
            bases=('infra.equipamento',),
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='infra.Equipamento')),
                ('aquisicao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Aquisição')),
                ('fonte', models.CharField(blank=True, max_length=255, null=True, verbose_name='Fonte')),
                ('protocolo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Protocolo')),
                ('controladora', models.IntegerField(blank=True, null=True, verbose_name='Número de controladoras')),
                ('atualizacao', models.DateTimeField(blank=True, null=True, verbose_name='atualizacao')),
            ],
            options={
                'verbose_name': 'Storage',
                'verbose_name_plural': 'Storages',
            },
            bases=('infra.equipamento',),
        ),
        migrations.CreateModel(
            name='Supercomputador',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='infra.Equipamento')),
                ('arquitetura', models.CharField(blank=True, max_length=255, null=True, verbose_name='Arquitetura')),
                ('nos', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nós Computacionais')),
                ('desempenho_pico', models.CharField(blank=True, max_length=255, null=True, verbose_name='Desempenho Pico')),
                ('desempenho_efetivo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Desempenho Efetivo')),
                ('memoria', models.CharField(blank=True, max_length=255, null=True, verbose_name='Memória')),
                ('kafka_topico_realtime', models.CharField(blank=True, max_length=255, null=True, verbose_name='Kafka Tópico Realtime')),
                ('kafka_topico_historico', models.CharField(blank=True, max_length=255, null=True, verbose_name='Kafka Tópico Histórico')),
            ],
            options={
                'verbose_name': 'Supercomputador',
                'verbose_name_plural': 'Supercomputador',
            },
            bases=('infra.equipamento',),
        ),
        migrations.CreateModel(
            name='StorageAreaGrupoTrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Quota (T)')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.GrupoTrabalho', verbose_name='Grupo')),
                ('storage_area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='infra.StorageArea', verbose_name='Area')),
            ],
            options={
                'verbose_name': 'Storage',
                'verbose_name_plural': 'Storage',
            },
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack', models.CharField(max_length=255, verbose_name='Rack')),
                ('marca', models.CharField(max_length=255, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=255, verbose_name='Modelo')),
                ('serie', models.CharField(max_length=255, verbose_name='Serial')),
                ('patrimonio', models.CharField(max_length=255, verbose_name='Patrimônio')),
                ('posicao_linha_inicial', models.CharField(max_length=2, null=True, verbose_name='Linha Inicial')),
                ('posicao_linha_final', models.CharField(max_length=2, null=True, verbose_name='Linha Final')),
                ('posicao_coluna_inicial', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(64)], verbose_name='Coluna Inicial')),
                ('posicao_coluna_final', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(64)], verbose_name='Coluna Final')),
                ('pdu1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Primeiro PDU')),
                ('pdu2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Segundo PDU')),
                ('consumo', models.IntegerField(verbose_name='Consumo Limite')),
                ('tamanho', models.IntegerField(default=44, verbose_name='Tamanho (U)')),
                ('kvm_posicao', models.IntegerField(blank=True, null=True, verbose_name='Posição do KVM')),
                ('predio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Predio', verbose_name='Prédio')),
            ],
            options={
                'ordering': ['predio', 'posicao_linha_inicial', 'posicao_coluna_inicial'],
            },
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocorrencia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ocorrência')),
                ('descricao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição')),
                ('data', models.DateTimeField(default=datetime.datetime.now, verbose_name='data')),
                ('equipamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infra.Equipamento', verbose_name='Equipamento')),
            ],
            options={
                'verbose_name': 'Ocorrência',
                'verbose_name_plural': 'Ocorrências',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='HostnameIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=255, verbose_name='Hostname')),
                ('ip', models.CharField(max_length=255, null=True, unique=True, verbose_name='IP')),
                ('reservado', models.BooleanField(blank=True, default=False, null=True, verbose_name='Reservado')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='infra.Rede')),
            ],
            options={
                'verbose_name': 'HostName IP',
                'verbose_name_plural': 'HostNames e IPs',
                'ordering': ['hostname'],
            },
        ),
        migrations.CreateModel(
            name='EquipamentoGrupoAcesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infra.Equipamento')),
                ('grupo_acesso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.GrupoAcesso')),
            ],
            options={
                'verbose_name': 'Grupo Acesso do Equipamento',
                'verbose_name_plural': 'Grupos Acesso do Equipamento',
                'ordering': ['grupo_acesso__grupo_acesso'],
            },
        ),
        migrations.AddField(
            model_name='equipamento',
            name='grupos_acesso',
            field=models.ManyToManyField(through='infra.EquipamentoGrupoAcesso', to='core.GrupoAcesso', verbose_name='Grupos de Acesso'),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='predio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Predio', verbose_name='Prédio'),
        ),
        migrations.AddField(
            model_name='equipamento',
            name='rack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='infra.Rack', verbose_name='Rack'),
        ),
        migrations.CreateModel(
            name='StorageGrupoAcessoMontagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.CharField(blank=True, max_length=255, null=True)),
                ('svm_name', models.CharField(blank=True, max_length=255, null=True)),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('path', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo', models.CharField(blank=True, max_length=255, null=True)),
                ('namespace', models.CharField(blank=True, max_length=255, null=True)),
                ('montagem', models.CharField(blank=True, max_length=255, null=True)),
                ('automount', models.CharField(blank=True, max_length=255, null=True)),
                ('parametro', models.CharField(blank=True, max_length=255, null=True)),
                ('grupo_trabalho', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.GrupoTrabalho')),
                ('rede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infra.Rede')),
                ('storage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='infra.Storage')),
            ],
        ),
        migrations.AddField(
            model_name='storagearea',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infra.Storage', verbose_name='Storage'),
        ),
        migrations.CreateModel(
            name='ServidorHostnameIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostnameip', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='infra.HostnameIP', verbose_name='Hostname')),
                ('servidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infra.Servidor')),
            ],
            options={
                'verbose_name': 'Hostname',
                'verbose_name_plural': 'Hostnames',
                'ordering': ['servidor__rack_posicao'],
                'unique_together': {('hostnameip',)},
            },
        ),
        migrations.AddField(
            model_name='servidor',
            name='hostname_ip',
            field=models.ManyToManyField(through='infra.ServidorHostnameIP', to='infra.HostnameIP'),
        ),
        migrations.AddField(
            model_name='servidor',
            name='vinculado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='servidor_vinculo', to='infra.Equipamento', verbose_name='Equipamento Vinculado'),
        ),
        migrations.CreateModel(
            name='EquipamentoParte',
            fields=[
                ('equipamento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='infra.Equipamento')),
                ('configuracao', models.TextField(blank=True, null=True, verbose_name='Configuração')),
                ('vinculado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='equipamentoparte_vinculo', to='infra.Equipamento', verbose_name='Equipamento Vinculado')),
            ],
            options={
                'verbose_name': 'Parte de Equipamento',
                'verbose_name_plural': 'Partes de Equipamento',
            },
            bases=('infra.equipamento',),
        ),
        migrations.CreateModel(
            name='AmbienteVirtual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('virtualizador', models.CharField(max_length=255, verbose_name='virtualizador')),
                ('versao', models.CharField(max_length=255, verbose_name='versao')),
                ('servidor', models.ManyToManyField(to='infra.Servidor')),
            ],
        ),
    ]