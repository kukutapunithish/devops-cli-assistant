import os

while(True):
    os.system("tput setaf 3")
    print('---------------------------Welcome to our Menu!!! Happy to Help!!!---------------------------\n')
    os.system("tput setaf 7")
    print("where do you want to run your program ")
    print("""\n
            press 1: Local
            press 2: Remote
            press 3: exit the Menu""")
    answer=input()
    answer1=int(answer)
    if(answer1==3):
        exit()
    elif (answer1>3):
        print("please enter a valid number")
        continue    
    elif (answer1==2):
        
        while(True):
            os.system("tput setaf 3")
            print("---------------------------Choose which tech you want to interact!!---------------------------")
            os.system("tput setaf 7")
            print("""\n
            press 1: Docker
            press 2: Linux OS
            press 3: Back to previous Choices""")
            y=input()
            x=int(y)
            if(x==3):
                break
            elif(x>3):
                print("please enter a valid number")
                continue
            elif(x==1):
                ip=input('enter the ip address : ')
                while(True):
                    os.system("tput setaf 3")
                    print('                         welcome in Docker world                 ')
                    print('----------------------------------------------------------------------------------')
                    os.system("tput setaf 7")
                    print("""\n
                    press 1: To install docker
                    press 2: To Check the status of docker
                    press 3: To start the services of Docker
                    press 4: To stop the services of Docker
                    press 5: To install and run the docker container
                    press 6: To see all docker images you have
                    press 7: To see all the docker container you have
                    press 8: To see all the docker running container
                    press 9: To delete the docker container
                    press 10: To terminate all the docker os
                    press 11: To launch the web server on docker container
                    press 12: Back to previous choices""")
                    c=int(input('Enter the choice : '))
                    if (c == 1):
                        os.system("ssh {} yum install docker-ce --nobest -y".format(ip))
                    elif (c == 2):
                        os.system("ssh {} docker info".format(ip))
                    elif (c == 3):
                        os.system("ssh {} systemctl start docker".format(ip))
                    elif (c == 4):
                        os.system("ssh {} systemctl stop docker".format(ip))
                    elif (c == 5):
                        name=input('enter the image name:version to install :')
                        naa=input('give name to container :')
                        os.system("ssh {} docker pull {} ".format(ip,name))
                        os.system("ssh {} docker run -dit --name {} {} ".format(ip,naa,name))	
                    elif (c == 6):
                        os.system("ssh {} docker images ".format(ip))
                    elif (c == 7):
                        os.system("ssh {} docker ps -a".format(ip))
                    elif (c == 8):
                        os.system("ssh {} docker ps".format(ip))
                    elif (c == 9):
                        a=input('enter os_name :')
                        os.system("ssh {} docker rm {}".format(ip,a))
                    elif (c == 10):
                        os.system("ssh {} docker rm `docker ps -a -q`".format(ip))
                    elif (c == 11):
                        name=input('enter the image name:version to install :')
                        naa=input('give name to container :')
                        os.system("docker pull {} ".format(name))
                        os.system("docker run -it --name {} {} ".format(naa,name))
                        os.system("ssh {} yum install httpd -y".format(ip))
                        fn=input('enter file name : ')
                        on=input('enter os name :') 
                        os.system("ssh {} docker cp {} {}:/var/www/html/ ".format(ip,fn,on))
                        os.system("ssh {} /usr/sbin/httpd".format(ip))
                    elif (c==12):
                        break
            elif(x==2):
                ip=input('enter the ip address : ')
                while(True):
                    os.system("tput setaf 3")
                    print('                         Interact with Linux OS                  ')
                    print('----------------------------------------------------------------------------------')
                    os.system("tput setaf 7")
                    print("""\n
                    press 1: To check date
                    press 2: To Check the current user
                    press 3: To know the current directory
                    press 4: To create a new folder
                    press 5: To see the calender 
                    press 6: To check memory
                    press 7: To check  storage
                    press 8: To check the free ports in your system
                    press 9: To check mounted folders to storage devices
                    press 10: To check your ip Address
                    press 11: Back to previous choices""")
                    d=int(input('Enter the choice : '))
                    if (d == 1):
                        os.system("ssh {} date".format(ip))
                    elif (d == 2):
                        os.system("ssh {} whoami".format(ip))
                    elif (d == 3):
                        os.system("ssh {} pwd".format(ip))
                    elif (d == 4):
                        os.system("ssh {} mkdir".format(ip))
                    elif (d == 5):
                        os.system("ssh {} cal ".format(ip))	
                    elif (d == 6):
                        os.system("ssh {} free -m ".format(ip))
                    elif (d == 7):
                        os.system("ssh {} fdisk -l".format(ip))
                    elif (d == 8):
                        os.system("ssh {} netstat -tnlp".format(ip))
                    elif (d == 9):
                        os.system("ssh {} df -h".format(ip))
                    elif (d == 10):
                        os.system("ssh {} ifconfig enp0s3".format(ip))
                    
                    elif (d==11):
                        break
    elif(answer1==1):
        
        while(True):
            os.system("tput setaf 3")
            print("---------------------------Choose which tech you want to interact!!---------------------------")
            os.system("tput setaf 7")
            print("""\n
            press 1: Docker
            press 2: Linux OS 
            press 3: Hadoop Cluster
            press 4: AWS cloud
            press 5: Back to previous Choices""")
            y=input()
            x=int(y)
            if(x==5):
                break
            elif(x>5):
                print("please enter a valid number")
                continue
            elif(x==1):
                while(True):
                    os.system("tput setaf 3")
                    print('                         welcome in Docker world                 ')
                    print('----------------------------------------------------------------------------------')
                    os.system("tput setaf 7")
                    print("""\n
                    press 1: To install docker
                    press 2: To Check the status of docker
                    press 3: To start the services of Docker
                    press 4: To stop the services of Docker
                    press 5: To install and run the docker container
                    press 6: To see all docker images you have
                    press 7: To see all the docker container you have
                    press 8: To see all the docker running container
                    press 9: To delete the docker container
                    press 10: To terminate all the docker os
                    press 11: To launch the web server on docker container
                    press 12: Back to previous choices""")
                    c=int(input('Enter the choice : '))
                    if (c == 1):
                        os.system("yum install docker-ce --nobest -y")
                    elif (c == 2):
                        os.system("docker info")
                    elif (c == 3):
                        os.system("systemctl start docker")
                    elif (c == 4):
                        os.system("systemctl stop docker")
                    elif (c == 5):
                        name=input('enter the image name:version to install :')
                        naa=input('give name to container :')
                        os.system("docker pull {} ".format(name))
                        os.system("docker run -it --name {} {} ".format(naa,name))	
                    elif (c == 6):
                        os.system("docker images ")
                    elif (c == 7):
                        os.system("docker ps -a")
                    elif (c == 8):
                        os.system("docker ps")
                    elif (c == 9):
                        na=input('enter os_name :')
                        os.system("docker rm {}".format(na))
                    elif (c == 10):
                        os.system("docker rm `docker ps -a -q`")
                    elif (c == 11):
                        name=input('enter the image name:version to install :')
                        naa=input('give name to container :')
                        os.system("docker pull {} ".format(name))
                        os.system("docker run -it --name {} {} ".format(naa,name))
                        os.system("yum install httpd -y")
                        fn=input('enter file name : ')
                        on=input('enter os name :') 
                        os.system("docker cp {} {}:/var/www/html/ ".format(fn,on))
                        os.system("/usr/sbin/httpd")
                    elif (c==12):
                        break
            elif(x==2):
                os.system("tput setaf 3")
                print('                         Interact with Linux OS                  ')
                print('----------------------------------------------------------------------------------')
                os.system("tput setaf 7")
                while(True):
                    print("""\n
                    press 1: To check date
                    press 2: To Check the current user
                    press 3: To know the current directory
                    press 4: To create a new folder
                    press 5: To see the calender 
                    press 6: To check memory
                    press 7: To check  storage
                    press 8: To check the free ports in your system
                    press 9: To check mounted folders to storage devices
                    press 10: To check your ip Address
                    press 11: Back to previous choices""")
                    d=int(input('Enter the choice : '))
                    if (d == 1):
                        os.system("date")
                    elif (d == 2):
                        os.system("whoami")
                    elif (d == 3):
                         os.system("pwd")
                    elif (d == 4):
                        print("enter the folder name")
                        foldername=input()
                        os.system("mkdir {}".format(foldername))
                    elif (d == 5):
                         os.system("cal")	
                    elif (d == 6):
                         os.system("free -m")
                    elif (d == 7):
                         os.system("fdisk -l")
                    elif (d == 8):
                         os.system("netstat -tnlp")
                    elif (d == 9):
                         os.system("df -h")
                    elif (d == 10):
                         os.system("ifconfig")
                    
                    elif (d==11):
                        break
            elif(x==3):
                os.system("tput setaf 3")
                print('                         Interact with Hadoop Cluster                 ')
                print('----------------------------------------------------------------------------------')
                os.system("tput setaf 7")
                while(True):
                    print("""
                    \n
                    press 1: Get how many data nodes you have
                    press 2: To check all the files and folders in hadoop cluster
                    press 3: To remove a file in hadoop cluster
                    press 4: to read a file in hadoop cluster
                    press 5: to create a file in hadoop cluster directly
                    press 6: to create a directory in hadoop cluster
                    press 7: to put a file from your local system to hadoop cluster
                    press 8: to upload a file with different block size
                    press 9: back to previous choices
                    """)
                    print("pls write the option no. you want to choose:", end=' ')
                    y=input()
                    x=int(y)
                    if (x==1):
                        os.system("hadoop dfsadmin -report")
                    elif(x==2):
                        print("to check  files and folders in  root directory [y/n]")
                        answer=input()
                        if (answer=="y"):
                            
                            cmd= "hadoop fs -ls  /"
                            os.system(cmd)
                        else:
                            print("enter the name of folder(inside root directory)")
                            foldername=input()
                            cmd= "hadoop fs -ls /{0}".format(foldername)
                            os.system(cmd)

                    elif (x==9):
                        break
                    elif (x>9):
                        print("pls enter a valid option")
                        continue
                    elif (x==3):
                        print("to remove a file from root directory [y/n]")
                        answer=input()
                        if (answer=="y"):
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -rm /{0}".format(filename)
                            os.system(cmd)
                        else:
                            print("enter the name of folder")
                            foldername=input()
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -rm /{0}/{1}".format(foldername,filename)
                            os.system(cmd)
                    elif (x==4):
                        print("to read  a file from root directory [y/n]")
                        answer=input()
                        if (answer=="y"):
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -cat /{0}".format(filename)
                            os.system(cmd)
                            print()
                        else:
                            print("enter the name of folder")
                            foldername=input()
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -cat /{0}/{1}".format(foldername,filename)
                            os.system(cmd)
                            print()
                    elif (x==5):
                        print("to create  a file in the  root directory [y/n]")
                        answer=input()
                        if (answer=="y"):
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -touchz /{0}".format(filename)
                            os.system(cmd)
                            print()
                        else:
                            print("enter the name of folder")
                            foldername=input()
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -touchz /{0}/{1}".format(foldername,filename)
                            os.system(cmd)
                            print()

                    elif (x==6):
                        print("enter the name of directory you want to create(inside root directory)")
                        foldername=input()
                        cmd= "hadoop fs -mkdir /{0}".format(foldername)
                        os.system(cmd)
                    elif (x==7):
                        print("to put  a file in the  root directory [y/n]")
                        answer=input()
                        if (answer=="y"):
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -put {0} /".format(filename)
                            os.system(cmd)
                            print()
                        else:
                            print("enter the name of folder")
                            foldername=input()
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -put {1} /{0}".format(foldername,filename)
                            os.system(cmd)
                            print()
                    elif (x==8):
                        print("to put  a file in the  root directory [y/n]")
                        answer=input()
                        if (answer=="y"):
                            print("enter the block size (>=512) in bytes")
                            blocksize=input()
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -Ddfs.block.size={1} -put {0} /".format(filename,blocksize)
                            os.system(cmd)
                            print()
                        else:
                            print("enter the block size (>=512) in bytes")
                            blocksize=input()
                            print("enter the name of folder")
                            foldername=input()
                            print("enter the name of file")
                            filename=input()
                            cmd= "hadoop fs -Ddfs.block.size={2} -put {1} /{0}".format(foldername,filename,blocksize)
                            os.system(cmd)
                            print()
            elif(x==4):
                os.system("tput setaf 3")
                print('                         Interact with AWS Cloud                ')
                print('----------------------------------------------------------------------------------')
                os.system("tput setaf 7")
                while(True):
                    print("""
                    \n
                    press 1: Display all instances and their details
                    press 2: Start an instance
                    press 3: Stop an instance
                    press 4: Terminate an instance
                    press 5: Display all security groups
                    press 6: Display all images
                    press 7: Display all s3 buckets
                    press 8: Copy file from s3 to s3
                    press 9: Creating a http link for an file
                    press 10: Remove a bucket
                    press 11: Create a bucket
                    press 12: View billing
                    press 13: Display s3 monythly usage
                    press 14: Create a EBS volume
                    press 15: To create a key-pair
                    press 16: To create a security group
                    press 17: To add ingress rules to a security group
                    press 18: To launch an ec2 instance
                    press 19: To attach ebs volume to your instance
                    press 20: Back to previous choices

                    """)
                    print("please write the option number you want to choose:", end=' ')
                    y = input()
                    x = int(y)
                    if (x == 1):
                        cmd='aws ec2 describe-instances --filters Name=tag-key,Values=Name --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[0].Value}" --output text'
                        #cmd='aws ec2 describe-instances  --query Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,tag:Tags[0].Value}" --output table'
                        os.system(cmd)
                    elif(x == 2):
                        print("type the instance id which you want to start")
                        id = input()
                        cmd = "aws ec2 start-instances --instance-ids {}".format(id)
                        os.system(cmd)
                    elif (x == 3):
                        print("enter the id of the instance that you want to stop")
                        id = input()
                        cmd = "aws ec2 stop-instances --instance-ids {}".format(id)
                        os.system(cmd)
                    elif (x == 4):
                        print("enter the id of the instance that you want to terminate")
                        id = input()
                        cmd = "aws ec2 terminate-instances --instance-ids {}".format(id)
                        os.system(cmd)
                    elif (x == 5):
                        cmd = "aws ec2 describe-security-groups"
                        os.system(cmd)
                        print()
                    elif (x == 6):
                        cmd = "aws ec2 describe-images  --query Images[*].[ImageId]"
                        os.system(cmd)
                    elif (x == 7):
                        cmd = 'aws s3api list-buckets --query "Buckets[].Name"'
                        os.system(cmd)
                    elif (x == 8):
                        print("name of the bucket you want to move")
                        b1 = input()
                        print("name of the file want to move with extension")
                        m1 = input()
                        print("name of the destination bucket")
                        b2 = input()
                        print("name of the file want to move with extension")
                        m2 = input()
                        cmd = "aws s3 cp s3://{}/{} s3://{}/{}".format(b1, m1, b2, m2)
                        os.system(cmd)
                    elif (x == 9):
                        print("enter the name of the bucket")
                        b = input()
                        print("enter the name of the file with extension")
                        f = input()
                        cmd = "aws s3 presign s3://{}/{}".format(b, f)
                        os.system(cmd)
                    elif (x == 10):
                        print("enter the name of the bucket")
                        b = input()
                        print("enter the name of the file with extension")
                        f = input()
                        cmd = "aws s3 rm s3://{}/{}".format(b, f)
                        os.system(cmd)
                    elif (x == 11):
                        print("enter a unique name of the bucket")
                        b = input()
                        cmd = "aws s3api create-bucket --bucket {} --region ap-south-1".format(b)
                        os.system(cmd)
                    elif (x == 12):
                        print("start date and time in unix format")
                        s=input()
                        print("end date and time in unix format")
                        e=input()
                        cmd = "aws route53domains view-billing --region us-east-1 --start-time {} --end-time {}".format(s, e)
                        os.system(cmd)
                    elif (x == 13):
                        print("start date and time in yyyy-mm-dd format")
                        s=input()
                        print("end date and time in yyyy-mm-dd format")
                        e=input()
                        cmd = 'aws ce get-cost-and-usage --time-period Start={},End={} --granularity MONTHLY --metrics "BlendedCost" "UnblendedCost" "UsageQuantity" --group-by Type=DIMENSION,Key=SERVICE Type=TAG,Key=Environment --filter file://filters.json'.format(s, e)
                        os.system(cmd)
                    elif (x == 14):
                        print("enter the size of the EBS volume")
                        s = input()
                        cmd = "aws ec2 create-volume --volume-type gp2 --size {} --availability-zone us-east-1".format(s)
                        os.system(cmd)
                    elif( x==20):
                        break
                    elif(x == 15):
                        print("enter the name of your key-pair")
                        s = input()
                        cmd = "aws ec2 create-key-pair --key-name {}".format(s)
                        os.system(cmd)
                    elif(x==16):
                        print("enter the name of your security group")
                        s=input()
                        print("enter the discription of your security group")
                        e=input()
                        cmd = 'aws ec2 create-security-group --group-name {0} --description "{1}"'.format(s, e)
                        os.system(cmd)
                    elif(x==17):
                        print("""\n
                        Enter the rule you want to add
                        press 1: ssh
                        press 2: http
                        press 3: Custom tcp""")
                        g=input()
                        h=int(g)
                        if(h==1):
                            print("Enter the security group id")
                            sg=input()
                            os.system("aws ec2 authorize-security-group-ingress  --group-id {}     --protocol tcp       --port 22       --cidr 0.0.0.0/0".format(sg))
                        elif(h==2):
                            print("Enter the security group id")
                            sg=input()
                            os.system("aws ec2 authorize-security-group-ingress  --group-id {}     --protocol http       --port 80       --cidr 0.0.0.0/0".format(sg))
                        elif(h==3):
                            print("Enter the security group id")
                            sg=input()
                            print("enter the tcp port ")
                            port=input()
                            os.system("aws ec2 authorize-security-group-ingress  --group-id {}     --protocol tcp       --port {}       --cidr 0.0.0.0/0".format(sg,port))
                        elif(h>3):
                            print("pls enter a valid option")
                    elif(x==18):
                        print("enter the ami-id")
                        ami=input()
                        print("enetr the instance type")
                        typei=input()
                        print("enter the security group id you want to attach")
                        sgid=input()
                        print("number of instances you want to launch")
                        count=input()
                        print("enetr the key you want to attach")
                        key=input()
                        os.system("aws ec2 run-instances --image-id {0} --instance-type {1} --count {2} --key-name {3} --security-group-ids {4}".format(ami,typei,count,key,sgid))
                    elif(x==19):
                        print("enter the instance id")
                        iid=input()
                        print("enter the volume id")
                        vid=input()
                        os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdf".format(vid,iid))
