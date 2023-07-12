SELECT 
      users.uuid
    FROM users
    WHERE
      users.handle =%(handle)s