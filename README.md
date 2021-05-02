# Progress Bar By Mohammed Ouedrhiri

# Using Python

## Private University Of Fez

> (It's A University Project)

> Follow Me On Github For More Projects

> Mohammed Ouedrhiri &copy;

#### Linkedin Account [Linkedin](https://www.linkedin.com/in/mohammed-ouedrhiri-512183187 “Linkedin”)

# Lets Begin The explanation

## I've Used tqdm library to make the progress Bar

`from tqdm import tqdm`

## I used Time Library to Control The Speed and The Progress

`from time import sleep`

## The Description It The Text Showen in the left of The ProgressBar

> ### As We All Know The Progression Bar Goes From 0 to 100% And You Can Make it Relative to real Time Process By Give it argument instead of range
>
> </br>

    for i in tqdm(range(0, 100), desc ="Progress : "):
        sleep(.1)
