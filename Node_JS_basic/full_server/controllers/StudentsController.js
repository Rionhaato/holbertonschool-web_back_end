import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    response.type('text/plain');

    readDatabase(process.argv[2])
      .then((studentsByField) => {
        const fields = Object.keys(studentsByField)
          .sort((fieldA, fieldB) => fieldA.localeCompare(fieldB, undefined, {
            sensitivity: 'base',
          }));
        const output = ['This is the list of our students'];

        fields.forEach((field) => {
          const count = studentsByField[field].length;
          const list = studentsByField[field].join(', ');

          output.push(`Number of students in ${field}: ${count}. List: ${list}`);
        });

        response.status(200).send(output.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    response.type('text/plain');

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(process.argv[2])
      .then((studentsByField) => {
        response.status(200).send(`List: ${studentsByField[major].join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
