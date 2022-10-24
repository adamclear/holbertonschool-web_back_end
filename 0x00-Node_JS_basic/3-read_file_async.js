// Logs # of students in each field of database file

const fs = require('fs');

const countStudents = async (path) => {
  let students;
  try {
    students = await fs.promises.readFile(path, 'utf-8');
  } catch (error) {
    throw Error('Cannot load the database');
  }
  const lines = students.split('\n').slice(1).filter((line) => line !== '');
  console.log(`Number of students: ${lines.length}`);
  const fields = [...new Set(lines.map((line) => line.split(',')[3]))];
  const dict = {};
  let x = 0;
  fields.forEach((field) => {
    const studentsInField = lines.filter((line) => line.endsWith(field))
      .map((line) => line.split(',')[0]);
    const numberOfStudents = studentsInField.length;
    console.log(
      `Number of students in ${field}: ${
        numberOfStudents
      }. List: ${studentsInField.join(', ')}`,
    );
    dict[field[x]] = {
      numberOfStudents,
      studentsInField,
    };
    x += 1;
  });
  return dict;
};

module.exports = countStudents;
