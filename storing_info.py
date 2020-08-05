import  ast
with open("data.json",'r',encoding='cp1252') as read:
    red=read.readlines()
    # print(red)
    for i in red:
        print(i)
        print("\n")


    # for i in red:
    #     x=i.splitlines()
    #     print(x)
    #     print("\n")
    #     x=ast.literal_eval(i)
    #     main_list.append(x)
    # print(main_list[0][1])
