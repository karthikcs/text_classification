# How to use Ticket Categorize tool
## SmartCat tool

**Loading web app**
URL: [http://104.154.146.69:8000/](http://104.154.146.69:8000/)

It asks for a file to upload. The file is simple text file with short descriptions of the tickets, as below. The file should be uploaded 

```
extract the user data information 
please provide SOX data for audting
BW system is not accessible 
Unable to edit the table 
Issues with ZVFI output 
Change the Transportation Zone on Shipping Point 1977
almex contracts problems
Invoices could not be released to Accounting
Invoice stuck for the order 2234
delivery is lock for SO w4535 
Job in CRP Environment to be edited
BOBJ not working properly
``` 
Once uploaded the the tool will automatically download the file with categorized labels in CSV format. 


**Running server in Background**

- Step 1: run ```screen```

- Step 2: Execute the command you need to run in background

```gunicorn --bind 0.0.0.0:8000 saptickets.wsgi 2>&1 | tee smartcat.log```

- Step 3: Press Ctrl+a and press d. You detach the program from screen. You get following message

```[detached from 9128.pts-0.machine-learning2]```

- Step 4: You can disconnect SSH or Work on any other projects

- Step 5: To connect back to your screen, type ```screen -r```