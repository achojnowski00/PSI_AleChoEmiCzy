from django.db import models

class Type (models.Model):
    id_type = models.AutoField(primary_key=True)
    name_type = models.CharField(max_length=45)

    def __str__(self):
        return self.name_type

    class Meta:
        verbose_name_plural = "Types"

class Sneakers (models.Model):
    id_sneakers = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    price = models.FloatField()
    stock = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    size = models.IntegerField()
    color_way = models.CharField(max_length=45)
    type = models.ForeignKey(Type, related_name = 'sneakers', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.color_way}'

    class Meta:
        verbose_name_plural = "Sneakers"

class Clients(models.Model):
    id_client = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Clients"

class Orders(models.Model):
    id_order = models.AutoField(primary_key=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField()
    payment_method = models.CharField(max_length=20)
    payment_date = models.DateTimeField()
    shipment_method = models.CharField(max_length=20)
    sneakers =  models.ForeignKey(Sneakers,related_name='orders', on_delete=models.CASCADE)
    client =  models.ForeignKey(Clients, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.id_order)}, {str(self.id_client)}'
        
    class Meta:
        verbose_name_plural = "Orders"


