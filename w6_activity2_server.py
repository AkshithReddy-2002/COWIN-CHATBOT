
# No other modules apart from 'socket', 'BeautifulSoup', 'requests' and 'datetime'
# need to be imported as they aren't required to solve the assignment

# Import required module/s
import socket
from bs4 import BeautifulSoup
import requests
import datetime



# Define constants for IP and Port address of Server
# NOTE: DO NOT modify the values of these two constants
HOST = '127.0.0.1'
PORT = 10009


def fetchWebsiteData(url_website):
	"""Fetches rows of tabular data from given URL of a website with data excluding table headers

	Parameters
	----------
	url_website : str
		URL of a website

	Returns
	-------
	bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""
	
	web_page_data = ''

	##############	ADD YOUR CODE HERE	##############
	req=requests.get(url_website)
	soup=BeautifulSoup(req.text,'html.parser')
	web_page_data=soup.find('tbody').find_all('tr')
	##################################################

	return web_page_data


def fetchVaccineDoses(web_page_data):
	"""Fetch the Vaccine Doses available from the Web-page data and provide Options to select the respective Dose.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers

	Returns
	-------
	dict
		Dictionary with the Doses available and Options to select, with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineDoses(web_page_data))
	{'1': 'Dose 1', '2': 'Dose 2'}
	"""

	vaccine_doses_dict = {}
	lst=[]
	##############	ADD YOUR CODE HERE	##############
	for i in web_page_data:
		if(i.find('td',class_='dose_num').text) not in lst:
			lst.append(i.find('td',class_='dose_num').text)
	for i in range(len(lst)):
		if lst[i]=='1':
			s=str(i+1)
			vaccine_doses_dict[s]='Dose 1'
		if lst[i]=='2':
			s=str(i+1)
			vaccine_doses_dict[s]='Dose 2'	
	

	##################################################

	return vaccine_doses_dict


def fetchAgeGroup(web_page_data, dose):
	"""Fetch the Age Groups for whom Vaccination is available from the Web-page data for a given Dose
	and provide Options to select the respective Age Group.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Age Groups (for whom Vaccination is available for a given Dose) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchAgeGroup(web_page_data, '1'))
	{'1': '18+', '2': '45+'}
	>>> print(fetchAgeGroup(web_page_data, '2'))
	{'1': '18+', '2': '45+'}
	"""

	age_group_dict = {}
	l=[]
	##############	ADD YOUR CODE HERE	##############
	for i in web_page_data:
		if(i.find('td',class_='dose_num').text)==dose:
			if(i.find('td',class_='age').text) not in l:
				l.append(i.find('td',class_='age').text)
	l.sort()
	for i in range(len(l)):
		s=str(i+1)
		age_group_dict[s]=l[i]
	#print(age_group_dict)
	##################################################

	return age_group_dict


def fetchStates(web_page_data, age_group, dose):
	"""Fetch the States where Vaccination is available from the Web-page data for a given Dose and Age Group
	and provide Options to select the respective State.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the States (where the Vaccination is available for a given Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchStates(web_page_data, '18+', '1'))
	{
		'1': 'Andhra Pradesh', '2': 'Arunachal Pradesh', '3': 'Bihar', '4': 'Chandigarh', '5': 'Delhi', '6': 'Goa',
		'7': 'Gujarat', '8': 'Harayana', '9': 'Himachal Pradesh', '10': 'Jammu and Kashmir', '11': 'Kerala', '12': 'Telangana'
	}
	"""

	states_dict = {}
	l=[]
	##############	ADD YOUR CODE HERE	##############
	for i in web_page_data:
		if(i.find('td',class_='dose_num').text)==dose:
			if(i.find('td',class_='age').text)==age_group:
				if(i.find('td',class_='state_name').text) not in l:
					l.append(i.find('td',class_='state_name').text)
	l.sort()
	for i in range(len(l)):
		s=str(i+1)
		states_dict[s]=l[i]		
	#print(states_dict)
	##################################################

	return states_dict


def fetchDistricts(web_page_data, state, age_group, dose):
	"""Fetch the District where Vaccination is available from the Web-page data for a given State, Dose and Age Group
	and provide Options to select the respective District.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Districts (where the Vaccination is available for a given State, Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
	{
		'1': 'Kargil', '2': 'Leh'
	}
	"""

	districts_dict = {}
	l=[]
	##############	ADD YOUR CODE HERE	##############
	for i in web_page_data:
		if(i.find('td',class_='dose_num').text)==dose:
			if(i.find('td',class_='age').text)==age_group:
				if(i.find('td',class_='state_name').text)==state:
					if(i.find('td',class_='district_name').text) not in l:
					
					 					l.append(i.find('td',class_='district_name').text)
	l.sort()
	for i in range(len(l)):
		s=str(i+1)
		districts_dict[s]=l[i]		
	#print(districts_dict)
																													

	##################################################

	return districts_dict


def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	"""Fetch the Hospital and the Vaccine Names from the Web-page data available for a given District, State, Dose and Age Group
	and provide Options to select the respective Hospital and Vaccine Name.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Hosptial and Vaccine Names (where the Vaccination is available for a given District, State, Dose, Age Group)
		and Options to select, with Key as 'Option' and Value as another dictionary having Key as 'Hospital Name' and Value as 'Vaccine Name'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchHospitalVaccineNames(web_page_data, 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {
				'MedStar Hospital Center': 'Covaxin'
			}
	}
	>>> print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {
				'Eden Clinic': 'Covishield'
			}
	}
	"""
	
	hospital_vaccine_names_dict = {}
	lst=[]
	l=[]
	ls={}
	##############	ADD YOUR CODE HERE	##############
	for i in web_page_data:
		if (i.find('td',class_='dose_num').text==dose):
			if (i.find('td',class_='age').text==age_group) :
				if (i.find('td',class_='state_name').text==state) :
					if (i.find('td',class_='district_name').text==district):
						if not (i.find('td',class_='hospital_name').text) in lst:
							lst.append(i.find('td',class_='hospital_name').text)
							l.append((i.find('td',class_='vaccine_name').text))
	for i in range(len(lst)):
		ls[lst[0]]=l[0]
		s=str(i+1)
		hospital_vaccine_names_dict[s]=ls
	#print(hospital_vaccine_names_dict)
	

	##################################################

	return hospital_vaccine_names_dict


def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	"""Fetch the Dates and Slots available on those dates from the Web-page data available for a given Hospital Name, District, State, Dose and Age Group
	and provide Options to select the respective Date and available Slots.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	hospital_name : str
		Name of Hospital where Vaccination is available for given District, State, Dose and Age Group
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Dates and Slots available on those dates (where the Vaccination is available for a given Hospital Name,
		District, State, Dose, Age Group) and Options to select, with Key as 'Option' and Value as another dictionary having
		Key as 'Date' and Value as 'Available Slots'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineSlots(web_page_data, 'MedStar Hospital Center', 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '81'}, '3': {'May 17': '109'}, '4': {'May 18': '78'},
		'5': {'May 19': '89'}, '6': {'May 20': '57'}, '7': {'May 21': '77'}
	}
	>>> print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '137'}, '3': {'May 17': '50'}, '4': {'May 18': '78'},
		'5': {'May 19': '145'}, '6': {'May 20': '64'}, '7': {'May 21': '57'}
	}
	"""

	vaccine_slots = {}
	ls={}
	lst=[]
	##############	ADD YOUR CODE HERE	##############
	for i in web_page_data:
		if (i.find('td',class_='dose_num').text==dose):
			if (i.find('td',class_='age').text==age_group) :
				if (i.find('td',class_='state_name').text==state) :
					if (i.find('td',class_='district_name').text==district):
						if (i.find('td',class_='hospital_name').text==hospital_name):
							lst.append(i.find('td',class_='may_15').text)
							lst.append(i.find('td',class_='may_16').text)
							lst.append(i.find('td',class_='may_17').text)
							lst.append(i.find('td',class_='may_18').text)
							lst.append(i.find('td',class_='may_19').text)
							lst.append(i.find('td',class_='may_20').text)
							lst.append(i.find('td',class_='may_21').text)
							
	#print(lst)
	for i in range(len(lst)):
		ls={}
		if i==0:
			ls['May 15']=lst[i]
		if i==1:
			ls['May 16']=lst[i]
		if i==2:
			ls['May 17']=lst[i]
		if i==3:
			ls['May 18']=lst[i]
		if i==4:
			ls['May 19']=lst[i]
		if i==5:
			ls['May 20']=lst[i]
		if i==6:
			ls['May 21']=lst[i]
		s=str(i+1)
		vaccine_slots[s]=ls
	#print(vaccine_slots)
	

	##################################################

	return vaccine_slots


def openConnection():
	"""Opens a socket connection on the HOST with the PORT address.

	Returns
	-------
	socket
		Object of socket class for the Client connected to Server and communicate further with it
	tuple
		IP and Port address of the Client connected to Server
	"""

	client_socket = None
	client_addr = None
	ADDR=(HOST,PORT)
	#socket.setdefaulttimeout(10)

	##############	ADD YOUR CODE HERE	##############
	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind(ADDR)
	server.listen()
	client_socket,client_addr=server.accept()
        

	##################################################
	
	return client_socket, client_addr

flag=True
def startCommunication(client_conn, client_addr, web_page_data):
	"""Starts the communication channel with the connected Client for scheduling an Appointment for Vaccination.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	client_addr : tuple
		IP and Port address of the Client connected to Server
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""

	##############	ADD YOUR CODE HERE	##############
	print(f"Client is connected at: {client_addr}")
	msg="""
============================
# Welcome to CoWIN ChatBot # 
============================
	
Schedule an Appointment for Vaccination:

>>> Select the Dose of Vaccination:"""
	msg=msg+"\n"+str(fetchVaccineDoses(web_page_data))+"\n\n"
	client_conn.sendall(msg.encode('utf-8'))
	global flag	
	while True:
		if not flag:
			break
		
		function_1(client_conn,web_page_data)
	stopCommunication(client_conn)
	
		

	##################################################


