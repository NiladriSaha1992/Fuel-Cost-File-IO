# importing modules
import Fuel

try:
  # reading the content of FuelRecordsInput file
  f1 = open('FuelRecordsInput.txt', 'r')  # open this file in read mode
  
  # reading the entire file content of the input file
  fileContent = f1.read()

  # creating a list with the above file contents
  ListOfContents = fileContent.split('\n')

  # making a group of the elements in contentList list for each vehicle
  subListOfContents = [ListOfContents[n:n+3] for n in range(0, len(ListOfContents), 3)]
  listOfCalculatedContent = []
  for el in subListOfContents:
    m = float(el[0])
    mpg = float(el[1])
    octane = float(el[2])
    cpg = Fuel.calcCpg(octane)
    fuelcost = Fuel.calcFuelCost(m, mpg, cpg)
    dictOfContents = {}
    dictOfContents.update({'Miles': m, 'MPG': mpg, 'Octane': octane, 'CPG': cpg, 'Fuel_cost': fuelcost})
    listOfCalculatedContent.append(dictOfContents)

  try:
    f2 = open('FuelCostOutput.txt', 'w')  # open this file in write mode
    try:
      for e in listOfCalculatedContent:
        for k, v in e.items():
          match k:
            case 'CPG':
              f2.write(f'CPG : ${e["CPG"]:.2f},\n')
            case 'Fuel_cost':
              f2.write(f'Fuel Cost : ${e["Fuel_cost"]:.2f}\n')
            case _:
              f2.write(f'{k} : {v},\n')
        f2.write('\n')
    except:
      print("something went wrong while writing to the FuelCostOutput.txt file!")
    finally:
      # closing the FuelCostOutput file
      f2.close()
  except:
    print("Something went wrong while opening the FuelCostOutput file!")
  finally:
    # closing the FuelRecordsInput file
    f1.close()
except:
  print('Something went wrong while opening the FuelRecordsInput file!')