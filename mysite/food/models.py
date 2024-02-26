from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    rest_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default = 1
   
    )
    prod_code = models.IntegerField(default=50)
    # for_user = models.CharField(
    #     max_length=100,
    #     default='RestOwner'
    # )
    added_by = models.CharField(
        max_length =50,
        default='user',
    
    )
    
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(
        max_length=500,
        default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae ratione ipsum tenetur quos expedita distinctio eligendi ea rem eum accusamus sit, dolore possimus tempore, veritatis qui dignissimos officiis fugiat quibusdam.'
    )
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://www.fnasafety.com/wp-content/uploads/2016/04/ComingSoon2-fnasafety.png"
    )

    def __str__(self):
        return str(
            (
                self.item_name,
                self.prod_code,
                self.rest_owner
            )
        )
    
class History(models.Model):
    
    username = models.CharField(max_length=100)
    prod_code = models.IntegerField()
    item_name = models.CharField(max_length=100)
    operation_type = models.CharField(max_length=100) 
    user_type = models.CharField(max_length=100)

    def __str__(self):
        return str(
            {
                self.prod_code,
                self.item_name,
                self.username,
                self.user_type,
                self.operation_type,   
            }
        )   



class NavbarForm(models.Model):
    data = models.CharField(max_length=100)

    def __str__(self):
        return str(
            self.data
        )
    
    
    
