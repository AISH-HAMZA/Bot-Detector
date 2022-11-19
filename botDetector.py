import datetime as dt

fileLoader = open("log.txt", 'r')
total_lines = fileLoader.read()
total_lines = total_lines.split("\n")

firstTime = ""
IP = ""
status = ""


def initialize_data(time_data, current_status, ip_addr):
    global firstTime, status, IP

    if firstTime == "":
        firstTime = time_data

    if status == "":
        status = current_status

    if IP == "":
        IP = ip_addr


bot_time = dt.timedelta(hours=0, minutes=0, seconds=1)

for line in total_lines:
    if not len(line) < 5:
        split_data = line.replace("-", "").split(" ", 7)
        time_data = split_data[4]
        ip_addr = split_data[5].split("|")[1]
        
        current_status = split_data[-1]

        initialize_data(time_data, current_status, ip_addr)

        if firstTime != "" and "logged in" in status and IP == ip_addr and ("logged in" in current_status or
                                                                            "logged off" in current_status or
                                                                            "changed password" in current_status):
            if "logged off" in current_status:

                time_split = firstTime.split(":")
                time_split1 = time_data.split(":")
                time_1 = dt.timedelta(hours=int(time_split[0]), minutes=int(time_split[1]), seconds=int(time_split[2]))
                time_2 = dt.timedelta(hours=int(time_split1[0]), minutes=int(time_split1[1]),
                                      seconds=int(time_split1[2]))

                time_interval = time_2 - time_1

                firstTime = ""
                status = ""
                IP = ""

                if time_interval <= bot_time:
                    print("---> Bot Detected\n")

                    print("User = ", split_data[5].split("|")[2])
                    print("IP of user = ", ip_addr)
                    print("Total Time Taken to complete cycle = ", time_interval)
                    print("Current Status = ", current_status)
                    print("\n")

        elif firstTime != "" and "logged in" in status and IP != ip_addr and ("logged in" in current_status or
                                                                              "logged off" in current_status or
                                                                              "changed password" in current_status):
            firstTime = ""
            status = ""
            IP = ""
            initialize_data(time_data, current_status, ip_addr)

        else:
            firstTime = ""
            status = ""
            IP = ""
