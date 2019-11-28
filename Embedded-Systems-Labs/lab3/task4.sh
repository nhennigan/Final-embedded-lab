#!/bin/bash

ls -l > file.txt

ls -l >> file.txt

ls fake_dir 2> errors.txt

ls 1> both.txt
ls 2>>both.txt
