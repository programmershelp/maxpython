#!/usr/bin/env python

def convert(temperature, unit):
    unit = unit.lower()
    if unit == "c":
        temperature = 9.0 / 5.0 * temperature + 32
        return "%s degrees Fahrenheit"% temperature
    if unit == "f":
        temperature = (temperature - 32)  / 9.0 * 5.0
        return "%s degrees Celsius"% temperature
 
inptemp = int(input("What is the temperature?\n"))
inpunit = str(input("Please enter the unit of measure (f or c):\n"))
 
print (convert(inptemp, inpunit))