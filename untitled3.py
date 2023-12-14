import veryfi

client_id = "vrftXjKwnRGHG5RVtV7KhSOpwWNUp03LdZhtRGm"
client_secret = "P2nImuUmbJsdpRCSJFtOSsBFlxXWEm6hIrGCtlPaeeZ8xVXsVu2iZHxnbVtPWUZj1LjOGCznzXlpvz6jjLBEsGHSW97IJjTbElEKYWHy3Vb0OjpB0Kk7eIbJJsNTsgb4"
username = "lokeshpatil1105"
api_key = "67d5ddf5bdb798ee6342f0372b3efcd1"

client = veryfi.Client(client_id, client_secret, username, api_key)

categories = ["Travel","Airforce", "Loding", "job supplies and Materials","Grocery"]
jason_result = client.process_document("test1.jpg")
print(jason_result)