from django.db import models
from django.core.validators import MinValueValidator

class Sistemascomputo(models.Model):
    
    nombre = models.CharField(max_length = 20, verbose_name = 'Nombre')
    pais_origen = models.CharField(max_length = 54, verbose_name = 'País de origen')
    ram = models.FloatField(null = True, blank = True, validators = [MinValueValidator(0.0)], verbose_name = 'RAM (TB)') 
    rom = models.FloatField(null = True, blank = True, validators = [MinValueValidator(0.0)], verbose_name = 'ROM (TB)') 
    flops = models.FloatField(null = True, blank = True, validators = [MinValueValidator(0.0)], verbose_name = 'TeraFLops')
    OPCIONES_SO = [
        ('AlmaLinux', 'AlmaLinux'),
        ('CentOS', 'CentOS'),
        ('Debian', 'Debian'),
        ('FreeBSD', 'FreeBSD'),
        ('Linux', 'Linux'),
        ('Oracle Linux', 'Oracle Linux'),
        ('Red Hat Enterprise Linux', 'Red Hat Enterprise Linux'),
        ('Rocky Linux', 'Rocky Linux'),
        ('SUSE Linux Enterprise Server', 'SUSE Linux Enterprise Server'),
        ('Ubuntu Server', 'Ubuntu Server'),
        ('Unix', 'Unix'),
        ('Windows Server', 'Windows Server'),
        ('Otro', 'Otro')
    ]
    
    so = models.CharField(max_length = 30, blank = True, choices = OPCIONES_SO, verbose_name = 'Sistema Operativo')

    def __str__(self):
        
        return f'{self.nombre} ({self.pais_origen})'