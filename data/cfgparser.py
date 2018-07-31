# -*- coding: utf-8 -*-

import ConfigParser

""" Interface to manage .cfg conf files.
	No error checking implemented"""
 
########################### user_list.cfg ##########################
def add_user(self,
	uid,name,birth_date, license_year, total_km, n_session):

	config = ConfigParser.SafeConfigParser()
	config.add_section(uid)
	config.set(uid, u'name', name)
	config.set(uid, u'birth_date', birth_date)
	config.set(uid, u'license_year', license_year)
	config.set(uid, u'total_km', total_km)
	config.set(uid, u'n_session', n_session)

	with open('data/user_list.cfg', 'ab+') as configfile:
		config.write(configfile)

def remove_user(uid):
	config = ConfigParser.SafeConfigParser()
	config.read('data/user_list.cfg')
	config.remove_section(uid)

	with open('data/user_list.cfg', 'ab+') as configfile:
		config.write(configfile)

def getDict(section,Config):
	dict1 = {}
	options = Config.options(section)
	for option in options:
		try:
			dict1[option] = Config.get(section, option)
			if dict1[option] == -1:
				DebugPrint("skip: %s" % option)
		except:
			print("exception on %s!" % option)
			dict1[option] = None
	return dict1

def get_users(): #return
	config = ConfigParser.SafeConfigParser()
	config.read('data/user_list.cfg')
	users = config.sections() #['user1','user2',...]]
	user_list = [] # each user is a dictionary with all the information
	
	for u in users:
		one_user=getDict(u,config)
		user_list.append(one_user)
	return user_list	

############################ car_list.cfg ##############################

def add_car(car_id,maker,model, gear_box, n_gears):

	config = ConfigParser.SafeConfigParser()
	config_pid = ConfigParser.SafeConfigParser() #PIDS
	config.add_section(car_id)
	config.set(car_id, u'maker', maker)
	config.set(car_id, u'model', model)
	config.set(car_id, u'gear_box', gear_box)
	config.set(car_id, u'n_gears', n_gears)

	with open('data/car_list.cfg', 'ab+') as configfile:
		config.write(configfile)
	
	#PIDS
	config_pid.add_section(car_id)
	with open('data/pid_list.cfg', 'ab+') as configfile:
		config_pid.write(configfile)

def remove_car(car_id):
	config = ConfigParser.SafeConfigParser()
	config.read('data/car_list.cfg')
	config.remove_section(car_id)

	with open('data/car_list.cfg', 'ab+') as configfile:
		config.write(configfile)

def get_cars(): #return
	config = ConfigParser.SafeConfigParser()
	config.read('data/car_list.cfg')
	cars = config.sections() #['car1','car2',...]]
	car_list = [] # each car is a dictionary with all the information
	
	for c in cars:
		one_car=getDict(c,config)
		car_list.append(one_car)
	return car_list
############################ pid_list.cfg ##############################

def get_pids():
	config = ConfigParser.SafeConfigParser()
	config.read('data/pid_list.cfg')
	#store all possible pids known by the python obd library in [0]
	pids = config.sections()
	pid_list = []
	
	for p in pids:
		one_pid_car = getDict(p,config)
		pid_list.append(one_pid_car)
	return pid_list

def add_pids(car,pid_number,pid_description):
	config = ConfigParser.SafeConfigParser()
	config.read('data/pid_list.cfg')

	config.set(car, unicode(pid_number), unicode(pid_description))

	with open('data/pid_list.cfg', 'ab+') as configfile:
		config.write(configfile)
##ADD PID list returned from the manufacturer

#~ add_user(u'user1',u'Alfredo Ferreras',u'16/03/1994', u'2018',u'500',u'0')
#~ add_user(u'user2',u'Senior Rezungon',u'23/05/1974', u'1992',u'85000',u'2')
#~ add_user(u'user3',u'Seniora Conductora',u'8/01/1961', u'1983',u'175000',u'1')

#~ add_car(u'car1',u'obdsim',u'OBDII',u'Automatic',u'*')
#~ add_car(u'car2',u'Renault',u'Zoe',u'Automatic', u'*')
#~ add_car(u'car3',u'Mercedes',u'Class E',u'Standard',u'6')

#~ usuarios = get_users()

#~ for u in usuarios:
	#~ print u['name']

#~ print usuarios[2]['total_km'] # se almacenan en orden del archivo de configuración

#~ coches = get_cars()

#~ for c in coches:
	#~ print c['model']

#~ print coches[0],'\n',coches[2]

#~ pids = get_pids()

#~ for p in pids:
	#~ print p

#~ print '\n\n', p
# ~ try:
	# ~ remove_user(u'user2')
# ~ except NoSectionError as ne:
	# ~ print ne.message


