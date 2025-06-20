#!/bin/bash

echo "Utilisateurs actuellement connectés :"
who | awk '{print $1}' | sort | uniq

read -p "Entrez le nom d'utilisateur à supprimer : " user

if who | grep -qw "$user"; then
    read -p "Êtes-vous sûr de vouloir supprimer $user ? (y/n) : " confirm
    if [[ $confirm == "y" ]]; then
        pkill -KILL -u "$user"
        userdel -r "$user"
        echo "Utilisateur $user supprimé."
    else
        echo "Suppression annulée."
    fi
else
    echo "L'utilisateur $user n'est pas connecté."
fi

# MADE BY cseren, take it as a reference since it is more readable
# This script lists currently logged-in users, prompts for a username to delete,
# and if the user is logged in, it confirms deletion and removes the user along with their home directory.
# If the user is not logged in, it simply informs that the user is not connected.
# It uses `who` to list logged-in users, `pkill` to kill processes for the user, and `userdel` to delete the user account and home directory.
# It also includes a confirmation step before proceeding with the deletion.
# The script is designed to be user-friendly and provides clear prompts and messages.