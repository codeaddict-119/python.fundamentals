# USE of match case
def https_status(code):
       match code:
              case 200:
                     return "OK"
              case 400:
                     return "warning!!"
              case 404:
                     return "----NOT FOUND----"
              case 500:
                     return "------sever error[::::::]--------\nhttps://1111/x55/000000x/"
              case _:
                     return "-----------"
print(https_status(400))
print("_______________")
print(https_status(200))
print("_______________")
print(https_status(404))
print("_______________")
print(https_status(500))
       
              