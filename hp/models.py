from django.db import models

# Create your models here.
from django.db import models

class Tranceiver(models.Model):
	tranceiver_type = models.CharField(max_length=30)


	def __str__(self):
		return "%s" % (self.tranceiver_type)

class Switch_100M(models.Model):
	transceiver = models.ForeignKey(Tranceiver, on_delete=models.CASCADE)

	switch_model = models.CharField(max_length=100)

	HBASET = models.CharField(max_length=20)
	HFX = models.CharField(max_length=20)
	HLX = models.CharField(max_length=20, default='')
	HEX = models.CharField(max_length=20)
	HZX = models.CharField(max_length=20)
	HBD = models.CharField(max_length=20)
	HBU = models.CharField(max_length=20)


	def __str__(self):
		return self.switch_model

	class Meta:
		ordering = ['switch_model']


class Switch_1G(models.Model):
	transceiver = models.ForeignKey(Tranceiver, on_delete=models.CASCADE)

	switch_model = models.CharField(max_length=100)

	G_T = models.CharField(max_length=20)
	G_SX = models.CharField(max_length=20)
	G_LX = models.CharField(max_length=20)
	G_LH = models.CharField(max_length=20)
	G_EX = models.CharField(max_length=20)
	G_ZX = models.CharField(max_length=20)
	G_EZX_100KM = models.CharField(max_length=20)
	G_EZX_120KM = models.CharField(max_length=20)
	G_BD = models.CharField(max_length=20)
	G_BU = models.CharField(max_length=20)


	def __str__(self):
		return self.switch_model

	class Meta:
		ordering = ['switch_model']



class Switch_10G(models.Model):
	transceiver = models.ForeignKey(Tranceiver, on_delete=models.CASCADE)

	switch_model = models.CharField(max_length=100)

	SR = models.CharField(max_length=20)
	LRM = models.CharField(max_length=20)
	LR = models.CharField(max_length=20)
	ER = models.CharField(max_length=20)
	ZR = models.CharField(max_length=20)
	XFP_SR = models.CharField(max_length=20)
	XFP_LR = models.CharField(max_length=20)
	XFP_ER = models.CharField(max_length=20)
	XFP_ZR = models.CharField(max_length=20)
	DAC_05M = models.CharField(max_length=20)
	DAC_1M = models.CharField(max_length=20)
	DAC_3M = models.CharField(max_length=20)
	DAC_5M = models.CharField(max_length=20)
	DAC_7M = models.CharField(max_length=20)
	DAC_10M = models.CharField(max_length=20)
	DAC_15M = models.CharField(max_length=20)
	AOC_7M = models.CharField(max_length=20)
	AOC_10M = models.CharField(max_length=20)
	AOC_20M = models.CharField(max_length=20)
	X2_SR = models.CharField(max_length=20)
	X2_LRM = models.CharField(max_length=20)
	X2_LR = models.CharField(max_length=20)
	X2_ER = models.CharField(max_length=20)
	X2_ZR = models.CharField(max_length=20)



	def __str__(self):
		return self.switch_model

	class Meta:
		ordering = ['switch_model']