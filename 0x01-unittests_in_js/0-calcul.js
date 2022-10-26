// Function that rounds two numbers and adds them
const calculateNumber = (a, b) => {
	if (isNaN(a) || isNaN(b)) throw new TypeError("a and b must be numbers");
	return Math.round(a) + Math.round(b);
};

module.exports = calculateNumber;
