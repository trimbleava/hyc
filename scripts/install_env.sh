#!/bin/bash

echo "Entered $0 ********************"
echo


# Descr: This file checks on all the application dependencies first
#
# Run  : ./install_env.sh 
#
# Dev  : Beheen Moghaddam-Trimble, 4/12/2021 
#
# TODO : Find all the commands we need to suppress sudo for, instead of ALL that is currently implemented!!
#        Which one to use for the username value, below? whoami versus linux environment variables $USER or $LOGNAME 


#
# add the user to sudoer group
#
username=$LOGNAME
echo "Adding $username to sudoer group .........." 
# [: too many arguments -- one variable is split out into many arguments. double quote variable
# echo $(sudo -l -U beheen) 
TEST=$(sudo -l -U $username | grep "may run")
if [ ! "$TEST" ];  then
	sudo usermod -aG sudo $username
	sudo groups
fi
echo $TEST
echo

#
# suppress the sudo password during the automation run. See /etc/sudoers format <%yourusername%	ALL=(ALL:ALL) ALL>
# where 1st ALL means: rule applies to this user, 2nd ALL means: rule applies to all hosts, 3rd:4th means this user
# can run commands on behalf of all_users:all_groups, fifth ALL means: all_commands or cmd1 cmd2 cmd3 cmd4 ...
# To manually add the NOPASSWD to the system file create a file with this command: "sudo visudo -f /etc/sudoers.d/a_file
# with no extension and not space in file name as shown below:
#         "beheen ALL=NOPASSWD: /usr/bin/apt-get /usr/bin/apt  or ALL instead of individual commands that is dangerous!
# any file you put on /etc/sudoers.d/ directory is being read by master file /etc/sudoers.
# 
# To do it progmatically, user runs all commands on behalf of all users and all groups. 
echo "Suppressing password prompt for sudoer .........."
fname=$username"_nopass"
if [ ! -f /etc/sudoers.d/$fname ]; then
  text="$username ALL=(ALL) NOPASSWD: ALL"
  echo $text > $fname
  chmod 0440 $fname && sudo chown root:root $fname
  sudo mv $fname /etc/sudoers.d
fi
echo `ls -la /etc/sudoers.d/$fname`
echo



#
# update and upgrade once at deploy time, recommended is 2 weeks
#
echo "Upgrading packages .........."
sudo apt-get -y upgrade
echo


echo "Updating packages .........."
sudo apt-get -y update	 
echo

# add-apt-repository command is part of package software-properties-common 
# 
# install for git, lsb_release, netstat, curl
#
array=( git lsb-core net-tools curl wget software-properties-common)
for i in "${array[@]}"
do
	TEST=`apt list --installed $i | grep installed`
	[[ $TEST ]] || sudo apt-get -y install $i 
done
echo




