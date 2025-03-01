This project is made to research and analyze the general IT job market trends in Ukraine, and the relevance and prospects of the Analyst role comparing the data from Jan 2024 and Jan 2025.
The project uses the data from: https://jobs.dou.ua/trends/categories.
The data is uploaded under the ```data``` folder as ```csv``` files. Here is the preview example of the data structure:

<img width="272" alt="Screenshot 2025-03-01 at 21 43 19" src="https://github.com/user-attachments/assets/237245f2-3c20-476d-a5be-9913f2e2a566" />

Each table has 3 columns: ```category```, ```job_count``` and ```applications```.

Where ```category``` is the job category,
```job_count``` is the number of open applications on the market,
and ```applications``` column represents the number of applications for this category within a month.

To start the analysis the program adds a new column to each dataframe: ```ratio```.

```ratio``` = ```job_count```/```applications```

Ratio shows the correlation between open jobs and number of applications in the category, in other words how many jobs are available per candidate.

To inspect the data for a single month the program uses ```visualize_single(load_data(file_path))``` function.
(```load_data(file_path)``` function uploads the ```csv``` file and returns a filtered pandas dataframe with an added ```ratio``` column, 
```visualize_single(load_data(file_path))``` visualizes the data for a given data set.)

This chart is the result for Jan 2024 for any experience level:

![job_market_by_category_jan_2024](https://github.com/user-attachments/assets/0c7a7139-cb42-46a0-9432-db9e0e811712)

This chart is the result for Jan 2025 for any experience level:

![job_market_by_category_jan_2025](https://github.com/user-attachments/assets/84b27807-5f73-4c81-8157-01643e618e47)

To conclude these 2 charts the Analyst role is staying on the top of the market by the ratio. 
It gains the relevance on the market with the ratios of ```19.38``` and ```26.20``` for Jan 2024 and Jan 2025 respectively.

Additionaly, to combine these two charts, and finalize the results in a single chart, the program uses ```visualize_comparison(load_data(file_path_1), load_data(file_path_2))```
function which shows the difference between Jan 2025 and Jan 2024 numbers.

The result proves that Analyst role is growing in demand:

![job_market_ratio_comparison_jan_2024_2025](https://github.com/user-attachments/assets/e5ba33dc-17ea-4c41-8a80-38a32d26a7d2)

The next inspection is about the prospects of the Analyst role as the candidate's experience grows. 
In this case the program will use 4 different data sets: _less than 1 year of experience_, _1-3 years of experience_, _3-5 years of experience_, _5+ years of experience_.
Each data set gets it's own ratio, let's name them: _ratio_1_, _ratio_2_, _ratio_3_, _ratio_4_.
To analyze that, the program calculates the ```ratio_sum_change``` value.

```ratio_sum_change``` = (```ratio_2```-```ratio_1```) + (```ratio_3```-```ratio_2```) + (```ratio_4```-```ratio_3```)

Which basically calculates how the ratio changes over the years of experience.

To visualize it the program uses the ```visualize_exp_trends([load_data(file) for file in list_of_files_by_exp])```.

This chart is the result for Jan 2024:

![job_market_trends_by_exp_jan_2024](https://github.com/user-attachments/assets/387ac44c-063e-4e0d-a5be-d29525e5db32)

This chart is the result for Jan 2025:

![job_market_trend_by_exp_jan_2025](https://github.com/user-attachments/assets/0fb211b8-b401-4734-bcb7-da01c4882046)

The charts also highlight the Data Science role as experience growth in Analyst role can potentially lead to the Data Science role.

These charts display that both Analyst and Data Science role keep the top of the chart and stay prospective as the candidate gains experience. 

The final part of the analysis will be related to the comparison in gains and demand of the Analyst role between Jan 2024 and 2025 with the growth of experience.

Here, the program uses ```visualize_analytics_exp_trends([load_data(file) for file in list_of_files_by_exp_1], [load_data(file) for file in list_of_files_by_exp_2])```.
This function takes 2 arguments which are the 4-element lists of data sets representing the experience level for Jan 2024 and Jan 2024 respectively.

And here is the final resulting chart:

![analyst_ratio_trend_jan_24_25](https://github.com/user-attachments/assets/e03699d5-0900-4046-982a-696817b32ada)

To sum up, the Analyst role can be considered is one of the top categories which gains the demand and shows a great potential in the prospectiveness on the Ukrainian job market.
This program analyzes only a small period of time but it clearly answers the question about the relevance of the Analyst professionals.
