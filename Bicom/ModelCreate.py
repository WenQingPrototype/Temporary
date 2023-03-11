# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:35:45 2023

@author: 柴文清
"""

from django.db import models
'''
  ` result_id` int(11) NOT NULL AUTO_INCREMENT,
  `lga_name` varchar(50) NOT NULL,
  `party_abbreviation` char(4) NOT NULL,
  `party_score` int(11) NOT NULL,
  `entered_by_user` varchar(50) NOT NULL,
  `date_entered` datetime NOT NULL,
  `user_ip_address` varchar(50) NOT NULL,
  PRIMARY KEY (`result_id`)
'''

#create models

class announced_lga_results(models.Model):
    result_id =models.IntegerField(max_length=11)
    lga_name = models.CharField(max_length=40)
    party_abbreviation = models.CharField(max_length=4)
    entered_by_user = models.CharField(max_length=50)
    party_score =models.IntegerField(max_length=11)
    date_entered = models.DateField(verbose_name='date')
    user_ip_address = models.CharField(max_length=50,primary_key=True)

'''
DROP TABLE IF EXISTS `announced_pu_results`;
CREATE TABLE IF NOT EXISTS `announced_pu_results` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `polling_unit_uniqueid` varchar(50) NOT NULL,
  `party_abbreviation` char(4) NOT NULL,
  `party_score` int(11) NOT NULL,
  `entered_by_user` varchar(50) NOT NULL,
  `date_entered` datetime NOT NULL,
  `user_ip_address` varchar(50) NOT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=261 ;

'''
class announced_pu_results(models.Model):
    result_id =models.IntegerField(max_length=11,primary_key=True)
    lga_name = models.CharField(max_length=40)
    party_abbreviation = models.CharField(max_length=4)
    entered_by_user = models.CharField(max_length=50)
    party_score =models.IntegerField(max_length=11)
    date_entered = models.DateField(verbose_name='date')
    user_ip_address = models.CharField(max_length=50)
    
'''
DROP TABLE IF EXISTS `announced_state_results`;
CREATE TABLE IF NOT EXISTS `announced_state_results` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `state_name` varchar(50) NOT NULL,
  `party_abbreviation` char(4) NOT NULL,
  `party_score` int(11) NOT NULL,
  `entered_by_user` varchar(50) NOT NULL,
  `date_entered` datetime NOT NULL,
  `user_ip_address` varchar(50) NOT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

'''
class announced_state_results(models.Model):
    result_id =models.IntegerField(max_length=11,primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    entered_by_user = models.CharField(max_length=50)
    party_score =models.IntegerField(max_length=11)
    date_entered = models.DateField(verbose_name='date')
    user_ip_address = models.CharField(max_length=50)
    
'''
DROP TABLE IF EXISTS `announced_ward_results`;
CREATE TABLE IF NOT EXISTS `announced_ward_results` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `ward_name` varchar(50) NOT NULL,
  `party_abbreviation` char(4) NOT NULL,
  `party_score` int(11) NOT NULL,
  `entered_by_user` varchar(50) NOT NULL,
  `date_entered` datetime NOT NULL,
  `user_ip_address` varchar(50) NOT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

'''
class announced_ward_results_results(models.Model):
    result_id =models.IntegerField(max_length=11,primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    entered_by_user = models.CharField(max_length=50)
    party_score =models.IntegerField(max_length=11)
    date_entered = models.DateField(verbose_name='date')
    user_ip_address = models.CharField(max_length=50)
'''
DROP TABLE IF EXISTS `lga`;
CREATE TABLE IF NOT EXISTS `lga` (
  `uniqueid` int(11) NOT NULL AUTO_INCREMENT,
  `lga_id` int(11) NOT NULL,
  `lga_name` varchar(50) NOT NULL,
  `state_id` int(50) NOT NULL,
  `lga_description` text,
  `entered_by_user` varchar(50) NOT NULL,
  `date_entered` datetime NOT NULL,
  `user_ip_address` varchar(50) NOT NULL,
  PRIMARY KEY (`uniqueid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=26 ;
'''
class lga(models.Model):
    unique_id =models.IntegerField(max_length=11,primary_key=True)
    lga_id =models.IntegerField(max_length=11)
    lga_name = models.CharField(max_length=50)
    state_id = models.IntergerField(max_length=50)
    lga_description = models.CharField(max_length=300)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateField(verbose_name='date')
    user_ip_address = models.CharField(max_length=50)
    
'''
DROP TABLE IF EXISTS `party`;
CREATE TABLE IF NOT EXISTS `party` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `partyid` varchapartyr(11) NOT NULL,
  `partyname` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;
'''
class party(models.Model):
    id =models.IntegerField(max_length=11,primary_key=True)
    partyid =models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)
'''
DROP TABLE IF EXISTS `polling_unit`;
CREATE TABLE IF NOT EXISTS `polling_unit` (
  `uniqueid` int(11) NOT NULL AUTO_INCREMENT,
  `polling_unit_id` int(11) NOT NULL,
  `ward_id` int(11) NOT NULL,
  `lga_id` int(11) NOT NULL,
  `uniquewardid` int(11) DEFAULT NULL,
  `polling_unit_number` varchar(50) DEFAULT NULL,
  `polling_unit_name` varchar(50) DEFAULT NULL,
  `polling_unit_description` text,
  `lat` varchar(255) DEFAULT NULL,
  `long` varchar(255) DEFAULT NULL,
  `entered_by_user` varchar(50) DEFAULT NULL,
  `date_entered` datetime DEFAULT NULL,
  `user_ip_address` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uniqueid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=280 ;
'''
class polling_unit(models.Model):
    uniqueid =models.IntegerField(max_length=11,primary_key=True)
    polling_unit_id =models.IntegerField(max_length=11)
    ward_id =models.IntegerField(max_length=11)
    lga_id =models.IntegerField(max_length=11)
    uniquewardid =models.IntegerField(max_length=11)
    polling_unit_number = models.CharField(max_length=50)
    polling_unit_name = models.CharField(max_length=50)
    polling_unit_description = models.CharField(max_length=300)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateField(verbose_name='date')
    user_ip_address = models.CharField(max_length=50)

'''
DROP TABLE IF EXISTS `states`;
CREATE TABLE IF NOT EXISTS `states` (
  `state_id` int(11) NOT NULL,
  `state_name` varchar(50) NOT NULL,
  PRIMARY KEY (`state_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
'''

class state(models.Model):
    state_id =models.CharField(max_length=11,primary_key=True)
    state_name = models.CharField(max_length=50)

'''

DROP TABLE IF EXISTS `ward`;
CREATE TABLE IF NOT EXISTS `ward` (
  `uniqueid` int(11) NOT NULL AUTO_INCREMENT,
  `ward_id` int(11) NOT NULL,
  `ward_name` varchar(50) NOT NULL,
  `lga_id` int(11) NOT NULL,
  `ward_description` text,
  `entered_by_user` varchar(50) NOT NULL,
  `date_entered` datetime NOT NULL,
  `user_ip_address` varchar(50) NOT NULL,
  PRIMARY KEY (`uniqueid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=264 ;

'''
class polling_unit(models.Model):
    uniqueid =models.IntegerField(max_length=11,primary_key=True)
    ward_id =models.IntegerField(max_length=11)
    ward_name =models.IntegerField(max_length=50)
    lga_id =models.IntegerField(max_length=11)
    ward_description = models.CharField(max_length=300)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateField(verbose_name='date')
    user_ip_address = models.CharField(max_length=50)

