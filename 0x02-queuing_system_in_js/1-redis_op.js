// Connects to redis server and logs message to console
const { client } = require('kue/lib/redis');
const redis = require('redis');
const redisCLI = redis.createClient();

redisCLI
	.on('connect', () => {
		console.log('Redis client connected to the server');
	})
	.on('error', (err) => {
		console.log(`Redis client not connected to the server: ${err}`);
	});

const setNewSchool = (schoolName, value) => {
	redisCLI.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
	redisCLI.get(schoolName, (err, value) => {
		if (err) {
			console.log(err);
		}
		console.log(value);
	});
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
