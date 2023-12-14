import veryfi
import pprint

shop_keeper_id = "vrftXjKwnRGHG5RVtV7KhSOpwWNUp03LdZhtRGm"
shop_keeper_secret = "P2nImuUmbJsdpRCSJFtOSsBFlxXWEm6hIrGCtlPaeeZ8xVXsVu2iZHxnbVtPWUZj1LjOGCznzXlpvz6jjLBEsGHSW97IJjTbElEKYWHy3Vb0OjpB0Kk7eIbJJsNTsgb4"
username = "lokeshpatil1105"
api_key = "67d5ddf5bdb798ee6342f0372b3efcd1"

shop_keeper = veryfi.Client(shop_keeper_id, shop_keeper_secret, username, api_key)

bill = shop_keeper.process_document("opencv_frame_0.png")

pprint.pprint(bill)