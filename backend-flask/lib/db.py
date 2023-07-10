from psycopg_pool import ConnectionPool
import os
import re
from flask import current_app as app
class textColours:
  # Reset
  Color_Off='\033[0m'       # Text Reset

  # Regular Colors
  Black='\033[0;30m'        # Black
  Red='\033[0;31m'          # Red
  Green='\033[0;32m'        # Green
  Yellow='\033[0;33m'       # Yellow
  Blue='\033[0;34m'         # Blue
  Purple='\033[0;35m'       # Purple
  Cyan='\033[0;36m'         # Cyan
  White='\033[0;37m'        # White

  # Bold
  BBlack='\033[1;30m'       # Black
  BRed='\033[1;31m'         # Red
  BGreen='\033[1;32m'       # Green
  BYellow='\033[1;33m'      # Yellow
  BBlue='\033[1;34m'        # Blue
  BPurple='\033[1;35m'      # Purple
  BCyan='\033[1;36m'        # Cyan
  BWhite='\033[1;37m'       # White

  # Underline
  UBlack='\033[4;30m'       # Black
  URed='\033[4;31m'         # Red
  UGreen='\033[4;32m'       # Green
  UYellow='\033[4;33m'      # Yellow
  UBlue='\033[4;34m'        # Blue
  UPurple='\033[4;35m'      # Purple
  UCyan='\033[4;36m'        # Cyan
  UWhite='\033[4;37m'       # White

  # Background
  On_Black='\033[40m'       # Black
  On_Red='\033[41m'         # Red
  On_Green='\033[42m'       # Green
  On_Yellow='\033[43m'      # Yellow
  On_Blue='\033[44m'        # Blue
  On_Purple='\033[45m'      # Purple
  On_Cyan='\033[46m'        # Cyan
  On_White='\033[47m'       # White

  # High Intensity
  IBlack='\033[0;90m'       # Black
  IRed='\033[0;91m'         # Red
  IGreen='\033[0;92m'       # Green
  IYellow='\033[0;93m'      # Yellow
  IBlue='\033[0;94m'        # Blue
  IPurple='\033[0;95m'      # Purple
  ICyan='\033[0;96m'        # Cyan
  IWhite='\033[0;97m'       # White

  # Bold High Intensity
  BIBlack='\033[1;90m'      # Black
  BIRed='\033[1;91m'        # Red
  BIGreen='\033[1;92m'      # Green
  BIYellow='\033[1;93m'     # Yellow
  BIBlue='\033[1;94m'       # Blue
  BIPurple='\033[1;95m'     # Purple
  BICyan='\033[1;96m'       # Cyan
  BIWhite='\033[1;97m'      # White

  # High Intensity backgrounds
  On_IBlack='\033[0;100m'   # Black
  On_IRed='\033[0;101m'     # Red
  On_IGreen='\033[0;102m'   # Green
  On_IYellow='\033[0;103m'  # Yellow
  On_IBlue='\033[0;104m'    # Blue
  On_IPurple='\033[0;105m'  # Purple
  On_ICyan='\033[0;106m'    # Cyan
  On_IWhite='\033[0;107m'   # White

class DB:
  
  def __init__(self):
    self.init_pool()    

  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)
  
  def template(self,*args):

    current_path = os.path.dirname(os.path.abspath(__file__))
    parent_path = os.path.abspath(os.path.join(current_path, '..'))

    pathing = list((parent_path,'db','sql',) + args)
    pathing[-1] = pathing[-1] + ".sql"

    template_path = os.path.join(*pathing)


    print(f'{textColours().BIGreen} Load SQL Template: {template_path}{textColours().Color_Off}')

    with open(template_path, 'r') as f:
      template_content = f.read()
    return template_content

  def query_commit(self,title,sql,params={}):
    self.print_sql(title,sql,params)
    pattern = r"\bRETURNING\b"
    is_returning = re.search(pattern, sql)

    try:
      with self.pool.connection() as conn:
        cur =  conn.cursor()
        cur.execute(sql,params)
        if is_returning:
          returning_param = cur.fetchone()[0]
        conn.commit() 
        if is_returning:
          return returning_param
    except Exception as err:
      self.print_sql_err(err)

  def query_value(self,title,sql,params={}):
    self.print_sql(title,sql,params)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql,params)
        json = cur.fetchone()
        return json[0]

  def query_object_json(self,title,sql,params={}):
    wrapped_sql = self.query_wrap_object(sql)
    self.print_sql(title, wrapped_sql,params)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql,params)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
    if json is None:
      return "{}"
    else:
      return json[0]
  
  def query_array_json(self,title,sql,params={}):
    wrapped_sql = self.query_wrap_array(sql)
    self.print_sql(title,wrapped_sql,params)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql,params)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
    if json is None:
      return "[]"

    else:
      return json[0]   
  
  def query_wrap_object(self,sql):
    wrapped_sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {sql}
    ) object_row);
    """
    return wrapped_sql

  def query_wrap_array(self,sql):
    wrapped_sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[null]'::json) FROM (
    {sql}
    ) array_row);
    """
    return wrapped_sql

  def print_params(self,title,params):
    print(f'{textColours().Blue}======{title}======')
    for key, value in params.items():
      print(key, ":", value)
    print(f'======{title}======{textColours().Color_Off}')

  def print_sql(self,title,sql,params={}):
    print(f'{textColours().Purple}======SQL STATEMENT-[{title}]======')
    print(f'{sql}')
  
    print(f'Params {params}')
  
    print(f'======SQL STATEMENT-[{title}]======\n{textColours().Color_Off}')

  def print_sql_err(self,err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print(f"{textColours().Red}======ERROR======\n")
    print(f"psycopg ERROR: " + err + " on line number: " + line_num)
    print(f"psycopg traceback: " + traceback + " type: " + err_type)
    print(f"======ERROR======{textColours().Color_Off}")

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

db = DB()