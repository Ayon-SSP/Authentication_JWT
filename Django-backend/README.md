

we have used Json web token for authentication and authorization.
https://djoser.readthedocs.io/en/latest/base_endpoints.html#user-create

### POST: Register
http://127.0.0.1:8000/auth/users/
```json
{
    "username": "Ayonssp2",
    "email": "ayoniiiiii10@gmail.com",
    "password": "AYON#8sjJy@!",
    "re_password": "AYON#8sjJy@!"
}
```
Mail:
You're receiving this email because you need to finish activation process on Yes Twitter Clone.
Please go to the following page to activate account:
http://localhost:3000/activate/MTE/bot3rq-97cf78d5e769d1e34466e6faaa32b0ad
Thanks for using our site!
The Yes Twitter Clone team

![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/de0a2804-db4b-4a6b-a744-07afa283567f)
![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/bfcb2ff6-cf95-4bb3-a1d3-3fa55c498c47)





### POST: activate process
http://127.0.0.1:8000/auth/users/activation/
```json
{
    "uid": "MTQ",
    "token": "bot4pg-05dddb4b8d335c5f42158e3b824a95bb"
}
```

MAIL:
Your account has been created and is ready to use!
Thanks for using our site!
The Yes Twitter Clone team
![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/43a9dcf0-374e-4217-838a-c81e8954f17d)
![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/26d8605f-73c9-4118-a5c5-c7a93bf4af5a)




### POST: Get new access token
http://127.0.0.1:8000/auth/jwt/create/
```json
Request:
{
    "email": "ayoniiiiii10@gmail.com",
    "password": "AYON#8sjJy@!"
}
```
Response:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NTQ1MTMwNCwianRpIjoiNmUzYzdkYjU3YzZkNGM0ODk0Y2RhMGI0NDYzMGY3ZGMiLCJ1c2VyX2lkIjoxNH0.4Tkiuxv5CYXjqVXX_3psAzqemRs42FQR4b6jUS1TjMc",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1Mjc4NTA0LCJqdGkiOiIyODI1NThjOGNiOGI0YjdlYmZmZjE4YWY4MTg1YjczZCIsInVzZXJfaWQiOjE0fQ.FTWgGW4NZOdFgIwxB_Tpo65lROgl-EEjgJvs9hwda_I"
}
```

![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/c6ecde36-3506-407f-98d6-7b927ede70cd)


### POST: refresh token
http://127.0.0.1:8000/auth/jwt/refresh/

```json
{
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NTQ0MDQwMCwiaWF0IjoxNjg1MzU0MDAwLCJqdGkiOiI5ZWExM2Y3NWFjMWE0Mjc3YmU2OWMyYjM3NDE0MDRjMiIsInVzZXJfaWQiOjF9.VfQHNQBfH41INcGaLCRffVu5BeJokLzzXYUoYFk0jb8"
}
```
Response:
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1MzU0NDY3LCJpYXQiOjE2ODUzNTQwMDAsImp0aSI6IjUxNTA3NjcyMTI3NzQ0NTJhMWIxOTYxODc4MzQwMGI4IiwidXNlcl9pZCI6MX0.rG3r0xeC4fHTjxkd_Phv855U5Bavu-SnDyGovxji6Tc"
}
```

![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/04d59a62-37f6-4ce4-a40e-cdae7ba03585)


### POST: RESETPASSWORD

http://127.0.0.1:8000/auth/users/reset_password/
```json
Request:
{
    "email": "ayoniiiiii10@gmail.com"
}
```
![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/51ff5c07-1cb9-4d05-ba8d-d3eb045e98c4)
![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/a3bb0ea9-909b-4f13-9686-52940d8b8c1e)


http://127.0.0.1:8000/auth/users/reset_password_confirm/
### POST: RESETPASSWORD Conformation
```json
{
    "uid": "MQ",
    "token": "boyhrt-94965e13f5aea47e3562920f4f4482b1",
    "new_password": "AYON#8sjJy@!",
    "re_new_password": "AYON#8sjJy@!_new"
}
```

![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/8931abbd-586f-42fa-b55a-0733c8e6232e)

![image](https://github.com/Ayon-SSP/Artical_temp/assets/80549753/e3738f28-c4b4-42ae-8872-49252116cd73)




And More [`djoser`](https://djoser.readthedocs.io/en/latest/jwt_endpoints.html)