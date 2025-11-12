#!/bin/usr/node
const headerElement = document.queryselector('h1');
if (headerElement) {
    headerElement.Style.color = '#FF0000';
} else {
    console.log("header element not found.");
}
