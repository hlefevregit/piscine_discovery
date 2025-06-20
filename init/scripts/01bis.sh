 #!/bin/bash

printf "%-20s | %-6s | %-s\n" "Login" "UID" "Path"
printf "%-20s-+-%-6s-+-%-s\n" "--------------------" "------" "-------------------------"

sort -t ':' -k3,3n /etc/passwd | while IFS=':' read -r login _ uid _ _ path _; do
    printf "%-20s | %-6s | %-s\n" "$login" "$uid" "$path"
done 



# MADE BY cseren, take it as a reference since it is more readable