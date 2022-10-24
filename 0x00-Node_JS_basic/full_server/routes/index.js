// Express router
const express = require('express');
const AppController = require('../contollers/AppController');
const StudentsController = require('../contollers/StudentsController');

const router = express.Router();
router.get('/students/:major', StudentsController.getAllStudentsByMajor);
router.get('/students', StudentsController.getAllStudents);
router.get('/', AppController.getHomepage);

module.exports = router;
