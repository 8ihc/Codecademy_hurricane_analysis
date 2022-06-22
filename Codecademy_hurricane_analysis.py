# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
conversion = {"M": 1000000,
              "B": 1000000000}

def edit_damages(records):
    edit_damages = []
    for record in records:
        if record == 'Damages not recorded':
            edit_damages.append(record)
        else:
            if 'M' in record:
                edit_damages.append(float(record.replace('M', '000000')))
            elif 'B' in record:
                edit_damages.append(float(record.replace('B', '000000000')))
    return edit_damages

edited_damages = edit_damages(damages)
print(edited_damages)


# write your construct hurricane dictionary function here:

def dic_hurricane(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dict = {}
    for i in range(len(names)):
        dict.update({names[i]: {'Name': names[i],
                               'Month': months[i],
                               'Year': years[i],
                               'Max Sustained Wind': max_sustained_winds[i],
                               'Areas Affected': areas_affected[i],
                               'Damage': damages[i],
                               'Deaths': deaths[i]}})
    return dict

hurricanes = dic_hurricane(names, months, years, max_sustained_winds, areas_affected, edited_damages, deaths)
print(hurricanes)


# write your construct hurricane by year dictionary function here:

def hurricanes_order_by_year(original_dic):
    year_ordered_dict = {}
    for key, value in original_dic.items():
        current_year = value['Year']
        current_cane = [value]
        if current_year not in year_ordered_dict:
            year_ordered_dict.update({current_year:current_cane})
        else:
            year_ordered_dict[current_year].append(current_cane)
    return year_ordered_dict
hurricanes_by_year = hurricanes_order_by_year(hurricanes)
print(hurricanes_by_year)


# write your count affected areas function here:

def count_affected_areas(areas_affected):
    areas_dict = {}
    for lst in areas_affected:
        for area in lst:
            num = 1
            if area not in areas_dict:
                areas_dict.update({area: num})
            else:
                areas_dict[area] += 1
    return areas_dict

areas_dict = count_affected_areas(areas_affected)
print(areas_dict)


# write your find most affected area function here:

def most_affeted_area(areas_dic):
    most_dict = {}
    counter = 0
    for area, frequency in areas_dic.items():
        if frequency > counter:
            most_dict.update({area:frequency})
            counter = frequency
    return most_dict

highest_affetced_area = most_affeted_area(areas_dict)
print(highest_affetced_area)

# write your greatest number of deaths function here:

def deadliest_cane(hurricanes):
    deadliest = {}
    cane = ''
    counter = 0
    for key, value in hurricanes.items():
        if value['Deaths'] > counter:
            cane = key
            counter = value['Deaths']
    deadliest.update({key:counter})
    return deadliest

highest_death_cane = deadliest_cane(hurricanes)
print(highest_death_cane)


# write your catgeorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mortality_rating(hurricanes):
    m_rates = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for key, value in hurricanes.items():
        if value['Deaths'] == 0:
            m_rates[0].append(key)
        elif value['Deaths'] <= 100:
            m_rates[1].append(key)
        elif value['Deaths'] <= 500:
            m_rates[2].append(key)
        elif value['Deaths'] <= 1000:
            m_rates[3].append(key)
        elif value['Deaths'] <= 10000:
            m_rates[4].append(key)
        else:
            m_rates[5].append(key)
    return m_rates

mortality_rates = mortality_rating(hurricanes)
print(mortality_rates)

# write your greatest damage function here:

def greatest_damage_cost(hurricanes):
    greatest_cane = {}
    counter = 0
    cane = ''
    for key, value in hurricanes.items():
        if value['Damage'] == 'Damages not recorded':
            continue
        elif value['Damage'] > counter:
            counter = value['Damage']
            cane = key
    greatest_cane.update({cane:counter})
    return greatest_cane

highest_cost_cane = greatest_damage_cost(hurricanes)
print(highest_cost_cane)

# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_scale(hurricanes):
    damage_rates = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, value in hurricanes.items():
        if value['Damage'] == 'Damages not recorded':
            continue
        if value['Damage'] == 0:
            damage_rates[0].append(key)
        elif value['Damage'] <= 100000000:
            damage_rates[1].append(key)
        elif value['Damage'] <= 1000000000:
            damage_rates[2].append(key)
        elif value['Damage'] <= 10000000000:
            damage_rates[3].append(key)
        elif value['Damage'] <= 50000000000:
            damage_rates[4].append(key)
        else:
            damage_rates[5].append(key)
    return damage_rates

damage_ratings = damage_scale(hurricanes)
print(damage_ratings)