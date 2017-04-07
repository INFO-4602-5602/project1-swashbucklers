# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Account(models.Model):
	account_id = models.CharField( max_length=15, primary_key=True )
	industry = models.CharField( max_length=50, null=True, blank=True )
	vertical = models.CharField( max_length=50, null=True, blank=True )
	total_brr = models.FloatField( null=True, blank=True )
	annual_revenue = models.FloatField( null=True, blank=True )
	number_of_employees = models.IntegerField()
	dandb_revenue = models.FloatField( null=True, blank=True )
	dandb_total_employees = models.IntegerField()

	def __unicode__(self):
		return self.account_id

class Building(models.Model):
	building_id = models.CharField( max_length=15, primary_key=True )
	market = models.CharField( max_length=50 )
	street_address = models.CharField( max_length=50 )
	city = models.CharField( max_length=50 )
	state = models.CharField( max_length=5 )
	postal_code = models.CharField(max_length=10, null=True, blank=True )
	latitude = models.CharField(max_length=10, null=True, blank=True )
	longitude = models.CharField(max_length=10, null=True, blank=True )
	zayo_network_status = models.CharField( max_length=50 )
	net_classification = models.CharField( max_length=20 )
	building_type = models.CharField( max_length=50 )
	network_proximity = models.FloatField( null=True, blank=True )
	estimated_build_cost = models.FloatField()

	def __unicode__(self):
		return self.building_id

class Site(models.Model):
	site_id = models.CharField( max_length=15, primary_key=True )
	account = models.ForeignKey(Account)
	building = models.ForeignKey(Building)

	def __unicode__(self):
		return self.site_id

class Cpq(models.Model):
	cpq_id = models.CharField( max_length=15, primary_key=True )
	account = models.ForeignKey( Account, null=True, blank=True )
	created_date = models.DateField()
	product_group = models.CharField(max_length=50)
	x36_mrc_list = models.FloatField( null=True, blank=True )
	x36_nrr_list = models.FloatField( null=True, blank=True )
	x36_npv_list = models.FloatField( null=True, blank=True )
	building = models.ForeignKey(Building)

	def __unicode__(self):
		return self.cpq_id

class Opportunity(models.Model):
	opportunity_id = models.CharField( max_length=15, primary_key=True )
	account = models.ForeignKey( Account, null=True, blank=True )
	stage_name = models.CharField(max_length=50)
	is_closed = models.BooleanField()
	is_won = models.BooleanField()
	created_date = models.DateField()
	term_in_months = models.IntegerField( null=True, blank=True )
	service = models.CharField( max_length=50, null=True, blank=True )
	opportunity_type = models.CharField( max_length=50, null=True, blank=True )
	product_group = models.CharField(max_length=50)
	building = models.ForeignKey(Building)

	def __unicode__(self):
		return self.opportunity_id

class Service(models.Model):
	service_id = models.CharField( max_length=15, primary_key=True )
	account = models.ForeignKey( Account, null=True, blank=True )
	total_mrr = models.FloatField( null=True, blank=True )
	next_mrc = models.FloatField( null=True, blank=True )
	product_group = models.CharField(max_length=50)
	status = models.CharField(max_length=20)
	building_id = models.CharField( max_length=15, null=True, blank=True )
	street_address = models.CharField( max_length=50, null=True, blank=True )
	city = models.CharField( max_length=50, null=True, blank=True )
	state = models.CharField( max_length=5, null=True, blank=True )
	postal_code = models.CharField(max_length=10, null=True, blank=True )
	country = models.CharField(max_length=50, null=True, blank=True )

class Market(models.Model):
	market = models.CharField( max_length=50 )
	base_cost = models.FloatField()
	distance_less_500_ft = models.FloatField()
	distance_greater_500_ft = models.FloatField()