def stopCommunication(client_conn):
	"""Stops or Closes the communication channel of the Client with a message.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	"""

	##############	ADD YOUR CODE HERE	##############
	client_conn.sendall("<<< See ya! Visit again :)".encode('utf-8'))
	
	
	client_conn.close()
	

	##################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################
count=0
def redirect1(client_conn,web_page_data):
	"""redirects to selecting dose"""
	message=">>> Select the Dose of Vaccination:"+"\n\n"
	message=message+str(fetchVaccineDoses(web_page_data))+"\n\n"
	client_conn.sendall(message.encode('utf-8'))
	function_1(client_conn,web_page_data)
def redirect1_22(client_conn,web_page_data,dose):
	"""redirects to selecting Age when dose 2 is selected succesfully"""
	message=">>> Select the Age Group:"
	message=message+"\n"+str(fetchAgeGroup(web_page_data, dose))+"\n\n"
	client_conn.sendall(message.encode('utf-8'))
	function_2d1(client_conn,web_page_data,dose)
def redirect1_2(client_conn,web_page_data,dose):
	"""redirects to selecting Age"""
	message=">>> Select the Age Group:"
	message=message+"\n"+str(fetchAgeGroup(web_page_data, dose))+"\n\n"
	client_conn.sendall(message.encode('utf-8'))
	function_2d1(client_conn,web_page_data,dose)
