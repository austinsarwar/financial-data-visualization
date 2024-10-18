import os
import pandas as pd
import kagglehub
import matplotlib.pyplot as plt



path = kagglehub.dataset_download("adhoppin/financial-data")



"""Walks through directory structure and find target directory followed by target csv. Generates 4 graphs based on csv data"""
def visualize_data(main_directory : str, target_directory: str,  target_file: str ): 
                                                                            
    for dir_path, dir_path_names, filenames in os.walk(main_directory):
        if(target_directory.lower() in dir_path.lower()):
            path_to_target = dir_path
            break
    
            
    for file in os.listdir(path_to_target):
            if(target_file.lower() in file.lower()):
                path_to_return = os.path.join(path_to_target, file)
                df = pd.read_csv(path_to_return)

    df = df.dropna()
   
    df['Date'] = pd.to_datetime(df['Date'])
    df["1000_day_average"] = df["Close"].rolling(1000).mean()
    df["200_day_average"] = df["Close"].rolling(250).mean()
    df["50_day_average"] = df["Close"].rolling(50).mean()

    # Clean data remove null values
   
    # Get the length of the dataframe
    df_count = len(df)
    
    print(f"Info: {df.info()}")
    print(df)

    fig, axs = plt.subplots(2,2, figsize=(12, 10))

    axs1 = axs[0][0]
    axs1.set_title("Price History last 20 Years")
    axs1.plot(df.loc[:, 'Date'], df.loc[:, 'Close'])
   
    # axs1_sub = axs1.twinx()
    # axs1_sub.plot(df.loc[:, 'Date'], df.loc[:, '200_day_average'])

    axs2 = axs[0][1]
    axs2.set_title("Price history 20 years with moving averages")
    axs2.plot(df.loc[:, 'Date'], df.loc[:, 'Close'], label='Stock Price')
    axs2.plot(df.loc[:, 'Date'], df.loc[:, '200_day_average'], color='green', label='200 day avg')
    axs2.plot(df.loc[:, 'Date'], df.loc[:, '50_day_average'], color='orange', label='50 day avg')
    axs2.legend(loc='upper left')

    axs3 = axs[1][0]
    axs3.set_title("Price history over Volume last 20 years")
    axs3.bar(df['Date'], df['Volume'])
    axs3.set_yscale('log')


    axs3_sub = axs3.twinx()  # instantiate a second Axes that shares the same x-axis
    color = 'tab:blue'
    axs3_sub.set_ylabel('Price', color=color)  # we already handled the x-label with ax1
    axs3_sub.plot(df.loc[:, 'Date'], df['Close'])
    axs3_sub.tick_params(axis='y', labelcolor=color)

    axs4 = axs[1][1]
    axs4.set_title("Price history 2022-2023")
    dates = df.iloc[-366:, df.columns.get_loc('Date')].tolist()
    close_values = df.iloc[-365:, df.columns.get_loc('Close')].tolist()

    # Plot with correct axis ordering
    axs4.stairs(close_values, dates)
    
    for i in range(2):
        for j in range(2):    
            axs[i][j].xaxis.set_major_locator(plt.MaxNLocator(10))
            axs[i][j].tick_params(axis='both', which='major', labelsize=10)

    plt.suptitle(f"Stock Price History for {target_file} ", fontsize=50)

    plt.show()
    
visualize_data(path, "stocks", "nvda")




     