from django.db import models


class Workers(models.Model):
    email = models.EmailField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Workers, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()


class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    author = models.ForeignKey(Workers, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    add_date = models.DateField()