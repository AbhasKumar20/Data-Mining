
============================================ SECTIONS IN this README.txt  ====================================

					1. General Information about Folders and Files Present
					2. Detailed Information about each Folder and Files.
					3. How to run the assignment?

===============================================================================================================

------------------------------- Section 1: General Information About Folders and Files Present ---------------

There are 11 folders in total. 
10 of them are for one question each given in the assignment numbered 1 to 10.
------8 of them contains 2 files each , a .sh and .py file.
------1 contains README.txt
------1 contains report.tex, report.pdf,report.zip

One folder is Input Folder that contains 2 files.
There is one README.txt file
There is one script named 'assign1.sh'.

------------------------------- Section 2: Detailed Infoformation about each folder and files -----------------

'Input_Folder': Contains two files namely 'neighbor-districts.json' and 'districts.csv' which serves as input files to the entire assignment.
				
a.'neighbor-districts.json' contains name of various districts(total 723 districts) as key and their 
neighborors as value.

b.'districts.csv' contains district wise confirmed cases on a daily basis till 5 september 2020. Latest 
version of this file can be found here 'https://api.covid19india.org/csv/latest/districts.csv'.


'Question1': Contains a json file named 'neighbor-districts-modified.json' which has modified district names and their neighbors according to the districts found in 'district.csv'.All districts in the 'neighbor-districts-modified.json' are sorted(lexicographically) and are having ids starting from '101' as value for key 'district_id'. Each 			district also has list of neighbors as value for the key 'neighbors'.


'Question2': Contains 2 files namely 'case-generator.sh' and 'case-generator.py' which counts number of confirmed covid cases weekly(25 weeks in total) , monthly(7 months in total) and overall. Where the time duration for the  counting and analysis is from 15 March 2020 to 5 September 2020.

a.'case-generator.sh' just invokes the python script 'case-generator.py'.

b.'case-generator.py' takes 'neighbor-districts.json' and 'districts.csv' as input files from the 'Input_Folder' calulates confirmed covid cases and produces 3 output files named 'cases-week.csv','case-month.csv' and 'cases-overall.csv' in the 'Question2' folder.It also produces a json file named 'cases.json' in 'Input_Folder' which contains all required infomation for a district required further in the assignment.


'Question3': Contains 2 files namely 'edge-generator.sh' and 'edge-generator.py' which makes pair of district with their neighbors.

 a.'edge-generator.sh' just invokes the python script 'edge-generator.py'.

 b.'edge-generator.py' takes file 'cases.json' from Input_Folder as input and produces a file 'edge-graph.csv' in folder 'Question3' where each row is a pair of ids of district with its neighbor.



'Question4': Contains 2 files namely 'neighbor-generator.sh' and 'neighbor-generator.py' which calutates the mean and  standard deviation of confirmed covid cases of all neighbors for each district.

a.'neighbor-generator.sh' just invokes the python script 'neighbor-generator.py'.

b.'neighbor-generator.py' takes file 'cases.json' from Input_Folder as input and calulates mean and standard deviation of neighbors of each district then produces 3 files namely 'neighbor-week' (calculations for 25 			weeks for each district ),'neighbor-month'(calculations for 7 months for each district ),'neighbor-overall'(calculations for entire period between 15/03/2020 to 5/09/2020) in folder 'Question4'.


'Question5': Contains 2 files namely 'state-generator.sh' and 'state-generator.py' which calutates the mean and 
standard deviation of confirmed covid cases of all districts belonging to the same state for each district.

 a.'state-generator.sh' just invokes the python script 'state-generator.py'.

 b.'state-generator.py' takes file 'cases.json' from Input_Folder as input and calulates mean and standard deviation of all districts of the same state for each district then produces 3 output files namely 'state-week' (calculations for 25 weeks for each district ),'state-month'(calculations for 7 months for each district ),'state-overall'(calculations for entire period between 15/03/2020 to 5/09/2020) in the folder 'Question5'.

'Question6':Contains 2 files namely 'zscore-generator.sh' and 'zscore-generator.py' which calutates two z-scores,one on 
the basis of neighbor districts and another on the basis of all districts of the same state, for each district

a.'zscore-generator.sh' just invokes the python script 'zscore-generator.py'.

b.'zscore-generator.py' takes file 'cases.json' from Input_Folder and outputs produced in folders of 'Question2','Question3' and 'Question5' as input and calulates both zscores for each district then produces 3 output files namely 'zscore-week.csv'(calculations for 25 weeks for each district ),'zscore-month.csv'(calculations for 7 months for each district ) and 'zscore-overall.csv'(calculations for entire period between 15/03/2020 to 5/09/2020) in the folder 'Question6'.


'Question7':Contains 2 files namely 'method-spot-generator.sh' and 'method-spot-generator.py' which tags each district  as either Hotspot or Coldspot on the basis of Z-scores of neighbor and state.

a.'method-spot-generator.sh' just invokes the python script 'method-spot-generator.py'.

b.'method-spot-generator.py' takes file 'cases.json' from Input_Folder and outputs produced in folder named 'Question6' as input. Tags each district as Hotspot/Coldspot on the basis of 2 Z-scores then produces 3 output files namely 'method-spot-week.csv','method-spot-month.csv' and 'method-spot-overall.csv' in the folder 'Question7'.


'Question8':Contains 2 files namely 'top-generator.sh' and 'top-generator.py' which calculates top-5 Hotspot and top-5 
Coldspot districts for each 25 weeks , 7 months and overall(between 15/03/2020 to 5/09/2020).

a.'top-generator.sh' just invokes the python script 'top-generator.py'.

b.'top-generator.py' takes file 'cases.json' from Input_Folder and outputs produced in folder named 'Question6' as input. Finds district ids of  top-5 Hotspot/Coldspot district both on the basis neighbors and districts of same state then produces 3 output files namely 'top-week.csv'(for each 25 weeks),'top-month.csv'(for each 7 months) and 'top-overall.csv'(between 15/03/2020 to 5/09/2020) in the folder 'Question8'.

'Question9': Contains this README.txt too.

'Question10': Contains the report in LATEX named as report.tex together with all images(.png) used in the report. It 
also contains PDF version of report named as report.pdf. Also report.zip is there, one can upload this zip file to see the report on overleaf.

------------------------------------------- Section 3: How to run the Assighnment? ---------------------------------

* Programming languages used are 'python3' and 'bash'.
* No need of Internet if your Machine has python3 interpreter and if you can make following imports.
	1.import json
	2.from collections import OrderedDict
	3.import csv
	4.import requests
	5.import pandas 
	6.from difflib import SequenceMatcher
	7.import math

Steps to run the entire Assignment:-

Step1: Unzip 20111001-assign1.zip.

step2: Open terminal go to folder 20111001-assign1.

Step3. Make the file named assign1.sh executable using command: 
			
			chmod +x assign1.sh

step4. Now run the script assign1.sh using command:

			./assign1.sh

Done!


* All required output files corresponding to each question will get produced sequentially (Starting from Question 1 to 
  Question 10 of the assignment) in their respective QuestionNumber Folder. 

------------------------------------------------------------------------------------------------------------------------


