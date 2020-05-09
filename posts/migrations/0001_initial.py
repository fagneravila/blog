# Generated by Django 3.0.5 on 2020-05-04 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_post', models.CharField(max_length=255, verbose_name='Titulo')),
                ('data_post', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('conteudo_post', models.TextField(verbose_name='Conteudo')),
                ('excerto_post', models.TextField(verbose_name='Execerto')),
                ('imagem_post', models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d', verbose_name='Imagem')),
                ('publicado_post', models.BooleanField(default=False, verbose_name='Publicado')),
                ('autor_post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categoria_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.Categoria', verbose_name='Categoria')),
            ],
        ),
    ]
