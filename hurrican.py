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



####################################################################
# write your update damages function here:

def update_damage(dmg):
    
    """
        this funciton updates the damages of hurricanes, preserving the 'Damages 
        not recorded' term and transform the numberical terms into float
        
        B/M stands for billion and million
    
    """
    
    result =[]
    
    for temp in dmg:
        
        if temp == 'Damages not recorded': # preserve the term
            
            result.append(temp) 
            
        elif 'B' in temp: # transform values measured in billions
            
            result.append(float(temp[:-1])*1e9)
    
        elif 'M' in temp: # transform values measured in millions
            result.append(float(temp[:-1])*1e6)
            
    
    return result

# test out the function above
test_ud = update_damage(damages)


####################################################################
# write your construct hurricane dictionary function here:

def hurr_dict(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths):
    
    """
        this funciton constructs a dictionary 
        which contains all the relevant information
        of the hurrican.
        keys: hurrican name
        values: Name, Month, Year, Max Sustained Wind, Areas Affected, Damage, Death
    """
    
    result = dict()
    
    # store the information of each hurrican using the name as key
    for i in range(len(names)):
        
        result[names[i]] = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damage': damages[i],
            'Death': deaths[i]
            }
    
    return result

# test out the function above
test_hurr_dict = hurr_dict(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths)

####################################################################
# write your construct hurricane by year dictionary function here:

def hurr_by_year(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths):
    
    """
        this function group the hurricans by the year it occured
    """
    
    result = dict()
    
    
    # get the dictionary of all the hurricans using the hurr_dict function
    all_hurr = hurr_dict(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths)
    
    
    # iterate through each hurrican
    for hurr in all_hurr.values():
        
        ind = hurr['Year']
        
        if ind not in list(result.keys()): # check if the current year has already been a key of the dict
        
            result[ind] = [] # if not, add a new key/value pair, with the year as key and an empty list as value
        
        result[ind].append(hurr) # add the current selected hurrican to the corresponding year
            
    
    return result

# test out the function above
test_hurr_by_year = hurr_by_year(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths)


####################################################################
# write your count affected areas function here:


def count_area_affected(aa):
    
    """
        this function calculates the time that an area was affected by a hurrican 
    
    """
    
    
    result = dict()
    
    
    
    for area in aa: # iteratre through the affected area of all the hurrican 
        
        for temp in area:  # for each area affectd by the target hurrican
            
            if temp not in list(result.keys()): # add the area as key to the result dict if this area hasn't appreaded previously
                
                result[temp] = 0 # assign value 0 to the count
            
            result[temp] += 1 # add the count
            
    return result

# test out the function above     
test_aa = count_area_affected(areas_affected)
    
####################################################################
# write your find most affected area function here:

def most_aa(aa):
    
    """
        this function finds the most affected area
    """
    
    temp = count_area_affected(aa) # generate the counts for all area

    aa_l = [(area,temp[area]) for area in temp] # transform dict to list
    
    max_aa = max(aa_l, key = lambda x: x[1])[1] # find out the maximum count
    
    result = [temp for temp in aa_l if temp[1] == max_aa ] # find the area/count pair of the most affect area, can be more than one pair
    
    for item in result: # print out the finding
        print('The most affected area is {area}, which has been affected {time} times.'.format(
        area = item[0], time = item[1]))   
        
    return result 

# test out the function above
test_most_aa = most_aa(areas_affected)


####################################################################
# write your greatest number of deaths function here:

def deadliest_hurr(names, deaths):
    
    """
        this function finds the hurrican that causes the greatest number of deaths
    """
    
    
    # zip the name and deaths list into tuples
    # find the pairs that have the highest value in deaths 
    
    dd_hurr = [temp_pairs for temp_pairs in list(zip(names,deaths)) 
               if temp_pairs[1] == max(deaths)]
    
    # print out the result, format the number with comma in thousand
    for item in dd_hurr:
        
        print('The deadliest hurrican is {name}, which killed {num} people.'.format(
            name = item[0], num = item[1]))
    
    return dd_hurr

