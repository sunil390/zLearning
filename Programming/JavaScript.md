# Javascript

## Variables

### Types
#### Basic
1. numric
2. string
3. Objects
#### Constant
#### Literals

#### Examples
1. var x; declare
2. x = 5; initialize
3. var name = "John"; Global
4. let name = "Mary"; within curly braces
5. const daysOfweek = 7;
## Functions

1. perform a task
2. first class objects/citizen
3. starts with function keyword and then {}

## Classes
```
class Course {
  constructor(name, instructor ) {
    this.name = name ;
    this.instructor = instructor;
  }
  getInstrctor() {
    return instructor;
  }
}
let course = new Course("Java Scipt", "Axle");
```
## Arrays and Objects
1. string array and numeric array
```
const courses = ["JS", "CSS", "HTML" ];
const scores = [1, 3, 4, 5, 6];
```
2. builtin functions
```
scores.sort();
courses.length;
courses.push("Node JS");
scores.pop();
```
3. Object
```
const student = 
  { name:"Angela",
    GPA:3.92,
    Major:"Computer Science"
  }
