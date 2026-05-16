const fs = require('fs').promises;
const express = require('express');

const app = express();

function buildStudentReport(data) {
  const lines = data
    .split(/\r?\n/)
    .filter((line) => line.trim().length > 0);
  const students = lines.slice(1);
  const fields = {};
  const output = [`Number of students: ${students.length}`];

  students.forEach((student) => {
    const [firstname, , , field] = student.split(',');

    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstname);
  });

  Object.keys(fields).forEach((field) => {
    const count = fields[field].length;
    const list = fields[field].join(', ');

    output.push(`Number of students in ${field}: ${count}. List: ${list}`);
  });

  return output.join('\n');
}

async function getStudentReport(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    return buildStudentReport(data);
  } catch {
    throw new Error('Cannot load the database');
  }
}

app.get('/', (request, response) => {
  response.type('text/plain');
  response.send('Hello Holberton School!');
});

app.get('/students', (request, response) => {
  response.type('text/plain');

  getStudentReport(process.argv[2])
    .then((report) => {
      response.send(`This is the list of our students\n${report}`);
    })
    .catch((error) => {
      response.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245);

module.exports = app;
