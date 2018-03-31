
# coding: utf-8

# In[4]:


f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
g = f.read()
list=g.split("\n")
print(list[0:10])


# In[2]:


def read_csv(input_lst):
    f = open(input_lst).read()
    string_list=f.split("\n")
    string_list=string_list[1:len(string_list)] 
    final_list=[]
    
    for rows in string_list:
        string_fields=rows.split(",") 
        int_fields=[]
        
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]


# In[9]:


def month_births(list_of_lists):
    births_per_month={}
    for value in list_of_lists:
        month=value[1]
        births=value[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births  
    return births_per_month
    
cdc_month_births = month_births(cdc_list)
cdc_month_births



# In[11]:


def dow_births(list_of_lists):
    births_per_dow={}
    for value in list_of_lists:
        day=value[3]
        births=value[4]
        if day in births_per_dow:
            births_per_dow[day] = births_per_dow[day] + births
        else:
            births_per_dow[day] = births  
    return births_per_dow
cdc_day_births=dow_births(cdc_list)
cdc_day_births
    


# In[15]:


def calc_counts(data,column_number):
    calculated_list={}
    for value in data:
        column=value[column_number]
        births=value[4]
        if column in calculated_list:
            calculated_list[column] = calculated_list[column] + births
        else:
            calculated_list[column] = births  
    return calculated_list

cdc_year_births=calc_counts(cdc_list,0)
cdc_month_births=calc_counts(cdc_list,1)
cdc_dom_births=calc_counts(cdc_list,2)
cdc_dow_births=calc_counts(cdc_list,3)

cdc_year_births
#cdc_month_births
#cdc_dom_births
#cdc_dow_births



    
    

