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

        sql = f"""
        INSERT INTO public.users (display_name, handle,email, cognito_user_id)
        VALUES(%(name)s,%(handle)s, %(email)s, %(userID)s)
        """
        print ("SQL ============")
        print(sql)

        print("Details =====================================")
        print('name: ', user['name']) 
        print('handle: ', user['preferred_username']) 
        print('email: ', user['email'])
        print('userID: ', user['sub'])

        conn = psycopg2.connect(os.getenv('CONNECTION_URL'))
        cur = conn.cursor()
        cur.execute(sql, {'name':user['name'], 'handle':user['preferred_username'], 'email':user['email'], 'userID':user['sub']})
        conn.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')

    return event