#!/bin/bash

correct_password=$MY_PASSWORD
attempts=0

while [ $attempts -lt 3 ]; do
  read -s -p "Enter your password: " entered_password

  if [ "$entered_password" == "$correct_password" ]; then
    echo "Password accepted!!!"
    break
  else
    echo "Password incorrect, please try again"
    ((attempts++))
  fi
done

if [ $attempts -eq 3 ]; then
  echo "You have reached the maximum number of attempts"
  exit 1
fi

echo -e "You can proceed with the rest of your script\n"
echo "What you want to do?"

echo "1. Encrypt"
echo "2. Decrypt"

read -p "Enter your choice: " choice

if [ $choice -eq 1 ]; then
  echo "Encrypting..."
  python3 ./encrypt.py
elif [ $choice -eq 2 ]; then
  echo "Decrypting..."
  python3 ./decrypt.py
else
  echo "Invalid choice"
fi
