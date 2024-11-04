import json
import psycopg2
import os

def lambda_handler(event, context):
    # Extract data from the event payload
    name = event.get('name')
    email = event.get('email')
    country = event.get('country')

    # Database connection details (use environment variables for security)
    db_host = os.environ['DB_HOST']
    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']
    db_password = os.environ['DB_PASSWORD']
    db_port = os.environ.get('DB_PORT', 5432)  # default PostgreSQL port

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        cursor = conn.cursor()

        # Insert data into the table (replace 'your_table' with your table name)
        insert_query = """
            INSERT INTO your_table (name, email, country) VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (name, email, country))
        conn.commit()

        # Close the database connection
        cursor.close()
        conn.close()

        return {
            'statusCode': 200,
            'body': json.dumps({
                'status': 'success',
                'message': 'Data successfully stored in the database.'
            })
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'status': 'error',
                'message': str(e)
            })
        }

