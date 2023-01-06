# Delete project Function
def delete_project():
     print(" Delete Project")
     project_title = input("Project Title: ")
     total_target = input("Total Target : ")
     f = open("projects.txt", 'r')
     lines = f.readlines()
     f.close()

     new_lines = []
     for line in lines:
        line = line.split(":")
        if not (line[0] == project_title and line[2] == total_target):
            line = ":".join(line)+'\n'
            new_lines.append(line)

     f = open("projects.txt", 'w')
     f.writelines(new_lines)
     f.close()
     print("It is deleted")