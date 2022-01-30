import socket
import time

# gibt die verschiedenen Dienste aus
def get_user_options():
	print("\n")
	for i in range(len(options)):
		print(f"{i+1:}: {options[i+1]}")

def get_info_host_and_domain():
	"""
		User kann von sich, aber auch Websiten den Host und IP-Adresse bekommen
	"""
	print(f"Your Host:\n{socket.gethostname()}\n")
	print(f"Your IP-Adresse:\n{socket.gethostbyname(socket.gethostname())}")
	while True:
		user_input = input("\nType Domain:\n")
		try:
			print(f"\nHost:\n{socket.gethostbyname(user_input)}\n")
			print(f"IP-Adresse:\n{socket.gethostbyaddr(socket.gethostbyname(user_input))}\n")
		except:
			print("\nSomething went wrong\n")
		check = input("Again?[yes/no]:\n").lower()
		if check == "no":
			break

def time_server():
	"""
		User kann über einen Zeitserver die Sekunden ab 1900 abfragen
	"""
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	url = 'ptbtime1.ptb.de'
	port = 123
	request = '\x1b' + 47 * '\0' 
	client.sendto(request.encode('utf-8'), (url, port))
	data = client.recvfrom(256)
	print(f"Data:\n{data[0][16:20]}\n")
	data = list(data[0][16:20])
	seconds = 0
	data.reverse()

	for i in range(len(data)):
		seconds += data[i] * (256**i)
	print(f"Seconds since 1.1.1900:\n{seconds}\n")

def http_client():
	pass

def echo_server():
	pass

# Dienste 
options = {
	1: "host and domain",
	2: "Zeit-Client",
	3: "HTTP-Client",
	4: "Echo-Server"
}

# Weiterleitung an Dienst
choose_function = {
	1: get_info_host_and_domain,
	2: time_server,
	3: http_client,
	4: echo_server
}

# Start
if __name__ == "__main__":
	print("[WELCOME]")
	print("You can choose between the following options:")
	time.sleep(1)
	get_user_options()

	while True:
		user_choose = int(input("\nChoose one of them [1, 2, 3, 4]:\n"))
		choose_function[user_choose]()

		see_options_again = input("\nDo you want to see the options again [yes/no]:\n").lower()
		if see_options_again == "yes":
			get_user_options()

		quit_programm = input("\nQuit [yes/no]:\n").lower()
		if quit_programm == "yes":
			quit()