def redirect2_3(client_conn,web_page_data,age_group,dose):
	"""redirects to selecting the state"""
	message=">>> Select the State:"
	message=message+"\n"+str(fetchStates(web_page_data, age_group, dose))+"\n\n"
	client_conn.sendall(message.encode('utf-8'))
	function_3(client_conn,web_page_data,age_group,dose)
def redirect3_4(client_conn,web_page_data,state,age_group,dose):
	"""redirects to selecting the district"""
	message=">>> Select the District:"
	message=message+"\n"+str(fetchDistricts(web_page_data, state, age_group, dose))+"\n\n"
	client_conn.sendall(message.encode('utf-8'))
	function_4(client_conn,web_page_data,state,age_group,dose)
def redirect4_5(client_conn,web_page_data,districts,state,age_group,dose):
	"""redirects to selecting the vaccination centre"""
	message=">>> Select the Vaccination Center Name:"
	message=message+"\n"+str(fetchHospitalVaccineNames(web_page_data, districts, state, age_group, dose))+"\n\n"
	client_conn.sendall(message.encode('utf-8'))
	function_5(client_conn,web_page_data,districts,state,age_group,dose)
def redirect5_6(client_conn,web_page_data,hospital_name,districts,state,age_group,dose):
	"""redirects to selecting the vaccination slots"""
	message1=">>> Select one of the available slots to schedule the Appointment:"
	message1=message1+"\n"+str(fetchVaccineSlots(web_page_data, hospital_name, districts, state, age_group, dose))+"\n\n"
	client_conn.sendall(message1.encode('utf-8'))
	function_6(client_conn,web_page_data,hospital_name,districts,state,age_group,dose)
	
