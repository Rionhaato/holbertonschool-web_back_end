# ES6 Basics

This project introduces core ECMAScript 6 features used in modern JavaScript.
All files are written as ES modules and export their functions for testing with
Jest and Babel.

## Learning Objectives

- Explain what ES6 is and identify features introduced in ECMAScript 2015.
- Use `const` and `let` instead of `var`.
- Explain block scope and how it differs from function scope.
- Write arrow functions and understand lexical `this`.
- Define default function parameters.
- Use rest parameters and spread syntax.
- Build strings with template literals.
- Use object property shorthand and computed property names.
- Define methods with ES6 method property syntax.
- Iterate with `for...of` loops.
- Create and combine objects for simple reports.

## Requirements

- Ubuntu 20.04 LTS
- Node.js 20.x.x
- npm 9.x.x or newer
- Files use the `.js` extension
- Functions are exported
- Code is tested with Jest
- Code is linted with ESLint

## Files

| File | Description |
| --- | --- |
| `0-constants.js` | Uses `const` and `let` for variable declarations. |
| `1-block-scoped.js` | Demonstrates block-scoped variables. |
| `2-arrow.js` | Uses an arrow function to preserve lexical `this`. |
| `3-default-parameter.js` | Defines default parameter values. |
| `4-rest-parameter.js` | Counts arguments with rest parameter syntax. |
| `5-spread-operator.js` | Combines arrays and string characters with spread syntax. |
| `6-string-interpolation.js` | Builds a string with template literals. |
| `7-getBudgetObject.js` | Uses object property value shorthand. |
| `8-getBudgetCurrentYear.js` | Uses computed property names. |
| `9-getFullBudget.js` | Uses ES6 method properties. |
| `10-loops.js` | Rewrites iteration with `for...of`. |
| `11-createEmployeesObject.js` | Creates an employee object by department. |
| `12-createReportObject.js` | Creates a report object with department counts. |

## Usage

After installing the project dependencies, run a task file with the provided
Holberton command pattern:

```bash
npm run dev 0-main.js
```
