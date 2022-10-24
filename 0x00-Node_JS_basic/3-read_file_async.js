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
  const fields = [...new Set(lines.map((line) => line.split(',')[3]))];
  let textBlock = `Number of students: ${lines.length}\n`;
  fields.forEach((field) => {
    const studentsInField = lines.filter((line) => line.endsWith(field))
      .map((line) => line.split(',')[0]);
    const numberOfStudents = studentsInField.length;
    textBlock += `Number of students in ${field}: ${
      numberOfStudents
    }. List: ${studentsInField.join(', ')}\n`
  });
  const editedTextBlock = textBlock.slice(0, -1);
  console.log(editedTextBlock);
  return editedTextBlock;
};

module.exports = countStudents;
