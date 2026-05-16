# NodeJS Basics

This project introduces backend JavaScript fundamentals with Node.js and Express.
It covers running JavaScript with Node, reading from standard input, working with
files synchronously and asynchronously, creating HTTP servers, and organizing an
Express application with controllers and routes.

## Requirements

- Ubuntu 20.04 LTS
- Node.js 20.x
- JavaScript files must use the `.js` extension
- Files should end with a new line
- Functions and apps for the early tasks use CommonJS exports:

```js
module.exports = myFunction;
```

- The organized Express server in `full_server/` uses ES6 `import` and
  `export default` syntax with Babel.

## Project Files

| File | Description |
| --- | --- |
| `0-console.js` | Exports `displayMessage`, which prints a string to STDOUT. |
| `1-stdin.js` | Reads a name from STDIN and prints closing text when input ends. |
| `2-read_file.js` | Reads `database.csv` synchronously and logs student counts. |
| `3-read_file_async.js` | Reads `database.csv` asynchronously and returns a Promise. |
| `4-http.js` | Creates a basic HTTP server with Node's `http` module. |
| `5-http.js` | Creates a Node HTTP server with `/` and `/students` routes. |
| `6-http_express.js` | Creates a basic Express server for `/`. |
| `7-http_express.js` | Creates an Express server with `/` and `/students` routes. |
| `database.csv` | Student database used by the file-reading and server tasks. |
| `full_server/` | Organized Express server using controllers, routes, and utilities. |

## Full Server Structure

```text
full_server/
+-- controllers/
|   +-- AppController.js
|   +-- StudentsController.js
+-- routes/
|   +-- index.js
+-- server.js
+-- utils.js
```

## Running

Install dependencies first:

```bash
npm install
```

Run the organized Express server:

```bash
npm run dev
```

Test endpoints:

```bash
curl localhost:1245
curl localhost:1245/students
curl localhost:1245/students/CS
curl localhost:1245/students/SWE
```

## Testing

Run tests:

```bash
npm run test
```

Run lint and tests:

```bash
npm run full-test
```
