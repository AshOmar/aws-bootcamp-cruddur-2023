INSERT INTO public.users (display_name,email, handle, cognito_user_id)
VALUES
  ('Andrew Brown','ashraf.aomar+cruddur@gmail.com', 'andrewbrown' ,'MOCK'),
  ('Andrew Bayko','ashraf.aomar+cruddurBayko@gmail.com', 'bayko' ,'MOCK'),
  ('Ashraf Omar','ashraf.aomar@gmail.com','ashrafomar','MOCK'),
  ('Ashraf Ahmad Omar','ashraf.a.omar@gmail.com','aaomar','MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )