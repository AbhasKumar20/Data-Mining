
=============================================== Section Info ==============================================

Section 1. General Information about Folders and Files Present

Section 2: How to run this Assignment?

Section 3: Handling Execptions.

===========================================================================================================

****************** Section 1. General Information about Folders and Files Present *****************

There are 15 folders in total.

1 folder named 'Data' contains the datasets required.
11 folders are there for one question each given in the assignment numbered 1 to 11. Each of them has
one python file and one shell file initially, after execution of a question corresponding output files will
get produced here.

1 folder named as Question12 contains this README.txt only.
1 folder named as Question13 contains report.tex, report.pdf,report.zip

There is 1 folder named as Helpers, initially which will be empty subsequently 3 json files will get produced 
inside it, these will serves as input to some of the questions later.

-------------------------------------------------------------------------------------------------------------

************************** Section 2: How to run this Assignment? *********************************

* Programming languages used are 'python3' and 'bash'.
* No need of Internet if your Machine has python3 interpreter and if you can make following python imports.

	1.import json
	2.from collections import OrderedDict
	3.import csv
	4.import networkx as nx
	5.import pandas 


Steps to run the entire Assignment:-

Step1: Unzip 20111001-assign2.zip.

step2: Open terminal go to folder 20111001-assign2.

Step3. Make the file named assign2.sh executable using command: 
			
			chmod +x assign2.sh

step4. Now run the script assign1.sh using command:

			./assign2.sh

Done!


* All required output files corresponding to each question will get produced sequentially (Starting from Question 1 to 
  Question 11 of the assignment) in their respective QuestionNumber Folder. 

-----------------------------------------------------------------------------------------------------------------------

******************************** Section 3: Handling Execptions ***********************************

*Note: All Exception handlings are done as Instructed by the Professor.

1.While solving Question 3 , Articles that are in this list [Directdebit, Donation ,Friend_Directdebit ,Pikachu, Sponsorship_Directdebit, Wowpurchase] didn't had any category. I have assigned them category ID of Root node (Subject) i.e C0001.

2.While solving Question 6 , one human path(in paths_finished.tsv) having source as 'Bird' and Destination as 'wikipedia-gnu ' didn't had any paths between them so i have removed that entry from paths_finished.tsv. Also 11 human paths  were there having only 1 article both as source and destination given in this list ['Lesotho','Moon','Coal','Pyramid','Apple','Snow_Goose','Royal_Navy','Abel_Tasman','American_Samoa','Florence_Nightinangle','William_and_Marry'], I have removed those 11 entries from paths_finished.tsv.

3.While solving Question 10, 25 of the Destination articles in paths_unfinished.tsv were not present in the articles.tsv hence I have taken  category of these 25 articles as category of Root node i.e C0001.


---------------------------------------------------------------------------------------------------------------------


