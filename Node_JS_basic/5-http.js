const http = require('http');
const fs = require('fs').promises;

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
  } catch (error) {
    if (error) {
      throw new Error('Cannot load the database');
    }
    throw new Error('Cannot load the database');
  }
}

const app = http.createServer((request, response) => {
  if (request.url === '/students') {
    getStudentReport(process.argv[2])
      .then((report) => {
        response.writeHead(200, { 'Content-Type': 'text/plain' });
        response.end(`This is the list of our students\n${report}`);
      })
      .catch((error) => {
        response.writeHead(500, { 'Content-Type': 'text/plain' });
        response.end(`This is the list of our students\n${error.message}`);
      });
    return;
  }

  response.writeHead(200, { 'Content-Type': 'text/plain' });
  response.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
