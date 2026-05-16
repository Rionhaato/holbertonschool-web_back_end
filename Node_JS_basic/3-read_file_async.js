const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .catch(() => {
      throw new Error('Cannot load the database');
    })
    .then((data) => {
      const lines = data
        .split(/\r?\n/)
        .filter((line) => line.trim().length > 0);
      const students = lines.slice(1);
      const fields = {};

      console.log(`Number of students: ${students.length}`);

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

        console.log(`Number of students in ${field}: ${count}. List: ${list}`);
      });
    });
}

module.exports = countStudents;
