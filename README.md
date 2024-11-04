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

Creating Dependencies:

# Start a new container
docker run -it --rm -v $(pwd):/opt python:3.9-slim bash

# Inside the container, install psycopg2-binary
apt-get update && apt-get install -y gcc libpq-dev zip
pip install psycopg2-binary -t /opt/python

# Create the zip file
zip -r /opt/psycopg2_layer.zip /opt/python
exit

#aws s3 cp /path/to/psycopg2_layer.zip s3://your-bucket-name/

Create or Update the Lambda Layer:

In the AWS Management Console, go to Lambda > Layers.
Create a new layer or update the existing one using the zip file you just uploaded to S3.
Step 3: Add the Layer to Your Lambda Function
Add the Layer:

Go to your Lambda function in the AWS Management Console.
In the Layers section, click Add a layer.
Choose Custom layers, and select the layer you just created or updated.
Ensure the Lambda Function Has the Correct Permissions:

Ensure your Lambda function has permission to access the layer. If the layer is in a different account or region, you need to set the appropriate resource-based policy.

