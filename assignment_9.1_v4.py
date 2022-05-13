#first step is to import our libraries, noteably the requests library
#you will need to download the requests library, if you do not have it already
import json
import requests

#here we use a while loop to allow the user to run the program multiple times
while True:
	#here we use the main function
	def main():
		#the user inputs the city they wish to know the weather for
		city=input("Enter the city name or zipcode: ")
		print()

		#here we use our API key to connect to our webservice and then convert the results from json
		def weather_info(query):
			api= "acf3e20cc24ca3b0c786b5d5bd4ad252"
			url = "http://api.openweathermap.org/data/2.5/weather?"
			whole_url = url + "appid=" + api +"&q=" + city
			res=requests.get(whole_url);
			return res.json();

		#here we query our city based on user input, we check to see if the city exists, 
		#then print an error message if we cannot locate it
		#This also checks whether the user input valid data or not
		#i.e. a real city and then displays an error message if so
		try:
			query='&q='+city;
			w_data=weather_data(query);
			disyplay_info(w_data, city)
			print()
		except:
			print("City name not found")
			print()

		#here we display the weather information, most noteably the temperature in 
		#a nice and readible format
		def display_info(weather, city):
			print("{}'s temperature: {} C".format(city, weather['main']['temp']))
			print()

		#Here we test connection with the web service via a try block. 
		#we also print a message indicating whether it was successful or not
		try:
			response.raise_for_status()
			print('Connection was successful')
			print()
		except:
			print('Connection was not succesful')
			print()


	if __name__=='__main__':
		main()

	#This allows the user to re-run the program
	another_search = input(('Do you want infomration on a different city? (yes or no): '))
	print()

	#This breaks the loop and prints a goodbye message
	if another_search == 'no' or another_search == 'n':
		print("Have a nice day!")
		break 