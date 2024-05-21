import time
from country_request import country_requests

def main():
    # While true:
    while True:
        # Sleep for 1 second
        time.sleep(1)
        # check which country selected
        with open('country_input.txt', 'r+') as f:
            read_country = f.read()
            print(read_country)
            # check with api which cities the are
            capital = country_requests(read_country)
            # write to output file a list of cities or make my own file with top 5 cities in each country?
            f.close()
        with open('country_output.txt', "w+") as output_file:
            print(capital)
            output_file.write(capital)
            output_file.close()


if __name__== "__main__":
    main()