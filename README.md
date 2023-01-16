# Front Finder

This project was the result of a collaboration with my university college:
- [Mara Gheorghe](https://github.com/maraGheorghe)
- [Iulian Bogdan](https://github.com/IulianBogdan21)
- [Stefan Bodea](https://github.com/BodeaPeGitHub)

 - [Purpose](#purpose)
 - [App functionalities](#app-functionalities)
 - [Other studies and articles](#other-studies-and-articles)
 - [Project content](#project-content)

### Purpose
Identification of atmospheric fronts in images and their correlation with stroke incidents. It was found that over time the distribution of vascular accidents by day can be correlated with certain weather factors such as the atmospheric front, pressure, temperature, etc. The first step would be to identify these fronts in the "synoptic map" images.

### App functionalities
The app has the following functionality: When uploading a synoptic map, the model will classify the atmospheric fronts in one of the main three categories: "warm", "cold", "occluded".

### Other studies and articles
 - Machine Learning-Based Front Detection in Central Europe (https://www.mdpi.com/2073-4433/12/10/1312)
 - Automated detection and classification of synoptic-scale fronts from atmospheric data grids (https://wcd.copernicus.org/articles/3/113/2022/wcd-3-113-2022.pdf)
 - A global climatology of atmospheric fronts (https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2010GL046451)
 - Recent global trends in atmospheric fronts (https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2011GL049481)

### Project content
```bash
├── Code                                            | (THE CODE PART)   
│   ├── classifier                                  | (The classifier)  
│   │   ├── classifier.py  
│   │   ├── __init__.py  
│   ├── GUI                                         (The GUI part of the application)  
│   │   ├── gui_main.py  
│   │   ├── __init__.py  
│   ├── main.py   
│   └── model_utils                                 (Here are all the datasets used and the .ipynb where we developed the AI)  
│       ├── all  
│       ├── crops  
│       ├── data                                    (The first dataset)  
│       ├── dataset                                 (The black and white dataset)  
│       ├── dataset_final_1                         (The final dataset)  
│       │   ├── test  
│       │   │   ├── cold  
│       │   │   ├── occluded  
│       │   │   ├── warm  
│       │   │   └── white  
│       │   └── train  
│       │       ├── cold  
│       │       ├── occluded  
│       │       ├── warm  
│       │       └── white  
│       ├── filter_images.py                        (The filter image part)  
│       ├── fronts                                  (Another dataset)  
│       ├── FrontsModel.ipynb  
│       ├── models                                  (Here we save the models)  
│       │   └── model_v1.h5                         (This is the model that we use)  
│       ├── new_fronts   
│       ├── test.ipynb  
│       └── white_to_move    
├── Documentation   
│   ├── App_Report.pdf                              (The documantation)  
│   ├── images                                      (All the images used into the documenatation)  
│   ├── main_nou.tex                                (The .tex file, from LaTeX)  
│   ├── MIRPR_FRONT.pdf                             (The final documentation)  
│   └── presentation                                (All the presenatation files)  
│       └── FrontFinder-Teaser.mp4                  (Teaser)  
│       └── swot.png                                (SWOT Analysis)  
|       └── presentation.ppt                        (Final presentation 18.01.2023)  
└── README.md                                       (You are here.)  
```
