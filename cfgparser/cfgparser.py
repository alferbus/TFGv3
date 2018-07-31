# -*- coding: utf-8 -*-

import ConfigParser

""" Interface to manage .cfg conf files.
	No error checking implemented"""

########################### user_list.cfg ##############################

def add_user(uid,name,birth_date, license_year, total_km, n_session):

	config = ConfigParser.SafeConfigParser()
	config.add_section(uid)
	config.set(uid, u'name', name)
	config.set(uid, u'birth_date', birth_date)
	config.set(uid, u'license_year', license_year)
	config.set(uid, u'total_km', total_km)
	config.set(uid, u'n_session', n_session)

	with open('user_list.cfg', 'ab+') as configfile:
		config.write(configfile)

def remove_user(uid):
	config = ConfigParser.SafeConfigParser()
	config.read('user_list.cfg')
	config.remove_section(uid)

	with open('user_list.cfg', 'ab+') as configfile:
		config.write(configfile)

############################ car_list.cfg ##############################

def add_car(car_id,maker,model, gear_box, n_gears):

	config = ConfigParser.SafeConfigParser()
	config_pid = ConfigParser.SafeConfigParser() #PIDS
	config.add_section(car_id)
	config.set(car_id, u'maker', maker)
	config.set(car_id, u'model', model)
	config.set(car_id, u'gear_box', gear_box)
	config.set(car_id, u'n_gears', n_gears)

	with open('car_list.cfg', 'ab+') as configfile:
		config.write(configfile)
	
	#PIDS
	config_pid.add_section(car_id)
	with open('pid_list.cfg', 'ab+') as configfile:
		config_pid.write(configfile)

def remove_car(car_id):
	config = ConfigParser.SafeConfigParser()
	config.read('car_list.cfg')
	config.remove_section(car_id)

	with open('car_list.cfg', 'ab+') as configfile:
		config.write(configfile)

############################ pid_list.cfg ##############################

##ADD PID list returned from the manufacturer

add_user(u'user1',u'Alfredo Ferreras',u'16/03/1994', u'2018',u'500',u'0')
add_user(u'user2',u'Senior Rezungon',u'23/05/1974', u'1992',u'85000',u'2')
add_user(u'user3',u'Seniora Conductora',u'8/01/1961', u'1983',u'175000',u'1')

add_car(u'car1',u'obdsim',u'OBDII',u'Automatic',u'*')
add_car(u'car2',u'Renault',u'Zoe',u'Automatic', u'*')
add_car(u'car3',u'Mercedes',u'Class E',u'Standard',u'6')


# ~ try:
	# ~ remove_user(u'user2')
# ~ except NoSectionError as ne:
	# ~ print ne.message


