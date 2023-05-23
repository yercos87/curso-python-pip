import utils
import read_csv
import charts
#print(dir(utils))



def run():
    data = read_csv.read_csv('world_population.csv')
    data = list(filter(lambda item: item["Continent"] == "South America", data))

    countries = list(map(lambda x: x["Country"], data))
    percentages = list(map(lambda x: float(x["World Population Percentage"]), data))
    charts.generate_pie_chart(countries, percentages)



   
    country = input("Type Country ==> ")
    #print(country)
    
    result = utils.population_by_country(data, country)
    print(result)

    if len(result) > 0:
        country = result[0]
        #print(country['Country'])
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels,values)
 

if __name__ == "__main__":
    run()