def function_6(client_conn,web_page_data,hospital_name,districts,state,age_group,dose):
	"""function when vaccination Center is selected correctly and used after redirection"""
	global flag
	global count
	input_from_client=client_conn.recv(1024).decode('utf-8')
	if input_from_client in fetchVaccineSlots(web_page_data, hospital_name, districts, state, age_group, dose).keys():
		selected_dict=fetchVaccineSlots(web_page_data, hospital_name, districts, state, age_group, dose)[input_from_client]
		selected_date="".join(selected_dict.keys())
		selected_slot=selected_dict[selected_date]
		message1="\n\n"+"<<< Selected Vaccination Appointment Date: "+selected_date+"\n"+"<<< Available Slots on the selected Date: "+selected_slot
		print("Vaccination Date selected: "+selected_date+"\n"+"Available Slots on that date: "+selected_slot)
		if int(selected_slot) == 0:
			message1=message1+"\n"+"<<< Selected Appointment Date has no available slots, select another date!"
			client_conn.sendall(message1.encode('utf-8'))
			count=0
			redirect5_6(client_conn,web_page_data,hospital_name,districts,state,age_group,dose)
			
			
		
		else:
			message1=message1+"\n"+"<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!\n"
			client_conn.sendall(message1.encode('utf-8'))
			count=0
			flag=False
	

		

	elif input_from_client=='b' or input_from_client=='B':
		redirect4_5(client_conn,web_page_data,districts,state,age_group,dose)
		count=0
	elif input_from_client=='q' or input_from_client=='Q':
		message="Client wants to quit!\nSaying Bye to client and closing the connection!"
		print(message)
		flag=False
		count=0
	else:
		count=count+1
		print("Invalid input detected "+str(count)+" time(s)!")
		message="<<< Invalid input provided "+str(count)+" time(s)! Try again."
		client_conn.sendall(message.encode('utf-8'))
		if count!=3:
			redirect5_6(client_conn,web_page_data,hospital_name,districts,state,age_group,dose)
		if(count==3):
			count=0
			print("Notifying the client and closing the connection!")
			flag=False
			
		

	

	
	
	
def function_5(client_conn,web_page_data,districts,state,age_group,dose):
	"""function when district is selected correctly and used after redirection when invalid"""
	global flag
	global count
	input_from_client=client_conn.recv(1024).decode('utf-8')
	if input_from_client in fetchHospitalVaccineNames(web_page_data, districts, state, age_group, dose).keys():
		message1="\n\n"+"<<< Selected Vaccination Center: "+("".join(fetchHospitalVaccineNames(web_page_data, districts, state, age_group, dose)[input_from_client].keys()))+"\n\n"+">>> Select one of the available slots to schedule the Appointment:"
		hospital_name="".join(fetchHospitalVaccineNames(web_page_data, districts, state, age_group, dose)[input_from_client].keys())
		message1=message1+"\n"+str(fetchVaccineSlots(web_page_data, hospital_name, districts, state, age_group, dose))+"\n\n"
		print("Hospital selected: "+hospital_name)
		client_conn.sendall(message1.encode('utf-8'))
		count=0
		function_6(client_conn,web_page_data,hospital_name,districts,state,age_group,dose)
	elif input_from_client=='b' or input_from_client=='B':
		redirect3_4(client_conn,web_page_data,state,age_group,dose)
		count=0
	elif input_from_client=='q' or input_from_client=='Q':
		message="Client wants to quit!\nSaying Bye to client and closing the connection!"
		print(message)
		flag=False
		count=0
	else:
		count=count+1
		print("Invalid input detected "+str(count)+" time(s)!")
		message="<<< Invalid input provided "+str(count)+" time(s)! Try again."
		client_conn.sendall(message.encode('utf-8'))
		if count!=3:
			redirect4_5(client_conn,web_page_data,districts,state,age_group,dose)
		if(count==3):
			count=0
			flag=False
			print("Notifying the client and closing the connection!")
			
			
		
	
