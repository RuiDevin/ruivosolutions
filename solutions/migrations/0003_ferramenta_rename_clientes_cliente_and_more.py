# Generated by Django 4.2.4 on 2023-08-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("solutions", "0002_caixa_clientes_funcionarios_itemestoque_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ferramenta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "codigo",
                    models.CharField(
                        choices=[
                            ("FDC", "Ferramentas de Celular"),
                            ("FDPC", "Ferramentas de Computador"),
                            ("FDN", "Ferramentas de Notebook"),
                        ],
                        default="FDC",
                        max_length=4,
                        unique=True,
                    ),
                ),
                ("descricao", models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name="Clientes",
            new_name="Cliente",
        ),
        migrations.RenameModel(
            old_name="Funcionarios",
            new_name="Funcionario",
        ),
        migrations.DeleteModel(
            name="Ferramentas",
        ),
    ]
