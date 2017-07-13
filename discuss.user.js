// ==UserScript==
// @name           Bring it Back
// @description    Bring back the Discuss button in the header!
// @match          https://scratch.mit.edu/*
// ==/UserScript==

link = document.createElement('li');
link.innerHTML = '<a href="/discuss">Discuss</a>';
document.querySelector('div#topnav div ul').insertBefore(link, document.querySelector('div#topnav div ul').getElementsByTagName('li')[2]);
