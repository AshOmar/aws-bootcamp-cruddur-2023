import json
import psycopg2
import os 

def lambda_handler(event, context):
    user = event['request']['userAttributes']
    try:
        print("User:============")
        print(user)

        print("event:=============")
        print(event)

        print("context:===========")
        print(context)

        conn = psycopg2.connect(os.getenv('CONNECTION_URL'))
        sql = f"""
        INSERT INTO users (display_name, handle,email, cognito_user_id)
        VALUES(%s, %s, %s)"
        """
        cur = conn.cursor()
        cur.execute(sql, (user['name'], user['email'], user['preferred_name'], user['sub']))
        conn.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')

    return event