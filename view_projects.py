# View projects Function

def view_all_projects():
    f = open("projects.txt", 'r')
    lines = f.readlines()
    f.close()

    print("View All Projects")
    counter = 1
    for line in lines:
        if line == '\n':
            break
        line = line.split(":")
        print("Project Title: %s" % line[0])
        print("Project Details: %s" % line[1])
        print("Total Target: %s" % line[2])
        print("Start Time: %s" % line[3])
        print("End Time: %s" % line[4])
        
        
        counter += 1
