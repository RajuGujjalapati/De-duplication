import  ast
with open("personal.json",'r',encoding='cp1252') as read:
    main_list=[]
    for i in read.readlines():
        x=i.splitlines()
        print(x)
        print("\n")
    #     x=ast.literal_eval(i)
    #     main_list.append(x)
    # print(main_list[0][1])
    print("\n")
