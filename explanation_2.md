using recursion because it will be difficult to predict the incoming paths' depth of directory
looping the outer directory to get hold of objects inside
checking if the object is file and return the appended path else call the recurring func again passing the current list element as the path to check inside the directory

os.listpathdir(path) : this takes o(n) depending on the files found in the directory
the for_loop traverse the number of files returned by above func so that is O(n)
the two if_statements inside : O(log(n))
recursive call is O(n) for searching folders, appending found folders/files, calling os.listdir(path) again : makes O(3n)

other assignments statements takes O(1) which is negligible effect

The total time complexity is O(n)   
The total space complexity is O(n) will depend on the number of sub-directory found on each calls     
    