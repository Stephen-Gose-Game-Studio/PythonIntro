### NASCAR Submission Extra Exploration
I created this addition to the NASCAR directory because as I was testing my original submission, I noticed that the winners average speed, as well as time elapsed, was not consistent with **speed * time = 500** as expected. 

Originally, I manually ran the program 10 times and plotted **time vs the winner's average speed** on a graph to see if there was any obvious correlation. It was clear that there wasn't so I stepped up my testing.

In the **NASCAR_Original** file, I removed code which was unnecessary for testing, and added code so that 1000 races would automatically be run, and the results added to a csv. **test_data_original** shows that there was no correlation between speed, time, and distance travelled.
With **NASCAR_Edited**, I changed my method for calculating an average speed, and ran the same test, this time to **test_data_edited**, which clearly shows that this change gave the desired result.

###### This was a fun experience testing why the program's output wasn't behaving as expected, and implementing a solution, albeit for a simple problem.
