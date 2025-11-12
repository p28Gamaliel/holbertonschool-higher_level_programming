#!/bin/usr/node
const redHeader = document.querySelector('#red_header');
redHeader.addEventListener('click', () => {
    const header = document.querySelector('header');
    header.text.color = '#FF0000';
});
