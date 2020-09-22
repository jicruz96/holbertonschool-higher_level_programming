# 0x13. JavaScript - Objects, Scopes & Closers

## So, what is this?

This is Project 13 of the Holberton School Higher Level Programming curriculum for the Foundations course for Full-Stack Software Engineering.

**This is our third project on the JavaScript programming language.**

All of the files in this folder are exercises associated with the curriculum.
* The first five files ( `[0-4]-rectangle.js` ) incrementally add features to a Rectangle class.
* The next two files (`[5-6]-square.js`) create a Square class that inherits properties from the Rectangle class.
* Files 7 through 10 are differenttypes of small functions that deal with variable scopes and closures.

The rest of this README:
* [lists some of the resources I used to learn these subjects](#project-resources)
* [summarizes my notes on the project's Learning Objectives](#learning-objectives)


## Project Resources
|ID|Resource  | Source
|--|--|--|
|1 | [JavaScript Object Basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics) | **Mozilla Development Network (MDN)**
|2 | [Object-oriented JavaScript for Beginners](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS) |**MDN**|
|3 | [JavaScript Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) | **MDN** |
|4 | [the `super` keyword](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) | **MDN** |
|5 | [the `extends` keyword](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends) | **MDN**
|6 | [JavaScript Object Prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes) | **MDN** |
|7 | [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance) | **MDN** |
|8 | [JavaScript Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures) | **MDN** |
|9 | [`this` binding](https://alistapart.com/article/getoutbindingsituations/) | **A List Apart Blog** |
|10 | [**THE** Modern JavaScript Cheatsheet](https://github.com/mbeaudru/modern-js-cheatsheet) | **mbeadru GitHub**


## Learning Objectives

By the end of this project, I am expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/JeG-kC426HCi3zYomikQvw "explain to anyone") the following learning objectives:

### How to create an object in JavaScript
```
/* Example of creation of a literal object */
const object_name = {
	property: 'value',
	other_property: ['Other', 'Value'],
	sub_namepsace: {
		sub_property: 'value',
		other_property: 123
	},
	last_property: True,
	method: function() {
		console.log("I am an object method. Or function.");
	}
};

/* Example of class */
class className {
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}
};
```
#### See Resource 1 for more

### What  `this`  means
`this` is a keyword used to refer to one's own namespace, within a particular object/class. 

In the case of classes that inherit from other classes, the `super()` constructor must be used to "connect" the `this` keyword to the class.

### What  `undefined`  means
`undefined` is a keyword for the value of a variable, const, etc. that has been declared but has not been defined.

### Why the variable type and scope is important

There are three main "variable"  types in JavaScript:

 - `let` , which is local in scope
 - `var`, which is global in scope in annoying ways
 - `const`, which is constant and global in scope

In JavaScript, instantiated objects inherit their environment-- and then preserve it. It's important to keep track of how variable's scope affects how their values change and how those value's are accessible to other functions.


### What is a closure
From [**MDN Resource 8**](#project-resources):
> A **closure** is the combination of a function bundled together (enclosed) with references to its surrounding state (the **lexical environment**). In other words, a closure gives you access to an outer function’s scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time.


### What is a prototype
A prototype is an object property basically present in all JavaScript objects. The prototype property serves as a list of methods and properties that the object has inherited and would have allowed to be inherited.

### How to inherit an object from another

In the case of a class, you can use the `extends` keyword. For example:
```
class Rectangle {
	constructor (w, h) {
		this.width = w;
		this.height = h;
	}
};

class Square extends Rectangle {
	constructor (size) {
		super(size, size);
	}
};
```
