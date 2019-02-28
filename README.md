This project is aimed at building a CLI tool which can be used to run queries on Treasure Data Platform 

## **Getting Started**
       

-Please follow the instructions below to successfully run the 

##  **Prerequisites**

- Python 3.X or higher 

-  Install Python on machine by following the instructions given in the link https://docs.python-guide.org/starting/installation/ 

- Retrieve the API Key from Treasure Data by following instructions given in the link https://support.treasuredata.com/hc/en-us/articles/360000746587-Access-Control

- set the environment variable 'TDI_API_KEY'  with the API key generated  


##  **Installing**
- Install Treasure Data client
 `pip install td-client` 

- Install Click library  
`pip install click`

## **Instructions to Run the CLI**

1. Download the treasuredatacli.py file and run the command 
`python treasuredatacli.py  query <options> <database> <table>`

2. following are the valid options

![text](https://user-images.githubusercontent.com/10234508/53539545-d00d9f00-3ac6-11e9-9744-01ec7f35012f.png)



## **Examples** 

- To access the help menu enter
`python treasuredatacli.py  --help`

![image](https://user-images.githubusercontent.com/10234508/53539748-aef97e00-3ac7-11e9-9fc6-3f48a80f4ba0.png)

- Execute the query using limit option

  `python3 TreasureDataCLI query -l 10 sample_datasets nasdaq`

![image](https://user-images.githubusercontent.com/10234508/53540090-f6ccd500-3ac8-11e9-86e8-61738cc88bab.png)

- Execute the query with engine option.Supports Hive and Presto 

  `python3 TreasureDataCLI query  -f tabular -e hive sample_datasets nasdaq`

![image](https://user-images.githubusercontent.com/10234508/53540584-fc2b1f00-3aca-11e9-9b1c-468fc7d94c8d.png)

 Based on engine option the job is created and use the specified engine to run the query. In this instance its run using hive

![image](https://user-images.githubusercontent.com/10234508/53540689-68a61e00-3acb-11e9-918d-39f456eb0034.png)

- Execute query by giving min and max unix time stamp

`python3 TreasureDataCLI query -f tabular -e hive -l 10 -m 1327968000 -M 1546214400 sample_datasets nasdaq`

![image](https://user-images.githubusercontent.com/10234508/53541362-5aa5cc80-3ace-11e9-88a7-b906a16f6e4c.png)

Based on snapshot you can see the time stamp filtering 

![image](https://user-images.githubusercontent.com/10234508/53541382-6ee9c980-3ace-11e9-9f88-d7c4b5edf8c1.png)

- Execute the query with using column options

`python3 TreasureDataCLI query -f tabular -e hive -l 10 -c 'symbol' sample_datasets nasdaq`

![image](https://user-images.githubusercontent.com/10234508/53541624-91c8ad80-3acf-11e9-93d7-6689d89e0f78.png)

## **Test Cases** 

- Time stamp validation 

![image](https://user-images.githubusercontent.com/10234508/53542026-5fb84b00-3ad1-11e9-862a-329dd3f62e26.png)

![image](https://user-images.githubusercontent.com/10234508/53542121-d6554880-3ad1-11e9-9684-8ae81cba83b2.png)

if min time stamp is greater than max it shows an error message

![image](https://user-images.githubusercontent.com/10234508/53542244-54b1ea80-3ad2-11e9-9ed5-8f5328d4f917.png)

-  Mandatory Argument Validations 

![image](https://user-images.githubusercontent.com/10234508/53568819-c9f3de80-3b17-11e9-8880-34896848f4e6.png)

- Output Format Validations

![image](https://user-images.githubusercontent.com/10234508/53572034-27d7f480-3b1f-11e9-8801-aa224720f6a2.png)

- Other validations

![image](https://user-images.githubusercontent.com/10234508/53572408-088d9700-3b20-11e9-8d6b-032d93859260.png)







 



 

