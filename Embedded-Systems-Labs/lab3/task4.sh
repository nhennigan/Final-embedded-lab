#!/bin/bash

ls -l > file.txt

ls -l >> file.txt

ls fake_dir 2> errors.txt

ls &>both.txt
