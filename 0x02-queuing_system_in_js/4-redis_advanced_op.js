// Create a client and store a hash value
const redis = require('redis');
const redisCLI = redis.createClient();

redisCLI
	.on('connect', () => {
		console.log('Redis client connected to the server');
	})
	.on('error', (err) => {
		console.log(`Redis client not connected to the server: ${err}`);
	});

const hashValues = {
	'Portland': 50,
	'Seattle': 80,
	'New York': 20,
	'Bogota': 20,
	'Cali': 40,
	'Paris': 2
}

for (const [key, value] of Object.entries(hashValues)) {
	redisCLI.hset('HolbertonSchools', key, value, redis.print);
}

redisCLI.hgetall('HolbertonSchools', (error, result) => {
	console.log(result);
})
