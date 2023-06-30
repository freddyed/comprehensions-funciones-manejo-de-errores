import utils

data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)



    country = input('Type Country => ')

    result = utils.population_by_country(data, country)
    print(result)

# Llama almetodo run() si es corrido desde la terminal
# permite una dualidad de correr como script o por terminal
if __name__ == '__main__':
    run()
