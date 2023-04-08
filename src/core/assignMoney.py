def assign_money(object, data: dict, iterable: list):
    temp_list = []
    for words in iterable.split():
        temp_list.append(words)
    print(temp_list)
    loop_list = [4,3,2,1]
    for words in temp_list:
        for items in data.keys():
            for i in loop_list:
                if (
                    words.title() == items.title()
                    and temp_list[temp_list.index(words) + i].isdigit()
                ):
                    print(words)
                    print("Success")
                    data[items][0] = temp_list[
                        temp_list.index(words) + i
                    ]


            # if (
            #     words.title() == items.title()
            #     and temp_list[temp_list.index(words) + 1].isdigit()
            # ):
            #     print(words)
            #     print("Success")
            #     data[items][0] = temp_list[
            #         temp_list.index(words) + 1
            #     ]
            # elif (
            #     words.title() == items.title()
            #     and temp_list[temp_list.index(words) + 2].isdigit()
            # ):
            #     print(words)
            #     print("Success")
            #     data[items][0] = temp_list[
            #         temp_list.index(words) + 2
            #     ]
            # elif (
            #     words.title() == items.title()
            #     and temp_list[temp_list.index(words) + 3].isdigit()
            # ):
            #     print(words)
            #     print("Success")
            #     data[items][0] = temp_list[
            #         temp_list.index(words) + 3
            #     ]
            # elif (
            #     words.title() == items.title()
            #     and temp_list[temp_list.index(words) + 4].isdigit()
            # ):
            #     print(words)
            #     print("Success")
            #     data[items][0] += int(temp_list[
            #         temp_list.index(words) + 4
            #     ])
            
    print(data)