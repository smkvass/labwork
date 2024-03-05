with open("test.txt", "r") as testtxt:
    #testtxt.write("HELLO!!! \n" +
     #             "My name is Saya \n"+
      #            "I'm kazakh")
    lines = len(testtxt.readlines())
    print('Total number of lines:', lines)