def function_4(client_conn,web_page_data, state,age_group, dose):
	"""function when state is selected correctly and used after redirection when invalid"""
	global flag
	global count
	input_from_client=client_conn.recv(1024).decode('utf-8')
	if input_from_client in fetchDistricts(web_page_data, state, age_group, dose).keys():
		message1="\n\n"+"<<< Selected District: "+fetchDistricts(web_page_data, state, age_group, dose)[input_from_client]+"\n\n"+">>> Select the Vaccination Center Name:"
		message1=message1+"\n"+str(fetchHospitalVaccineNames(web_page_data, fetchDistricts(web_page_data, state, age_group, dose)[input_from_client], state, age_group, dose))+"\n\n"
		districts=fetchDistricts(web_page_data, state, age_group, dose)[input_from_client]
		print("District Selected: "+districts)
		client_conn.sendall(message1.encode('utf-8'))
		count=0
		function_5(client_conn,web_page_data,fetchDistricts(web_page_data, state, age_group, dose)[input_from_client],state,age_group,dose)
	elif input_from_client=='b' or input_from_client=='B':
		redirect2_3(client_conn,web_page_data,age_group,dose)
		count=0
	elif input_from_client=='q' or input_from_client=='Q':
		message="Client wants to quit!\nSaying Bye to client and closing the connection!"
		print(message)
		count=0
		flag=False
	else:
		count=count+1
		print("Invalid input detected "+str(count)+" time(s)!")
		message="<<< Invalid input provided "+str(count)+" time(s)! Try again."
		client_conn.sendall(message.encode('utf-8'))
		if count!=3:
			redirect3_4(client_conn,web_page_data,state,age_group, dose)
		if(count==3):
			count=0
			flag=False
			print("Notifying the client and closing the connection!")
			
			
		
	
	
def function_3(client_conn,web_page_data,age_group,dose):
	"""function when age_group is selected correctly and used after redirection when invalid"""
	global flag
	global count
	input_from_client=client_conn.recv(1024).decode('utf-8')

	if input_from_client in fetchStates(web_page_data, age_group, dose).keys():
		message1="\n\n"+"<<< Selected State: "+fetchStates(web_page_data, age_group, dose)[input_from_client]+"\n\n"+">>> Select the District:"
		state=fetchStates(web_page_data, age_group, dose)[input_from_client]
		message1=message1+"\n"+str(fetchDistricts(web_page_data, state, age_group, dose))+"\n\n"
		print("State selected: "+state)
		client_conn.sendall(message1.encode('utf-8'))
		count=0
		function_4(client_conn,web_page_data,fetchStates(web_page_data, age_group, dose)[input_from_client],age_group,dose)
	elif input_from_client=='b' or input_from_client=='B':
		redirect1_2(client_conn,web_page_data,dose)
		count=0
	elif input_from_client=='q' or input_from_client=='Q':
		message="Client wants to quit!\nSaying Bye to client and closing the connection!"
		print(message)
		count=0
		flag=False
		
		
	else:
		count=count+1
		print("Invalid input detected "+str(count)+" time(s)!")
		message="<<< Invalid input provided "+str(count)+" time(s)! Try again."
		client_conn.sendall(message.encode('utf-8'))
		if count!=3:
			redirect2_3(client_conn,web_page_data,age_group,dose)
		if(count==3):
			count=0
			flag=False
			print("Notifying the client and closing the connection!")
			
			
			
		
	
	
	
def function_2d2(client_conn,web_page_data):
	"""function when dose 2 is selected"""
	global flag
	input_from_client=client_conn.recv(1024).decode('utf-8')
	
	if input_from_client=='b' or input_from_client=='B':
		redirect1(client_conn,web_page_data)

	elif input_from_client!='q' and input_from_client!='Q':
		
		
		l=input_from_client.split('/')
		curr_date=str(datetime.date.today())
		l1=curr_date.split('-')
		d0=datetime.date(int(l[-1]),int(l[-2]),int(l[-3]))
		d1=datetime.date(int(l1[0]),int(l1[1]),int(l1[2]))
		diff=int((d1-d0).days)//7
		
		if diff<0:
			message="\n<<< Invalid Date provided of First Vaccination Dose: "+input_from_client
			message=message+"\n"+">>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021\n"
			client_conn.sendall(message.encode('utf-8'))
			function_2d2(client_conn,web_page_data)
		if diff>=4 and diff<=8:
			client_conn.send(b"\n\n<<< Date of First Vaccination Dose provided: "+bytes(str(input_from_client),'utf-8')+b'\n')
			client_conn.send(b"<<< Number of weeks from today: "+bytes(str(diff),'utf-8')+b'\n')
			client_conn.send(b"<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.\n")
			redirect1_22(client_conn,web_page_data,'2')
		elif diff>8:
			client_conn.send(b"\n\n<<< Date of First Vaccination Dose provided: "+bytes(str(input_from_client),'utf-8')+b'\n')
			client_conn.send(b"<<< Number of weeks from today: "+bytes(str(diff),'utf-8')+b'\n')
			client_conn.send(b"<<< You have been late in scheduling your 2nd Vaccination Dose by "+bytes(str(diff),'utf-8')+b" weeks.\n\n")
			redirect1_22(client_conn,web_page_data,'2')
		elif diff<4 and diff>=0:
			client_conn.send(b"<<< Date of First Vaccination Dose provided: "+bytes(str(input_from_client),'utf-8')+b'\n')
			client_conn.send(b"<<< Number of weeks from today: "+bytes(str(diff),'utf-8')+b'\n')
			message="\n"+"<<< You are not eligible right now for 2nd Vaccination Dose! Try after "
			message=message+str(4-diff)+" weeks."+"\n"
			client_conn.sendall(message.encode('utf-8'))
			flag=False
	else:
		message="Client wants to quit!\nSaying Bye to client and closing the connection!"
		print(message)
		flag=False

		
			

	
	
	
	
