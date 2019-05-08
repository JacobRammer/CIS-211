#!/usr/bin/env bash
#chmod +x /home/nithin/cis211-TA/Duck_Sudoku-master-Github/Duck_Sudoku-master/test_sdk.py
#./test_sdk.py
python3 test_sdk.py
echo "-------------All _tests_passed---------------"
python3 sudoku.py data/nakedsingle1.sdk
echo "Next_board-------------------------"
python3 sudoku.py data/nakedhiddensingle3.sdk
echo "Next_board_bad---------------------"
python3 sudoku.py data/bad.sdk
echo "Next_board-------------------"
python3 sudoku.py data/nakedhiddensingle2.sdk

echo "Next_board-------------------"
python3 sudoku.py data/nakedhiddensingle3.sdk

echo "Next_board-------------------"
python3 sudoku.py data/nakedhiddensingle4.sdk

echo "Next_board-------------------"
python3 sudoku.py -d data/nakedhiddensingle5.sdk

echo "*******************Checking guesses_solver*************"
echo "Next_board-------very hard---------"
python3 sudoku.py data/veryhard.sdk

echo "Next_board----------hardest----"
python3 sudoku.py data/hardest.sdk

echo "Next_board----- evil--------------"
python3 sudoku.py data/evil.sdk

echo "Next_board-----brute breaker--------------"
python3 sudoku.py data/brutebreaker.sdk

echo "Next_board-----101-not-so-solvable--------------"
python3 sudoku.py data/101-not-so-solvable.sdk






