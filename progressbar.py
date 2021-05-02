#I've Used tqdm library to make the progress Bar
from tqdm import tqdm
#I used Time Library to Control The Speed and The Progress
from time import sleep
#The Description It The Text Showen in the left of The ProgressBar
for i in tqdm(range(0, 100), desc ="Progress : "):
        sleep(.1)

