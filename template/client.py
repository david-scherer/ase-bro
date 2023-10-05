import requests
import json
import sys
import math

# https://reset.inso.tuwien.ac.at/ase/slot1-185e01ee92/assignment/11777743/token
# https://reset.inso.tuwien.ac.at/ase/slot1-185e01ee92/assignment/11777743/stage/1/pdf?token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMTc3Nzc0MyIsInNvbHZlZCI6IjAiLCJzY2VuYXJpbyI6Imh5cGVybG9vcCIsImV4cCI6MTY3ODE3NzEyN30.sF5pmZ4Mnlof8ZqU0o4H55TDYnr2Fk0WDpORs8i_oaA
# https://reset.inso.tuwien.ac.at/ase/slot1-185e01ee92/assignment/11777743/stage/1/testcase/1?token=https://reset.inso.tuwien.ac.at/ase/slot1-185e01ee92/assignment/11777743/stage/1/pdf?token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMTc3Nzc0MyIsInNvbHZlZCI6IjAiLCJzY2VuYXJpbyI6InBsYW5ldHMiLCJleHAiOjE2NzgwOTA2ODR9.kbz32CBw_NhZMZ9JQd_P05OJF4MFWYxhUY2QkIY6kxQ
# https://reset.inso.tuwien.ac.at/ase/slot1-185e01ee92/assignment/11777743/finished?token=eyJhbGciO

class Target:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


targets = []
obstacle = None
accessiblePoints = []
origin = Target(0, 0)
obastaclePoints = []
obstacle = None

o1 = None
o2 = None
o1Tan = None
o2Tan = None

def s1Fill(url):
    response = getRequest(url).json()
    print(response)
    for target in response["targets"]:
        targets.append(Target(target["x"], target["y"]))
    
    key = None
    value = None
    #for key, value in response["obstacle"].items():
    #    if "point" in key:
    #       obastaclePoints.append(Target(value["x"], value["y"])) 
    global o1, o2, o1Tan, o2Tan
    if "pointA" in response["obstacle"]:
        o1 = Target(response["obstacle"]["pointA"]["x"], response["obstacle"]["pointA"]["y"])
        o2 = Target(response["obstacle"]["pointB"]["x"], response["obstacle"]["pointB"]["y"])
        o1Tan = math.atan2(o1.x, o1.y)
        o2Tan = math.atan2(o2.x, o2.y)
        # print("x: %s, y: %s" % (o1.x, o1.y))

    global obstacle
    if "line" in response["obstacle"]:
        obstacle = response["obstacle"]["line"]
    print(obstacle)
    # print(obastaclePoints)
    

def stage1():
    global obstacle
    if obstacle is None:
        print("muois")
    print("+++++++++ obstacle is %s" % (obstacle))
    for target in targets:
        if obstacle != None and obstacle > 0:
            if target.y < obstacle:
                point = {"x": target.x, "y": target.y}
                accessiblePoints.append(point)
        elif obstacle != None and obstacle < 0:
            if target.y > obstacle:
                point = {"x": target.x, "y": target.y}
                accessiblePoints.append(point)


