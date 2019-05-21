<p align="center">
  <img width="500" height="300" src="./static/readme_logo.png">
</p>


# VAMAP

A SIMPLE USER DATA-DRIVEN MAP-ANALYZING TOOL BASED ON FOLIUM

### Prerequisites

Python 3.7+ , folium 0.8.3

```
pip install folium
```

### Installing

1. Cloning our repo

```
git clone https://github.com/opensource-projectteam16/Team16_Development.git
```

2. Change addresses written in your excel file to location values through commands below

```
python roadmanager.py <your_roadfile.xlsx> <sheet_name> <column_name> 
```
this will return a pair of new columns that are ***<column_name>_x***  and ***<column_name>_y*** which refer latitude, longitude.


3. Set up your input variables and Run main

Write setup.txt according to setup rules (you can check them in the file)
then execute command line below

```
python main.py setup.txt
```

4. Then you will get ***MAP.html*** which shows you **2 different markers**, which are **roads and others**, and **one marker evaluated by surrounded objects that are in the given coverage** 

## Deployment

[GIF 파일 반드시 준비하자]
Add additional notes about how to deploy this on a live system

## Contributing

Please read [CONTRIBUTING.md](https://github.com/opensource-projectteam16/Vamap/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/opensource-projectteam16/Vamap/blob/master/tags). 

## Authors

* **HYUNJAE LEE** - *Team leader* - [hyunjae-lee](https://github.com/hyunjae-lee)
* **SUNGJAE MIN** - *Developer* - [alstjdwo1601](https://github.com/alstjdwo1601)
* **SANGMIN LEE** - *Developer* - [sangminBangbada](https://github.com/sangminBangbada)
* **SEOKCHEON JU** - *Developer* - [smallfish06](https://github.com/smallfish06)

See also the list of [contributors](https://github.com/opensource-projectteam16/Vamap/blob/master/Contributors.md) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/opensource-projectteam16/Vamap/blob/master/LICENSE.md) file for details
