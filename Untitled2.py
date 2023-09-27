#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Celsius to Fahrenheit
def Celsius_to_Fahrenheit(Celsius):
    return (Celsius * 9/5) + 32

# Fahrenheit to Celsius
def Fahrenheit_to_Celsius(Fahrenheit):
    return (Fahrenheit - 32) * 5/9


# In[32]:


# Setting dictionary to mapping the user input to the function

conversion_features = {
    'c' : Celsius_to_Fahrenheit,
    'f' : Fahrenheit_to_Celsius
}

print("Choose the conversion direction.")
print("Put C for celsius to Fahrenheit or F for Fahrenheit to Celsius")

choice = input("Enter your choice: ").strip().lower()

if choice in conversion_features:
    temperature = float(input("Enter the temperature: "))
    
    # Conversion
    converted_temperature = conversion_features[choice](temperature)
    
    print(f"{temperature} degrees {'Celsius' if choice == 'c' else 'Fahrenheit'} is {converted_temperature} degress {'Fahrenheit' if choice == 'c' else 'Celsius'}")
          
else:
    print("This was not a valid input. Please enter a C or a F.")


# In[ ]:




