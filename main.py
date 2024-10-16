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
            if(target_file in file.lower()):
                path_to_return = os.path.join(path_to_target, file)
                df = pd.read_csv(path_to_return)


    df['Date'] = pd.to_datetime(df['Date'])
    
    print(f"Info: {df.info()}")
    print(df)

    fig, axs = plt.subplots(2,2, figsize=(12, 10))

    axs1 = axs[0][0]
    axs1 .set_title("Close Price History")
    axs1 .plot(df.loc[:, 'Date'], df['Close'])

    axs2 = axs[0][1]
    axs2.set_title("Open Price vs Volume")
    axs2.scatter(df['Volume'], df['Close'], color='orange', alpha=0.5, marker='x')
    axs2.set_xlabel('Volume')
    axs2.set_ylabel('Close Price')

    axs3 = axs[1][0]
    axs3.set_title("Volume")
    axs3.bar(df['Date'], df['Volume'])
    axs3.set_yscale('log')


    axs4 = axs[1][1]
    axs4.set_title("Open price history")
    axs4.plot(df['Date'], df['YTD Gains'])
    
    for i in range(2):
        for j in range(2):    
            axs[i][j].xaxis.set_major_locator(plt.MaxNLocator(6))
            axs[i][j].tick_params(axis='both', which='major', labelsize=10)

    plt.suptitle(f"Stock Price History for {target_file} ", fontsize=50)

    plt.show()
    
visualize_data(path, "stocks", "aapl")




     