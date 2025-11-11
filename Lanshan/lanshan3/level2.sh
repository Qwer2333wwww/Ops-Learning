#!/bin/bash
echo "Rock Paper Scissors!"
while true; do
    read -p "Enter your choice (rock, paper, scissors) or 'q' to quit: " user
    if [[ "$user" == "q" ]]; then
        echo "Thanks for playing!"
        break
    fi
    if [[ "$user" != "rock" && "$user" != "paper" && "$user" != "scissors" ]]; then
        echo "Invalid input!"
        continue
    fi
    computer_choice=$((RANDOM % 3))
    case $computer_choice in
        0) comp="rock" ;;
        1) comp="paper" ;;
        2) comp="scissors" ;;
    esac
    echo "Computer chose: $comp"
    if [[ "$user" == "$comp" ]]; then
        echo "It's a tie!"
    elif [[ ("$user" == "rock" && "$comp" == "scissors") || 
            ("$user" == "paper" && "$comp" == "rock") || 
            ("$user" == "scissors" && "$comp" == "paper") ]]; then
        echo "Win!😋"
    else
        echo "Lose!😭"
    fi
done