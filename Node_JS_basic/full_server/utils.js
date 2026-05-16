import fs from 'fs';

function readDatabase(path) {
  return fs.promises.readFile(path, 'utf8')
    .then((data) => {
      const lines = data
        .split(/\r?\n/)
        .filter((line) => line.trim().length > 0);
      const studentsByField = {};

      lines.slice(1).forEach((student) => {
        const [firstname, , , field] = student.split(',');

        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstname);
      });

      return studentsByField;
    });
}

export default readDatabase;
