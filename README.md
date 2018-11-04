# drinkingsensor
Analyzes data from a mouse drinking sensor.

This code takes data output by an Arduino Uno that uses IR beam sensors to monitor mice's frequency duration of drinking.
The results are exported as a .txt file where the beginning of a drinking bout is labeled "brok" and the end of the bout is labeled "unbrok."

This Python code imports all .txt files in the current working directory. For each file, it calculates the total time spent drinking, as well as the number of individual drinking bouts lasting > 500 ms. It summarizes all the data in a single excel file.
