This script gets named a.csv to z.csv files from https://public.wiwdata.com/engineering-challenge/data/.
Simply run main() to execute the script and get the output csv.

get_files() downloads the files with the wget package. </br>
combine_a_to_z() uses the string package to loop through 
the 26 letters and concatenate the dataframes together. </br>
sum_of_length(df) groups the dataframe by user_id and path,
and then calculates the sum of the length for each combination of
user_id and path. </br>
main() runs the above functions and outputs the csv of our interest.