test_dh = deadliest_hurr(names, deaths)

####################################################################
# write your catgeorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}    


def morality_ctg(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths):
    
    """
        this function recaculate the rate of hurricans 
        based on the morality they have caused, and group
        them by their morality rate
    
    """
    
    # generate the formatted information of all hurricans using the hurr_dict() function
    all_hurr = hurr_dict(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths)
    
    result = dict()
    
    # iterate through each hurrican, and rate them by the number of the deaths they have caused
    # using the morality scale provided above.
    for hurr in all_hurr.values():
        
        if hurr['Death'] > 10000:
            
            temp_mr = 5
            
        elif hurr['Death'] > 1000:
            
            temp_mr = 4
            
        elif hurr['Death'] > 500:
            
            temp_mr = 3
            
        elif hurr['Death'] > 100:
            
            temp_mr = 2
        
        elif hurr['Death'] > 0:
            
            temp_mr = 1
            
        else:
            temp_mr = 0
            
        
        # add the current selected hurrican to the proper category. 
        # if the proper category did not exist in the current result dict
        # add the new pair
        
        if temp_mr not in list(result.keys()):
            
            result[temp_mr]=[]
            
        result[temp_mr].append(hurr)
    
    # add rate 0 if it does not exists
    if 0 not in list(result.keys()):
        
        result[0]=[]
        
    return result

# test out the function above    
test_morality_ctg = morality_ctg(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths)
        


####################################################################
# write your greatest damage function here:
def most_damage(names, damages):
    
    # transfer the damage information using update_damage funciton
    temp_damage = update_damage(damages)    
    
    # get the pair of name/damage information while removing records with no damage information
    result = [temp for temp in list(zip(names, temp_damage)) if 
               (type(temp[1]) == float)]
    
    # calculate the maximum damage from the current data
    max_dmg = max(result, key = lambda x:x[1])[1]
    
    # find out the pair that has the maximum damage
    result = [temp for temp in result if temp[1] == max_dmg]
    
    # print out the result
    for item in result:
        
        print("""The hurrican that caused the most amount of damage is {name},
              with a total damage of ${value:,}.""".format(name = item[0],value = item[1]))
              
    
    return result

# test out the function above
test_md = most_damage(names, damages)
        
       
####################################################################
# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_ctg(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths):
    
    """
        this function recaculate the rate of hurricans 
        based on the damage they have caused, and group
        them by their damage rate
    
    """
    
    # update the damage using the update_damage function
    updated_dmg = update_damage(damages)
    
    # construct the formatted hurrican dictionary using the updated damage inforamtion
    all_hurr = hurr_dict(names, months, years, max_sustained_winds,areas_affected,
              updated_dmg, deaths)
    
    result = dict()
    
    # rate each hurrican based on the damage they have caused
    # using the damage scale provided
    for hurr in all_hurr.values():
        
        # categroize the hurrican whose damages were not recorded as rate 0 
        if (hurr['Damage'] == 'Damages not recorded' or 
            hurr['Damage'] <= 0):
            
            temp_dr = 0            
        
        elif hurr['Damage'] > 50000000000:
            
            temp_dr = 5
            
        elif hurr['Damage'] > 10000000000:
            
            temp_dr = 4
            
        elif hurr['Damage'] > 1000000000:
            
            temp_dr = 3
            
        elif hurr['Damage'] > 100000000:
            
            temp_dr = 2
        
        elif hurr['Damage'] > 0:
            
            temp_dr = 1
            
            
        if temp_dr not in list(result.keys()):
            
            result[temp_dr]=[]
            
        result[temp_dr].append(hurr)
        
    return result

# test out the function above    
test_damage_ctg = damage_ctg(names, months, years, max_sustained_winds,areas_affected,
              damages, deaths)