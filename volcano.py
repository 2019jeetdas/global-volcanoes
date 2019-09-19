# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")

#-------- Question-00 --------------------

# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

#------------ Question -01 ------------------------
#----- Yearwise number of Volcanoes & total no. -----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


df_yearwise = df.groupby(['Year'])[['Month']].count()
print(df_yearwise)
print("--------------------------------------\n")
print("Total number of Volcanoes = \n",sum(df_yearwise))

plt.title("[Question-01] Number of Volcanoes yearwise ")
plt.xlabel("Year --->")
plt.ylabel("No. of Volcanoes ---->")
plt.plot(df_yearwise)
plt.show()

#------------ Question -02 ------------------------
#----- Types of the volcanoes -----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


df['Month'] = df['Month'].replace(np.nan,0)
df_type = df.groupby(['Type'])[['Month']].count()

print(df_type)
print("--------------------------------------\n")
print("Total number of Volcanoes = \n",sum(df_type))

sl_no = np.arange(0,20)

plt.title("[Question - 02] Different types of volcanoes :") 
plt.xlabel("Sl. no. of the different types of volcanoes -->") 
plt.ylabel("no. of Different types of volcanoes --->")   
plt.plot(sl_no,df_type)
plt.show()


#------------ Question -03 ------------------------
#----- Status of the volcanoes -----


# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


df['Month'] = df['Month'].replace(np.nan,0)

df_status = df.groupby(['Status'])[['Month']].count()

print(df_status)
print("--------------------------------------\n")
print("Total number of Volcanoes = \n",sum(df_status))

sl_no = np.arange(0,7)

plt.title("[Question - 03] Status of volcanoes :") 
plt.xlabel("Sl. no. of status of volcanoes -->") 
plt.ylabel("no. of Different status of volcanoes --->")   
plt.plot(sl_no,df_status)
plt.show()


#------------ Question -04 ------------------------
#----- position of the volcanoes -----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


lat = df['Latitude'].replace(np.nan,0)
lon = df['Longitude'].replace(np.nan,0)

plt.title("[ Question - 04 ] : Volcanoes source plotting")
plt.xlabel("latitude --->")
plt.ylabel("longitude --->") 
plt.scatter(lat,lon)
plt.show()


#------------ Question -05 ------------------------
#----- Location of the volcanoes -----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


df['Month'] = df['Month'].replace(np.nan,0)

df_location = df.groupby(['Location'])[['Month']].count()

print(df_location)
print("--------------------------------------\n")
print("Total number of Volcanoes = \n",sum(df_location))     
     
sl_no = np.arange(0,78)

plt.title("[Question - 05] Location of volcanoes :") 
plt.xlabel("Sl. no. of locations of volcanoes -->") 
plt.ylabel("no. of Different locations of volcanoes --->")   
plt.plot(sl_no,df_location)
plt.show()



#------------ Question -06 ------------------------
#----- country wise of the volcanoes  and plotting-----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


df['Month'] = df['Month'].replace(np.nan,0)

df_country = df.groupby(['Country'])[['Month']].count()

print(df_country)
print("--------------------------------------\n")
print("Total number of Volcanoes = \n",sum(df_country))       
     
sl_no = np.arange(0,50)

plt.title("[Question - 06] Country wise no. of volcanoes  :") 
plt.xlabel("Sl. no. of countries -->") 
plt.ylabel("no. of volcanoes for the country --->")   
plt.plot(sl_no,df_country)
plt.show()



#------------ Question -07 ------------------------
#----- Deaths for the volcanoes  and plotting-----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


deaths = df['TOTAL_DEATHS'].replace(np.nan,0)

for i in range(0,833):
    print('Volcano =',i+1,'---->',int(deaths[i]))
    
plt.title("[Question - 07] Plots no. of deaths for Volcanoes")
plt.xlabel("Sl. no of the volcanoes ---->")
plt.ylabel("NO. of deaths ---->")
plt.plot(deaths)
plt.show()

#------------ Question -08 ------------------------
#----- Missing cases for the volcanoes  and plotting-----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


missing = df['TOTAL_MISSING'].replace(np.nan,0)

for i in range(0,833):
    print(int(missing[i]))
    
plt.title("[Question - 08] Plots no. of missing cases for Volcanoes")
plt.xlabel("Sl. no of the volcanoes ---->")
plt.ylabel("NO. of missing cases ---->")
plt.plot(missing)
plt.show()

#------------ Question -09 ------------------------
#----- NO. of injuries for the volcanoes  and plotting-----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


injuries = df['TOTAL_INJURIES'].replace(np.nan,0)

for i in range(0,833):
    print('Volcano =',i+1,'---->',int(injuries[i]))
    
    
plt.title("[Question - 09] Plots no. of injuries for Volcanoes")
plt.xlabel("Sl. no of the volcanoes ---->")
plt.ylabel("NO. of injuries ---->")
plt.plot(injuries)
plt.show()

#------------ Question - 10 ------------------------
#----- TOTAL_DAMAGE_MILLIONS_DOLLARS for the volcanoes  and plotting-----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


damage = df['TOTAL_DAMAGE_MILLIONS_DOLLARS'].replace(np.nan,0)

for i in range(0,833):
    print('Volcano =',i+1,'---->',int(damage[i]))
    
    
plt.title("[Question - 10] TOTAL_DAMAGE_MILLIONS_DOLLARS for Volcanoes")
plt.xlabel("Sl. no of the volcanoes ---->")
plt.ylabel("TOTAL_DAMAGE_MILLIONS_DOLLARS ---->")
plt.plot(damage)
plt.show()

#------------ Question - 11 ------------------------
#----- TOTAL_HOUSES_DESTROYED for the volcanoes  and plotting-----

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


house = df['TOTAL_HOUSES_DESTROYED'].replace(np.nan,0)

for i in range(0,833):
    print('Volcano =',i+1,'---->',int(house[i]))
    
    
plt.title("[Question - 11] TOTAL_HOUSES_DESTROYED for Volcanoes")
plt.xlabel("Sl. no of the volcanoes ---->")
plt.ylabel("TOTAL_HOUSES_DESTROYED ---->")
plt.plot(house)
plt.show()


#-------- Question-12 ---------------
#------- Detailed description of the volcanoes ---------------

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# Reading and converting to CSV file

df = pd.read_table('/home/jeet/Desktop/all_volcano.txt')
df.to_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8',sep=',',index=False)

# Reading the newly created CSV file

df=pd.read_csv("/home/jeet/Desktop/all_volcano.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("Volcano data analysis \n[ with Earthquake & Tsunami status ]:")
print("\n-----------------------------------\n")


year = df['Year']
name = df['Name']
types = df['Type']
status = df['Status']

loc = df['Location']
coun = df['Country']
lat = df['Latitude']
lon = df['Longitude']

tsu = df['TSU']
eq = df['EQ']

time =df['Time']

for i in range(401,584):
    print("\n\n---------------------------------------")
    print('\tVolcano number = ',i)
    print('-----------------------------------\n')

    print("Year = ",year[i]) 
    print("Name = ",name[i])
    print("Type = ",types[i])
    print("Status = ",status[i])

    print("\nLocation = ",loc[i]) 
    print("Country = ",coun[i])
    print("latitude = ",lat[i]) 
    print("longitude = ",lon[i]) 

    print("\nTsunami status = ",tsu[i]) 
    print("Eartquake status = ",eq[i]) 

    print("\nTime = ",time[i])
    
print("---------------------------------------\n")




