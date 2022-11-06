// Create a client subscribe to 5-publisher.js
const redis = require('redis');
const redisCLI = redis.createClient();

redisCLI
	.on('connect', () => {
		console.log('Redis client connected to the server');
	})
	.on('error', (err) => {
		console.log(`Redis client not connected to the server: ${err}`);
	})
	.on('message', (channel, message) => {
		if (channel === 'holberton school channel') {
			console.log(message);
		}
		if (message === 'KILL_SERVER') {
			redisCLI.unsubscribe();
			redisCLI.quit();
		}
	})
	.subscribe('holberton school channel');
