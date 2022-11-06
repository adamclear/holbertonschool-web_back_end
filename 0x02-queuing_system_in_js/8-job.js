//Takes in an array of jobs and adds it to given Kue
function createPushNotificationsJobs(jobs, queue) {
	if (!Array.isArray(jobs)) {
		throw Error('Jobs is not an array');
	}
	for (const job of jobs) {
		const curJob = queue.create('push_notification_code_3', job).save();
		try {
			curJob
				.on('enqueue', () => {
					console.log(`Notification job created: ${curJob.id}`);
				})
				.on('complete', () => {
					console.log(`Notification job ${curJob.id} completed`);
				})
				.on('failed', (error) => {
					console.log(`Notification job ${curJob.id} failed: ${error}`);
				})
				.on('progress', (progress) => {
					console.log(`Notification job ${curJob.id} ${progress}% complete`);
				});
		} catch (error) {}
	};
};

module.exports = createPushNotificationsJobs;
