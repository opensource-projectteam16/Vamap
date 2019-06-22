<p align="center">
  <img width="500" height="300" src="./static/readme_logo.jpg">
</p>

| **`LICENSE`** | **`Watch`** | **`Size`** |**`Download`**|**`Issues`**|**`Pull Request`**|
|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
|![GitHub](https://img.shields.io/github/license/opensource-projectteam16/Vamap.svg) |![GitHub](https://img.shields.io/github/watchers/opensource-projectteam16/Vamap.svg?label=Watch&style=social)|![GitHub](https://img.shields.io/github/repo-size/opensource-projectteam16/Vamap.svg)|![GitHub](https://img.shields.io/github/downloads/opensource-projectteam16/Vamap/total.svg)|![GitHub](https://img.shields.io/github/issues/opensource-projectteam16/Vamap.svg)|![GitHub](https://img.shields.io/github/issues-pr/opensource-projectteam16/Vamap.svg)


# VAMAP

A SIMPLE USER DATA-DRIVEN MAP-ANALYZING TOOL BASED ON FOLIUM

### Prerequisites

Python 3.7+ , folium 0.8.3

```
$ pip install folium
```

### Installing

1. Cloning our repo

```
$ git clone https://github.com/opensource-projectteam16/Team16_Development.git
```

2. Installing modules
```
$ pip install -r requirements.txt
```

3. Change addresses written in your excel file to location values through commands below
this will return a pair of new columns that are ***<column_name>_x***  and ***<column_name>_y*** which refer latitude, longitude.

```
$ python roadmanager.py <your_roadfile.xlsx> <sheet_name> <column_name> 
```

4. Set up your input variables and Run main

Write setup.txt according to setup rules (you can check them in the file)
then execute command line below

```
$ python main.py setup.txt
```

5. Then you will get ***MAP.html*** which shows you **2 different markers**, which are **roads and others**, and **one marker evaluated by surrounded objects that are in the given coverage** 

## Deployment

[GIF 파일 반드시 준비하자]
Add additional notes about how to deploy this on a live system

## Contributing

Please read [CONTRIBUTING.md](https://github.com/opensource-projectteam16/Vamap/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **HYUNJAE LEE** - *Team leader* - [hyunjae-lee](https://github.com/hyunjae-lee)
* **SUNGJAE MIN** - *Developer* - [alstjdwo1601](https://github.com/alstjdwo1601)
* **SANGMIN LEE** - *Developer* - [sangminBangbada](https://github.com/sangminBangbada)
* **SEOKCHEON JU** - *Developer* - [smallfish06](https://github.com/smallfish06)

See also the list of [contributors](https://github.com/opensource-projectteam16/Vamap/blob/master/Contributor.md) who participated in this project.

## How to open an issue
If you have found any issue from our project, Please check our issue template and open yours.

## How to send a pull request
If you have accepted an issue, then you can send us a pull request. Please check our pull request template before you send it.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/opensource-projectteam16/Vamap/blob/master/LICENSE.md) file for details
