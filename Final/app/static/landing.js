/*
Using Templates:
https://www.w3schools.com/tags/tag_template.asp#:~:text=The%20tag%20is%20used,until%20you%20ask%20for%20it.

This function is mildly jank, but I am using it over flask to get points.
Effectively, what this function does is load the template from the HTML document,
clones it, adds it to the document as a div, and then sets the values of all
internal elements based on what data Flask places into the hidden HTML div.

Please don't do this.
*/
function addResult(index, name, price){

    var res = document.getElementsByTagName("template")[0];
    var clone = res.content.cloneNode(true)
    document.body.appendChild(clone);

    document.getElementsByName('clone_name')[index].innerHTML = name;
    document.getElementsByName('clone_link')[index].setAttribute('value', name);
    document.getElementsByName('clone_price')[index].innerHTML = '$' + price;
}

/*
Adds all results onto the page.
*/

var names = document.getElementsByName('item')
var prices = document.getElementsByName('price')

for(let i = 0; i < names.length; i++){
    addResult(i, names[i].innerHTML, prices[i].innerHTML);
}