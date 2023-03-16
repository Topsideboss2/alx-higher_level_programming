#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (isNaN(number)) {
	console.log("Missing size");
}
else {
	for (let i = 0, side; i < number; i++) {
		side = '';
		for (let j = 0; j < number; j++) {
			side += 'X';
		}
		console.log(side);
	}
}
