[Project Two README.docx](https://github.com/nat-dykh/protfolio/files/6989198/Project.Two.README.docx)
CS 340 Project Two

About the Project

This project uses MongoDB and Jupyter Notebook to create an interactive dashboard to allow individuals to easily look up profiles on potential search-and-rescue dogs and filter the data. The client for the project is for a non-profit organization that specializes in the training of search-and-rescue dogs.

Motivation

The motivation for this project is to allow for easy access to information in the database that contains profiles on different dogs. In the search-and-rescue training field there are certain qualities that trainers look for in dogs so having an interactive dashboard allows for the data to be easily accessible.
Getting Started
In order to successfully use the interactive dashboard, users must open Mongodb by using the following code in the terminal.
/usr/local/bin/mongod_ctl start
This allows for the dashboard to authenticate the user and access the data.
Once this is done, users must have the two files, animalshelter.py, which holds the animal shelter class, and the Projecttwo.ipynb files, which holds the code for the interactive dashboard. The user just needs to run the code in the Projecttwo.ipynb files and the dashboard will appear and allow for them to interact with it.

The project was completed in steps starting with getting the data table and geolocation map. These features were relatively easy to set up but there was challenges as the database would not load into he table for me so I could not debug the code for anything related to the table. This presented issues with the radio items and dropdown menu as well. They will display and allow a selected but since the data did not upload there was no way to see if they could update the table.

The drop down menu and the radio items work in similar ways when a selection is made. When a selection is made the value is passed to the function to update the table. The value given is used as a query or way to query in order to narrow the results in order to get the desired data.

Installation

MongoDB in Linux is used to house the database of dog profiles. The Mongo shell allows for the database to be stored and indexed making it easy to query within the database. The shell also allows for user authentication therefore protecting information. Jupyter Notebook within Linux is also used to create script that allows easy use of the database. The project also uses a CSV file that contains the database used and requires the Projecttwo.ipynb and the animalshelter.py files.

Usage

When using the dashboard, users will be able to use a dropdown menu and radio items in order to filter and navigate the data. The following code shows how the radio items works:

dcc.RadioItems(
        id='radio',
        options=[
            {'label': 'Water', 'value': 'water'},
            {'label': 'Mountain or Wilderness', 'value': 'mountain'},
            {'label': 'Disaster or Individual Tracking', 'value': 'disaster'},
            {'label': 'Reset', 'value':'reset'}],
        style={'width':'75%'}
    )
@app.callback(Output('datatable-interactivity',"data"),
             Input('radio','value'))
def Filter_Rescue(value):
    if(value == 'water'):
        df=pd.DataFrame(list(shelter.read({"animal_type":"Dog",
        "breed":{"$in":["Labrador Retriever Mix","Chesapeake Bay Retriever","Newfoundland"]},
        "sex_upon_outcome":"Intact Female",
        "age_upon_outcome_in_weeks":{"$gte":26},
        "age_upon_outcome_in_weeks":{"$lte":156}})))
        return df.to_dict('records')
    if(value == 'mountain'):
        df=pd.DataFrame(list(shelter.read({"animal_type":"Dog",
        "breed":{"$in":["German Shepherd","Alaskan Malamute"," Old English Sheepdog","Siberian Husky","Rottweiler"]},
        "sex_upon_outcome":"Intact Male",
        "age_upon_outcome_in_weeks":{"$gte":26},
        "age_upon_outcome_in_weeks":{"$lte":156}})))  
        return df.to_dict('records')
    if(value == 'disaster'):
        df=pd.DataFrame(list(shelter.read({"animal_type":"Dog",
        "breed":{"$in":["German Shepherd","Doberman Pinscher","Golden Retriever","Bloodhound","Rottweiler"]},
        "sex_upon_outcome":"Intact Male",
        "age_upon_outcome_in_weeks":{"$gte":20},
        "age_upon_outcome_in_weeks":{"$lte":300}})))
        return df.to_dict('records')
    if(value == 'reset'):
        df=pd.DataFrame(list(shelter.read({})))
        return df.to_dict('records')

When data is selected in the table, the map and chart will dynamically update showing information related to the selected data. This is done by having a callback for each of them that updates both as well as the data table when filters are applied.

*No screenshots are applied as the data table will not load in order to see result

Additional Notes:

How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
       
  To write programs that are maintainable and readable, programmers must understand their clients and what they want to see in the program. For example, creating a CRUD Python Module allows for maintainability between a database and a dashboard. Creating a dashboard to go with a CRUD module allows for adaptability as the commands in the CRUD module can be used for many different purposes in the dashboard. This makes the dashboard adaptable to the users need and the CRUD module allow adapts the database to a dashboard. In order to write maintainable, readable, and adaptable programs, programmers must be able to use multiple means of creating a program like using a program for a database and using a different program for the dashboard. By using multiple means of creating a program, programmers can construct the program from different perspectives and have multiple means of editing the program. In the future, a CRUD module could be used as a way to make connections between two means of programming. CRUD modules act as a middle man that makes it easier to adapt and manage programs.

How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
       
   In order to successfully complete a task or problem in computer science, I break everything down into small steps. For each assignment in this course, I broke down step by step what needed to be done in order to build-up to the result. For example, when creating the dashboard for Project Two I started by working to understand how to make a data table and then step by step added each feature to the project. This allows for problems to be managed in smaller bits. It is easier to make an interactive drop-down menu when you understand how to make a drop-down menu that does not complete everything. In the end, it all comes together but is easier to be done in smaller pieces. This approach differs from my approaches in previous classes because in previous classes I have had more background knowledge on the topic, therefore, allowing me to complete assignments without needing to break them down into smaller pieces. In the future, I will definitely approach everything by breaking it down in order to work on each piece individually. By doing this, the project becomes more manageable and easier to complete.
   
   What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
        
   Computer scientists are problem solvers. Clients come to them wanting something like a dashboard that will easily allow them to navigate data and computer scientists need to solve the problem of figuring out to make data accessible and easily navigatable. Computer scientists create a connection between data and users making everything more accessible to users. Work like the work done for Project Two, allows companies to access data needed in order to aid staff and/or consumers to see data in a manageable and navigable way. When users are able to easily access data they are more likely to interact with the data and work with the company.

Contact

Natalie Dykhuis

natalie.dykhuis@snhu.edu
