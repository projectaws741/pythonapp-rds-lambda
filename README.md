Create a AWS RDS postgres db and create table your_table.
copy the credentials endpoint, username, password, db name and port as envronmental variables in lambda function as shown in below.
![image](https://github.com/user-attachments/assets/1ecb4993-8d5a-4c05-8ccb-3f133b08580e)

once lambda function is add dependecy pyscopg2. 
What i did is created dependencies using docker image and copied in to hostmachine. I created a s3 bucket and uploaded the zip file in to s3 bucket. From additional resources-->layers in lambda function create layer source from s3(copy the url and paste it). create the layer and add it in layers.
Once dependecy is added test the lambda function.
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "country": "USA"
}
If we are able to add the data in to db then connection b/w lamda and db is good.

Now update the name of the lambda function in app.py file.

Now start the application.
