Communication contract capital finder
Microservice A

To REQUEST data: 

Open a file country_input.txt and write a country name into it. Close the file and add a sleep time of 5 seconds to it. 

EXAMPLE: 

with open("country_input.txt.", "w+") as f:
  f.write("united kingdom")
  f.close()
time.sleep(5)

To RECEIVE data:

Open a file country_output.txt and read the contents of the file. 

EXAMPLE:

with open("country_output.txt", "r+") as f:
  capital = f.read()
  f.close()

<img width="964" alt="Screen Shot 2024-05-20 at 10 22 24 PM" src="https://github.com/veenessaly/361_cityMicroservice/assets/67206999/e4845e87-ba3a-48cd-ad13-1a201a35dd7a">
