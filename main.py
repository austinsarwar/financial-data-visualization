import os
import pandas as pd
import kagglehub
import matplotlib.pyplot as plt
import mplfinance as mpf


path = kagglehub.dataset_download("adhoppin/financial-data")



"""Walks through directory structure and find target directory followed by target csv"""
def visualize_data(main_directory : str, target_directory: str,  target_file: str ): 
                                                                            
                                                                        


    for dir_path, dir_path_names, filenames in os.walk(main_directory):
        if(target_directory.lower() in dir_path.lower()):
            path_to_stocks = dir_path
            break
    
            
    for file in os.listdir(path_to_stocks):
            if(target_file in file.lower()):
                path_to_return = os.path.join(path_to_stocks, file)
                df = pd.read_csv(path_to_return)

   
    
    fig, axs = plt.subplots(2,2)
    axs[0][0].plot(df['Date'], df['Close'])
    axs[0][1].scatter(df['Date'], df['Close'])
    axs[1][0].bar(df['Date'], df['Close'])
    axs[1][1].stem(df['Date'], df['Close'])
    
  
    for i in range(2):
        for j in range(2):    
            axs[i][j].xaxis.set_major_locator(plt.MaxNLocator(6))
            axs[i][j].tick_params(axis='both', which='major', labelsize=10)
            
    
    for ax in axs.flat:
        ax.set(xlabel='Years', ylabel='Price')

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.suptitle(f"Stock Price History for {target_file.title()} ", fontsize=50)

    plt.show()
    
visualize_data(path, "stocks", "aapl")




     