// ==UserScript==
// @name           Bring it Back
// @description    Bring back the Discuss button in the header!
// @match          https://scratch.mit.edu/*
// ==/UserScript==

link = document.createElement('li');
link.innerHTML = '<a href="/discuss">Discuss</a>'
document.querySelector('div.container ul.site-nav').insertBefore(link, document.querySelector('div.container ul.site-nav li.last'))