def function_2d1(client_conn,web_page_data,dose):
	"""function when dose is selected 1"""

	global flag
	global count
	input_from_client=client_conn.recv(1024).decode('utf-8')
	if input_from_client in fetchAgeGroup(web_page_data, dose).keys():
		message1="\n\n"+"<<< Selected Age Group: "+fetchAgeGroup(web_page_data, dose)[input_from_client]+"\n\n"+">>> Select the State:"
		age_group=fetchAgeGroup(web_page_data, dose)[input_from_client]
		print("Age Group selected: "+age_group)
		message1=message1+"\n"+str(fetchStates(web_page_data, age_group, dose))+"\n\n"
		client_conn.sendall(message1.encode('utf-8'))
		count=0
		function_3(client_conn,web_page_data,fetchAgeGroup(web_page_data, dose)[input_from_client],dose)
	elif input_from_client=='b' or input_from_client=='B':
		redirect1(client_conn,web_page_data)
		count=0
	elif input_from_client=='q' or input_from_client=='Q':
		message="Client wants to quit!\nSaying Bye to client and closing the connection!"
		print(message)
		flag=False
		
		
	else:
		count=count+1
		print("Invalid input detected "+str(count)+" time(s)!")
		message="<<< Invalid input provided "+str(count)+" time(s)! Try again."
		client_conn.sendall(message.encode('utf-8'))
		if count!=3:
			redirect1_2(client_conn,web_page_data,dose)
		if(count==3):
			count=0
			flag=False
			print("Notifying the client and closing the connection!")
			
			
		
	
	
def function_1(client_conn,web_page_data):
	global count
	global flag
	input_from_client=client_conn.recv(1024).decode('utf-8')
	if input_from_client=='1':
		message1="\n\n"+"<<< Dose selected: 1"+"\n\n"+">>> Select the Age Group:\n"
		message1=message1+str(fetchAgeGroup(web_page_data, '1'))+"\n\n"
		client_conn.sendall(message1.encode('utf-8'))
		count=0
		print("Dose selected: 1")
		function_2d1(client_conn,web_page_data,'1')
		
	elif input_from_client=='2':
		message2="\n\n"+"<<< Dose selected: 2"+"\n\n"+">>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021"+"\n"	
		client_conn.sendall(message2.encode('utf-8'))
		print("Dose selected: 2")
		function_2d2(client_conn,web_page_data)
		count=0
	elif input_from_client=='b' or input_from_client=='B':
		redirect1(client_conn,web_page_data)
		count=0
	elif input_from_client=='q' or input_from_client=='Q':
		message="Client wants to quit!\nSaying Bye to client and closing the connection!"
		print(message)
		flag=False
		count=0
		
		
	else:
		count=count+1
		print("Invalid input detected "+str(count)+" time(s)!")
		message="<<< Invalid input provided "+str(count)+" time(s)! Try again."
		client_conn.sendall(message.encode('utf-8'))
		if count!=3:
			redirect1(client_conn,web_page_data)
		if(count==3):
			count=0
			flag=False
			print("Notifying the client and closing the connection!")
			
			
			


##############################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	
	client_conn, client_addr = openConnection()
	startCommunication(client_conn, client_addr, web_page_data)
	
