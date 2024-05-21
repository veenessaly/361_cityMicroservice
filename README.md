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
