//Tests for 8-job.js
import createPushNotificationsJobs from './8-job.js';
const kue = require('kue');
const queue = kue.createQueue();
const expect = require('chai').expect;

describe('createPushNotificationsJobs', () => {
	before(() => {
		queue.testMode.enter();
	});
	afterEach(() => {
		queue.testMode.clear();
	});
	after(() => {
		queue.testMode.exit();
	});

	it('Testing job creation', () => {
		const jobs = [
			{
				phoneNumber: '9185555555',
				message: 'This is the code 1234 to verify your account',
			},
			{
				phoneNumber: '4055555555',
				message: 'This is the code 5678 to verify your account',
			},
			{
				phoneNumber: '1115555555',
				message: 'This is the code 9100 to verify your account',
			},
		];
		createPushNotificationsJobs(jobs, queue);
		expect(queue.testMode.jobs.length).to.equal(3);
		
		expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
		expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('9185555555');
		expect(queue.testMode.jobs[0].data.message).to.equal(
			'This is the code 1234 to verify your account'
		);
		expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
		expect(queue.testMode.jobs[1].data.phoneNumber).to.equal('4055555555');
		expect(queue.testMode.jobs[1].data.message).to.equal(
			'This is the code 5678 to verify your account'
		);
		expect(queue.testMode.jobs[2].type).to.equal('push_notification_code_3');
		expect(queue.testMode.jobs[2].data.phoneNumber).to.equal('1115555555');
		expect(queue.testMode.jobs[2].data.message).to.equal(
			'This is the code 9100 to verify your account'
		);
	});

	it('Testing error message', () => {
		expect(() => createPushNotificationsJobs({1:0}, queue)).to.throw(
			Error, 'Jobs is not an array'
		);
	})
})