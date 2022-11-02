// Connects to redis server and logs message to console
const redis = require('redis');
const redisCLI = redis.createClient();

redisCLI
	.on('connect', () => {
		console.log('Redis client connected to the server');
	})
	.on('error', (err) => {
		console.log(`Redis client not connected to the server: ${err}`);
	});
