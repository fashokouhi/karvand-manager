import json
import os
import pprint 
count_id = 0
flag = True
if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists("data/karvands.json"):
    data ={ 
        "bootcamp" : {
            "title" : "karvand python",
            "year" : 2026
        },
        "karvands" : []
    }
    with open("data/karvands.json", "w") as file:
        json.dump(data, file, indent=4)
try:
    while flag == True:
        print("--"*20)
        print("Choose one of the options below:")
        print("1. Add karvand ")
        print("2. Show all karvands")
        print("3. Search for an employee with ID")
        print("4. Employee search based on skills ")
        print("5. Edit user information")
        print("6. Delete the application. ")
        print("7. General report")
        print("8. Exit")
        choice = int(input())
        
        #add
        if choice == 1:
            if os.path.exists("data/karvands.json") and os.path.getsize("data/karvands.json") > 0:
                with open("data/karvands.json","r") as file:
                    data = json.load(file)
                if len(data["karvands"]) == 0:
                    count_id = 1
                else:
                    count_id = data["karvands"][-1]["id"] + 1
            else:
                data = {
                    "bootcamp" : {
                        "title" : "karvand python",
                        "year" : 2026
                    },
                    "karvands" : []
                }
                count_id =1 

            name_karvand = input("Enter name and last name please : ")
            email = input("Enter your email : ")
            city = input("Enter your city name :")
            educational = input("Enter your educational qualification :")
            field_study = input("Enter your field of study :")
            skill_name = input("Enter skill name :")
            skill_level = input("Enter skill level :")
            # skill_Points = input("Enter skill Points (a number between 0 to 100 ): ")
           
            while True:
                try:
                    skill_Points = int (input("Enter skill point(0 to 100)"))
                    if  0 <= skill_Points <= 100:
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number .")
           

            education = {
                "degree" : educational,
                "field" : field_study
                }

            skills = {
                "name" : skill_name,
                "level" : skill_level,
                "score" : skill_Points
            } 
            
           
           
            new_karvand = {
                "id" : count_id,
                "full_name" : name_karvand,
                "email" : email,
                "city" : city,
                "education" : education,
                "skills" : [skills]
            }


            
                
            data["karvands"].append(new_karvand)


            with open ("data/karvands.json","w") as file:
                json.dump(data ,file ,indent=4)
            pprint.pprint(new_karvand,sort_dicts= False)


        elif choice == 2:
            with open("data/karvands.json" , "r") as file:
                data = json.load(file)

                if len(data["karvands"]) == 0:
                    print("no karvands found")
                else:
                    for line in data["karvands"]:
                        print("ID :",line["id"])
                        print("full name : ",line["full_name"])
                        print("email : ",line["email"])
                        print("city",line["city"])
                        print("field : ",line["education"]["field"])
                        print("degree :", line["education"]["degree"])

                        print("Skills:")
                        for skill in line["skills"]:
                            print("  Name:", skill["name"])
                            print("  Level:", skill["level"])
                            print("  Score:", skill["score"])

        elif choice == 3:
            id_search = int(input("Enter the ID that you want search : "))
            with open("data/karvands.json", "r") as file:
                data = json.load(file)
            for karvand in data["karvands"]:
                if id_search == karvand["id"]:
                    print("full name :",karvand["full_name"])
                    print("full name : ",karvand["full_name"])
                    print("email : ",karvand["email"])
                    print("city",karvand["city"])
                    print("field : ",karvand["education"]["field"])

                    print("Skills:")
                    for skill in karvand["skills"]:
                        print("  Name:", skill["name"])
                        print("  Level:", skill["level"])
                        print("  Score:", skill["score"])
                    break
            else:
                print("no karvand found.")
                    
        elif choice == 5:
            id_edit = int(input("Enter the ID that you want edit informaion : "))
            with open("data/karvands.json", "r") as file:
                data = json.load(file)
            for karvand in data["karvands"]:

                if id_edit == karvand["id"]:
                    print("1. email ")
                    print("2. city")
                    print("3. educational")
                    print("4.  field_study")
                    choice_edit = int(input("Enter choice for edit :"))
                    
                    if choice_edit == 1:
                        new_email = input("Enter new email : ")
                        karvand["email"] = new_email


                    elif choice_edit == 2:
                        new_city = input("Enter new city : ")
                        karvand["city"] = new_city

                    elif choice_edit == 3:
                        new_educational = input("Enter new educational : ")
                        karvand["education"]["degree"] = new_educational


                    elif choice_edit == 4:
                        new_field_study = input("Enter new field_study: ")
                        karvand["education"]["field"] = new_field_study
                    with open("data/karvands.json", "w") as file:
                        json.dump(data, file,indent=4)
                    print("Information updated successfully.")
                    
                    break
            else : 
                    print("no karvand found.")

        elif choice == 6:
            id_del = int(input("Enter the ID that you want delete : "))
            with open("data/karvands.json", "r") as file:
                data = json.load(file)
            for karvand in data["karvands"]:
                if id_del == karvand["id"]:
                    data["karvands"].remove(karvand)
                    break
            else:
                print("no karvand found.")

            with open("data/karvands.json", "w") as file:
                json.dump(data, file,indent=4)
            print("Deletion completed successfully.")


        elif choice == 8:
            flag = False
            break




except Exception as e:
    print(f"Error : {e}")