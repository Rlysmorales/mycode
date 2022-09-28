#!/bin/bash

LOOPER='yes'

while [ "$LOOPER" == "yes" ]
do
    echo "Please enter a username:"
    read LOGIN

    echo "creating user $LOGIN"
    useradd $LOGIN

    echo "Input a group for the new user: "
    read GROUP

    echo "Creating a new Group $GROUP"
    groupadd $GROUP

    adduser $LOGIN $GROUP
    
    echo "Do you want to create another user? (yes/no) "
    read LOOPER 

done
echo "done"

