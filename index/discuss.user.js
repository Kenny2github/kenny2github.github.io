// ==UserScript==
// @name           Bring it Back
// @description    Bring back the Discuss button in the header!
// @match          https://scratch.mit.edu/*
// @run-at         document-end
// ==/UserScript==

window.addEventListener('load', function(){
link = document.createElement('li');
link.innerHTML = '<a href="/discuss">Discuss</a>';
link.className = 'link discuss';
try {document.querySelector('div#navigation div.inner ul').insertBefore(link, document.querySelector('div#navigation div.inner ul').getElementsByTagName('li')[3]);}
catch(err) {document.querySelector('div#topnav ul.site-nav').insertBefore(link, document.querySelector('div#topnav ul.site-nav').getElementsByTagName('li')[2]);}
}, false);