def stage2():
    global obstacle, o1Tan, o2Tan
    for target in targets:
        if o1Tan != None:
            targetTan = math.atan2(target.x, target.y)
            left = o2Tan
            right = o1Tan
            
            if obstacle is None:
                if (o1Tan > 0 and o1Tan < 1.5707963267948966) or (o1Tan < 0 and o1Tan > -1.5707963267948966):
                    if o1Tan < o2Tan:
                        print("swap")
                        min = o1Tan
                        right = o2Tan
                        left = min
                    print("obstacle is %s and obere h mit %s und %s and ttan is %s" % (obstacle, o1Tan, o2Tan, targetTan))
                    if not (targetTan >= left and targetTan <= right):
                        print("add")
                        point = {"x": target.x, "y": target.y}
                        accessiblePoints.append(point)
                else:
                
                    print("obstacle is %s and untere h mit %s und %s and ttan is %s" % (obstacle, o1Tan, o2Tan, targetTan))
                    if left < 0 and right > 0:
                        if o1Tan < o2Tan:
                            print("swap")
                            min = o1Tan
                            o1Tan = o2Tan
                            o2Tan = min
                        if not (abs(o2Tan) <= abs(targetTan) and abs(o1Tan) <= abs(targetTan)):
                            print("add")
                            point = {"x": target.x, "y": target.y}
                            accessiblePoints.append(point)
                    elif o2Tan < 0 and o1Tan < 0:
                        if o1Tan > o2Tan:
                            print("swap")
                            min = o1Tan
                            o1Tan = o2Tan
                            o2Tan = min
                        if not (o2Tan >= targetTan >= o1Tan):
                            print("add")
                            point = {"x": target.x, "y": target.y}
                            accessiblePoints.append(point)
                    elif o2Tan > 0 and o1Tan > 0:
                        if o1Tan > o2Tan:
                            print("swap")
                            min = o1Tan
                            o1Tan = o2Tan
                            o2Tan = min
                        if not (o2Tan >= targetTan >= o1Tan):
                            print("add")
                            point = {"x": target.x, "y": target.y}
                            accessiblePoints.append(point)

            else: 
                if (o1Tan > 0 and o1Tan < 1.5707963267948966) or (o1Tan < 0 and o1Tan > -1.5707963267948966):
                    print("o is %s and obere h mit %s und %s and ttan is %s" % (obstacle, o1Tan, o2Tan, targetTan))
                    if not (targetTan >= o2Tan and targetTan <= o1Tan):
                        if obstacle > 0:
                            if target.y < obstacle:
                                print("add")
                                point = {"x": target.x, "y": target.y}
                                accessiblePoints.append(point)
                        elif obstacle < 0:
                            if target.y > obstacle:
                                print("add")
                                point = {"x": target.x, "y": target.y}
                                accessiblePoints.append(point)
                else:
                    print("o is %s and untere h mit %s und %s and ttan is %s" % (obstacle, o1Tan, o2Tan, targetTan))
                    if not (abs(o2Tan) <= abs(targetTan) >= abs(o1Tan)):
                        if obstacle > 0:
                            if target.y < obstacle:
                                print("add")
                                point = {"x": target.x, "y": target.y}
                                accessiblePoints.append(point)
                        elif obstacle < 0:
                            if target.y > obstacle:
                                print("add")
                                point = {"x": target.x, "y": target.y}
                                accessiblePoints.append(point)
        else: 
            stage1()
    obstacle = None
    o1Tan = None
    o2Tan = None

def postSolution(url, data):
    response = requests.post(url, json=data)
    return response

def getRequest(url):
    response = requests.get(url)
    return response

def main():    
    token = getRequest("https://reset.inso.tuwien.ac.at/ase/retake-37by915390/assignment/11777743/token").json()["token"]
    print(token)
    url = "https://reset.inso.tuwien.ac.at/ase/retake-37by915390/assignment/11777743/stage/1/testcase/1?token=%s" % (token)
    #url = "https://reset.inso.tuwien.ac.at/ase/retake-37by915390/assignment/11777743/stage/2/testcase/1?token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMTc3Nzc0MyIsInNvbHZlZCI6IjUwIiwic2NlbmFyaW8iOiJoeXBlcmxvb3AiLCJleHAiOjE2NzgxODMwNjV9.7T-QoOq79RTqB3vj30-4Nn24BucYVMfTWxODk_aftQ0"

    idk = True
    while(idk):
        if "stage/1" in url:
            s1Fill(url)
            stage1()
        elif "stage/2" in url:
            global obstacle
            obstacle = None
            s1Fill(url)
            stage2()
        data = {"accessiblePoints": accessiblePoints}
        # print(["x:%s and y:%s" % (t.x, t.y) for t in targets])
        # print(accessiblePoints)
        print(data)
        resp = postSolution(url, data)
        print(resp.json())
        if "linkToNextTask" in resp.json():
            url = resp.json()["linkToNextTask"]
        else: 
            idk = False

        print("\n--------------\n")
        reset()
    
def reset():
    targets.clear()
    accessiblePoints.clear()


if __name__ == "__main__":
    #print(math.atan2(-3, -5))
    #print(math.atan2(4, -6))
    #print(math.atan2(0, -6))
    #print(math.atan2(0, 6))
    #print(math.atan2(5, 0))
    #print(math.atan2(-15, 0))

    main()
