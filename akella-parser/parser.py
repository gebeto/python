import requests
from bs4 import BeautifulSoup

videos = [
{
	"id": 45,
	"title": "Полосатые объекты на кривых и шейдерах",
	"url": "VYpcD6yRkQE",
	"tags" : [],
	"description": "",
	"img": "45.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 44,
	"title": "Волны и эффект преломления на вертекс-фрагмент шейдерах",
	"url": "hChWdAgJr58&t=28s",
	"tags" : [],
	"description": "",
	"img": "44.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 43,
	"title": "Буквы с физикой",
	"url": "ha6dpKnmPOo",
	"tags" : [],
	"description": "",
	"img": "43.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 42,
	"title": "3d Emoji анимация на GPU и синусах",
	"url": "WzLg2K6T7XI",
	"tags" : [],
	"description": "",
	"img": "42.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 41,
	"title": "ASCII анимация",
	"url": "1TDAgF_S7ys",
	"tags" : [],
	"description": "",
	"img": "41.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 40,
	"title": "Decompiled animation from murmure.me website",
	"url": "AERIjhFzuaI",
	"tags" : [],
	"description": "",
	"img": "40.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 39,
	"title": "Houdini и лайфхак с greensock",
	"url": "oxyBJMmHbSI",
	"tags" : [],
	"description": "",
	"img": "39.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 38,
	"title": "Самолётики, кривые, кватернионы",
	"url": "d3JGRn0llqM",
	"tags" : [],
	"description": "",
	"img": "38.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 37,
	"title": "Земля, координаты, кватернионы, Лида",
	"url": "8Xzwc-hSOvw&t=3003s",
	"tags" : [],
	"description": "",
	"img": "37.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 36,
	"title": "Огонь на шейдерах и шуме",
	"url": "l7xy3iMYsuQ",
	"tags" : [],
	"description": "",
	"img": "36.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 35,
	"title": "Wordpress минисайт с нуля за час",
	"url": "PrvilFct91I",
	"tags" : [],
	"description": "",
	"img": "35.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 34,
	"title": "GPU анимация 400к частиц",
	"url": "QGMygnzlifk",
	"tags" : [],
	"description": "",
	"img": "34.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 33,
	"title": "Анимация косых фонов на PIXI.js и clip:rect,",
	"url": "WScZAbi8A_Y",
	"tags" : [],
	"description": "",
	"img": "33.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 32,
	"title": "Волнистые картинки на PIXI.JS",
	"url": "WuRQkLYgPTo",
	"tags" : [],
	"description": "",
	"img": "32.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 31,
	"title": "Вёрстка простого макета и общение",
	"url": "IJ5qDr7DWew&t=5097s",
	"tags" : [],
	"description": "",
	"img": "31.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 30,
	"title": "3D сетка с помощью линий и шейдеров",
	"url": "RKjfryYz1qY",
	"tags" : [],
	"description": "",
	"img": "30.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 29,
	"title": "Жидкие частицы, SVG + Canvas",
	"url": "CakNmQEmf1I",
	"tags" : [],
	"description": "",
	"img": "29.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 28,
	"title": "Шейдеры, триангуляция, освещение, физика.",
	"url": "F5iydF5mreI&t=1599s",
	"tags" : [],
	"description": "",
	"img": "28.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 27,
	"title": "Новогодняя анимация с Лидой",
	"url": "qxTPZiL2s9U",
	"tags" : [],
	"description": "",
	"img": "27.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 26,
	"title": "SVG и WebGL маски",
	"url": "krSHZddzZPI",
	"tags" : [],
	"description": "",
	"img": "26.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 25,
	"title": "Рисуем фото линиями в 3d, three.js",
	"url": "D2SRg5qh9oo",
	"tags" : [],
	"description": "",
	"img": "25.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 24,
	"title": "Кастомный скролл и css свойство clip",
	"url": "JQMryV9X1R4",
	"tags" : [],
	"description": "",
	"img": "24.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 23,
	"title": "Лендинг с полноэкранным скроллом и анимациями на PubSub",
	"url": "SmaeS_U366M",
	"tags" : [],
	"description": "",
	"img": "23.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 22,
	"title": "Анимация «Мандала» или как рисовать синусами и вдохновляться",
	"url": "MoEjp5E5tBs",
	"tags" : [],
	"description": "",
	"img": "22.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 21,
	"title": "SVG кривые и анимация лого css-live.ru на snap.svg",
	"url": "2N1MP44OvN8&t=21s",
	"tags" : [],
	"description": "",
	"img": "21.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 20,
	"title": "Рисуем эффекты на PIXI и его фильтрах (ака шейдерах), и немного про gulp sass",
	"url": "8DH13eslS3U",
	"tags" : [],
	"description": "",
	"img": "20.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 19,
	"title": "Ласточки в небе под Штрауса",
	"url": "fU-vywo5BKM",
	"tags" : [],
	"description": "",
	"img": "19.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 18,
	"title": "intersectionObserver и SVG анимация маски",
	"url": "Y6dbEGjgjD8&t=1s",
	"tags" : [],
	"description": "",
	"img": "18.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 17,
	"title": "Perlin Noise, 1d, 2d, 3d",
	"url": "xN_KOacUDhU",
	"tags" : [],
	"description": "",
	"img": "17.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 16,
	"title": "Анимации по скроллу с сайта iPhoneX",
	"url": "-EdessdvqSY",
	"tags" : [],
	"description": "",
	"img": "16.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 15,
	"title": "Плавные переходы между страницами с Barba.js (PJAX)",
	"url": "pwmHB_veoko",
	"tags" : [],
	"description": "",
	"img": "15.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 14,
	"title": "Анимируем графики на SVG и Canvas, + perlin noise",
	"url": "M7NGYXMp4JM",
	"tags" : [],
	"description": "",
	"img": "14.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 13,
	"title": "Анимируем SVG в 3D с помощью Three.js",
	"url": "Q9BXGh9sdZw",
	"tags" : [],
	"description": "",
	"img": "13.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 12,
	"title": "часть), Chrome Extension для показа FPS",
	"url": "GFNnPMlIzoQ",
	"tags" : [],
	"description": "",
	"img": "12.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 12,
	"title": "Chrome Extension для показа FPS",
	"url": "isRIUNTiTi8",
	"tags" : [],
	"description": "",
	"img": "12.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 11,
	"title": "Треугольники с физикой и Glitch на шейдерах",
	"url": "MXOYkZ59-zE",
	"tags" : [],
	"description": "",
	"img": "11.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 10,
	"title": "Code In The Dark, акварель, и триангуляция",
	"url": "TIz8KXsrdp0",
	"tags" : [],
	"description": "",
	"img": "10.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 9,
	"title": "Многоязычность в Gulp и трюк с канвас анимацией",
	"url": "o2MR8GDZH2s",
	"tags" : [],
	"description": "",
	"img": "9.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 8,
	"title": "Gulp и верстка простой AMP страницы",
	"url": "ejOPpUNxXu4",
	"tags" : [],
	"description": "",
	"img": "8.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 7,
	"title": "Distortion with WebGL, CSS-Canvas masking",
	"url": "RTYJ1fmYZ3g",
	"tags" : [],
	"description": "",
	"img": "7.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 6,
	"title": "Triangles in CSS, Canvas, WebGL",
	"url": "LNSvO-jJhKg",
	"tags" : [],
	"description": "",
	"img": "6.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 5,
	"title": "Sexy Fragment Shader and throttle-debounce",
	"url": "YEYmYI7ZpQc",
	"tags" : [],
	"description": "",
	"img": "5.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 4,
	"title": "Various landing page animations with GSAP",
	"url": "b8P-6DDKU_c",
	"tags" : [],
	"description": "",
	"img": "4.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 3,
	"title": "Canvas Jelly Effect",
	"url": "XqB_Ulfpd0w",
	"tags" : [],
	"description": "",
	"img": "3.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 2,
	"title": "Верстка лендинга за час, почти",
	"url": "mLVBoH5Dwv0",
	"tags" : [],
	"description": "",
	"img": "2.png",
	"demo": "",
	"github": "",
	"video": ""
},

{
	"id": 1,
	"title": "Logo animation live",
	"url": "AajoBGoz8TQ",
	"tags" : [],
	"description": "",
	"img": "1.png",
	"demo": "",
	"github": "",
	"video": ""
}
]


url = "https://www.youtube.com/watch?v="
for video in videos:
	resp = requests.get(url + video["url"]).content
	soup = BeautifulSoup(resp, "html.parser")
	description = soup.find("div", {"class": "action-panel-content yt-uix-expander yt-card yt-card-has-padding yt-uix-expander-collapsed"}).find("p", {"id": "eow-description"})
	video["raw"] = description.text
	print video["id"]

import json

json.dump(videos, open("res.json", "w"), indent=4)