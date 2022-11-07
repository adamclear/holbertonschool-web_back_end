//Creates a queue with Kue, listens for queue notifs from job_creator.js
const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process('push_notification_code', (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message);
	done();
});