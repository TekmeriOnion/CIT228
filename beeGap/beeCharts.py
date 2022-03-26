import csv
import matplotlib.pyplot as plt
import plotly.express as px
from plotly import offline

# initialize empty dictionary to track species richness by family
famCounts = {}
# initialize total species counter
speciesCount = 0
# initialize Great Lakes present species counter
presentCount = 0
# initialize IL counter
ilCount = 0
# initialize IN counter
inCount = 0
# initialize MI counter
miCount = 0
# initialize MN counter
mnCount = 0
# initialize NY counter
nyCount = 0
# initialize OH counter
ohCount = 0
# initialize PA counter
paCount = 0
# initialize WI counter
wiCount = 0
# initialize distribution tracker
distro = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}
famPresCounts = {}

with open('data/beeGap.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header_row = next(csv_reader)
    for row in csv_reader:
        speciesCount += 1
        fam = row[1]
        dist = str(row[14])
        distro[dist] += 1
        if row[5] == 'Y':
            presentCount +=1
        else:
            continue
        if fam in famCounts.keys():
            famCounts[fam] +=1
        else:
            famCounts[fam] = 1
        if int(row[6]) == 1:
            ilCount += 1
        else:
            continue
        if int(row[7]) == 1:
            inCount += 1
        else:
            continue
        if int(row[8]) == 1:
            miCount += 1
        else:
            continue
        if int(row[9]) == 1:
            mnCount += 1
        else:
            continue
        if int(row[10]) == 1:
            nyCount += 1
        else:
            continue
        if int(row[11]) == 1:
            ohCount += 1
        else:
            continue
        if int(row[12]) == 1:
            paCount += 1
        else:
            continue
        if int(row[13]) == 1:
            wiCount += 1
        else:
            continue
# compile dictionary with species counts by state
stateCounts = {}
stateCounts["Illinois"] = ilCount
stateCounts["Indiana"] = inCount
stateCounts["Michigan"] = miCount
stateCounts["Minnesota"] = mnCount
stateCounts["New York"] = nyCount
stateCounts["Ohio"] = ohCount
stateCounts["Pennsylvania"] = paCount
stateCounts["Wisconsin"] = wiCount

# initialize lists to store compiled counts and other aggregated data
states = []
state_counts = []
numStates = []
distributions = []
families = []
familyCts =[]
famPresCts =[]
presenceX = ['Present', 'Absent']
absent = speciesCount - presentCount
presenceY = [presentCount, absent]
# bring in total species counts by family from related data set
famTotals = [1078,1283,238,563,732,31]
# get sorted lists with aggregated data for plotting
for k in stateCounts.keys():
    states.append(k)
    state_counts.append(stateCounts[k])

del(distro['0'])
for k in distro.keys():
    numStates.append(k)
    distributions.append(distro[k])

for k in famCounts.keys():
    families.append(k)
    familyCts.append(famCounts[k])

# make a pie chart of Bee Species counts by family
explode = [0,0,0,0,0,0]
wedgeColors = ["#8D4AFF", "#5443E8", "#5773FF", "#438AE8", "#4AC7FF", "#68F5FF"]
plt.pie(familyCts, explode=explode,labels=families,autopct='%3.1f%%',shadow=False,colors=wedgeColors)
plt.title("Bee Species Counts by Family (Great Lakes)")
plt.show()

#make pie chart showing relationship between present and absent bee species in Great Lakes
explode=[.2,0]
plt.pie(presenceY, explode=explode,labels=presenceX, colors=["#425BFF","#FFCD29"],autopct='%3.1f%%')
plt.title("Proportional Presence of Bee Species in Great Lakes")
plt.show()

# make bar chart highlighting where MI stands relative to other Great Lakes states re: bee species richness
c = ['blue','blue','orange','blue','blue','blue','blue','blue']
plt.bar(states, state_counts, color = c)
plt.ylabel("# of Bee Species Present")
plt.title("Bee Species by State (Great Lakes)")
plt.show()

# make bar chart showing distributions 
plt.bar(numStates, distributions, color="#8F45FE")
plt.title("Bee Species Prevalence Across Great Lakes States")
plt.ylabel("# Species")
plt.xlabel("# States")
plt.show()

# make scatter plot showing species counts by family
plt.scatter(families,familyCts, color="red", label="Present Species")
plt.scatter(families, famTotals, color="green", label="Total Species")
plt.title("Bee Family Presence in Great Lakes States")
plt.legend(loc="upper right",ncol=1, fontsize="9")
plt.grid()
plt.show()

# make heat map of species by state
fig = px.choropleth(locations=["IL", "IN", "MI", "MN", "NY", "OH", "PA", "WI"], locationmode="USA-states", color=[*state_counts],color_continuous_scale="algae", scope="usa", title="Bee Species by State (Great Lakes)")
offline.plot(fig,filename="bees.html")