
'''


curl -X POST -d "username=Sagar&password=******" http://127.0.0.1:8000/api/auth/token/


eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNhZ2FyIiwidXNlcl9pZCI6MSwiZW1haWwiOiJzYWdhcm1hbmphcmU3OTdAZ21haWwuY29tIiwiZXhwIjoxNDY2Nzk4MzkyfQ.s4xDw4JlY1RRD3oSO7LczP_NWUqCa7u-pBsZfhrN1F0


curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNhZ2FyIiwidXNlcl9pZCI6MSwiZW1haWwiOiJzYWdhcm1hbmphcmU3OTdAZ21haWwuY29tIiwiZXhwIjoxNDY2Nzk3OTMxfQ.8YlxTchWdNQqYrdkGe80To_K5JLiUTRzafRsn0-hykw" http://127.0.0.1:8000/api/comments/


curl -X POST -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNhZ2FyIiwidXNlcl9pZCI6MSwiZW1haWwiOiJzYWdhcm1hbmphcmU3OTdAZ21haWwuY29tIiwiZXhwIjoxNDY2Nzk5NDk1fQ.-U5vM5wVyQt--ZYySqdVLVAzFk1jxwo2pc_Yix6eGQU" -H "Content-Type: application/json" -d '{"content":"Child of JWT!"}' 'http://127.0.0.1:8000/api/comments/create/?slug=second-post&type=post&parent_id=12'


curl http://127.0.0.1:8000/api/comments/

'''